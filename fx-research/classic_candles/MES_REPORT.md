# Morning / Evening Star — XAUUSD M5 (task morning-evening-star-20261029)
Source: Dukascopy free feed (mid), not IC MT5. Data < 2025-10-10 UTC only (engine.HOLDOUT_START untouched).
Prereg: prereg/MORNING_EVENING_STAR_PREREG.md sha256 665bca267dfa072cc6bf15f39c5bd210d31d938a9ce52e467d70a0319e32e6b1
Frozen: classic_candles/MES_FROZEN_PARAMS.md sha256 37a71cc20cb76e4f890ba179f14571a5bc2d5b39c6508c64559f94f8850b3596
Script: classic_candles/run_mes.py (disc|hold). Raw: mes_discovery.json, mes_holdout.json.
Internal split 70/30 per set; holdout starts ~2023-09-15/18 UTC.

## Frozen params
- MES_V0: E1 SL=TP=$2.58; E2 k=1.5 (SL=1.5*ATR14, TP=1.5*SL)
- MES_V1: E1 SL=TP=$2.48; E2 k=1.5

## Measurement (disc → hold)
| Set | n | hit +1/+3/+6/+12/+24 % | MFE p50/p80 | MAE p50/p80 | mean move24 |
|---|---|---|---|---|---|
| V0 disc | 7314 | 46.5/48.4/48.4/48.4/48.8 | 2.16/5.04 | 2.27/5.06 | -0.043 |
| V0 hold | 3135 | 49.1/47.3/48.8/49.3/49.3 | 3.47/8.08 | 3.57/8.55 | -0.294 |
| V1 disc | 4340 | 46.9/49.1/49.8/50.1/49.4 | 2.16/5.04 | 2.20/5.05 | -0.059 |
| V1 hold | 1860 | 50.1/47.1/49.2/49.2/49.4 | 3.37/8.05 | 3.52/8.25 | -0.200 |

## Exits after $0.28 RT (1x cost; PF at 1.5x in brackets)
| Set | Disc E1 | Disc E2k1.0 | Disc E2k1.5 | Hold E1 | Hold E2 |
|---|---|---|---|---|---|
| V0 | PF 0.754 (0.663) n5758 | 0.661 | 0.748 n6035 | PF 0.785 (0.699) n2722, DD 321R%, streak 9 | PF 0.800 (0.739) n2594, DD 379%, streak 12 |
| V1 | PF 0.748 (0.654) n3788 | 0.665 | 0.752 n3903 | PF 0.759 (0.673) n1723, DD 229%, streak 11 | PF 0.791 (0.731) n1683, DD 280%, streak 11 |
Holdout by year (1x, mean net/trade): every year 2023/2024/2025 negative for both sets and both exits.

## Pass bar check
PF>=1.2 FAIL; PF>1.0 at 1.5x FAIL; positive every year FAIL; DD<=20% FAIL; n>=300 OK; streak<=12 OK.
**Verdict: MES_V0 FAIL / NO EDGE; MES_V1 FAIL / NO EDGE.** EMA5 prior-trend filter adds nothing. Not a live signal.
Trials added: 6 (N_TRIALS 937→943, Z_BONF 3.876).
