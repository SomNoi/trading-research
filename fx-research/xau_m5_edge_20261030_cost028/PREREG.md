# PREREG — XAU M5 human-behavior edge, cost $0.28 (2026-10-30, locked before results)
Data: Dukascopy XAUUSD M1 parquet → Asia/Bangkok, ≥2022-01-01, resampled 5min (left/left; O first, H max, L min, C last, V sum).
Sessions (BKK): ASIA 05:00–13:00, LDN 14:00–19:00, NY 19:30–23:30. Signal & entry bar both in-session. Entry next M5 open. No lookahead.
Exits: SL $3.5, TP 1.5R, time stop 25 M5 bars. Cost $0.28/oz RT. One position at a time per hyp. No martingale.
Splits: IS 2022–2023; OOS 2024→data end; Recent 2025→end.
## M5 thresholds (25 families, same names as M1)
01/02 Asia H/L sweep (first per day, LDN/NY, wick beyond close back) · 03/04 equal H/L sweep: 30-bar window, tol $0.5, ≥2 touches · 05/06 PDH/PDL fake (first per day) · 07 fractal 3-bar hunt
08 big-bar rejection: prior bar range >$5.0, close back past its mid · 09 3-bar run >$8 then opposite bar · 10 pin: range ≥$1.5, wick ≥70%, close in outer third · 11/12 wick ≥50% after 5-bar move >$5, range ≥$1.0 · 13 expansion fade: range >2× median20 & ≥$1.5 · 14 double expansion fade
15/16 LDN/NY first FVG (gap ≥$0.5) in 14:05–14:30 / 19:35–20:00, fade · 17/18 LDN/NY 15-min drive >$3.5 fade (evaluated on bar 14:10/19:40 close) · 19 Asia drive >$2.5 fade · 20 session-open gap vs prior close >$0.75 fill
21 EMA20 dev >1.5 ATR14 · 22 session VWAP dev >1.5 ATR · 23 EMA dev >2.5 ATR · 24 EMA dev >2.0 ATR · 25 8-bar streak fade
## Kill bar (all on OOS)
PF>1.25, WR>48% (R:R≥1.3), net>0, maxDD<25% of net, n>150; sensitivity entry ±2 bars and SL ±$0.5 all PF>1.15. Else NO EDGE. Research only; NOT a live signal.
Trials: 25 × (1 base + 4 sens) = 125 (+8 per base survivor grid).
