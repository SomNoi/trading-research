# PREREG — Round 11 xau_m5_usdjpy_residual_20261031 (locked before any run)
Distinct from INDEX `10_xpair_residual` (FAIL, PF 0.71–0.85): that round was cross-pair residual reversion on 4 FX pairs, NOT XAU.
This round: XAUUSD residual vs USDJPY beta, IC MT5 M5 BID, traded on XAUUSD ONLY (USDJPY is a regressor, never traded).
Data: data/ic-mt5-2026-10-10/csv/{XAUUSD,USDJPY}_M5.csv, inner-joined on time_utc. IS first 60% joined bars, OOS last 40%.
Returns: log close-to-close. beta_t = trailing 288-bar OLS of r_xau on r_jpy using bars ≤ t only (cov/var). e_t = r_xau - beta_t*r_jpy.
z_t(k) = sum(e_{t-k+1..t}) / (std_288(e) * sqrt(k)), trailing only.
Grid (12, frozen): k∈{6,12} × thr∈{1.5,2.0,2.5} × mode∈{rev (z≥thr short, z≤-thr long), mom (opposite)}.
Entry: signal at bar t close → XAU open t+1. One position. Exit SL$3.5, TP 1.5R, time 5 bars. Cost $0.28 RT. Session any.
One OOS pass. PASS (desk): OOS PF≥1.25, n≥150, E>0, PF@1.5x cost>1, sens min PF>1 (SL{3,4}×R{1.25,1.75}), MDD≤25% (1% risk), IS PF>1. Else ไม่เจอ.
