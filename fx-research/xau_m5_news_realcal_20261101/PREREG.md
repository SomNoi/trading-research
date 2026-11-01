# R228 PREREG — XAU M5 real-calendar news spike CONT/FADE (2026-11-01)
Locked before any result. N 6250 → 6266, Z_bonf=4.3150.
Data prep: see R227 PREREG (shared `_r227_229/prep.py`). Calendar `data/news/us_macro_calendar.csv` = REAL release dates (FRED release calendars for BLS Employment Situation & CPI incl. the 2025 shutdown-shifted dates 2025-10-24 CPI, 2025-11-20/12-16 NFP; FOMC statement days from federalreserve.gov), times = standard 08:30 ET / 14:00 ET (quality: official date, standard time, not per-release verified). In XAU sample (2025-05-14→2026-10-09): NFP 16, CPI 15, FOMC 11 → thin-n, ไม่เจอ is prior.
Explicit contrast: R221 used DOW/first-Friday PROXIES; this uses real dates.
## Rule
- XAU IC BID M5. Window = bars with open time in [event−w, event+w), w∈{5,15} min.
- Spike = first bar in window with |C−O| ≥ λ·ATR14(t−1) OR (H−L) ≥ λ·ATR14(t−1); dir = sign(C−O) (skip if 0). One trade max per event.
- Arm CONT side=dir, FADE side=−dir. Entry next M5 open. SL $5 TP $10 (chosen dim; 2R). Time stop T=12 bars (close). Cost $0.28.
- Grid 16: EventFamily{NFP, CPI∪FOMC} × Arm{CONT,FADE} × λ{1.0,1.5} × w{±5,±15}. (Deviation: requested ALL family would make 24 cells; ALL = union of the two families, not separately tested, to hold +16.)
- 60/40 split by calendar day (same cut as other rounds). PASS: OOS E>0, PF≥1.2, n≥50 (impossible here → auto-FAIL by n; reported anyway), IS E>0. EDGE needs z_oos≥Z_bonf.
