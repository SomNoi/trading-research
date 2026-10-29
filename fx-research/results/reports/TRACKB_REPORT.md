# Track B: M5 low-cost FX with an IS gate. REPORT

**Verdict: 0 of 12 system/symbol candidates pass the full bar.**

- Pre-registration: prereg/TRACK_A_B_PREREG.md (sha256 7ee2d001…, registered 2026-10-11T05:12:04Z = 12:12 ICT).
- Costs: Kai's p90 file plus $7 RT commission and 0.1 pip slippage per side; flat 1% risk.
- Walk-forward: 10 non-overlapping OOS windows, 2021-01..2025-10-09. Holdout untouched.
- Multiple testing: 584 trials in total (Track B adds 48); Bonferroni t threshold 3.76.

## Gate (IS 2019-01..2020-12)

A param passes when mean gross per trade ≥ 2 × mean round-trip cost and IS n ≥ 30. Every param was logged as a trial, whether or not it passed.

Survivors went on to the walk-forward, which chose only among gate-passing params:
- EURUSD B1 (3 of 4 params passed)
- USDJPY B2 (4 of 4)
- USDJPY B3 (1 of 4)

| system        | symbol   | param               |   is_n |   is_gross_mean |   is_cost_mean |   ratio | gate_pass   |
|:--------------|:---------|:--------------------|-------:|----------------:|---------------:|--------:|:------------|
| B1_ldn_mom    | EURUSD   | ('B1', 0.5, 12)     |    304 |        3e-05    |       0.0001   |    0.3  | False       |
| B1_ldn_mom    | EURUSD   | ('B1', 0.5, 16)     |    304 |        0.000248 |       0.000102 |    2.42 | True        |
| B1_ldn_mom    | EURUSD   | ('B1', 1.0, 12)     |    133 |        0.000421 |       0.0001   |    4.21 | True        |
| B1_ldn_mom    | EURUSD   | ('B1', 1.0, 16)     |    133 |        0.000685 |       0.000102 |    6.7  | True        |
| B2_range_bo   | EURUSD   | ('B2', 0.3, 'opp')  |    487 |       -3.2e-05  |       0.000102 |   -0.31 | False       |
| B2_range_bo   | EURUSD   | ('B2', 0.3, 'half') |    487 |       -1.5e-05  |       0.000102 |   -0.15 | False       |
| B2_range_bo   | EURUSD   | ('B2', 0.5, 'opp')  |    406 |       -4.3e-05  |       0.000102 |   -0.42 | False       |
| B2_range_bo   | EURUSD   | ('B2', 0.5, 'half') |    406 |       -7e-05    |       0.000102 |   -0.69 | False       |
| B3_overnight  | EURUSD   | ('B3', 'mom', 0.0)  |    414 |       -0.000135 |       0.0001   |   -1.35 | False       |
| B3_overnight  | EURUSD   | ('B3', 'mom', 0.25) |    226 |       -4.2e-05  |       0.0001   |   -0.42 | False       |
| B3_overnight  | EURUSD   | ('B3', 'rev', 0.0)  |    414 |        0.000126 |       0.0001   |    1.26 | False       |
| B3_overnight  | EURUSD   | ('B3', 'rev', 0.25) |    226 |        3.1e-05  |       0.0001   |    0.31 | False       |
| B4_rsi2_trend | EURUSD   | ('B4', 1, '5/95')   |   1825 |        4.2e-05  |       0.0001   |    0.42 | False       |
| B4_rsi2_trend | EURUSD   | ('B4', 2, '5/95')   |   1654 |        4.4e-05  |       0.0001   |    0.43 | False       |
| B4_rsi2_trend | EURUSD   | ('B4', 1, '10/90')  |   3155 |        1.8e-05  |       0.0001   |    0.18 | False       |
| B4_rsi2_trend | EURUSD   | ('B4', 2, '10/90')  |   2831 |        2.2e-05  |       0.0001   |    0.22 | False       |
| B1_ldn_mom    | USDJPY   | ('B1', 0.5, 12)     |    232 |       -0.000986 |       0.011531 |   -0.09 | False       |
| B1_ldn_mom    | USDJPY   | ('B1', 0.5, 16)     |    232 |        0.004927 |       0.011992 |    0.41 | False       |
| B1_ldn_mom    | USDJPY   | ('B1', 1.0, 12)     |     79 |        0.007161 |       0.011524 |    0.62 | False       |
| B1_ldn_mom    | USDJPY   | ('B1', 1.0, 16)     |     79 |        0.020586 |       0.011986 |    1.72 | False       |
| B2_range_bo   | USDJPY   | ('B2', 0.3, 'opp')  |    463 |        0.025396 |       0.01199  |    2.12 | True        |
| B2_range_bo   | USDJPY   | ('B2', 0.3, 'half') |    463 |        0.030418 |       0.011938 |    2.55 | True        |
| B2_range_bo   | USDJPY   | ('B2', 0.5, 'opp')  |    363 |        0.040875 |       0.01204  |    3.39 | True        |
| B2_range_bo   | USDJPY   | ('B2', 0.5, 'half') |    363 |        0.024598 |       0.011915 |    2.06 | True        |
| B3_overnight  | USDJPY   | ('B3', 'mom', 0.0)  |    414 |        0.016851 |       0.011552 |    1.46 | False       |
| B3_overnight  | USDJPY   | ('B3', 'mom', 0.25) |    197 |        0.027979 |       0.011549 |    2.42 | True        |
| B3_overnight  | USDJPY   | ('B3', 'rev', 0.0)  |    414 |       -0.011352 |       0.011552 |   -0.98 | False       |
| B3_overnight  | USDJPY   | ('B3', 'rev', 0.25) |    197 |       -0.023032 |       0.011549 |   -1.99 | False       |
| B4_rsi2_trend | USDJPY   | ('B4', 1, '5/95')   |   1812 |        0.002673 |       0.01158  |    0.23 | False       |
| B4_rsi2_trend | USDJPY   | ('B4', 2, '5/95')   |   1671 |        0.002662 |       0.011585 |    0.23 | False       |
| B4_rsi2_trend | USDJPY   | ('B4', 1, '10/90')  |   3106 |        0.002753 |       0.011578 |    0.24 | False       |
| B4_rsi2_trend | USDJPY   | ('B4', 2, '10/90')  |   2849 |        0.003211 |       0.011582 |    0.28 | False       |
| B1_ldn_mom    | AUDUSD   | ('B1', 0.5, 12)     |    249 |        0.000155 |       0.0001   |    1.55 | False       |
| B1_ldn_mom    | AUDUSD   | ('B1', 0.5, 16)     |    249 |        0.000135 |       0.000102 |    1.32 | False       |
| B1_ldn_mom    | AUDUSD   | ('B1', 1.0, 12)     |     69 |        0.000115 |       0.0001   |    1.15 | False       |
| B1_ldn_mom    | AUDUSD   | ('B1', 1.0, 16)     |     69 |        0.000198 |       0.000102 |    1.93 | False       |
| B2_range_bo   | AUDUSD   | ('B2', 0.3, 'opp')  |    468 |        8e-06    |       0.000102 |    0.08 | False       |
| B2_range_bo   | AUDUSD   | ('B2', 0.3, 'half') |    468 |        3.9e-05  |       0.000102 |    0.38 | False       |
| B2_range_bo   | AUDUSD   | ('B2', 0.5, 'opp')  |    373 |        4.7e-05  |       0.000102 |    0.46 | False       |
| B2_range_bo   | AUDUSD   | ('B2', 0.5, 'half') |    373 |       -4.1e-05  |       0.000102 |   -0.41 | False       |
| B3_overnight  | AUDUSD   | ('B3', 'mom', 0.0)  |    414 |        1.8e-05  |       0.0001   |    0.18 | False       |
| B3_overnight  | AUDUSD   | ('B3', 'mom', 0.25) |    212 |        0.000193 |       0.0001   |    1.93 | False       |
| B3_overnight  | AUDUSD   | ('B3', 'rev', 0.0)  |    414 |       -5e-05    |       0.0001   |   -0.5  | False       |
| B3_overnight  | AUDUSD   | ('B3', 'rev', 0.25) |    212 |       -0.000386 |       0.0001   |   -3.86 | False       |
| B4_rsi2_trend | AUDUSD   | ('B4', 1, '5/95')   |   1775 |        2.3e-05  |       0.0001   |    0.23 | False       |
| B4_rsi2_trend | AUDUSD   | ('B4', 2, '5/95')   |   1636 |        2.3e-05  |       0.0001   |    0.23 | False       |
| B4_rsi2_trend | AUDUSD   | ('B4', 1, '10/90')  |   3045 |        2.6e-05  |       0.0001   |    0.26 | False       |
| B4_rsi2_trend | AUDUSD   | ('B4', 2, '10/90')  |   2803 |        2.2e-05  |       0.0001   |    0.22 | False       |

## Full walk-forward on gate survivors (OOS, after costs)

| strategy     | symbol   |   n |    pf |   pf_1_5x |   pf_2x |   exp_R |   maxdd_pct |   worst_streak |   tstat |   dsr_strict |   dsr_pooled | years_pos   | wf_pos   |   avg_gross_pips |   avg_cost_pips | passes   | failed                                                        |
|:-------------|:---------|----:|------:|----------:|--------:|--------:|------------:|---------------:|--------:|-------------:|-------------:|:------------|:---------|-----------------:|----------------:|:---------|:--------------------------------------------------------------|
| B2_range_bo  | USDJPY   | 996 | 1.281 |     1.204 |   1.134 |   0.117 |     -31.397 |             12 |   1.793 |            0 |            0 | 4/5         | 7/10     |            5.512 |           1.397 | False    | positive expectancy every OOS year, max DD <= 20% at 1% risk  |
| B1_ldn_mom   | EURUSD   | 615 | 1.084 |     1.044 |   1.006 |   0.017 |     -10.424 |              8 |   0.772 |            0 |            0 | 3/5         | 5/10     |            1.796 |           1.021 | False    | positive expectancy every OOS year, PF>=1.2 combined OOS (1x) |
| B3_overnight | USDJPY   | 482 | 1.068 |     1.013 |   0.961 |   0.019 |     -12.807 |             10 |   0.562 |            0 |            0 | 3/5         | 5/10     |            1.294 |           1.348 | False    | positive expectancy every OOS year, PF>=1.2 combined OOS (1x) |

## Near-miss: USDJPY B2 range-expansion breakout
- PF 1.28 / 1.20 / 1.13 at 1x / 1.5x / 2x costs; 996 OOS trades; worst streak 12.
- It FAILS on two items:
  - 2023 is a losing year (−0.02R per trade). That gives 4 of 5 years positive, but all 5 are required when there are only 5 OOS years.
  - Max DD is −31% (limit 20%).
- Its t-stat of 1.79 is far below the Bonferroni threshold, and DSR is 0, so the result is not significant after 584 trials.
- This is the same USDJPY breakout behaviour seen in NYBO and Donchian. The pre-registered NYBO test showed that it does not carry over to other pairs.
- By prereg rules there is no tuning, so it stops here.

Per-year (1x, OOS):

|    y |   count |   mean |    sum |
|-----:|--------:|-------:|-------:|
| 2021 |     197 |  0.165 | 32.536 |
| 2022 |     179 |  0.154 | 27.651 |
| 2023 |     211 | -0.022 | -4.556 |
| 2024 |     232 |  0.072 | 16.789 |
| 2025 |     177 |  0.249 | 44.124 |

Windows:

| oos_start                 | oos_end                   | param               |   is_score |   n_oos |     oos_R |
|:--------------------------|:--------------------------|:--------------------|-----------:|--------:|----------:|
| 2021-01-01 00:00:00+00:00 | 2021-07-01 00:00:00+00:00 | ('B2', 0.5, 'opp')  |   1.03932  |      99 |  18.1834  |
| 2021-07-01 00:00:00+00:00 | 2022-01-01 00:00:00+00:00 | ('B2', 0.5, 'opp')  |   1.74579  |      98 |  14.3523  |
| 2022-01-01 00:00:00+00:00 | 2022-07-01 00:00:00+00:00 | ('B2', 0.5, 'opp')  |   1.94858  |      88 |  35.9582  |
| 2022-07-01 00:00:00+00:00 | 2023-01-01 00:00:00+00:00 | ('B2', 0.5, 'opp')  |   2.21635  |      91 |  -8.30678 |
| 2023-01-01 00:00:00+00:00 | 2023-07-01 00:00:00+00:00 | ('B2', 0.5, 'opp')  |   1.8546   |     100 |  -9.06657 |
| 2023-07-01 00:00:00+00:00 | 2024-01-01 00:00:00+00:00 | ('B2', 0.3, 'half') |   1.3095   |     111 |   4.51063 |
| 2024-01-01 00:00:00+00:00 | 2024-07-01 00:00:00+00:00 | ('B2', 0.3, 'half') |   0.601498 |     117 | -12.415   |
| 2024-07-01 00:00:00+00:00 | 2025-01-01 00:00:00+00:00 | ('B2', 0.3, 'half') |  -0.24366  |     115 |  29.2036  |
| 2025-01-01 00:00:00+00:00 | 2025-07-01 00:00:00+00:00 | ('B2', 0.3, 'opp')  |   0.558421 |     111 |  32.1424  |
| 2025-07-01 00:00:00+00:00 | 2025-10-10 00:00:00+00:00 | ('B2', 0.3, 'opp')  |   1.26211  |      66 |  11.9818  |
