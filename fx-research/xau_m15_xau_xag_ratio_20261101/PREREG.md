# R231 PREREG — XAU/XAG ratio z FADE, M15 (2026-11-01)
Locked before any result. N_before=6298 (+16 → 6314), Z_bonf=norm.ppf(1−0.05/6314) one-sided.
## Data (MIXED FEEDS — label): XAU = IC MT5 BID M15 (`data/cross/XAUUSD_IC_BID_M15.parquet`); XAG = Dukascopy public BID M15 close only (`data/cross/XAGUSD_DUKA_BID_M15.parquet`) — Dukascopy ≠ IC.
## Rule
- Inner-join timestamps. Ratio Rt = XAU_close/XAG_close. z=(R−SMA_W(R))/σ_W(R) (window includes bar t).
- Signal at close of bar t when |z|≥θ (touch once; re-arm after |z|<θ/2). FADE trade XAU only: z>0 → short XAU, z<0 → long XAU. Entry next XAU M15 open.
- ATR(R) = SMA14 of |ΔR| close-to-close (XAG has close only, so true range on ratio not available — documented deviation). SL$ = k·ATR(R)·XAG_close_t; TP = 2·SL. Skip if SL$<0.5.
- Flat at open of first bar at 20:00 UTC (fixed ON). Hold otherwise until SL/TP.
- Sess: any | LDNNY = signal-bar hour 07–19 UTC.
- Grid 16: W{48,96} × θ{2.0,2.5} × k{1.0,1.5} × Sess{any,LDNNY}. Arm FADE only.
- Novelty: ≠ R227 (OLS residual on DXY/US10Y/XAG returns) — pure price-ratio level z.
Data XAU IC Markets MT5 BID (2025-05-14→2026-10-09). Cost $0.28/0.01 lot per trade; R=(pnl−0.28)/SL; engine `_r227_229/eng.py` sim (entry next open, SL checked before TP intrabar, one position at a time). Split 60/40 chronological by calendar day. PASS(soft): OOS E>0, PF≥1.2, n≥50, IS E>0. EDGE requires PASS and z_oos ≥ Z_bonf (one-sided), and no IS/OOS side-flip; default verdict ไม่เจอ. No demo. R94/R227 untouched (watch-only).
