# R229 PREREG — HTF trend+structure bias → M15 pullback + swing-break entry (2026-11-01)
Locked before any result. N 6266 → 6282, Z_bonf=4.3156.
Data prep: R227 PREREG (XAU IC BID M5 → M15/H1/H4 resample).
## ONE clean rule (pullback + M15 swing break; the Donchian/ADX alternative NOT used)
- Bias TF ∈ {H1,H4}, completed bars only. Pivots L=3 (high > 3 bars each side), confirmed 3 bars after. BULL if close>EMA55 AND last confirmed pivot high > prior pivot high AND last pivot low > prior pivot low (HH+HL). BEAR mirror. Else neutral. Bias applies to M15 bars from the next HTF bar open.
- M15 (BULL): ext = running max high since bias start / last signal. Pullback armed when ext − low_t ≥ φ·ATR14_M15(t−1) AND low_t ≤ midpoint of last completed bias-TF bar ("half-range"). After armed: first M15 close > most recent confirmed M15 pivot high (L=3) → long at next M15 open; then reset ext=high, disarm. BEAR mirror.
- SL ${5,10}, TP 2·SL, time stop 24 M15 bars, one position, cost $0.28. Sess: any | signal hour 07–19 UTC.
- Grid 16: TF{H1,H4} × φ{1.0,2.0} × SL{5,10} × Sess{any,LDNNY}.
- Report expectancy in $/0.01 lot (goal context $5–10 post-cost). 60/40 by day. PASS: OOS E>0, PF≥1.2, n≥50, IS E>0; EDGE z_oos≥Z_bonf.
- ≠ R8 (H4 EMA PB M5 reclaim), ≠ xau_h1_m5_structure (BOS+engulf), ≠ R222 (H1 EMA + M5 micro).
