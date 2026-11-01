# R217 PREREG — Opening-drive first bar > κ·ATR14 → CONT, IC BID, 3R
Data: IC BID XAUUSD_M5 (data/ic-mt5-2026-10-10). Label IC BID.
Signal: session open bar (LDN 07:00 UTC, NY 12:00 UTC). TR(first bar) ≥ κ·ATR14 (SMA of TR over prior 14 bars, excl. signal bar).
Dir = sign(C−O); doji skip. Enter next bar open. SL $2, TP $6, both-hit same bar → SL. Time stop: close of bar Hold (T3=15m, T6=30m). Cost $0.28/trade. R=(pnl−0.28)/2.
Grid 16: Sess{LDN,NY} × κ{1.0,1.5} × Hold{T3,T6} × Filter{any, close_beyond_mid (close in dir half of bar range)}. CONT only. 1 trade/session-open.
Split 60/40 by calendar day (IS first 60% days). Z one-sided on OOS mean R. MT N 6074→6090; Bonferroni z threshold at N=6090.
Pass: OOS E>0, z ≥ Z_BONF, n≥100. Else ไม่เจอ. Distinct from R55/R58 (full-session), R195 (LDN15 FADE), R175 (hour-open).
