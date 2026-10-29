# XAUUSD daily-range (ADR) hypothesis: report
Prereg: prereg/XAU_ADR_PREREG.md (sha256 22951dde…, registered 2026-10-15 13:49 ICT, before any computation).
Data: Dukascopy XAU/USD M1 **mid** (bid/ask mid; spreads come from IC costs), 2019-01-01 to 2025-10-09 UTC, pre-holdout only. Holdout NOT used.
Day: IC server midnight, which is UTC+2, or UTC+3 while US DST is in effect (21:00/22:00 UTC; 04:00/05:00 ICT). Sat/Sun stub bars merge into Monday (0 found). Short day = under 18h of bars: 1 found (2025-10-10, partial/truncation), excluded. US holiday early closes still have ≥18h of bars from the prior evening, so they are kept. Same-bar ambiguous first moves: 2 days. No first move: 1 day.

## Part 1: descriptive, IN-SAMPLE, not a trial (1729 full days with ADR20)
- Daily range: median $23.86/oz, IQR $16.81–34.89. By year (median): 2019 13.67 | 2020 25.12 | 2021 21.09 | 2022 23.08 | 2023 21.00 | 2024 30.73 | 2025 45.18.
- range/ADR14 deciles 10/25/50/75/90: 0.57/0.70/0.92/1.23/1.59 (ADR20 almost identical). **Only 36.8% of days land within ±20% of ADR14** (36.3% for ADR20). Every year is 33–40%. A fixed 21:00 UTC boundary gives the same numbers (36.7%).
- First move (first side to reach 0.15×ADR14), X = whole-day excursion on that side, E = opposite extension, n=1732:
  - Hypothesis E ≈ ADR14 − X: Pearson 0.47, Spearman 0.60, median abs error $6.83 (27.7% of ADR), 14.5% of days within ±20%.
  - Naive E ≈ 0.251×ADR14 (c fitted on 2019–20): median abs error **$4.68 (17.6% of ADR)**, 10.2% within ±20%.
  - Evaluated on 2021–25: hypothesis $7.40 / 27.1% vs baseline $5.00 / 17.7%.
  - **The constant-fraction baseline beats the hypothesis on error.** The correlation is mostly common ADR scale plus the identity X+E = range.
- Failure days (X < 0.5×ADR14, 47.5% of days):
  - E reaches 50% of (ADR−X) on 64.5% of days, 75% on 43.3%, and 100% on 28.3%. Median E/(ADR−X) = 0.65.
  - Error: hypothesis $7.85 (31.5%) vs baseline $5.83 (21.5%).
- Chart: results/reports/XAU_ADR_part1.png. Data files: results/xau_adr_desc.json, xau_adr_byyear.csv, xau_adr_firstmove.parquet.

## Part 2: tradable test (18 pre-registered variants, M15 signals, M5 simulation)
Costs: IC p90 session spread, $3.50/lot/side, $0.05/oz/side slippage, swap (Wed ×3). Risk 1%. One trade per day. Exit at day end. Rollover block 20:30–24 UTC (if confirmation falls in the block, the next unblocked confirmation that day is used).
Full-period, per variant (IS+OOS, 2019-01..2025-10-09):
- Gross PF 0.88–1.11. Net PF at 1x 0.81–1.01. Best variant: (0.15, rt50, 1.0) net PF 1.008, t=0.13.
- **The `sw` confirmation is negative even before costs in all 9 variants.**
- Average cost $0.31/oz against median stops of $3.5–8.
- Full table: results/xau_adr_variants.csv.

Walk-forward, stitched OOS 2021-01..2025-10-09 (10 windows, choice switches between rt50 and sw):
| metric | value |
|---|---|
| trades | 1086 |
| win rate | 29.1% |
| gross $/oz per trade | +0.09 (gross PF 1.02, +0.012R) |
| net $/oz per trade (1x) | −0.22 |
| avg net R | −0.053 (1x), −0.086 (1.5x), −0.118 (2x) |
| PF net | 0.92 (1x) / 0.88 (1.5x) / 0.84 (2x) |
| max DD | −104R (1x) |
| worst losing streak | 16 |
| per year sumR (1x) | 2021 −38.2, 2022 −21.0, 2023 −22.8, 2024 +30.2, 2025 −6.0 |
| windows positive | 2/10 |

Multiple testing: N_TRIALS now 819 (18 added). Bonferroni z threshold 3.84; OOS t = −0.99; DSR ≈ 0.

## Verdict: FAIL, NO EDGE
Fails on: OOS years positive (1/5), PF 0.92 < 1.2, PF at 1.5x < 1, DD > 20%, streak 16 > 12. Passes only on trade count. Holdout not run (gate not met; no HOLDOUT_USED_XAU_ADR file).
Part 1 shows the premise is weak. Gold's daily range is not "fixed": only about 37% of days fall within ±20% of ADR. After a failed first move, the far side gets reached (100% of ADR−X) only 28% of the time.
