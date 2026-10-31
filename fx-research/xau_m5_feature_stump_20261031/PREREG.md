# PREREG — Round 10 xau_m5_feature_stump_20261031 (locked before any fit)
Data: IC MT5 XAUUSD M5 BID (data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv). IS first 60% bars, OOS last 40%.
Features (7): r1,r3,r12 = Δclose(k)/ATR14 (Wilder); atr_pct = ATR14 pct rank vs trailing 20d (5520 bars, 0–1);
relvol = tick_volume/SMA48 clip[0,5]; sin/cos of ICT (UTC+7) time-of-day (hour+min/60)/24.
Z-score with IS mean/std ONLY; same stats applied to OOS. Warmup NaN rows dropped.
Target y=sign(close[t+5]-close[t]), y=0 excluded; IS labels only (last 5 IS bars excluded to avoid boundary leakage).
Models: ridge(L2) logistic C∈{0.1,1.0}; stump = single feature with max IS |AUC-0.5|, p = IS-fitted 1-D logistic on that feature (monotone; sign by AUC).
Entry at bar t close signal → open t+1: long p≥τ, short p≤1−τ, τ∈{0.55,0.60,0.65}. One position. Exit SL$3.5, TP 1.5R, time 5 bars. Session any. Cost $0.28 RT.
Grid 9 cells, frozen. One OOS pass.
PASS (desk): OOS PF≥1.25, n≥150, E>0, PF@1.5x cost>1, sens min PF>1 (SL{3,4}×R{1.25,1.75}), MDD≤25% (1%risk), IS PF>1. Else ไม่เจอ.
