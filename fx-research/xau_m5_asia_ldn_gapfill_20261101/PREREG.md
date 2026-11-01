# R238 PREREG — XAU Asia→London gap-fill FADE
Written 2026-11-01 ~22:40 ICT before any outcome scoring. Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv, cost $0.28/0.01lot per trade, split 60/40 by unique UTC day (cut 2026-03-18). Hours UTC. LDNNY=07–19 UTC. Entry next M5 OPEN; exits SL/TP intrabar (both same bar → SL first), else close of 12th bar (T≤12). One position at a time. R = PnL/SL. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided vs Z_BONF(N). No demo.
Per UTC day: C_asia = close of last M5 with time<07:00 (must be 06:55); O_ldn = open of 07:00 bar. G=O_ldn−C_asia; ATR14 (M5 TR) at the 06:55 bar. Require |G|≥λ·ATR. Fill level F=C_asia+f·G. First M5 close in 07:00–07:55 crossing F toward C_asia (G>0: C≤F → short; G<0: C≥F → long) → entry next open. 1 trade/day.
SL_mode: beyond_open = stop at O_ldn ± 0.25·ATR beyond (dist=|entry−stop|, min $1); half_gap = dist 0.5·|G| (min $1). TP = TPmult×SL dist. T12.
Grid 16: λ{0.3,0.6} × f{0.5,0.7} × SL_mode{beyond_open,half_gap} × TPmult{1.5,2.0} (no session dim needed: window fixed). N 6410→6426.
NOT R217 open-drive CONT, NOT R55 LDN drive, not R63 UTC-day gap.
