# REB-H4 cross-pair independent OOS: REPORT

**Verdict: CLEAR FAIL. The pooled new-pair result does not meet the full bar, so the holdout was NOT run and stays unused.**

- Pre-registration: prereg/REB_H4_XPAIR_PREREG.md (sha256 ec2aecc3…, registered 2026-10-11T11:14:37Z = 18:14 ICT), written before any run.
- System: V2 unchanged (B2 4-param grid + H4 swing filter; walk-forward selection per window). Symbols chosen on measured cost only: EURUSD, GBPUSD, AUDUSD.
- Costs: Kai's file. Walk-forward: 10 non-overlapping OOS windows 2021-01..2025-10-09. Flat 1% risk; portfolio DD on closed-trade equity.
- Multiple testing: 632 trials in total (12 new); Bonferroni t threshold 3.78.

## Results (OOS, after costs)

| set                                    |    n |   pf_1x |   pf_1_5x |   pf_2x |   exp_R |   maxdd_pct |   worst_streak |   tstat | years_pos   |   dsr_strict |   dsr_pooled | passes   |
|:---------------------------------------|-----:|--------:|----------:|--------:|--------:|------------:|---------------:|--------:|:------------|-------------:|-------------:|:---------|
| EURUSD                                 |  300 |   1.117 |     1.057 |   1.001 |   0.063 |       -20.7 |             10 |    0.47 | 2/5         |            0 |            0 | False    |
| GBPUSD                                 |  287 |   0.842 |     0.799 |   0.759 |  -0.071 |       -38   |             13 |   -0.73 | 2/5         |            0 |            0 | False    |
| AUDUSD                                 |  308 |   0.715 |     0.672 |   0.633 |  -0.143 |       -53.2 |             10 |   -1.5  | 1/5         |            0 |            0 | False    |
| POOLED new pairs (DECISIVE)            |  895 |   0.898 |     0.848 |   0.803 |  -0.051 |       -98.3 |             16 |   -0.79 | 1/5         |            0 |            0 | False    |
| info: new pairs + USDJPY V2            | 1167 |   0.977 |     0.922 |   0.871 |  -0.011 |       -93.6 |             16 |   -0.19 | 1/5         |            0 |            0 | False    |
| info: fixed (0.5,opp) EURUSD           |  286 |   1.18  |     1.12  |   1.064 |   0.071 |       -18.3 |             10 |    0.63 | 3/5         |            0 |            0 | False    |
| info: fixed (0.5,opp) GBPUSD           |  276 |   0.927 |     0.881 |   0.839 |  -0.027 |       -35.9 |              7 |   -0.32 | 2/5         |            0 |            0 | False    |
| info: fixed (0.5,opp) AUDUSD           |  240 |   0.722 |     0.678 |   0.638 |  -0.117 |       -37.4 |             14 |   -1.3  | 1/5         |            0 |            0 | False    |
| info: fixed (0.5,opp) pooled new pairs |  802 |   0.952 |     0.902 |   0.855 |  -0.019 |       -75.9 |             13 |   -0.33 | 1/5         |            0 |            0 | False    |

## Per year (1x, expectancy in R)

|    y |   ('EURUSD', 'n') |   ('EURUSD', 'exp_R') |   ('GBPUSD', 'n') |   ('GBPUSD', 'exp_R') |   ('AUDUSD', 'n') |   ('AUDUSD', 'exp_R') |   ('POOLED new pairs (DECISIVE)', 'n') |   ('POOLED new pairs (DECISIVE)', 'exp_R') |   ('info: new pairs + USDJPY V2', 'n') |   ('info: new pairs + USDJPY V2', 'exp_R') |   ('info: fixed (0.5,opp) pooled new pairs', 'n') |   ('info: fixed (0.5,opp) pooled new pairs', 'exp_R') |
|-----:|------------------:|----------------------:|------------------:|----------------------:|------------------:|----------------------:|---------------------------------------:|-------------------------------------------:|---------------------------------------:|-------------------------------------------:|--------------------------------------------------:|------------------------------------------------------:|
| 2021 |                79 |                -0.186 |                58 |                 0.049 |                51 |                 0.029 |                                    188 |                                     -0.055 |                                    252 |                                     -0.039 |                                               166 |                                                -0.007 |
| 2022 |                56 |                 0.206 |                60 |                -0.036 |                68 |                -0.17  |                                    184 |                                     -0.012 |                                    246 |                                     -0     |                                               164 |                                                -0.036 |
| 2023 |                52 |                -0.015 |                55 |                -0.278 |                74 |                -0.06  |                                    181 |                                     -0.113 |                                    237 |                                     -0.082 |                                               159 |                                                -0.145 |
| 2024 |                66 |                -0.114 |                60 |                -0.117 |                68 |                -0.319 |                                    194 |                                     -0.187 |                                    240 |                                     -0.126 |                                               184 |                                                -0.108 |
| 2025 |                47 |                 0.647 |                54 |                 0.026 |                47 |                -0.169 |                                    148 |                                      0.161 |                                    192 |                                      0.246 |                                               129 |                                                 0.272 |

Window parameter choices: EURUSD: {"('B2', 0.5, 'half')": 6, "('B2', 0.3, 'half')": 3, "('B2', 0.5, 'opp')": 1}; GBPUSD: {"('B2', 0.5, 'opp')": 6, "('B2', 0.5, 'half')": 3, "('B2', 0.3, 'opp')": 1}; AUDUSD: {"('B2', 0.3, 'opp')": 5, "('B2', 0.5, 'opp')": 3, "('B2', 0.3, 'half')": 2}
