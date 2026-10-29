# XAUUSD M5 fuzzy-pattern scalp: report (no lookahead)
- **Pre-registration:** prereg/XAU_FUZZY_PREREG.md, sha256 ecede349…, registered 2026-10-15T19:19:27Z (02:19 ICT Oct 16), before any 2023+ data was loaded.
- **Data:** Dukascopy XAU/USD M1 **mid**, resampled to M5/H1 (UTC, label left). IS 2019-01..2022-12 (fit 2019–21, select on 2022). OOS 2023-01-01..2025-10-09, touched once. **Holdout 2025-10-10+ not used.**
- **Costs:** Kai's IC model = session p90 spread + $0.05/oz/side slippage + $0.07/oz commission, plus swap.
  - Round trip by session (UTC): Asia 0.29, London 0.28, overlap 0.27, NY 0.32, rollover 0.57 $/oz.
  - Each trade uses the average of its entry and exit session spreads.
  - 0.01 lot = 1 oz.
- **Method:**
  - Shapes of 3 or 5 bars, OHLC relative to the first bar's open, divided by ATR14.
  - k-means (64 clusters) or kNN (k=100), fit on 2019–21 and then frozen.
  - The threshold is set to give 4 or 5 raw signals per day on the fit period.
  - Context filter: none, trend (M5 EMA55 and H1 EMA55 agree, completed bars only), or high-ATR.
  - 4 exits: $0.48/$0.48 with a 3-bar stop; 1/1 ATR with 6 bars; 1.5/1 ATR with 12 bars; $1/$1 with 6 bars.
  - Entry at the next bar open, one position at a time, rollover block (20:30–24 UTC) on.
- **Search budget:** fixed at 96 configurations, all logged as FUZZY trials. Only 84 are distinct: k-means scores are discrete, so the 4/day and 5/day thresholds came out identical for k-means. Total trials are now 917 (Bonferroni z 3.87).

## IS (2019–2022)
- Unfiltered signals ran 4.1–4.5/day on fit and 3.7–4.1/day on 2022, close to the 4–5/day request.
- Net $/trade at 1x was negative in **95/96 configs on fit and 96/96 on validation 2022**. The best validation config was −$0.002.
- Gross was positive in 34/96 validation configs, but never by enough to cover about $0.29 of cost.
- **Selected finalist:** KM, L=3, trend filter, exit 1.5 ATR TP / 1 ATR SL / 12 bars. The pre-declared top 3 also included the 5/day duplicate and KM, L=3, high-ATR filter, same exit.

## OOS 2023-01..2025-10-09 (finalist, touched once)
| Metric | IS 2019–22 | OOS |
|---|---|---|
| Trades (per day) | 1518 (1.22) | 974 (1.13) |
| Win % | 42.6 | 39.6 |
| Gross $/trade (0.01 lot) | +0.128 | −0.040 |
| Net $/trade at 1x | −0.159 | −0.329 |
| Cumulative net $ | −242 | −320 |
| PF gross / net 1x / 1.5x / 2x | 1.17 / 0.82 | 0.97 / 0.75 / 0.67 / 0.59 |
| Max DD $ (0.01 lot) | −249 | −382 |
| Max DD at 1% risk | — | −227% |
| Worst losing streak | 10 | 12 |

- **OOS per year (net $):** 2023 −89 (358 trades), 2024 −225 (368), 2025 −6 (248).
- **Busiest hours (ICT):** 08, 19, 20, 21, 13.
- **Sample week 2024-03-04 (OOS):** Mon 3, Tue 3, Wed 0, Thu 3, Fri 4.
- The trend filter cuts the actual rate to about 1.1/day. Unfiltered configs did hit 4–5/day, but lost even more on validation (about −$0.15 to −$0.40 per trade).
- **High-ATR top-3 config, OOS:** 1857 trades (2.15/day), net −$0.35/trade, cumulative −$650, PF 0.78. Every year negative.
- **Net per trade clears +$0.20 per 0.01 lot? NO** (−$0.33).

## Verdict: NO EDGE
The finalist fails the pass bar on every OOS year being negative, PF 0.75 against the 1.2 required, and drawdown. Holdout not run.
At the 4–5/day frequency, about $0.28–0.32 of round-trip cost per trade is far larger than any pattern-predictable move in M5 gold.

Files:
- scripts/xau_fuzzy.py
- results/xau_fuzzy_is.csv
- results/xau_fuzzy_selection.json
- results/xau_fuzzy_oos.json
- results/xau_fuzzy_models.pkl
