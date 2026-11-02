# R246b — R246 follow-up: did price continue, or was the SL too tight? — ไม่เจอ
PREREG sha256 285a6123b86888b9a3bdfba816acdd1e805dce35d0d110007a0b4723b03ea3ea. Same data/split (cut 2026-03-19 server day)/cost $0.28. Timestamps: label = server−3h (see R246).

## Answer
**Price did NOT continue in the trend direction.** After the signal, moves are a coin flip: about 48–49% end in the trend direction at 30/60/120m, and OOS 120m median is −$1.70. MFE≈MAE (OOS median over 2h: $9.58 vs $10.47). A +$1 favorable move came before a −$1 adverse move only 35% of the time (OOS 32%). **The SL being too tight is not the main problem.** Many SL-hit trades later touched TP within 2h (PIN about 43–51%, DOJI about 65–74%), but that is what noise does to a $2–4 stop against a median $10 two-hour excursion. Widening the SL (ATR-based or fixed $3–10) never turned IS positive: 0/64 cells had IS>0, 5/64 had OOS>0, and 0 passed the gate.

## (1) Direction / excursions (union of 4 signal sets, deduped, n=2906)
|            |       IS |      OOS |      ALL |
|:-----------|---------:|---------:|---------:|
| n          | 1759     | 1147     | 2906     |
| pct_pos30  |    0.478 |    0.486 |    0.481 |
| med30      |   -0.28  |   -0.18  |   -0.24  |
| mean30     |   -0.016 |    0.145 |    0.048 |
| pct_pos60  |    0.505 |    0.474 |    0.493 |
| med60      |    0.12  |   -0.39  |   -0.095 |
| mean60     |    0.474 |   -0.09  |    0.251 |
| pct_pos120 |    0.517 |    0.452 |    0.491 |
| med120     |    0.43  |   -1.7   |   -0.26  |
| mean120    |    1.09  |   -0.95  |    0.284 |
| medMFE12   |    4.78  |    7.05  |    5.465 |
| medMAE12   |    5     |    7.13  |    5.77  |
| pMFE>MAE12 |    0.489 |    0.501 |    0.494 |
| medMFE24   |    7.19  |    9.58  |    8.105 |
| medMAE24   |    7.21  |   10.47  |    8.525 |
| pMFE>MAE24 |    0.5   |    0.488 |    0.495 |
| fav1_first |    0.374 |    0.316 |    0.351 |

## (2) SL-hit trades that later reached original TP within 2h (best R246 cell = PIN_k2_tp1.5_T12)
| cell              |   n_trades |   n_SL |   pct_SL_then_TP2h |    IS |   OOS |
|:------------------|-----------:|-------:|-------------------:|------:|------:|
| PIN_k2_tp1.5_T6   |       1220 |    682 |              0.509 | 0.533 | 0.473 |
| PIN_k2_tp1.5_T12  |       1204 |    731 |              0.492 | 0.515 | 0.459 |
| PIN_k2_tp2.0_T6   |       1218 |    710 |              0.455 | 0.467 | 0.438 |
| PIN_k2_tp2.0_T12  |       1195 |    773 |              0.435 | 0.447 | 0.417 |
| PIN_k3_tp1.5_T6   |        600 |    340 |              0.506 | 0.519 | 0.485 |
| PIN_k3_tp1.5_T12  |        594 |    375 |              0.483 | 0.498 | 0.458 |
| PIN_k3_tp2.0_T6   |        599 |    354 |              0.455 | 0.453 | 0.457 |
| PIN_k3_tp2.0_T12  |        592 |    398 |              0.432 | 0.434 | 0.429 |
| DOJI_k2_tp1.5_T6  |       2172 |   1323 |              0.714 | 0.707 | 0.724 |
| DOJI_k2_tp1.5_T12 |       2157 |   1350 |              0.7   | 0.692 | 0.711 |
| DOJI_k2_tp2.0_T6  |       2163 |   1381 |              0.666 | 0.663 | 0.67  |
| DOJI_k2_tp2.0_T12 |       2140 |   1422 |              0.651 | 0.649 | 0.655 |
| DOJI_k3_tp1.5_T6  |       1053 |    655 |              0.724 | 0.709 | 0.744 |
| DOJI_k3_tp1.5_T12 |       1050 |    675 |              0.71  | 0.694 | 0.732 |
| DOJI_k3_tp2.0_T6  |       1050 |    692 |              0.686 | 0.676 | 0.701 |
| DOJI_k3_tp2.0_T12 |       1046 |    716 |              0.672 | 0.661 | 0.687 |

## (3) SL/TP sweep, PIN+k2 & DOJI+k2, time exit 2h, 64 cells (N+=64). $ per 0.01 lot
SL ATR: extreme ∓ m·0.5·ATR14 (m 1/1.5/2/3); fixed $3/5/8/10 from entry. TP 1.5R/2R/$5/$10.
Top 5 OOS:
| cell                    |   IS_n |   IS_E |   OOS_n |   OOS_hit |   OOS_E |   OOS_E15 |   OOS_PF |   OOS_Z |   OOS_DD |
|:------------------------|-------:|-------:|--------:|----------:|--------:|----------:|---------:|--------:|---------:|
| DOJI_k2_SLfix10_TPR2    |    947 | -0.286 |     636 |     0.409 |   0.165 |     0.025 |    1.031 |   0.344 |  277.56  |
| DOJI_k2_SLatr2_TPR2     |   1021 | -0.432 |     672 |     0.371 |   0.14  |     0     |    1.03  |   0.302 |  350.859 |
| DOJI_k2_SLfix10_TPusd10 |    991 | -0.47  |     684 |     0.51  |   0.062 |    -0.078 |    1.014 |   0.175 |  263.23  |
| DOJI_k2_SLatr3_TPR2     |    955 | -0.313 |     636 |     0.401 |   0.059 |    -0.081 |    1.011 |   0.104 |  356.831 |
| DOJI_k2_SLatr1_TPR2     |   1160 | -0.358 |     774 |     0.355 |   0.017 |    -0.123 |    1.005 |   0.054 |  378.95  |

Best: DOJI_k2_SLfix10_TPR2. OOS n=636, E +$0.165, PF 1.03, Z 0.34. At 1.5× cost E is +$0.025. IS E is −$0.286, so it fails the gate. Z_BONF(6614)=4.327. Gate passes: 0/64.
N 6550 → 6614.
