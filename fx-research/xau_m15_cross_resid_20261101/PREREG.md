# R227 PREREG — XAU M15 cross-asset residual FADE (SYNTH_DXY + US10Y + XAG), R:R 1:2 (2026-11-01)
Locked before any result computed. N_before=6234, +16 → 6250, Z_bonf=norm.ppf(1-0.05/6250)=4.3145 (one-sided).
## Data prep (shared R227–R229; script `_r227_229/prep.py`)
- XAU: IC Markets MT5 BID M5 `data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv` (2025-05-14→2026-10-09) resampled left-closed to M15/H1/H4 → `data/cross/XAUUSD_IC_BID_{M15,H1,H4}.parquet`.
- SYNTH_DXY (≠ ICE DX): 50.14348112·EURUSD^-0.576·USDJPY^0.136·GBPUSD^-0.119·USDCAD^0.091·USDCHF^0.036; **SEK leg (0.042) dropped – no USDSEK data**; AUDUSD not an ICE component, unused. Dukascopy M1 closes→M15 last. USDCAD/USDCHF local parquet ended 2025-10-09 → extended with Dukascopy public freeserv BID M1 (`data/cross/USD{CAD,CHF}_M1_ext_bid.parquet`). Mixed mid/bid FX feed; for returns immaterial. → `data/cross/SYNTH_DXY_M15.parquet`.
- XAG: Dukascopy public BID M1 (XAG/USD) 2025-05→2026-10 fetched OK → M15 `data/cross/XAGUSD_DUKA_BID_M15.parquet`. Yahoo SI=F daily only (intraday not available for span) – not used.
- US10Y: Yahoo ^TNX daily close (`data/cross/US10Y_TNX_daily_yahoo.csv`); bar value = close of the **previous** UTC date (no lookahead); ΔUS10Y nonzero only on first bar of a new date (weak intraday regressor – documented).
- News calendar (R228) `data/news/us_macro_calendar.csv`: real dates from FRED release calendars (BLS Empsit rid=50, CPI rid=10) and federalreserve.gov FOMC page; 08:30 ET / 14:00 ET → UTC with DST.
## Rule
- M15 XAU IC BID; intersection of timestamps with DXY, XAG (NaN return if any missing or a gap ≠15 min).
- r = log returns of completed bars. Rolling OLS (with intercept) r_XAU ~ r_DXY + ΔUS10Y + r_XAG over previous W bars (coefficients estimated on bars t−W..t−1, applied to bar t). e_t residual; σ_e = std of in-window residuals; z=e_t/σ_e.
- Lead/lag DXY filter: FIXED OFF ("ignore" branch) to keep grid=16.
- Signal at close of bar t when |z|≥θ (touch once; re-arm after |z|<θ/2). FADE: side = −sign(z). Entry next M15 open. SL $SL, TP $2·SL (bar-level; SL checked first if both). Flat at open of first bar at 20:00 UTC after entry (else hold). One position at a time. Cost $0.28/0.01 lot per trade. R=(pnl−0.28)/SL; $ per 0.01 lot = pnl−0.28.
- Sess: any | LDN∪NY = signal bar hour 07–19 UTC.
- Grid 16: W{64,128} × θ{1.5,2.0} × SL{$8,$15} × Sess{any,LDNNY}. Arm=FADE only.
- Split 60/40 by calendar day. PASS: OOS E>0, PF≥1.2, n≥50, IS E>0; EDGE requires also z_oos ≥ Z_bonf.
- ≠ R126 basket residual (M15, yields, XAG, big SL); ≠ R226 (USDJPY M5 3R).
