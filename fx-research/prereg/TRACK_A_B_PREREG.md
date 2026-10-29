# Track A (higher-TF, pooled) and Track B (M1/M5 low-cost FX, gated): pre-registration
Written before any Track A/B backtest. The hash and UTC time are recorded in results/prereg_hashes.txt.

## Common rules
- Walk-forward: IS 24 months / OOS 6 months, 10 non-overlapping OOS windows 2021-01-01..2025-10-09. The parameter is picked by the IS t-stat of net R.
- Holdout ≥ 2025-10-10 is never downloaded or loaded.
- Flat 1% risk per trade on the $10k reference account, non-compounded.
- Costs:
  - Kai's file (IC_COSTS_FROM_KAI_20261011.md): p90 session spreads, $3.50/lot/side commission, slippage 0.1 pip per side ($0.05 on XAU).
  - Sensitivity at 1x / 1.5x / 2x.
  - Entries blocked 20:30–24:00 UTC and at weekends.
  - Minimum stop 5 pips (XAU $1).
- The pass bar is unchanged. Every trial is logged in results/trials.csv. The DSR and Bonferroni figures are recomputed.

## Track A: H1/H4/D1, ONE parameter set per system pooled across 13 symbols
- Universe: EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, USDCHF, NZDUSD, EURJPY, GBPJPY, AUDJPY, EURGBP, EURCHF, XAUUSD.
- Bars: built from Dukascopy M1 mid.
  - H1.
  - H4: 4h bars anchored at 00:00 UTC.
  - D1: 24h bars from 20:00 UTC to 20:00 UTC, so the next-bar-open entry at 20:00 is before the rollover block.
- Proxy p90 spreads for pairs NOT in Kai's file (conservative, about 2× IC's published Raw average or more; same rule as the NYBO prereg):
  - EURJPY 7, GBPJPY 13, AUDJPY 8, USDCAD 5, USDCHF 7 points (as before).
  - New: NZDUSD 8, EURGBP 8, EURCHF 10 points.
  - ny_late 1.5×, rollover/weekend 15×.
  - Commission $7 RT per 100k base: 0.00007 quote units for NZDUSD/EURGBP/EURCHF (conservative), and via USDJPY for the JPY crosses.
- Swaps: time-varying and rate-based, because static 2026 swap tables are wrong for 2019–2024.
  - Rates: monthly OECD 3-month interbank rates from FRED, IR3TIB01{US,EZ,GB,JP,AU,CA,CH,NZ}M156N.
  - Long accrual per night = price × (r_base − r_quote − 1.5%) / 360. Short = price × (r_quote − r_base − 1.5%) / 360.
  - XAU: r_base = 0.
  - Wednesday counts ×3 (engine swap_nights).
  - The 1.5% broker markup is checked against Kai's IC swap table: IC's current EURUSD and XAU swaps are at or above the model on both sides, so the model is the more conservative.
  - The IC swap table itself is not applied, because it is a 2026 snapshot.
  - Carry SIGNALS use the previous month's rate (no lookahead).
- Long and short legs are simulated independently, one position at a time per symbol and direction.
- Initial stop = k × ATR20 of the system's timeframe; risk = |entry − stop|.

Systems (grid = 4 pooled parameter sets each, so 24 trials in total; each pooled set is 1 trial):
- **A1 MA trend:**
  - Entry: EMA(fast) crosses EMA(slow); enter at the next open in the cross direction.
  - Exit: opposite cross (next open) or the 3×ATR stop.
  - Grid: TF {H4, D1} × (fast, slow) {(20,100), (50,200)}.
- **A2 Donchian breakout:**
  - Entry: close > N-bar high (long) or < N-bar low (short); enter next open.
  - Exit: close beyond the N/2 opposite channel, or the 2×ATR stop.
  - Grid: TF {H4, D1} × N {20, 55}.
- **A3 ATR (Keltner) channel, D1:**
  - Entry: close > EMA(N) + k×ATR20 → long until close < EMA(N); mirror for shorts.
  - Stop 3×ATR.
  - Grid: N {20, 50} × k {1.5, 2.5}.
- **A4 Time-series momentum, D1:**
  - Signal: sign of the L-day return, checked every 5 D1 bars. Enter at the next open in the signal direction when flat; exit when the sign flips at a check.
  - Stop k×ATR20.
  - Grid: L {63, 252} × k {3, 5}.
- **A5 Cross-sectional momentum, D1, weekly:**
  - Every 5 bars, rank the 13 symbols by L-day return / ATR20.
  - Long the top n and short the bottom n. Positions are held while the symbol stays in its bucket at each check, otherwise exited at the next open.
  - Stop 3×ATR20.
  - Grid: L {63, 126} × n {2, 3}.
- **A6 Carry, D1, weekly, 12 FX pairs (XAU excluded):**
  - Differential d = r_base − r_quote, using the previous month's rate.
  - Long if d > th, short if d < −th. Hold while the condition persists at weekly checks.
  - Stop 4×ATR20.
  - Grid: th {0.5%, 1.5%} × trend filter {none, sign of the 63-day return must agree}.
- Reported for every system: pooled and per-symbol results; portfolio drawdown on all trades at 1% each (closed-trade equity); max and average concurrent open positions; average pairwise correlation of per-symbol daily R.

## Track B: M5 low-cost FX (EURUSD, USDJPY, AUDUSD)
- **GATE:**
  - IS screen = 2019-01-01..2020-12-31. This is the first IS window and never appears in any OOS window.
  - A (system, symbol, param) passes only if mean gross per trade ≥ 2 × mean round-trip cost (cost_1x).
  - A (system, symbol) goes on to the full walk-forward only if at least one param passes, and the walk-forward then chooses among the gate-passing params only.
  - All params are logged as trials whether or not they pass.
- **B1 London first-hour momentum:**
  - Signal: r = close(07:55 bar) − open(07:00 UTC). If |r| > k × ATR14(H1), enter at 08:00 in the direction of r.
  - Stop 1 × ATR20(D1). Exit at time T.
  - Grid: k {0.5, 1.0} × T {12:00, 16:00 UTC}.
- **B2 Range-expansion breakout (Williams-type):**
  - At 07:00 UTC, place stops at open ± f × previous-D1 range (D1 = 20:00→20:00 UTC). The first touch is taken.
  - Stop: the opposite stop level or 0.5 × range.
  - Exit 20:00 UTC.
  - Grid: f {0.3, 0.5} × stop {opp, half}.
- **B3 NY-session → Asia overnight:**
  - Signal: NY session return 13:00–20:00 UTC, with threshold |r| > th × ATR20(D1).
  - Entry 00:00 UTC; mode momentum or reversal. Exit 07:00 UTC. Stop 0.5 × ATR20(D1).
  - Grid: mode {mom, rev} × th {0, 0.25}.
- **B4 RSI(2) pullback with the H1 trend:**
  - Trend: H1 close vs H1 EMA200.
  - Entry, M5, 07:00–16:00 UTC only: RSI(2) < 5 in an uptrend (buy) or > 95 in a downtrend (sell). Enter next open.
  - Exit when M5 close crosses EMA5, or after 24 bars. Stop k × ATR14(H1).
  - Grid: k {1, 2} × RSI thresholds {5/95, 10/90}.
- Trials: 4 systems × 4 params × 3 symbols = 48 gate trials.
