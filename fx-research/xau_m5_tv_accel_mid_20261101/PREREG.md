# R237 PREREG — XAU M5 order-flow proxy: tickvol acceleration + mid-range close, CONT
Written 2026-11-01 ~22:40 ICT before any outcome scoring. Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv, cost $0.28/0.01lot per trade, split 60/40 by unique UTC day (cut 2026-03-18). Hours UTC. LDNNY=07–19 UTC. Entry next M5 OPEN; exits SL/TP intrabar (both same bar → SL first), else close of 12th bar (T≤12). One position at a time. R = PnL/SL. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided vs Z_BONF(N). No demo.
Signal bar t: Accel2: V_t>V_{t-1}; Accel3: V_t>V_{t-1}>V_{t-2} (tick_volume). Direction: C_t>(H_t+L_t)/2 → long, C_t< mid → short (= mid-side CONT bias); C=mid skip.
Grid 16: Accel{2,3} × SL$\{4,8\} × TPmult{1.5,2.0} × Sess{any,LDNNY}. Arm CONT only. N 6394→6410.
Distinct from R204 signed surge (no tvr threshold), R185 slope, R6 climax.
