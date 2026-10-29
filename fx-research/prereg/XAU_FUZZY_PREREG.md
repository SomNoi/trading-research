# XAU_FUZZY pre-registration (written before any 2023+ data is loaded)
Data: Dukascopy XAU/USD M1 mid resampled to M5 (label left, UTC), H1 for trend. Costs: Kai IC (session p90 spread + $0.05/oz/side slip + $0.07/oz commission RT; swap with Wed x3). 0.01 lot = 1 oz.
Periods: FIT 2019-01-01..2021-12-31, VALIDATION 2022-01-01..2022-12-31 (together IS); OOS 2023-01-01..2025-10-09 touched ONCE; holdout 2025-10-10+ only if finalist passes the full bar.
Features at completed bar t: last L bars (L in {3,5}) OHLC minus open of first bar, divided by ATR14(t) (Wilder, M5), clipped to +-6. Target for learning: close[t+6]-open[t+1] in $ (gross).
Methods (models fit on FIT only, then frozen):
- KM: k-means K=64 (sklearn, seed 0, on <=150k random FIT samples); per-cluster mean target on FIT; score = cluster mean.
- KNN: KNeighborsRegressor k=100 on 150k random FIT samples (seed 0); score = predicted mean target.
Signal: |score| >= thr, direction = sign(score). thr set on FIT as the quantile of |score| giving R in {4,5} signals/day (before context filter and one-position rule); thr frozen.
Context (3): none | trend (trade only in direction of both close vs M5 EMA55 and last completed H1 close vs H1 EMA55) | atrhi (ATR14 >= its rolling 20-day median of M5 ATR, prior bars).
Exits (4): E1 TP $0.48/SL $0.48/time 3 bars; E2 TP 1.0 ATR/SL 1.0 ATR/time 6; E3 TP 1.5 ATR/SL 1.0 ATR/time 12; E4 TP $1.00/SL $1.00/time 6. Same-bar TP+SL = SL. Time exit at close of the Nth bar after entry.
Entry next bar open; one position at a time; no entries 20:30-24:00 UTC or weekends.
Grid: 2 methods x 2 L x 2 rates x 3 contexts x 4 exits = 96 configurations, all logged as 'FUZZY' trials (budget fixed at 96).
Selection: on VALIDATION 2022, highest net mean $/trade at 1x among configs with >=200 validation trades; top-3 by same metric pre-declared and reported separately. Finalist evaluated once on OOS.
Pass bar (unchanged): every OOS year positive; PF>=1.2 at 1x and >1.0 at 1.5x; >=300 trades; maxDD<=20% at 1% risk per trade (R = net/SL distance); worst losing streak <=12; no martingale/grid/averaging. Also report whether net/trade >= +$0.20 per 0.01 lot.
