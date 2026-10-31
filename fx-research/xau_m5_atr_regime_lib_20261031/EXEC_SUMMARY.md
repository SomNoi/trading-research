# xau_m5_atr_regime_lib_20261031 — ไม่เจอ (no edge found)
Fleet task xau-m5-atr-regime-lib-20261031. Data: IC MT5 BID XAUUSD M5 (2025-05-14 to 2026-10). Cost $0.28/oz RT. Split 60/40 by time; OOS starts 2026-03-19 03:05 UTC. PREREG sha256 c9d54855…4cab, read-only.
- **0/16 pass.** No arm reaches OOS PF≥1.25 with n≥150. IS PF is below 1 in all 16 cells.
- Best OOS PF is Q4 FADE κ1.2 LDN∪NY: 1.21, n=86 (0.59/day), but IS PF is 0.75. This fails n, PF, and IS.
- Best cell with n≥150: Q4 FADE κ0.8 LDN∪NY, OOS PF 1.05 with n=157. PF at 1.5× cost is 0.98.
- The goal of a higher fire rate was met by CONT (4–9 trades/day OOS), but every CONT cell has OOS PF 0.64–0.82. Impulse continuation over 5 bars loses after cost in both low and high ATR.
- FADE is close to breakeven (0.93–1.21) but fires too rarely and has IS PF<1 everywhere.
- N_TRIALS 2791→2807, Z_BONF 4.134. See results/summary.csv and results/best_equity.png.
## How this differs from earlier rounds
- motif5 mined 7-symbol 5-bar codes in hindsight. This study uses fixed, rule-defined 3-bar impulse/exhaustion patterns and mines nothing.
- R1 (open imbalance) and R2 (VWAP bands) used session anchors and fired about once a day. This study has no anchor, uses ATR-percentile regime libraries, and fires many times a day.

