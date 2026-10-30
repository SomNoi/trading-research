# PREREG — XAU H1 human-behavior edge, cost $0.28 (2026-10-30, locked before results)
Data: Dukascopy XAUUSD M1 parquet → Asia/Bangkok, ≥2022-01-01, resampled 1h (left/left; O first, H max, L min, C last, V sum).
Why not data/htf/XAUUSD_H1.parquet: it covers ≥2019 but ENDS 2025-10-09 (UTC) — one year stale vs M1 (to 2026-10-10). M1 resample keeps parity with M1/M5 runs.
Sessions (BKK), H1 bar is in session if its OPEN time falls in: ASIA 05:00–13:00 (bars 05..12), LDN 14:00–19:00 (bars 14..18), NY 19:30–23:30 (bars 20..23; 19:00 bar NOT in NY).
Signal & entry bar both in-session. Entry next H1 open. No lookahead. Asia high/low = H1 bars with open in Asia window that day.
Exits: SL $3.5 (LOCKED, kept for apple-to-apple kill parity with M1/M5; many stop-outs expected on H1 ranges), TP 1.5R, time stop 25 H1 bars. Cost $0.28/oz RT. One position at a time. No martingale.
Splits: IS 2022–2023; OOS 2024→data end; Recent 2025→end.
## H1 thresholds (25 families, same names as M1/M5)
01/02 Asia H/L sweep (first per day, LDN/NY bars) · 03/04 equal H/L sweep: 25-bar window, tol $1.0, ≥2 touches · 05/06 PDH/PDL fake (first per day) · 07 fractal 3-bar hunt
08 big bar: prior range >$12, close back past its mid · 09 3-bar run >$20 then opposite bar · 10 pin: range ≥$4, wick ≥70%, close outer third · 11/12 wick ≥50% after 5-bar move >$12, range ≥$2 · 13 expansion: range >2× median20 & ≥$4 · 14 double expansion fade
15/16 LDN/NY first FVG (gap ≥$1.0) whose 3rd bar is in first 2 H1 of session (LDN 14,15 / NY 20,21), fade · 17/18 LDN/NY drive: first session H1 bar (14:00 / 20:00) close−open >$8, fade at next open · 19 Asia drive first H1 (05:00) >$5 fade · 20 session-open gap (bars 05/14/20 open vs prior close) >$1.5 fill
21 EMA20 dev >1.5 ATR14 · 22 session VWAP dev >1.5 ATR · 23 EMA dev >2.5 ATR · 24 EMA dev >2.0 ATR · 25 8-bar streak fade
## Kill bar (all on OOS) — identical to M1/M5
PF>1.25, WR>48%, net>0, maxDD<25% of net, n>150; sensitivity entry ±2 bars and SL ±$0.5 all PF>1.15. Else NO EDGE. Research only; NOT a live signal.
Trials: 25 × 5 = 125 (+8 per base survivor grid). N_TRIALS 1330→1455.
