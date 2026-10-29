# EXEC — Morning/Evening Star (XAUUSD M5) — FAIL / NO EDGE
- Prereg locked first (sha 665bca26…), params frozen from 70% discovery (sha 37a71cc2…), then 30% internal holdout.
- Two sets: V0 (pure 3-bar star), V1 (+ EMA5 prior-trend filter). ~10k / ~6k signals total.
- Direction hit rate ≈ 47–50% at every horizon (coin flip or slightly worse).
- MFE ≈ MAE (~$3.5 median in holdout): price moves equally both ways after the star.
- After $0.28/oz cost, holdout PF 0.76–0.80; negative every year; worse at 1.5x cost.
- Trend filter did not help. Verdict both sets: NO EDGE. Not a live signal.
- Trials 937→943; Z_BONF 3.876. Full: classic_candles/MES_REPORT.md
