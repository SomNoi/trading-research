# REB-H4 binary-option feasibility (numbers only). Pre-registration

- Registered before any binary hit-rate was computed. No trading and no IQ Option access; this is arithmetic on historical data.
- **Signals (fixed, no tuning):** REB-H4 fixed (f = 0.5, stop = opp) with the F2 H4 swing filter, exactly as in results/trades/USDJPY_REB_V2_F2_allparams.parquet and results/trades/EURUSD_REB_H4_XPAIR_allparams.parquet (param ('B2', 0.5, 'opp')).
- **Data:** USDJPY and EURUSD, Dukascopy M1 mid, 2019-01-01..2025-10-09. The holdout (2025-10-10+) is NOT used.
- **Entry instant:** the first M1 bar inside the M5 fill bar whose high (long) or low (short) reaches the trade's entry price. Strike = the trade's entry price (the level, or the bar open on a gap).
- **Expiry:** T ∈ {5, 15, 30, 60} min. The expiry price is the M1 mid open at entry_minute + T. If that minute is missing, use the next available M1 bar within 5 min; otherwise drop the signal and report the drop count.
- **Outcome:** win if the expiry price is strictly beyond the strike in the trade direction. A tie counts as a loss and is reported separately.
- **Statistics:**
  - Per symbol and pooled: n, wins, ties, hit rate, Wilson 95% interval (two-sided; the lower bound is the decision statistic).
  - Per year for pooled T = 15 and T = 30.
- **Breakevens:** 55.6% / 54.1% / 53.5% (80 / 85 / 87% payout; breakeven = 1/(1 + payout)).
- **Decision:** "feasible" only if the pooled Wilson lower bound ≥ breakeven at some T. Per-symbol results are information only. There is no multiple-comparison credit: 8 trials (2 symbols × 4 expiries) are logged in trials.csv.
- **Holdout:** not used under any outcome.
