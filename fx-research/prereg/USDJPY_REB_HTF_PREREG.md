# USDJPY M5 range-expansion breakout (Track B "B2") + higher-timeframe filters: pre-registration
Written BEFORE any run of these filters. The sha256 and UTC timestamp are recorded in results/prereg_hashes.txt.

## Base (UNCHANGED from prereg/TRACK_A_B_PREREG.md, Track B "B2", code scripts/trackB.py::b2_range_bo)
- Symbol USDJPY; M5 bars from Dukascopy M1 mid.
- D1 range: high − low of the last completed D1 bar. D1 bars run 20:00 → 20:00 UTC ("24h", offset 20h).
- At 07:00 UTC, set up = open(07:00) + f × range and dn = open(07:00) − f × range.
  - The first M5 bar touching one level triggers a stop entry at max(open, up) or min(open, dn).
  - If a bar touches both levels, that day is skipped.
- Stop: "opp" = the opposite level, or "half" = entry ∓ 0.5 × range. No TP.
- Time exit at 20:00 UTC (the open of the first bar ≥ 20:00).
- Grid (unchanged, 4 params): f ∈ {0.3, 0.5} × stop ∈ {opp, half}.
- Walk-forward selects among the 4 params in each window by IS t-stat. All 4 passed the Track B IS gate, so the gate is not re-applied.
- **Caveat:** the base and its grid were selected after seeing 2019-01..2025-10-09 data (Track B OOS PF 1.28). The 12-month holdout is the only fully clean test.

## HTF filters (at most 2), applied to the DIRECTION of each base trade at its entry time
Only fully completed HTF bars are used: the last H1/H4 bar with end ≤ entry bar start.
- **F1, H1 EMA trend:**
  - Longs only if the last completed H1 close > EMA(200) of H1 closes.
  - Shorts only if it is < EMA(200).
  - EMA is pandas ewm(span=200, adjust=False); the first 200 H1 bars are not used.
- **F2, H4 swing structure:**
  - Fractal swings on H4 (bars anchored 00:00 UTC). Bar k is a swing high if high[k] > the highs of the 2 bars before AND the 2 bars after it; swing lows are the mirror.
  - A swing is known only once bar k+2 has completed.
  - Uptrend when the last confirmed swing high > the previous swing high AND the last confirmed swing low > the previous swing low. Downtrend is the mirror image. Anything else is neutral.
  - Longs only in an uptrend, shorts only in a downtrend; neutral means no trade.

## Variants
| Variant | Filters | Trials (4 grid params each) |
|---|---|---|
| V0 | base | Already logged as the Track B trials; not re-logged |
| V1 | base + F1 | 4 new |
| V2 | base + F2 | 4 new |
| V3 | base + F1 + F2 combined | 4 new |

- Base trades last at most until 20:00 UTC of the same day (at most 1 per day), so filtering after simulation is identical to filtering signals before simulation.
- 12 new trials are added to results/trials.csv. The deflated Sharpe and Bonferroni threshold are recomputed by analyze.py.

## Costs, walk-forward, pass bar
- **Costs:** Kai's file (IC_COSTS_FROM_KAI_20261011.md). USDJPY p90 is 2 points in all sessions, ny_late 3 points, rollover/weekend 33 points. Commission is $7 RT converted to JPY; slippage 0.1 pip per side. Swaps are per the engine (none intraday). Entry block 20:30–24:00 UTC and at weekends; minimum stop 5 pips.
- **Walk-forward:** identical to Track B. IS 24 months / OOS 6 months; 10 non-overlapping OOS windows 2021-01-01..2025-10-09. Flat 1% risk.
- **Pass bar (all must hold):**
  - Positive expectancy in every OOS year 2021–2025.
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x.
  - ≥ 300 OOS trades.
  - Max DD ≤ 20%.
  - Worst losing streak ≤ 12.
  - No martingale, grid or averaging.

## Finalist rule (fixed now)
- Candidates are V0–V3 (V0 is already known to fail the bar: DD −31%, 2023 negative).
- The finalist is the variant that meets the FULL pass bar on walk-forward OOS. If several do, it is the one with the highest OOS t-stat at 1x; if those tie, the one with fewer filters.
- If no variant meets the full bar, there is NO finalist. The holdout stays unused and the result is a clear fail.

## Holdout gate (exactly once, finalist only)
- **Data:** USDJPY 2025-10-10 00:00 UTC → 2026-10-09 23:59 UTC, Dukascopy M1 mid (already on disk under data/raw/USDJPY).
- **Frozen parameters:** the finalist's filters, plus the base param chosen by the WF rule on the last IS window before the holdout (2023-10-10..2025-10-10, best IS t-stat).
- **Warm-up:** pre-holdout bars are used only for indicator and D1 history.
- **Holdout pass:** expectancy > 0 after costs AND PF > 1.0 at 1x. PF at 1.5x and 2x is also reported.
- **IC cross-check (not decisive):** run the same frozen rule on the IC MT5 M5 export (data/ic-mt5-2026-10-10/csv/USDJPY_M5.csv; bid converted to mid via half the spread, Kai's 2 points where the spread is missing) over the same holdout period. Report its PF and expectancy and the trade-level agreement with the Dukascopy run.
- A marker file results/HOLDOUT_USED_USDJPY_REB is written; the script refuses a second run.
