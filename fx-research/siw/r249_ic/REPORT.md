# R249 — SIW v2 entry + Exit v4 on IC BID XAUUSD M5 — ไม่เจอ (watch-only)
PREREG sha256 1124d52d76282fd6c25c8eda967f2637febe288a1b19c7026f56c12af939729e. ../siw.py is unchanged (detect, outcome_v4). Data: IC BID M5 2025-05-14→2026-10-09, the longest IC XAU file on the box. The 2019+ M5 file is Dukascopy mid, not IC, so it was not used. Timestamps: label = server−3h; true UTC = label in summer, label+1h in winter (verified vs Dukascopy). IS<2026-03-19≤OOS. Cost $0.28/0.01; 1.5× = $0.42. Every signal is traded, with no overlap filter. Counted cells: 4 (side × dedupe {1,3}). N 6642→6646, Z_BONF 4.328.

## Main ($ per 0.01 lot, net)
|   dedupe | side   |   IS_n |   IS_win |   IS_E |   IS_PF |   OOS_n |   OOS_win |   OOS_E |   OOS_E15 |   OOS_PF |   OOS_Z |   OOS_DD |   FULL_tot |   FULL_DD | months_pos   | gate   |
|---------:|:-------|-------:|---------:|-------:|--------:|--------:|----------:|--------:|----------:|---------:|--------:|---------:|-----------:|----------:|:-------------|:-------|
|        1 | SELL   |   6807 |    0.435 | -0.343 |   0.736 |    4337 |     0.487 |  -0.052 |    -0.192 |    0.968 |  -0.761 |   706.8  |   -2560.57 |   2866.42 | 3/18         | fail   |
|        1 | BUY    |   8778 |    0.459 | -0.176 |   0.848 |    3832 |     0.434 |  -0.517 |    -0.657 |    0.716 |  -7.549 |  2010.21 |   -3525.08 |   3663.18 | 2/18         | fail   |
|        1 | ALL    |  15585 |    0.448 | -0.249 |   0.796 |    8169 |     0.462 |  -0.27  |    -0.41  |    0.843 |  -5.587 |  2227.6  |   -6085.65 |   6166.42 | 0/18         | nan    |
|        3 | SELL   |   3853 |    0.431 | -0.336 |   0.751 |    2512 |     0.49  |  -0.058 |    -0.198 |    0.965 |  -0.637 |   391.25 |   -1440.46 |   1630.23 | 5/18         | fail   |
|        3 | BUY    |   4837 |    0.456 | -0.178 |   0.849 |    2240 |     0.438 |  -0.557 |    -0.697 |    0.703 |  -6.139 |  1266.72 |   -2108.45 |   2203.07 | 1/18         | fail   |
|        3 | ALL    |   8690 |    0.445 | -0.248 |   0.802 |    4752 |     0.466 |  -0.293 |    -0.433 |    0.834 |  -4.54  |  1455.55 |   -3548.91 |   3622.13 | 0/18         | nan    |
Exits: TIME 97%, SL 2.5%, TP 0.4%.

**Gate passes: 0/4.**
- SELL: OOS E −$0.05 (Z −0.76). IS E −$0.34. Gross before cost it is about +$0.23 OOS and −$0.06 IS, so there is a small positive gross OOS drift that the cost wipes out.
- BUY: clearly negative (OOS −$0.52, Z −7.5).
- Full-period totals over 17 months: SELL −$2,561 (dd1) / −$1,440 (dd3); BUY −$3,525 / −$2,108. Max drawdown is $1.6k–3.7k per 0.01.
- Monthly: SELL is positive in 3/18 months (dd1), BUY in 2/18.

## By pattern (descriptive)
|   dedupe | side   | pat    |   IS_n |   IS_E |   OOS_n |   OOS_win |   OOS_E |   OOS_PF |
|---------:|:-------|:-------|-------:|-------:|--------:|----------:|--------:|---------:|
|        1 | BUY    | A_PIN  |   3305 | -0.219 |    1532 |     0.438 |  -0.569 |    0.698 |
|        1 | BUY    | A_STAR |   2025 | -0.162 |     924 |     0.447 |  -0.426 |    0.755 |
|        1 | BUY    | B      |   2533 | -0.096 |    1041 |     0.414 |  -0.614 |    0.669 |
|        1 | BUY    | C      |    915 | -0.272 |     335 |     0.442 |  -0.225 |    0.861 |
|        1 | SELL   | A_PIN  |   2399 | -0.366 |    1659 |     0.496 |  -0.084 |    0.951 |
|        1 | SELL   | A_STAR |   1696 | -0.234 |     970 |     0.494 |   0.182 |    1.117 |
|        1 | SELL   | B      |   1986 | -0.362 |    1295 |     0.483 |  -0.046 |    0.97  |
|        1 | SELL   | C      |    726 | -0.472 |     413 |     0.446 |  -0.484 |    0.732 |
|        3 | BUY    | A_PIN  |   1992 | -0.164 |     975 |     0.436 |  -0.603 |    0.688 |
|        3 | BUY    | A_STAR |   1207 | -0.159 |     614 |     0.436 |  -0.611 |    0.674 |
|        3 | BUY    | B      |   1422 | -0.218 |     574 |     0.443 |  -0.514 |    0.72  |
|        3 | BUY    | C      |    216 | -0.152 |      77 |     0.455 |   0.133 |    1.095 |
|        3 | SELL   | A_PIN  |   1475 | -0.415 |    1094 |     0.493 |  -0.138 |    0.922 |
|        3 | SELL   | A_STAR |   1012 | -0.271 |     623 |     0.501 |   0.281 |    1.189 |
|        3 | SELL   | B      |   1201 | -0.333 |     719 |     0.48  |  -0.204 |    0.876 |
|        3 | SELL   | C      |    165 | -0.05  |      76 |     0.461 |  -0.313 |    0.838 |
SELL A_STAR is the only bucket positive OOS in both dedupe settings (+$0.18 / +$0.28, PF 1.12/1.19), but it is negative in IS (−$0.23 / −$0.27). Treat it as noise or a regime effect, not an edge.

## By session (true UTC; descriptive)
|   dedupe | side   | sess   |   IS_n |   IS_E |   OOS_n |   OOS_win |   OOS_E |   OOS_PF |
|---------:|:-------|:-------|-------:|-------:|--------:|----------:|--------:|---------:|
|        1 | BUY    | Asia   |   2671 | -0.177 |    1091 |     0.417 |  -0.814 |    0.606 |
|        1 | BUY    | London |   2078 | -0.213 |     950 |     0.415 |  -0.588 |    0.66  |
|        1 | BUY    | NY     |   3264 | -0.165 |    1392 |     0.447 |  -0.345 |    0.813 |
|        1 | BUY    | Late   |    765 | -0.116 |     399 |     0.481 |  -0.135 |    0.892 |
|        1 | SELL   | Asia   |   2180 | -0.286 |    1277 |     0.493 |  -0.049 |    0.972 |
|        1 | SELL   | London |   1573 | -0.343 |    1028 |     0.484 |  -0.022 |    0.986 |
|        1 | SELL   | NY     |   2348 | -0.371 |    1569 |     0.486 |  -0.018 |    0.99  |
|        1 | SELL   | Late   |    706 | -0.428 |     463 |     0.477 |  -0.24  |    0.807 |
|        3 | BUY    | Asia   |   1492 | -0.187 |     644 |     0.43  |  -0.765 |    0.627 |
|        3 | BUY    | London |   1152 | -0.192 |     558 |     0.423 |  -0.497 |    0.717 |
|        3 | BUY    | NY     |   1787 | -0.171 |     813 |     0.451 |  -0.494 |    0.746 |
|        3 | BUY    | Late   |    406 | -0.138 |     225 |     0.453 |  -0.337 |    0.756 |
|        3 | SELL   | Asia   |   1224 | -0.378 |     745 |     0.493 |  -0.11  |    0.939 |
|        3 | SELL   | London |    889 | -0.285 |     603 |     0.476 |  -0.051 |    0.968 |
|        3 | SELL   | NY     |   1352 | -0.275 |     905 |     0.502 |   0.043 |    1.025 |
|        3 | SELL   | Late   |    388 | -0.53  |     259 |     0.475 |  -0.279 |    0.788 |
By hour: by_hour.csv. No hour is positive in both IS and OOS with meaningful n.

## Per month (total $; dedupe/side)
| month   |   (1, 'BUY') |   (1, 'SELL') |   (3, 'BUY') |   (3, 'SELL') |
|:--------|-------------:|--------------:|-------------:|--------------:|
| 2025-05 |         17.3 |        -146.1 |        -14.7 |         -55.2 |
| 2025-06 |       -292.5 |        -183.9 |        -81.1 |        -142.1 |
| 2025-07 |       -296.7 |        -222.9 |       -125.6 |        -158   |
| 2025-08 |       -313.7 |        -358.6 |       -211.7 |        -173.6 |
| 2025-09 |       -201.8 |        -375   |       -115.5 |        -212.5 |
| 2025-10 |        -59.6 |         -86.7 |        -75.5 |          22.6 |
| 2025-11 |       -198.8 |        -301.1 |       -108.4 |        -227.5 |
| 2025-12 |       -117.5 |        -204.3 |        -63.7 |        -111.1 |
| 2026-01 |         23.7 |        -173.4 |        -14.6 |         -34.4 |
| 2026-02 |        -34.4 |        -264.8 |         22.9 |        -197   |
| 2026-03 |       -246.3 |         -10.5 |       -164.3 |         -23.1 |
| 2026-04 |       -291   |          31.2 |       -189.2 |          13.8 |
| 2026-05 |       -336.6 |          68.2 |       -229.7 |          42.3 |
| 2026-06 |       -404.6 |        -100.5 |       -243.4 |         -74.9 |
| 2026-07 |       -263.7 |        -294.9 |       -165.3 |        -166   |
| 2026-08 |       -163   |         -68.8 |        -54.7 |          17.8 |
| 2026-09 |       -291.5 |         169.4 |       -224.5 |          65.7 |
| 2026-10 |        -54.4 |         -38   |        -49.6 |         -27.5 |

## vs Dukascopy result (464 trades, +$96.79; sells +$103.30, buys −$6.51)
- **Period:** Dukascopy covers 2026-10-23→11-04, about 9 trading days. IC covers 17 months and ends 2026-10-09, so there is **no overlap**. The Dukascopy window was a sharp gold sell-off regime in which sells naturally win. IC SELL months are also positive in strong-down months (2026-04/05/09) and negative otherwise.
- **n / noise:** with per-trade SD ≈ $3.8 (sell), 253 trades have SE ≈ $0.24. The Dukascopy sell average of +$0.41 is ≈2σ, which is what one would expect from picking a single regime. Over 11k IC sells it is −$0.23.
- **Feed:** Dukascopy BID is about +$1.5 vs IC, and wick/body shapes differ bar-to-bar, which changes pattern flags. The 10-min exit makes results very sensitive to the spread/cost. IC costs $0.28 against an average gross move of about ±$0.2.
- Same code, same rules: the difference is regime and sample size, not implementation.

Verdict: **ไม่เจอ.** SIW v2 + Exit v4 has no edge on 17 months of IC BID. Sells are about flat after cost OOS, and buys lose. Keep it watch-only. Hand picks (90% win on 20) are discretion that the rules do not capture.
