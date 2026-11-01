# R239 PREREG — M15 variance-ratio regime → M5 FADE/CONT entry
Written 2026-11-01 ~22:40 ICT before any outcome scoring. Data IC BID data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv, cost $0.28/0.01lot per trade, split 60/40 by unique UTC day (cut 2026-03-18). Hours UTC. LDNNY=07–19 UTC. Entry next M5 OPEN; exits SL/TP intrabar (both same bar → SL first), else close of 12th bar (T≤12). One position at a time. R = PnL/SL. Soft PASS: PF_OOS≥1.2, n_OOS≥50, E_IS>0, E_OOS>0. Z one-sided vs Z_BONF(N). No demo.
Definition (single): Lo-MacKinlay VR(q=4) on completed M15 log-close returns over rolling W M15 bars: VR=Var(4-bar ret)/(4·Var(1-bar ret)). Regime from last COMPLETED M15 (no lookahead). MR if VR≤0.9; TREND if VR≥1.1; else no trade.
M5 entry: MR → FADE first bar with |z|≥θ, z=(C−SMA20)/SD20 (prev |z|<θ); short if z>0, long if z<0. TREND → CONT first break: C_t>H_{t-1} (prev bar C_{t-1}≤H_{t-2}) with SMA20 slope (SMA20_t−SMA20_{t-3})>0 → long; symmetric short.
Grid 16: W{64,128} × θ{2.0,2.5} × SL$\{4,8\} × Sess{any,LDNNY}. TP=2×SL, T12. Arm implied by regime (both in one stream; per-arm split reported). N 6426→6442.
Distinct from R61 (level only), R122 (VR trade), R163 (Hurst-diff).
