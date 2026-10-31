# xau_m5_h4_ema_pullback_20261031 — Round 8: H4 EMA50 bias + M5 EMA20 reclaim
Verdict: **ไม่เจอ**. 0 of 16 cells pass.
- All 16 cells lose in both IS (PF 0.83–0.88) and OOS (PF 0.83–0.88).
- Best OOS: δ any, H12, any session, slope off. PF 0.878, n=3196 (~22/day), E -$0.27/trade, WR 40%, IS PF 0.85. It still loses at $0.42 cost and at every SL/R sensitivity setting (min PF 0.78). MDD 94% at 1% risk.
- The δ, session, and slope filters change almost nothing (spread ±0.03 PF). The bias plus reclaim adds no edge over the cost.
- How it differs from combo_mtf: H4 EMA50 instead of H1 EMA55, and the entry is a mechanical EMA20 touch-and-reclaim with no pin or engulf pattern. Both still fail.
- N_TRIALS 2865→2881. OOS starts 2026-03-19 03:05 UTC.
