# USDJPY M5 range-expansion breakout + HTF filters: REPORT

**Verdict: CLEAR FAIL. No variant meets the full pass bar, so there is NO finalist and the 12-month holdout was NOT run (it remains unused).** results/HOLDOUT_USED_USDJPY_REB does not exist.

- Pre-registration: prereg/USDJPY_REB_HTF_PREREG.md (sha256 0792ebd5…, registered 2026-10-11T07:26:43Z = 14:26 ICT), written before any filter run.
- Variants:
  - V0 = base (Track B B2; existing trials, not re-logged).
  - V1 = + H1 EMA200 direction filter.
  - V2 = + H4 fractal swing structure (2 bars each side, HH+HL / LH+LL).
  - V3 = both filters.
  - Each variant has 4 base params; walk-forward selection; 12 new trials.
- Costs: Kai's file (USDJPY p90 2 points, commission $7 RT, 0.1 pip slippage per side). Walk-forward: same 10 non-overlapping OOS windows as Track B. Flat 1% risk.
- Caveat: the base parameters were chosen after seeing 2019–2025 data, so only the holdout would be a clean test. It was not run because no finalist exists.
- Multiple testing: 620 trials in total; Bonferroni t threshold 3.77.
- Pre-registered finalist rule: a variant must meet the full bar; among passers, take the highest OOS t-stat. Result: finalist = None.

## OOS results (after costs)

| strategy    |   n |    win |    pf |   pf_1_5x |   pf_2x |   exp_R |   maxdd_pct |   worst_streak |   tstat | t_vs_bonf   |   dsr_strict |   dsr_pooled | years_pos   | wf_pos   | passes   | failed                                                       |
|:------------|----:|-------:|------:|----------:|--------:|--------:|------------:|---------------:|--------:|:------------|-------------:|-------------:|:------------|:---------|:---------|:-------------------------------------------------------------|
| REB_V3_F1F2 | 207 | 50.242 | 1.561 |     1.477 |   1.398 |   0.194 |     -12.43  |              7 |   1.456 | 1.46/3.77   |            0 |            0 | 4/5         | 6/10     | False    | positive expectancy every OOS year, >=300 OOS trades         |
| REB_V2_F2   | 272 | 47.794 | 1.313 |     1.23  |   1.154 |   0.121 |     -12.176 |              9 |   1.087 | 1.09/3.77   |            0 |            0 | 5/5         | 7/10     | False    | >=300 OOS trades                                             |
| B2_range_bo | 996 | 42.57  | 1.281 |     1.204 |   1.134 |   0.117 |     -31.397 |             12 |   1.793 | 1.79/3.77   |            0 |            0 | 4/5         | 7/10     | False    | positive expectancy every OOS year, max DD <= 20% at 1% risk |
| REB_V1_F1   | 497 | 46.278 | 1.251 |     1.176 |   1.107 |   0.099 |     -23.694 |              8 |   1.354 | 1.35/3.77   |            0 |            0 | 4/5         | 8/10     | False    | positive expectancy every OOS year, max DD <= 20% at 1% risk |

## Per year (OOS, 1x)

|    y |   REB_V3_F1F2 n |   REB_V3_F1F2 exp_R |   REB_V2_F2 n |   REB_V2_F2 exp_R |   B2_range_bo n |   B2_range_bo exp_R |   REB_V1_F1 n |   REB_V1_F1 exp_R |
|-----:|----------------:|--------------------:|--------------:|------------------:|----------------:|--------------------:|--------------:|------------------:|
| 2021 |              46 |               0.232 |            64 |             0.008 |             197 |               0.165 |           119 |             0.091 |
| 2022 |              42 |               0.16  |            62 |             0.035 |             179 |               0.154 |            94 |             0.067 |
| 2023 |              48 |              -0.054 |            56 |             0.017 |             211 |              -0.022 |           101 |            -0.053 |
| 2024 |              35 |               0.054 |            46 |             0.129 |             232 |               0.072 |            99 |             0.178 |
| 2025 |              36 |               0.653 |            44 |             0.529 |             177 |               0.249 |            84 |             0.239 |

## Reading
- **Filters improve quality but cut breadth.**
  - V3 (both filters): PF 1.56, DD −12%, but only 207 trades (fewer than the 300 required) and 2023 negative.
  - V2 (H4 structure): PF 1.31 / 1.23 / 1.15 and 5 of 5 years positive, but 272 trades (fails ≥300 only).
  - V1 (H1 EMA): 2023 negative and DD −23.7%.
- **No t-stat comes near the Bonferroni threshold** (all ≤ 1.8 vs 3.77), and DSR is 0. After 620 trials this is indistinguishable from selection noise.
- Per-regime breakdowns are in results/reports/REB_V*_USDJPY.md and B2_range_bo_USDJPY.md.
