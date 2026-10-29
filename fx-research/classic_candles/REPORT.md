# Classic candles (Track B) — REPORT — task classic-candles-20261029-B
Source: Dukascopy free feed (mid), not IC MT5. XAUUSD M5 (from M1), 2019-01..2025-10-09; project holdout >=2025-10-10 never loaded.
Prereg: prereg/CLASSIC_CANDLES_PREREG.md sha256 fbbf03eef3f6fbc9fc614785d1003b91e51088ca9596eed433b2ef5d95231e82 (copy in classic_candles/).
Frozen params: classic_candles/FROZEN_PARAMS.md sha256 fc8de240388bf2d94a8d19b8e80e9c1b189309bdf95ce506870f338a345ba4db (hashed before hold stage).
Order followed: prereg → hash/chmod → discovery (70%) → freeze/hash → internal holdout (30%). Script: run.py (disc|hold). Raw: discovery.json, holdout.json.
Cost $0.28/oz RT per trade; sensitivity 1x/1.5x/2x. DD/streak in R at 1% risk (non-compounded). engine.run_sim/add_costs not used (bracket sim mirrors maemfe; deviation noted).
Ops note: project .venv lacked numba (engine.py import failed); installed numba 0.68.1 into .venv.

## Frozen params (from discovery)
| set | E1 SL=TP ($) | E2 k (SL=k·ATR14, TP=1.5·SL) | internal holdout from (UTC) |
|---|---|---|---|
| PIN_V0 | 2.58 | 1.5 | 2023-09-19 |
| PIN_V1 | 2.51 | 1.5 | 2023-09-21 |
| INSIDE | 2.63 | 1.5 | 2023-08-14 |
| DOJI | 2.55 | 1.5 | 2023-10-19 |

## Signal stats (hit% = close in signal direction at +k M5 bars)
| set | split | n | +1 | +3 | +6 | +12 | +24 | MFE p50 | MAE p50 |
|---|---|---|---|---|---|---|---|---|---|
| PIN_V0 | disc | 15315 | 48.6 | 49.9 | 49.7 | 50.0 | 49.9 | 2.17 | 2.21 |
| PIN_V0 | hold | 6565 | 50.1 | 49.8 | 50.7 | 50.3 | 50.5 | 3.55 | 3.50 |
| PIN_V1 | disc | 7345 | 47.4 | 48.2 | 48.7 | 49.5 | 49.1 | 2.13 | 2.19 |
| PIN_V1 | hold | 3149 | 49.9 | 49.7 | 50.5 | 50.0 | 50.2 | 3.51 | 3.49 |
| INSIDE | disc | 39773 | 49.6 | 48.8 | 49.1 | 48.9 | 49.2 | 2.23 | 2.30 |
| INSIDE | hold | 17046 | 49.0 | 49.4 | 49.7 | 49.6 | 50.3 | 3.33 | 3.38 |
| DOJI | disc | 27728 | 49.5 | 49.8 | 50.0 | 50.0 | 50.1 | 2.24 | 2.21 |
| DOJI | hold | 11884 | 50.2 | 49.6 | 49.7 | 49.9 | 50.8 | 3.60 | 3.68 |
MFE ≈ MAE everywhere → run vs retrace symmetric = no directional information.

## Exits after cost (internal holdout, 1x cost; PF at 1.5x / 2x)
| set | exit | n | win% | PF | PF1.5x | PF2x | mean net $/oz | maxDD (R) | worst streak |
|---|---|---|---|---|---|---|---|---|---|
| PIN_V0 | E1 | 5040 | 49.8 | 0.814 | 0.725 | 0.645 | -0.253 | 496 | 12 |
| PIN_V0 | E2 | 4662 | 41.5 | 0.843 | 0.777 | 0.716 | -0.287 | 548 | 13 |
| PIN_V1 | E1 | 2703 | 50.6 | 0.830 | 0.737 | 0.654 | -0.225 | 246 | 9 |
| PIN_V1 | E2 | 2599 | 41.6 | 0.856 | 0.788 | 0.726 | -0.260 | 285 | 15 |
| INSIDE | E1 | 10112 | 49.4 | 0.792 | 0.707 | 0.630 | -0.292 | 1133 | 16 |
| INSIDE | E2 | 8596 | 40.9 | 0.849 | 0.783 | 0.722 | -0.278 | 1125 | 14 |
| DOJI | E1 | 7866 | 48.9 | 0.771 | 0.687 | 0.611 | -0.319 | 987 | 11 |
| DOJI | E2 | 6654 | 41.1 | 0.859 | 0.795 | 0.736 | -0.268 | 799 | 17 |
Discovery was equally negative (PF 0.66–0.77 all 12 trials). Every OOS year (2023/2024/2025) negative mean net for every set/exit.
Gross ≈ 0; mean net ≈ −cost: the patterns are coin flips and $0.28 RT is the whole loss.

## Verdict (pass bar: all required)
PIN_V0 FAIL · PIN_V1 FAIL · INSIDE FAIL · DOJI FAIL — NO EDGE. Fails PF≥1.2, PF>1.0 @1.5x, positive years, DD≤20%. Only ≥300 trades met. Not a live signal.

## Multiple testing
12 new discovery trials appended to results/trials.csv (rows "classic-candles (discovery 70%)", mean_R column). Holdout evaluated 8 frozen configs. Parent: update multiple_testing tally +12.
