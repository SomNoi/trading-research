# COMBO_MTF REPORT — H1 EMA55 bias + M5 PIN/ENGULF ± RSI14 (XAUUSD)
Source: Dukascopy free feed (mid), not IC MT5. Data 2019-01..2025-10-09 (HOLDOUT_START 2025-10-10 never loaded). Cost $0.28/oz RT.
Prereg sha256 c4a31bd3d5eb7bef242a8f0c054692cb838b7d88f4aafe0c63bfdf9bea9ee603 (prereg/COMBO_MTF_PREREG.md, hashed + read-only before any counting).
FROZEN_PARAMS.md hashed + read-only before holdout. Trials: 12 (N_TRIALS 943→955, Z_BONF≈3.88).

## Frozen
| Set | E1 SL=TP | E2 k (SL=k·ATR14, TP 1.5×) | internal holdout from (UTC) |
|---|---|---|---|
| PIN_F0 | $2.52 | 1.5 | 2023-10-04 |
| PIN_F1 | $2.73 | 1.5 | 2023-10-10 |
| ENGULF_F0 | $2.57 | 1.5 | 2023-09-13 |
| ENGULF_F1 | $2.68 | 1.5 | 2023-08-08 |

Raw signals: PIN 26,260; ENGULF 74,434; H1 bias bull 55.2% of M5 bars.

## Results (1x cost; PF / mean R)
| Set | Disc E1 | Disc E2 | Hold n (E1/E2) | Hold E1 PF | Hold E2 PF | Hold PF @1.5x (E1/E2) | Hold hit +24 | Hold DD% (E1/E2) | Worst streak (E1/E2) |
|---|---|---|---|---|---|---|---|---|---|
| PIN_F0 | 0.765 / -0.114R | 0.749 / -0.208R | 2830/2714 | 0.828 | 0.854 | 0.74/0.79 | 51.3% | 258/273 | 14/13 |
| PIN_F1 | 0.785 / -0.100R | 0.787 / -0.176R | 434/430 | 0.848 | 0.798 | 0.76/0.74 | 49.6% | 46/56 | 10/8 |
| ENGULF_F0 | 0.746 / -0.127R | 0.751 / -0.222R | 6923/6192 | 0.806 | 0.845 | 0.72/0.78 | 49.4% | 722/828 | 14/18 |
| ENGULF_F1 | 0.736 / -0.125R | 0.759 / -0.219R | 409/414 | 0.801 | 0.722 | 0.71/0.67 | 51.4% | 51/79 | 12/12 |

Holdout by year mean net $/oz (E1): PIN_F0 23 -0.15, 24 -0.21, 25 -0.28; PIN_F1 23 +0.24, 24 -0.24, 25 -0.29; ENGULF_F0 all negative; ENGULF_F1 23 +0.21, 24 -0.43, 25 -0.32.
(Disc hit+24 for F1 sets 53.5–54.9% did not survive holdout: 49.6–51.4%.)

## Verdict: **FAIL / NO EDGE** for all 4 sets × 3 exits
Pass bar needs PF≥1.2 OOS, >1.0 at 1.5x, ≥300 trades, DD≤20%, streak≤12, positive years. Best holdout PF 0.854 (<1.0). Every set loses after costs; RSI filter cuts trades ~85% without improving PF.
Stacking H1 bias (+RSI) did not create an edge vs the stand-alone patterns (stand-alone PIN/ENGULF holdout PF ~0.77–0.86) — roughly same PF band.
NOT a live signal. Files: run.py, discovery.json, holdout.json, disc.log, hold.log.
