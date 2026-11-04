#!/usr/bin/env python3
"""SIW (Star-in-Wick) XAUUSD M5 detector + backtester -- v5 (2026-11-04). WATCH-ONLY: never sends orders.

Owner: Preda (ส้มน้อย). Alerts go out in Thai via the routine `xau-plan-watch` (runs in dr eggbot,
every 15 min weekdays 08:01-23:46 ICT; silent when nothing new). Handbook: README_HANDBOOK.md (same folder).

DATA
  Live: Dukascopy XAU/USD BID M5 (no key):
    curl -s -H "Referer: https://freeserv.dukascopy.com/" -A "Mozilla/5.0" \
      "https://freeserv.dukascopy.com/2.0/?path=chart/json3&instrument=XAU/USD&offer_side=B&interval=5MIN\
&splits=true&stocks=true&limit=500&time_direction=P&timestamp=<now_ms>&jsonp=_cb"
    Strip `_cb(` ... `)`; rows = [t_ms_UTC, o, h, l, c, vol], NEWEST FIRST. Newest row may be the forming bar.
    Stale if newest bar older than 15 min -> retry once -> fallback Yahoo GC=F 5m (futures, ~+$12 vs IC; levels only).
  Offsets: Dukascopy BID ~= IC Markets BID + $1.5. Backtests use IC Markets BID history (CSV cols t,o,h,l,c; t=ms UTC).

TIME
  Report ICT (Asia/Bangkok, UTC+7) AND MT5 server time: server = ICT-5h in winter (UTC+2, from 2026-11-01),
  ICT-4h in summer (UTC+3). Closed bars only. L = confirm bar; entry = OPEN of L+1.

RULES (sell shown; buy is the mirror)
  1 Direction: EMA21 vs EMA55 of M5 closes (warm-up 500 bars). EMA21<EMA55 -> sells only; > -> buys only.
  2 Pattern at L (modes abc): A pin (trend-opposite wick >=50% of range, body <=35%) or small body <=40% inside
    L-1's wick (+-$0.30); B engulfing in trend direction (tol $0.10); C L-1 is pin/star-in-wick and L closes trend colour.
  3 Leg filter: |close(L) - 12-bar extreme| <= $10.
  4 Fresh-extreme filter (R251, K=5, default ON): set = L-2..L. SELL needs max(high of set) >= every high of
    L-7..L-3; BUY needs min(low of set) <= every low of L-7..L-3. Order inside the set does not matter.
  5 Dedupe: skip same-direction signal within 3 bars of the last one alerted (live). Research default 1.
EXIT v4 (current): SL $10, TP $20, time exit at CLOSE of L+2 (10 min after entry); bar by bar, SL checked before TP,
  gap through a level fills at bar open. Cost $0.28 per 0.01 lot.
STATUS: R247-R251 found NO proven edge (N_TRIALS 6670). Alerts are information, not advice.

CLI
  python3 siw.py --live [--no-fresh] [--k 5] [--since-min 30]   # fetch Dukascopy, print signals as JSON lines
  python3 siw.py --backtest data.csv [--from YYYY-MM-DD] [--to ...] [--exit v4|v3|fixed] [--no-fresh] [--dedupe 3]
  python3 siw.py data.csv ...                                    # legacy form = --backtest
"""
import argparse, json, re, subprocess, time, sys, pandas as pd, numpy as np
P = dict(
  modes='abc',        # a: L itself pin/star-in-prev-wick; b: L engulfing; c: L-1 pin/star-in-wick + L colour confirm
  star_body_max=0.40, pin_wick_min=0.50, pin_body_max=0.35, wick_tol=0.30,
  engulf_tol=0.10,    # $ tolerance on body engulf
  leg_lookback=12,    # bars (incl. L) defining current leg extreme
  max_ext=10.0,       # skip if leg extreme -> close(L) distance > this ($)
  zone_max=None,      # optional pullback-zone check: distance <= zone_max (e.g. 3)
  touch=False,        # optional: sell needs leg high >= EMA21 - ema_tol (buy mirror)
  ema_tol=1.0, dedupe=1,  # dedupe=3 blocked 11 of his picks (fired 1 bar earlier)
  tp=10.0, sl=5.0, cost=0.28, timeout=48,
  exit='fixed',       # 'fixed' (tp/sl above) or 'v3'
  v3_sl=5.0, v3_tp=20.0, v3_after=3, v3_trail=3.0, v3_be=False,  # v3: after N bars trail from best price; optional BE
  v4_sl=10.0, v4_tp=20.0, v4_bars=2,  # v4 (2026-11-04, CURRENT): SL $10, TP $20 cap, close at close of L+2 (10 min after entry)
  fresh=True, fresh_k=5,  # R251 fresh-extreme filter: set L-(K-3)..L must make the extreme vs L-K-2..L-K+2 ... see fresh_ok()
  live=False,         # live: allow L = last closed bar (no L+1 yet)
)
def load(path):
    return prep(pd.read_csv(path))
def prep(df):
    df = df.copy(); df['utc'] = pd.to_datetime(df.t, unit='ms')
    df['srv'] = df.utc + pd.to_timedelta(np.where(df.utc < pd.Timestamp('2026-11-01'), 3, 2), unit='h')
    df['ict'] = df.utc + pd.Timedelta(hours=7)
    df['e21'] = df.c.ewm(span=21, adjust=False).mean(); df['e55'] = df.c.ewm(span=55, adjust=False).mean()
    return df.reset_index(drop=True)
def _shape(b):
    rng = max(b.h - b.l, 1e-9); top, bot = max(b.o, b.c), min(b.o, b.c)
    return abs(b.c-b.o)/rng, (b.h-top)/rng, (bot-b.l)/rng, top, bot
def rej(b, pv, d, p):
    """pin / shooting star / hammer, or small body inside prev bar's wick, in direction d"""
    bp, uw, lw, top, bot = _shape(b); ptop, pbot = max(pv.o, pv.c), min(pv.o, pv.c)
    if d == 'S':
        if uw >= p['pin_wick_min'] and bp <= p['pin_body_max']: return 'PIN'
        if bp <= p['star_body_max'] and bot >= ptop - p['wick_tol'] and top <= pv.h + p['wick_tol'] and pv.h > ptop: return 'STAR'
    else:
        if lw >= p['pin_wick_min'] and bp <= p['pin_body_max']: return 'PIN'
        if bp <= p['star_body_max'] and top <= pbot + p['wick_tol'] and bot >= pv.l - p['wick_tol'] and pbot > pv.l: return 'STAR'
    return None
def engulf(b, pv, d, t):
    if d == 'S': return b.c < b.o and pv.c > pv.o and b.o >= pv.c - t and b.c <= pv.o + t
    return b.c > b.o and pv.c < pv.o and b.o <= pv.c + t and b.c >= pv.o - t
def classify(df, i, d, p):
    L, p1, p2 = df.loc[i], df.loc[i-1], df.loc[i-2]
    colour = (L.c < L.o) if d == 'S' else (L.c > L.o)
    if 'a' in p['modes']:
        k = rej(L, p1, d, p)
        if k: return 'A_' + k
    if 'b' in p['modes'] and engulf(L, p1, d, p['engulf_tol']): return 'B_ENGULF'
    if 'c' in p['modes'] and colour:
        k = rej(p1, p2, d, p)
        if k: return 'C_' + k
    return None
def fresh_ok(df, i, d, k=5):
    """Fresh-extreme (user's eye rule, R251). K=5: set = L-2..L, reference = L-7..L-3 (K bars before the set).
    SELL: max high of set >= every high of reference. BUY: min low of set <= every low of reference."""
    s = df.loc[i-2:i]; r = df.loc[i-2-k:i-3]
    if len(r) < k: return False
    return s.h.max() >= r.h.max() if d == 'S' else s.l.min() <= r.l.min()
def detect(df, p=P):
    p = dict(P, **p); out, last = [], {'S': -99, 'B': -99}
    for i in range(max(60, p['leg_lookback']), len(df) - (0 if p['live'] else 1)):
        L = df.loc[i]; d = 'B' if L.e21 > L.e55 else 'S'
        k = classify(df, i, d, p)
        if not k: continue
        w = df.loc[i-p['leg_lookback']+1:i]
        dist = (w.h.max() - L.c) if d == 'S' else (L.c - w.l.min())
        if dist > p['max_ext']: continue
        if p['zone_max'] is not None and dist > p['zone_max']: continue
        if p['touch'] and not ((w.h.max() >= L.e21 - p['ema_tol']) if d == 'S' else (w.l.min() <= L.e21 + p['ema_tol'])): continue
        if p['fresh'] and not fresh_ok(df, i, d, p['fresh_k']): continue
        if i - last[d] < p['dedupe']: continue
        last[d] = i
        out.append(dict(i=i, dir=d, kind=k, conf_srv=L.srv, conf_ict=L.ict,
                        entry_srv=(df.loc[i+1].srv if i+1 < len(df) else L.srv + pd.Timedelta(minutes=5)),
                        entry_ict=(df.loc[i+1].ict if i+1 < len(df) else L.ict + pd.Timedelta(minutes=5)),
                        entry=(round(df.loc[i+1].o, 2) if i+1 < len(df) else None), conf_close=round(L.c, 2), leg_dist=round(dist, 2)))
    return pd.DataFrame(out, columns=['i','dir','kind','conf_srv','conf_ict','entry_srv','entry_ict','entry','conf_close','leg_dist'])
def outcome(df, ie, d, p=P):
    p = dict(P, **p); e = df.loc[ie].o
    for j in range(ie, min(ie + p['timeout'], len(df))):
        b = df.loc[j]; fav = (e-b.l) if d == 'S' else (b.h-e); adv = (b.h-e) if d == 'S' else (e-b.l)
        if adv >= p['sl']: return 'SL', -p['sl'] - p['cost']
        if fav >= p['tp']: return 'TP', p['tp'] - p['cost']
    j = min(ie + p['timeout'], len(df)) - 1; pnl = (e - df.loc[j].c) if d == 'S' else (df.loc[j].c - e)
    return 'TO', pnl - p['cost']
def outcome_v3(df, ie, d, p=P):
    """v3: SL v3_sl / TP v3_tp from entry. After v3_after bars closed, stop = tighter of SL and (best since entry -/+ v3_trail)
    (and >= breakeven if v3_be). Bar by bar; stop checked before TP; best updated AFTER the bar's checks (conservative)."""
    p = dict(P, **p); e = df.loc[ie].o; sg = -1 if d == 'S' else 1
    stop = e - sg*p['v3_sl']; tp = e + sg*p['v3_tp']; best = e
    for j in range(ie, min(ie + p['timeout'], len(df))):
        b = df.loc[j]
        if j - ie >= p['v3_after']:
            ts = best - sg*p['v3_trail']; stop = max(stop, ts) if sg > 0 else min(stop, ts)
            if p['v3_be']: stop = max(stop, e) if sg > 0 else min(stop, e)
        if (b.l <= stop) if sg > 0 else (b.h >= stop):
            x = stop if j > ie or True else stop
            if j > ie and ((b.o < stop) if sg > 0 else (b.o > stop)): x = b.o   # gap through stop
            return ('TRAIL' if j - ie >= p['v3_after'] else 'SL'), sg*(x - e) - p['cost']
        if (b.h >= tp) if sg > 0 else (b.l <= tp): return 'TP', p['v3_tp'] - p['cost']
        best = max(best, b.h) if sg > 0 else min(best, b.l)
    j = min(ie + p['timeout'], len(df)) - 1
    return 'TO', sg*(df.loc[j].c - e) - p['cost']
def outcome_v4(df, ie, d, p=P):
    """v4 (current, user decision 2026-11-04): entry = open of bar ie (=L+1). For bars ie..ie+v4_bars-1: SL v4_sl checked
    first (worst case), then TP v4_tp. Otherwise exit at close of bar ie+v4_bars-1 (= L+2, 10 min after entry). Gap-through -> bar open."""
    p = dict(P, **p); e = df.loc[ie].o; sg = -1 if d == 'S' else 1
    stop = e - sg*p['v4_sl']; tp = e + sg*p['v4_tp']; last = min(ie + p['v4_bars'], len(df)) - 1
    for j in range(ie, last + 1):
        b = df.loc[j]
        if (b.l <= stop) if sg > 0 else (b.h >= stop):
            x = b.o if (j > ie and ((b.o < stop) if sg > 0 else (b.o > stop))) else stop
            return 'SL', sg*(x - e) - p['cost']
        if (b.h >= tp) if sg > 0 else (b.l <= tp):
            x = b.o if (j > ie and ((b.o > tp) if sg > 0 else (b.o < tp))) else tp
            return 'TP', sg*(x - e) - p['cost']
    return 'TIME', sg*(df.loc[last].c - e) - p['cost']
DUKA = ("https://freeserv.dukascopy.com/2.0/?path=chart/json3&instrument=XAU/USD&offer_side=B&interval=5MIN"
        "&splits=true&stocks=true&limit=500&time_direction=P&timestamp={ts}&jsonp=_cb")
def fetch_duka(tries=2):
    """Return closed M5 bars oldest-first (cols t,o,h,l,c) from Dukascopy; drop forming bar; retry once if stale."""
    for n in range(tries):
        now = int(time.time()*1000)
        raw = subprocess.run(['curl', '-s', '-H', 'Referer: https://freeserv.dukascopy.com/', '-A', 'Mozilla/5.0',
                              DUKA.format(ts=now)], capture_output=True, text=True, timeout=30).stdout
        m = re.search(r'_cb\((.*)\)\s*;?\s*$', raw, re.S)
        if not m: continue
        rows = json.loads(m.group(1))
        df = pd.DataFrame([r[:5] for r in rows], columns=['t','o','h','l','c']).sort_values('t').reset_index(drop=True)
        df = df[df.t + 5*60*1000 <= now].reset_index(drop=True)          # closed bars only
        if now - df.t.iloc[-1] <= 15*60*1000 + 5*60*1000: return df, 'dukascopy'
        time.sleep(3)
    raise RuntimeError('Dukascopy stale/unreachable -> use Yahoo GC=F 5m fallback (levels only, ~+$12 vs IC)')
def live(a):
    df, src = fetch_duka(); df = prep(df)
    s = detect(df, dict(live=True, dedupe=3, fresh=not a.no_fresh, fresh_k=a.k))
    cut = df.utc.iloc[-1] - pd.Timedelta(minutes=a.since_min)
    s = s[df.loc[s.i, 'utc'].values >= cut] if len(s) else s
    last = df.iloc[-1]
    print(json.dumps(dict(source=src, last_closed_ict=f"{last.ict:%Y-%m-%d %H:%M}", last_close=round(last.c, 2),
                          trend='BUY-only' if last.e21 > last.e55 else 'SELL-only', n_signals=len(s)), ensure_ascii=False))
    for _, r in s.iterrows():
        print(json.dumps(dict(dir=r.dir, kind=r.kind, confirm_ict=f"{r.conf_ict:%Y-%m-%d %H:%M}", confirm_srv=f"{r.conf_srv:%H:%M}",
              entry_ict=f"{r.entry_ict:%H:%M}", entry_srv=f"{r.entry_srv:%H:%M}", entry=r.entry, confirm_close=r.conf_close,
              sl=round(r.conf_close + (10 if r.dir == 'S' else -10), 2), tp=round(r.conf_close + (-20 if r.dir == 'S' else 20), 2),
              time_exit_ict=f"{r.conf_ict + pd.Timedelta(minutes=15):%H:%M}", leg_dist=r.leg_dist, note='SL/TP shown from confirm close; recompute from actual entry open'), ensure_ascii=False))
def backtest(a):
    df = load(a.backtest); s = detect(df, dict(modes=a.modes, zone_max=a.zone, touch=a.touch, fresh=not a.no_fresh, fresh_k=a.k, dedupe=a.dedupe))
    if getattr(a, 'from'): s = s[s.conf_srv >= getattr(a, 'from')]
    if a.to: s = s[s.conf_srv < a.to]
    tot = []
    for _, r in s.iterrows():
        print(f"SIW2 {r.dir} {r.kind:9s} confirm {r.conf_srv:%m-%d %H:%M} srv  ENTRY {r.entry_srv:%H:%M} srv / {r.entry_ict:%m-%d %H:%M} ICT @ {r.entry} (bid)  leg {r.leg_dist}", end='')
        if a.exit == 'v4': k, pnl = outcome_v4(df, r.i+1, r.dir)
        elif a.exit == 'v3': k, pnl = outcome_v3(df, r.i+1, r.dir, dict(v3_trail=a.trail, v3_be=a.be))
        else: k, pnl = outcome(df, r.i+1, r.dir)
        tot.append(pnl); print(f"  {a.exit} {k} {pnl:+.2f}")
    if tot: print(f"# n={len(tot)} win={np.mean(np.array(tot)>0):.0%} total={sum(tot):+.2f} avg={np.mean(tot):+.2f}  (IN-SAMPLE, no proven edge)")
if __name__ == '__main__':
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'): sys.argv[1:1] = ['--backtest']   # legacy positional csv
    a = argparse.ArgumentParser(); g = a.add_mutually_exclusive_group(required=True)
    g.add_argument('--live', action='store_true'); g.add_argument('--backtest', metavar='CSV')
    a.add_argument('--from'); a.add_argument('--to'); a.add_argument('--modes', default='abc'); a.add_argument('--zone', type=float)
    a.add_argument('--touch', action='store_true'); a.add_argument('--exit', default='v4', choices=['fixed','v3','v4'])
    a.add_argument('--trail', type=float, default=3.0); a.add_argument('--be', action='store_true')
    a.add_argument('--no-fresh', action='store_true', help='disable R251 fresh-extreme filter'); a.add_argument('--k', type=int, default=5)
    a.add_argument('--dedupe', type=int, default=1); a.add_argument('--since-min', type=int, default=30, help='live: only signals confirmed in last N min')
    x = a.parse_args(); live(x) if x.live else backtest(x)
