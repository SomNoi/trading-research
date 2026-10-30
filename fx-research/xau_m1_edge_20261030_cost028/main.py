#!/usr/bin/env python3
"""XAU M1 human-behavior edge study. Run: python main.py (re-execs with fx-research venv)."""
import os, sys, json
VENV = "/workspace/fx-research/.venv/bin/python"
if os.path.exists(VENV) and sys.prefix != "/workspace/fx-research/.venv" and "FXR_REEXEC" not in os.environ:
    os.environ["FXR_REEXEC"] = "1"; os.execv(VENV, [VENV] + sys.argv)
import numpy as np, pandas as pd, numba
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
sys.path.insert(0, "/workspace/fx-research/scripts")
try:
    from fleet import Heartbeat; HB = Heartbeat("xau-m1-edge-cost028")
except Exception: HB = None
W = os.path.dirname(os.path.abspath(__file__)); os.chdir(W)
COST = 0.28; SL0, TP0, TSTOP = 3.5, 1.5, 25
print(f"COST MODEL: Kai/real $0.28/oz RT (Kai-ish IC); replaces old user $0.65 model -> ${COST}/trade RT")
def hb(s):
    print(s, flush=True)
    if HB: HB.tick(s)

d = pd.read_parquet("/workspace/fx-research/data/XAUUSD_M1.parquet")
d.index = d.index.tz_convert("Asia/Bangkok"); d = d[d.index >= "2022-01-01"]
DATA_END = str(d.index[-1]); hb(f"bars {len(d)} end {DATA_END}")
o, h, l, c, v = (d[k] for k in ["open", "high", "low", "close", "volume"])
mins = d.index.hour * 60 + d.index.minute; mins = pd.Series(mins, index=d.index)
day = pd.Series(d.index.date, index=d.index)
asia = (mins >= 300) & (mins < 780); ldn = (mins >= 840) & (mins < 1140); ny = (mins >= 1170) & (mins < 1410)
insess = asia | ldn | ny
sess_id = pd.Series(np.where(asia, 1, np.where(ldn, 2, np.where(ny, 3, 0))), index=d.index)
rng = h - l; uw = h - np.maximum(o, c); lw = np.minimum(o, c) - l
bull = c > o; bear = c < o

def first_per(mask, key):  # first True per group key
    m = mask.fillna(False).astype(bool)
    return m & (m.astype(int).groupby(key).cumsum() == 1)
sess_key = day.astype(str) + "_" + sess_id.astype(str)

S = {}  # name -> series in {+1,-1,0}
# A
ah = h.where(asia).groupby(day).transform("max"); al = l.where(asia).groupby(day).transform("min")
late = ldn | ny
S["01_ASIA_H_SWEEP"] = -first_per(late & (h > ah) & (c < ah), day).astype(int)
S["02_ASIA_L_SWEEP"] = first_per(late & (l < al) & (c > al), day).astype(int)
from numpy.lib.stride_tricks import sliding_window_view as swv
def eq_count(x, n=30, tol=0.3, high=True):
    a = x.to_numpy(np.float32); out_lvl = np.full(len(a), np.nan); out_n = np.zeros(len(a))
    for s0 in range(0, len(a) - n, 200000):  # chunked over windows (vectorized inside)
        e0 = min(s0 + 200000, len(a) - n); w = swv(a[s0:e0 + n - 1], n)  # w[j] = a[s0+j .. s0+j+n-1]
        lv = w.max(1) if high else w.min(1)
        cnt = (w >= lv[:, None] - tol).sum(1) if high else (w <= lv[:, None] + tol).sum(1)
        out_lvl[s0 + n: e0 + n] = lv[: e0 - s0]; out_n[s0 + n: e0 + n] = cnt[: e0 - s0]
    return pd.Series(out_lvl, index=x.index), pd.Series(out_n, index=x.index)
H30, nH = eq_count(h, high=True); L30, nL = eq_count(l, high=False)
S["03_EQH_SWEEP"] = -((nH >= 2) & (h > H30) & (c < H30)).astype(int)
S["04_EQL_SWEEP"] = ((nL >= 2) & (l < L30) & (c > L30)).astype(int)
dh = h.groupby(day).max(); dl = l.groupby(day).min()
pdh = day.map(dh.shift(1)); pdl = day.map(dl.shift(1))
S["05_PDH_FAKE"] = -first_per((h > pdh) & (c < pdh), day).astype(int)
S["06_PDL_FAKE"] = first_per((l < pdl) & (c > pdl), day).astype(int)
fh = (h.shift(1) > h.shift(2)) & (h.shift(1) > h); SH = h.shift(1).where(fh).ffill().shift(1)
fl = (l.shift(1) < l.shift(2)) & (l.shift(1) < l); SLv = l.shift(1).where(fl).ffill().shift(1)
S["07_FRACTAL_HUNT"] = ((l < SLv) & (c > SLv)).astype(int) - ((h > SH) & (c < SH)).astype(int)
# B
mid1 = (h.shift(1) + l.shift(1)) / 2; big1 = rng.shift(1) > 3.5
S["08_BIG_BAR_REJ"] = (big1 & bear.shift(1, fill_value=False) & (c >= mid1)).astype(int) - (big1 & bull.shift(1, fill_value=False) & (c <= mid1)).astype(int)
r3 = c.shift(1) - c.shift(4)
S["09_RUN3_REJ"] = ((r3 < -5) & bull).astype(int) - ((r3 > 5) & bear).astype(int)
S["10_PIN"] = ((rng >= 1) & (lw >= 0.7 * rng) & (c >= h - rng / 3)).astype(int) - ((rng >= 1) & (uw >= 0.7 * rng) & (c <= l + rng / 3)).astype(int)
r5 = c.shift(1) - c.shift(6)
S["11_UPWICK_AFTER_UP"] = -((r5 > 3) & (uw >= 0.5 * rng) & (rng >= 0.5)).astype(int)
S["12_LOWWICK_AFTER_DN"] = ((r5 < -3) & (lw >= 0.5 * rng) & (rng >= 0.5)).astype(int)
med20 = rng.shift(1).rolling(20).median(); exp_ = (rng > 2 * med20) & (rng >= 1)
S["13_EXPANSION_FADE"] = (exp_ & bear).astype(int) - (exp_ & bull).astype(int)
e1 = exp_.shift(1, fill_value=False)
S["14_DOUBLE_EXP_FADE"] = (exp_ & e1 & bear & bear.shift(1, fill_value=False)).astype(int) - (exp_ & e1 & bull & bull.shift(1, fill_value=False)).astype(int)
# C
bfvg = (l - h.shift(2)) >= 0.3; sfvg = (l.shift(2) - h) >= 0.3
for nm, a0, a1 in [("15_LDN_FVG", 842, 870), ("16_NY_FVG", 1172, 1200)]:
    win = (mins >= a0) & (mins < a1); f = first_per(win & (bfvg | sfvg), day)
    S[nm] = (f & sfvg).astype(int) - (f & bfvg).astype(int)
for nm, m0, thr in [("17_LDN_DRIVE", 840, 2), ("18_NY_DRIVE", 1170, 2), ("19_ASIA_DRIVE", 300, 1.5)]:
    op = day.map(o[mins == m0].groupby(day[mins == m0]).first())
    dd = c - op; at = mins == m0 + 14
    S[nm] = (at & (dd < -thr)).astype(int) - (at & (dd > thr)).astype(int)
g = o - c.shift(1); first_bar = mins.isin([300, 840, 1170])
S["20_OPEN_GAP_FILL"] = (first_bar & (g < -0.5)).astype(int) - (first_bar & (g > 0.5)).astype(int)
# D
ema = c.ewm(span=20, adjust=False).mean()
tr = pd.concat([rng, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1); atr = tr.rolling(14).mean()
def cross(dev, k):
    up = dev > k * atr; dn = dev < -k * atr
    return (dn & ~dn.shift(1, fill_value=False)).astype(int) - (up & ~up.shift(1, fill_value=False)).astype(int)
tp_ = (h + l + c) / 3; vv = v.replace(0, 1e-9)
vw = (tp_ * vv).groupby(sess_key).cumsum() / vv.groupby(sess_key).cumsum()
S["21_EMA_1p5ATR"] = cross(c - ema, 1.5)
S["22_VWAP_1p5ATR"] = cross(c - vw, 1.5).where(sess_id > 0, 0)
S["23_EMA_2p5ATR"] = cross(c - ema, 2.5)
S["24_ATR_CHANNEL"] = cross(c - ema, 2.0)
upc = (c > c.shift(1)).astype(int); dnc = (c < c.shift(1)).astype(int)
S["25_STREAK8"] = (dnc.rolling(8).sum().eq(8) & ~dnc.shift(1).rolling(8).sum().eq(8)).astype(int) - (upc.rolling(8).sum().eq(8) & ~upc.shift(1).rolling(8).sum().eq(8)).astype(int)
hb("signals built")

O, Hn, Ln, Cn = (x.to_numpy(np.float64) for x in (o, h, l, c))
gate = (insess & insess.shift(-1, fill_value=False)).to_numpy()  # signal bar and entry bar in session
@numba.njit
def sim(sig, O, H, L, C, sl, tpR, ts):
    n = len(O); ent = []; ex = []; dr = []; pnl = []; i = 0
    while i < n - 2:
        s = sig[i]
        if s == 0: i += 1; continue
        e = i + 1; px = O[e]; sp = px - s * sl; tpp = px + s * sl * tpR; xi = -1; xp = 0.0
        for j in range(e, min(e + ts, n)):
            if s > 0:
                if L[j] <= sp: xi = j; xp = sp; break
                if H[j] >= tpp: xi = j; xp = tpp; break
            else:
                if H[j] >= sp: xi = j; xp = sp; break
                if L[j] <= tpp: xi = j; xp = tpp; break
        if xi < 0: xi = min(e + ts, n) - 1; xp = C[xi]
        ent.append(e); ex.append(xi); dr.append(s); pnl.append(s * (xp - px)); i = xi + 1
    return np.array(ent), np.array(ex), np.array(dr), np.array(pnl)

idx = d.index
def run(name, sl=SL0, tpR=TP0, shift=0):
    s = (S[name].fillna(0).to_numpy() * gate).astype(np.int64)
    if shift: s = np.roll(s, shift); s[:max(shift, 0)] = 0; s[len(s) + min(shift, 0):] = 0
    e, x, dr, p = sim(s, O, Hn, Ln, Cn, sl, tpR, TSTOP)
    t = pd.DataFrame({"hyp": name, "entry_time": idx[e], "exit_time": idx[x], "dir": dr, "gross": p, "net": p - COST,
                      "session": sess_id.to_numpy()[e], "sl": sl, "tpR": tpR, "shift": shift})
    return t
def stats(t):
    n = len(t)
    if n == 0: return dict(N=0, PF=np.nan, WR=np.nan, net=0.0, maxDD=0.0, exp=np.nan)
    w = t.net[t.net > 0].sum(); ls = -t.net[t.net < 0].sum(); eq = t.net.cumsum()
    dd = float((eq.cummax().clip(lower=0) - eq).max())
    return dict(N=n, PF=w / ls if ls > 0 else np.inf, WR=(t.net > 0).mean(), net=t.net.sum(), maxDD=dd, exp=t.net.mean())
def split(t, which):
    et = t.entry_time
    if which == "IS": return t[et < "2024-01-01"]
    if which == "OOS": return t[et >= "2024-01-01"]
    return t[et >= "2025-01-01"]
def base_pass(s): return s["PF"] > 1.25 and s["WR"] > 0.48 and s["net"] > 0 and s["maxDD"] < 0.25 * s["net"] and s["N"] > 150

rows = []; alltr = []; ntr = 0; survivors = []
for name in S:
    t = run(name); ntr += 1; alltr.append(t)
    r = {"hyp": name}
    for sp in ["IS", "OOS", "REC"]:
        for k, val in stats(split(t, sp)).items(): r[f"{sp}_{k}"] = val
    so = stats(split(t, "OOS")); r["base_pass"] = base_pass(so)
    sens = []
    for kw in [dict(shift=-2), dict(shift=2), dict(sl=SL0 - 0.5), dict(sl=SL0 + 0.5)]:
        st = stats(split(run(name, **kw), "OOS")); ntr += 1; sens.append(st["PF"])
    r["sens_PF_min"] = min(sens); r["sens_PFs"] = ";".join(f"{x:.3f}" for x in sens)
    r["KILL_PASS"] = bool(r["base_pass"] and r["sens_PF_min"] > 1.15)
    for sp in ["IS", "OOS"]:  # by session
        for sid, sn in [(1, "ASIA"), (2, "LDN"), (3, "NY")]:
            ss = stats(split(t[t.session == sid], sp)); r[f"{sp}_{sn}_N"] = ss["N"]; r[f"{sp}_{sn}_PF"] = ss["PF"]
    rows.append(r); hb(f"{name} OOS N={so['N']} PF={so['PF']:.3f} WR={so['WR']:.3f} sensmin={r['sens_PF_min']:.3f}")
    if r["base_pass"]: survivors.append(name)
grid = []
for name in survivors:
    for sl in [2.5, 3.5, 4.5]:
        for tp in [1.2, 1.5, 2.0]:
            if sl == 3.5 and tp == 1.5: continue
            st = stats(split(run(name, sl=sl, tpR=tp), "OOS")); ntr += 1; grid.append({"hyp": name, "sl": sl, "tpR": tp, **st})
summ = pd.DataFrame(rows); summ.to_csv("summary.csv", index=False)
pd.DataFrame(grid).to_csv("grid_survivors.csv", index=False)
pd.concat(alltr).to_csv("trades.csv", index=False)
# equity charts: OOS, top 6 by OOS PF
os.makedirs("charts", exist_ok=True)
top = summ.sort_values("OOS_PF", ascending=False).head(6).hyp
fig, ax = plt.subplots(figsize=(11, 6))
for nm in top:
    t = split(alltr[list(S).index(nm)], "OOS"); ax.plot(t.entry_time, t.net.cumsum(), label=nm)
ax.axhline(0, c="k", lw=.5); ax.set_title(f"OOS 2024→{DATA_END[:10]} net $/oz equity, top6 by OOS PF (cost $0.28)"); ax.legend(); fig.savefig("charts/oos_equity_top6.png", dpi=110)
fig, ax = plt.subplots(figsize=(11, 6))
for nm, t in zip(S, alltr):
    t = split(t, "OOS"); ax.plot(t.entry_time, t.net.cumsum(), lw=.7)
ax.set_title("OOS equity all 25 hyps"); fig.savefig("charts/oos_equity_all25.png", dpi=110)
json.dump({"n_trials": ntr, "survivors_base": survivors, "kill_pass": summ[summ.KILL_PASS].hyp.tolist(), "data_end": DATA_END}, open("run_meta.json", "w"), indent=1)
hb(f"DONE trials={ntr} kill_pass={summ.KILL_PASS.sum()}")
