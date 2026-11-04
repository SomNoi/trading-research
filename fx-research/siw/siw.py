#!/usr/bin/env python3
"""SIW v2 XAUUSD M5. Listed/alert bar L = CONFIRM bar; entry = open of L+1.
Usage: python3 siw.py data.csv [--from 2026-10-29] [--to 2026-11-04] [--modes abc] [--zone 3] [--touch]"""
import argparse, pandas as pd, numpy as np
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
)
def load(path):
    df = pd.read_csv(path); df['utc'] = pd.to_datetime(df.t, unit='ms')
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
def detect(df, p=P):
    p = dict(P, **p); out, last = [], {'S': -99, 'B': -99}
    for i in range(max(60, p['leg_lookback']), len(df) - 1):
        L = df.loc[i]; d = 'B' if L.e21 > L.e55 else 'S'
        k = classify(df, i, d, p)
        if not k: continue
        w = df.loc[i-p['leg_lookback']+1:i]
        dist = (w.h.max() - L.c) if d == 'S' else (L.c - w.l.min())
        if dist > p['max_ext']: continue
        if p['zone_max'] is not None and dist > p['zone_max']: continue
        if p['touch'] and not ((w.h.max() >= L.e21 - p['ema_tol']) if d == 'S' else (w.l.min() <= L.e21 + p['ema_tol'])): continue
        if i - last[d] < p['dedupe']: continue
        last[d] = i
        out.append(dict(i=i, dir=d, kind=k, conf_srv=L.srv, entry_srv=df.loc[i+1].srv, entry_ict=df.loc[i+1].ict,
                        entry=round(df.loc[i+1].o, 2), leg_dist=round(dist, 2)))
    return pd.DataFrame(out, columns=['i','dir','kind','conf_srv','entry_srv','entry_ict','entry','leg_dist'])
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
if __name__ == '__main__':
    a = argparse.ArgumentParser(); a.add_argument('csv'); a.add_argument('--from'); a.add_argument('--to')
    a.add_argument('--modes', default='abc'); a.add_argument('--zone', type=float); a.add_argument('--touch', action='store_true')
    a.add_argument('--exit', default='fixed', choices=['fixed','v3','v4']); a.add_argument('--trail', type=float, default=3.0); a.add_argument('--be', action='store_true')
    x = a.parse_args(); df = load(x.csv); s = detect(df, dict(modes=x.modes, zone_max=x.zone, touch=x.touch))
    if getattr(x, 'from'): s = s[s.conf_srv >= getattr(x, 'from')]
    if x.to: s = s[s.conf_srv < x.to]
    for _, r in s.iterrows():
        print(f"SIW2 {r.dir} {r.kind:9s} confirm {r.conf_srv:%m-%d %H:%M} srv  ENTRY {r.entry_srv:%H:%M} srv / {r.entry_ict:%m-%d %H:%M} ICT @ {r.entry} (bid)  leg {r.leg_dist}", end='')
        if x.exit == 'v4': k, pnl = outcome_v4(df, r.i+1, r.dir); print(f"  v4 {k} {pnl:+.2f}")
        elif x.exit == 'v3': k, pnl = outcome_v3(df, r.i+1, r.dir, dict(v3_trail=x.trail, v3_be=x.be)); print(f"  v3 {k} {pnl:+.2f}")
        else: k, pnl = outcome(df, r.i+1, r.dir); print(f"  {k} {pnl:+.2f}")
