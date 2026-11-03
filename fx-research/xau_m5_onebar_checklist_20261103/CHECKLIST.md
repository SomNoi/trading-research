# R248 Step 2 — One-bar checklist (SHORT; derived from 2026-11-03 09:55 ICT GC=F bar)
⚠ **Overfit warning:** every threshold below is fitted to ONE bar from substitute futures data. Expect fewer signals and worse results out of sample. Tolerances are kept modest around the observed values. The IC backtest must be prereg'd and counted, and should be judged against random-in-context baselines (as in R247).

Primary EMA pair: **EMA20/EMA50** (the only pair where the bar's close was below both). All values use completed bars. ATR = ATR14 (simple mean of TR, lagged to signal bar).

| # | Item | Exact rule (bar i = signal) | Observed |
|---|---|---|---|
|1|Downtrend|EMA20_i < EMA50_i, and EMA20 has been below EMA50 for ≥5 bars|yes, 10 bars|
|2|Slope|EMA50_i − EMA50_{i−3} < 0|−0.29|
|3|Pullback into EMAs|At least 2 of bars i−3..i−1 make a higher high than the bar before|3 of 3|
|4|Pierce|H_i ≥ EMA20_i and H_i ≤ EMA50_i + 1.0·ATR|H−EMA20 +0.88A; H−EMA50 +0.57A|
|5|Close back below|C_i < EMA20_i − 0.1·ATR (so also < EMA50 only if EMA50>EMA20, which holds by #1); require C_i < EMA50_i too|−0.29A / −0.59A|
|6|Bearish engulfing|C_i<O_i; O_i ≥ C_{i−1}; C_i ≤ O_{i−1}; body_i ≥ 1.5 × body_{i−1} (body_{i−1}>0)|2.83×|
|7|Rejection shape|Upper wick ≥ 1.5 × body_i and close in lowest 25% of range|2.1×; 0.07|
|8|Bar size|0.8·ATR ≤ range_i ≤ 2.0·ATR|1.25A|
|9|Lower high|H_i < (max high of prior 36 bars, i.e. 3h) − 0.5·ATR|13.5 below (≈3.0A)|
|opt|Session (grid dim, not core)|Signal bar true-UTC hour ∈ [00,06) (Asia). IC label → true UTC: label (US-DST summer) / label+1h (winter)|02:55 UTC|
|opt|Prior star|Bar i−1 is a shooting star (uw ≥2×body, close in lower third)|yes|

## Trade
- Entry: open of bar i+1, short.
- SL: H_i + $0.30. R = SL − entry.
- Exits (4 variants, matching R247): TP 1.5R with a 2h cap; TP 2R with a 2h cap; time exit 30m (6 bars) with SL; time exit 60m (12 bars) with SL. SL-first on same bar; one position at a time.
- Cost $0.28/0.01 lot; stress test at 1.5×.
- **Long mirror: optional and off by default.** If enabled: EMA20>EMA50, low pierces EMA20 down to ≥ EMA50 − 1.0·ATR, close above both, bullish engulfing with lower wick ≥1.5×body and close in the top 25%, higher low vs 3h min + 0.5·ATR, SL = L_i − $0.30.

Not yet backtested (STOP after Step 2 per brief).
