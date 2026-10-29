# XAUUSD M5 engulfing scan — ICT day 2026-10-15 (UTC 2026-10-14 17:00 → 10-15 17:00)

Source: **Dukascopy free historical feed (BID M1 candles, resampled to M5, UTC)**. Prices may differ slightly from IC Markets (feed, spread, bid basis). Times = engulf bar CLOSE (entry). Server time = UTC+3 (IC Markets, DST).

M5 bars in window: 276

Rules: small = |body| <= median |body| of the 20 bars preceding the small bar(s); big = |body| >= 1.5×median. Type1: 1 small + big with high>=small high, low<=small low, and body engulfs small body. Type2: 2 small + big covering combined H-L of both. Side = big-bar color. Entry = engulf close. Fav = max favorable excursion over next 12 bars (1 pt = $0.01). Continuation = consecutive next bars making new extreme (starting from engulf-bar extreme). FailA = opposite extreme hit before +1×engulf range within 12 bars (same-bar tie counted as SL; unresolved excluded). FailB = next bar closes against direction.

## Summary by type/side

|             |   n |   avg_fav_pts |   med_fav_pts |   avg_cont |   failA_pct |   failA_unres |   failB_pct |
|:------------|----:|--------------:|--------------:|-----------:|------------:|--------------:|------------:|
| (1, 'Buy')  |   3 |        2626.5 |        2613.4 |        3   |           0 |             0 |        66.7 |
| (1, 'Sell') |   1 |         149   |         149   |        1   |         100 |             0 |       100   |
| (2, 'Buy')  |   3 |        2120.4 |        1385.3 |        3.3 |           0 |             0 |        33.3 |


## By type

|   type |   n |   avg_fav_pts |   avg_cont |   failA_pct |   failB_pct |
|-------:|----:|--------------:|-----------:|------------:|------------:|
|      1 |   4 |        2007.1 |        2.5 |          25 |        75   |
|      2 |   3 |        2120.4 |        3.3 |           0 |        33.3 |


## All signals

|   type | side   | ict             | server    |   rng_usd |   fav_pts |   cont | failA   | failB   |   bars |
|-------:|:-------|:----------------|:----------|----------:|----------:|-------:|:--------|:--------|-------:|
|      2 | Buy    | 10-15 01:55 ICT | 21:55 srv |      4.54 |    1095.3 |      2 | False   | False   |     12 |
|      1 | Buy    | 10-15 06:15 ICT | 02:15 srv |      4.96 |    2613.4 |      1 | False   | True    |     12 |
|      1 | Buy    | 10-15 06:45 ICT | 02:45 srv |      4.67 |    3880.7 |      8 | False   | False   |     12 |
|      2 | Buy    | 10-15 06:45 ICT | 02:45 srv |      4.67 |    3880.7 |      8 | False   | False   |     12 |
|      1 | Sell   | 10-15 14:20 ICT | 10:20 srv |      4    |     149   |      1 | True    | True    |     12 |
|      1 | Buy    | 10-15 14:40 ICT | 10:40 srv |      4.56 |    1385.3 |      0 | False   | True    |     12 |
|      2 | Buy    | 10-15 14:40 ICT | 10:40 srv |      4.56 |    1385.3 |      0 | False   | True    |     12 |

Script: /workspace/fx-research/scripts/xau_engulf_20261015.py
