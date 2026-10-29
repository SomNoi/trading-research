# REB-H4 cross-pair independent out-of-sample test: pre-registration
Written BEFORE any REB-H4 run on these pairs. The sha256 and UTC timestamp are recorded in results/prereg_hashes.txt.

## System (UNCHANGED from variant V2 in prereg/USDJPY_REB_HTF_PREREG.md; code scripts/usdjpy_reb_htf.py + scripts/trackB.py::b2_range_bo)
- **Bars:** M5 from Dukascopy M1 mid.
- **D1 range:** high − low of the last completed D1 bar; D1 runs 20:00 → 20:00 UTC.
- **Entry:**
  - At 07:00 UTC, set up = open(07:00) + f × range and dn = open(07:00) − f × range.
  - The first M5 bar touching a level triggers a stop entry at max(open, up) or min(open, dn).
  - If a bar touches both levels, the day is skipped. At most one entry per day.
- **Stop:** "opp" = the opposite level; "half" = entry ∓ 0.5 × range. No TP. Time exit at the first bar ≥ 20:00 UTC.
- **H4 swing filter (F2):**
  - Fractal swing high/low with 2 bars on each side, on H4 bars anchored 00:00 UTC. A swing is confirmed when bar k+2 completes.
  - Uptrend = last swing high > previous swing high AND last swing low > previous swing low; downtrend is the mirror. Only the last completed H4 bar at entry is used.
  - Longs only in an uptrend, shorts only in a downtrend.
- **Parameter grid (unchanged):** f ∈ {0.3, 0.5} × stop ∈ {opp, half}, with the identical walk-forward selection used for V2 (best IS t-stat in each window).
  - V2 on USDJPY chose (0.5, opp) in 8 of 10 windows, including the last one.
  - The fixed (0.5, opp) result is also REPORTED for information only (it is the demo-handoff configuration). It is not a separate decision basis.
- **Execution rules (engine):** entry block 20:30–24:00 UTC and at weekends; minimum stop 5 pips; one position at a time.
- **Costs:** Kai's file (IC_COSTS_FROM_KAI_20261011.md) at 1x / 1.5x / 2x. Flat 1% risk.

## Symbols (decided now, on cost alone)
- **Included: EURUSD, GBPUSD, AUDUSD.** These are the only pairs on disk, other than USDJPY, with broker-MEASURED p90 spreads in Kai's file:
  - EURUSD 1/1/1 points (Asia/London/NY), AUDUSD 1/1/1, GBPUSD 2/2/3.
  - USDJPY, for reference, is 2/2/2 points, i.e. 0.2 pip.
- **Excluded:** USDCAD, USDCHF, NZDUSD, EURGBP, EURCHF and the JPY crosses. Their costs are unmeasured proxies (5–13 points). XAUUSD is excluded too: different cost structure, and the M5 breakout family was already tested there.
- **Disclosure:** the unfiltered base (B2) was run on EURUSD and AUDUSD in Track B, where it failed the IS cost gate (2019–2020 gross < 2× cost). GBPUSD was not tested. The H4 filter has never been run on any of these three pairs.

## Window and contamination
- Data 2019-01-01..2025-10-09. Walk-forward IS 24 months / OOS 6 months; 10 non-overlapping OOS windows 2021-01-01..2025-10-09.
- For USDJPY, all of 2019-01..2025-10-09 was used to select the system (Track B → V2). That is irrelevant for the new pairs, whose REB-H4 results have never been seen.
- No tuning: no parameter, filter or session changes.

## Pooling and pass bar
- **Primary:** new-pair OOS trades pooled (EURUSD + GBPUSD + AUDUSD; walk-forward run per symbol, then pooled).
- **Full pass bar on the pooled new-pair result:**
  - Positive expectancy in every OOS year 2021–2025.
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x.
  - ≥ 300 OOS trades.
  - Portfolio max DD ≤ 20% (closed-trade equity at 1% per trade).
  - Worst losing streak ≤ 12.
- **Also reported, not decisive:** per-symbol results, and new pairs + USDJPY V2 OOS pooled.
- **Trials:** 4 grid params × 3 symbols = 12 new trials logged in results/trials.csv. The Bonferroni threshold and deflated Sharpe are recomputed.

## Holdout gate
- ONLY if the pooled new-pair result meets the full bar, run the untouched holdout 2025-10-10..2026-10-09 ONCE on USDJPY + EURUSD + GBPUSD + AUDUSD.
  - Data: Dukascopy, with the IC MT5 M5/M1 export as a price cross-check.
  - Parameters: frozen as the walk-forward rule's choice on the last IS window per symbol.
  - Write results/HOLDOUT_USED_REB_H4.
- Otherwise the holdout is NOT run and stays unused.
