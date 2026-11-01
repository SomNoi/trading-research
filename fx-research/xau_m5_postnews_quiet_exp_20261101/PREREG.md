# R232 PREREG — Post-news quiet → first expansion CONT, XAU M5 (2026-11-01)
Locked before any result. N_before=6314 (+16 → 6330), Z_bonf=norm.ppf(1−0.05/6330) one-sided.
## Rule
- Events: `data/news/us_macro_calendar.csv` (real FRED/Fed dates, R228). t0 = event UTC. ATR = ATR14 (M5, Wilder-free SMA of TR) at last bar closing ≤ t0.
- Quiet: every M5 bar starting in [t0+15m, quietEnd) has range < φ·ATR, φ=1.0 fixed. Require ≥2 such bars present; else skip event.
- Expansion: first bar starting in [quietEnd, t0+120m) with range ≥ λ·ATR → CONT sign(C−O) (skip if doji). Entry next open. SL $SL, TP 3·SL, time exit T=12 bars. Max 1 trade/event.
- Grid 16: quietEnd{t0+30m,t0+45m} × λ{1.0,1.5} × SL{$2,$4} × Event{NFP∪CPI, ALL (incl. FOMC)} = 16. Sess any.
- Novelty: ≠ R228 (first spike inside ±5/15m) — post-release quiet then later expansion.
Data XAU IC Markets MT5 BID (2025-05-14→2026-10-09). Cost $0.28/0.01 lot per trade; R=(pnl−0.28)/SL; engine `_r227_229/eng.py` sim (entry next open, SL checked before TP intrabar, one position at a time). Split 60/40 chronological by calendar day. PASS(soft): OOS E>0, PF≥1.2, n≥50, IS E>0. EDGE requires PASS and z_oos ≥ Z_bonf (one-sided), and no IS/OOS side-flip; default verdict ไม่เจอ. No demo. R94/R227 untouched (watch-only).
