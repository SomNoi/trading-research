# R240 PREREG — London PM gold auction (15:00 London) drift CONT
Written 2026-11-01 ~22:45 ICT before any outcome scoring. Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (time_utc treated as UTC); London clock via zoneinfo Europe/London (DST-aware; bar start London = UTC→London). Cost $0.28/0.01lot RT. Split 60/40 by unique UTC day (same cut as R237–R239). Entry at bar OPEN; SL/TP intrabar, both in same bar → SL first; else time exit at stated bar close. R=PnL/SL-distance. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided vs Z_BONF(N). Prefer ไม่เจอ. No demo.
Data span 2025-05→2026-10 ⇒ entirely post-2015 electronic LBMA auction era (ICE, since 2015-03-20).
ATR_L = SMA_L true range, lagged (value of bar before the auction bar).
Auction bar A = M5 bar with London start 15:00 (covers 15:00–15:05). Mark = last bar with London start ≤14:50 (close at 14:55) — informational.
Signal: |C_A−O_A| ≥ λ·ATR_L → dir = sign(C_A−O_A). Entry OPEN of 15:05 London bar. SL: long L_A−0.30, short H_A+0.30. TP: 1.5R or none (exit_1530_only). Time exit: close of the 15:25 London bar (=15:30 close). Max 1 trade/day (the 2-losses-same-day cap is thus inert).
Grid 16 = λ{0.3,0.5} × Arm{CONT_both, SHORT_only} × TP{1.5R, exit_1530_only} × ATR_L{14,20}.
N 6442 → 6458. Distinct from session-drive / halfhour-drive (clock bar is the LBMA PM auction fixed in London time, DST-aware).
