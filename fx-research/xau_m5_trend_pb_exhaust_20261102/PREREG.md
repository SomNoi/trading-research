# R246 PREREG — xau_m5_trend_pb_exhaust_20261102
Data: IC MT5 BID XAUUSD M5 `data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv` (2025-05-14 → last label 2026-10-09 17:55).
Timestamps: column `time_utc` is NOT true UTC year-round. Daily break sits at label 20:55→22:00 in BOTH summer and winter; real gold break is 00:00–01:00 server (IC server UTC+2 winter/UTC+3 summer, US DST). => label = server − 3h fixed. Server = label+3h. True UTC = label (summer) / label+1h (winter). ICT = server+4h (summer) / +5h (winter).
Related (not redone): R8 H4 EMA PB, R31 EMA ribbon PB, combo_mtf pin/engulf, R216 PA@SR, R198 micro PB.
Rules (all on completed bars, no lookahead):
- Trend long at bar i: C_i>EMA50_i and EMA20_i>EMA50_i (EMA on close). Short mirror.
- Pullback: bars i-k+1..i each close against trend (long: C<C_prev), k∈{2,3}, trend true at i; and within those bars low ≤ EMA20+δ·ATR14 (δ=0.25) (short: high ≥ EMA20−δ·ATR).
- Exhaustion at bar j ∈ {i, i+1} (first qualifying; trend still holds at j-1 checks at i):
  PIN long: lower wick ≥2×body and close in upper third of range; short mirror. DOJI: body ≤0.15·range (range>0).
- Entry open j+1 in trend direction. SL = exhaustion low −0.30 (long) / high +0.30 (short). TP = {1.5R,2R}. Time exit T∈{6,12} bars after entry (close of bar). SL-first on same bar. One position at a time.
- Cost $0.28 per trade round-trip per 0.01 lot ($ = price units ×1 for 0.01 oz=1). Stress 1.5×=0.42.
- Grid 16 = Candle{PIN,DOJI}×k{2,3}×TP{1.5,2}×T{6,12}. Split 60/40 by calendar day (chronological). N += 16. Z one-sided on OOS mean R; Bonferroni Z per multiple_testing.json.
- "เจอ" only if OOS E>0 after cost, OOS n≥100, Z ≥ Z_BONF, IS E>0, 1.5× cost still >0. Else ไม่เจอ.
