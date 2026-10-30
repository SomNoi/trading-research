# XAU M1 human-behavior edge — COST $0.28 RT
**Verdict: ไม่เจอ / NO EDGE — 0/25 pass kill.** Not a live signal.
Identical to xau_m1_edge_20261030 except COST=0.28 (PREREG_COST028.md). Best OOS: 06_PDL_FAKE PF 1.018 WR 47.8% n=253 net +$8.16/oz (sens min 0.83, fails). vs $0.65 run best OOS PF 0.83.
Trials +125 (N_TRIALS 1080→1205).

| hyp                 |   OOS_N |   OOS_PF |   OOS_WR |   OOS_net |   REC_PF |   sens_PF_min | KILL_PASS   |
|:--------------------|--------:|---------:|---------:|----------:|---------:|--------------:|:------------|
| 06_PDL_FAKE         |     253 |    1.018 |    0.478 |     8.156 |    1.009 |         0.827 | False       |
| 20_OPEN_GAP_FILL    |     324 |    1.001 |    0.5   |     0.559 |    0.976 |         0.201 | False       |
| 02_ASIA_L_SWEEP     |     357 |    0.964 |    0.465 |   -21.933 |    0.961 |         0.778 | False       |
| 17_LDN_DRIVE        |     344 |    0.936 |    0.439 |   -38.289 |    0.941 |         0.609 | False       |
| 14_DOUBLE_EXP_FADE  |    3924 |    0.92  |    0.445 |  -578.333 |    0.934 |         0.056 | False       |
| 15_LDN_FVG          |     685 |    0.898 |    0.45  |  -108.904 |    0.892 |         0.158 | False       |
| 13_EXPANSION_FADE   |   20756 |    0.878 |    0.434 | -4508.22  |    0.882 |         0.195 | False       |
| 12_LOWWICK_AFTER_DN |    7836 |    0.877 |    0.414 | -2040.34  |    0.877 |         0.404 | False       |
| 11_UPWICK_AFTER_UP  |    7538 |    0.865 |    0.41  | -2158.56  |    0.873 |         0.439 | False       |
| 21_EMA_1p5ATR       |   27113 |    0.864 |    0.433 | -6178.64  |    0.877 |         0.202 | False       |
| 16_NY_FVG           |     688 |    0.863 |    0.435 |  -172.982 |    0.835 |         0.117 | False       |
| 09_RUN3_REJ         |   13903 |    0.861 |    0.401 | -4312.82  |    0.859 |         0.311 | False       |
| 07_FRACTAL_HUNT     |   36009 |    0.853 |    0.423 | -9222.25  |    0.867 |         0.627 | False       |
| 23_EMA_2p5ATR       |   13793 |    0.852 |    0.433 | -3366.82  |    0.872 |         0.123 | False       |
| 08_BIG_BAR_REJ      |   12831 |    0.85  |    0.395 | -4365.34  |    0.848 |         0.287 | False       |
| 22_VWAP_1p5ATR      |   16318 |    0.844 |    0.425 | -4306.69  |    0.861 |         0.302 | False       |
| 25_STREAK8          |    2176 |    0.843 |    0.423 |  -549.8   |    0.859 |         0.25  | False       |
| 10_PIN              |   18760 |    0.84  |    0.41  | -6154.76  |    0.841 |         0.742 | False       |
| 24_ATR_CHANNEL      |   20694 |    0.84  |    0.427 | -5535.59  |    0.863 |         0.156 | False       |
| 03_EQH_SWEEP        |    9998 |    0.833 |    0.432 | -2498.9   |    0.869 |         0.513 | False       |
| 18_NY_DRIVE         |     415 |    0.828 |    0.412 |  -146.845 |    0.828 |         0.623 | False       |
| 04_EQL_SWEEP        |    9052 |    0.824 |    0.437 | -2400.7   |    0.86  |         0.466 | False       |
| 01_ASIA_H_SWEEP     |     417 |    0.786 |    0.42  |  -143.328 |    0.719 |         0.806 | False       |
| 19_ASIA_DRIVE       |     267 |    0.626 |    0.427 |  -166.475 |    0.604 |         0.571 | False       |
| 05_PDH_FAKE         |     264 |    0.613 |    0.39  |  -186.925 |    0.649 |         0.617 | False       |

Charts: charts/oos_equity_top6.png, charts/oos_equity_all25.png
