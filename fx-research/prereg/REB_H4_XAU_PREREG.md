# REB-H4 on XAUUSD: independent out-of-sample test. Pre-registration

- Written BEFORE any REB-H4 / B2 range-breakout result on XAUUSD was computed. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- REB-H4 and the unfiltered B2 base have **never** been run on XAUUSD. trials.csv has no B2/REB rows for XAUUSD.
- **Disclosure:** other M5 breakout-family systems were tested on XAUUSD and all failed: 3_session_bo, 7/8 ORB, T06 asia_break. This test is independent of them in rules, but not in the "breakout on gold" idea.
- Before registering I inspected only data structure: bar availability, the daily break, and early-close days. No REB-H4 or B2 result was seen.

## System: identical to the USDJPY V2 / demo-handoff setting (handoff/REB-H4/SPEC.md); no tuning
- **Bars:** M5 resampled from Dukascopy XAUUSD M1 mid, in UTC.
- **D1 range:** RANGE = high − low of the last completed, non-empty D1 bar. D1 runs 20:00 → 20:00 UTC. Monday uses the Friday 20:00 stub, as on USDJPY.
- **Levels:** at 07:00 UTC, up = open(07:00 M5 bar) + **f × RANGE**, dn = open − f × RANGE, with **f = 0.5** (relative, unchanged). No 07:00 bar → no trade that day.
- **Trigger and entry:** the first M5 bar between 07:00 and 20:00 UTC that touches a level gives a stop entry at max(open, up) or min(open, dn).
  - A bar touching both levels → day skipped. The first touch ends the day; at most one trade per day.
- **H4 filter F2 (unchanged):**
  - Fractal swing high/low with 2 bars on each side, on H4 bars anchored 00:00 UTC; confirmed when bar k+2 completes.
  - UP = last swing high > previous AND last swing low > previous; DOWN is the mirror.
  - Use the last completed H4 bar at the entry bar's start. Long only if UP, short only if DOWN.
- **Stop-loss:** the **opposite level** (distance = RANGE; relative, unchanged). No take-profit.
- **Time exit:** at the first M5 bar ≥ 20:00 UTC (its open), unchanged.

## Translation of absolute-unit settings to XAU (rule fixed now)
- **Minimum stop:** USDJPY used 5 pips. XAU uses the engine's existing XAU minimum of **$1.00/oz**, as used in all earlier XAU research (engine.MIN_STOP). If the SL distance is < $1.00, the SL is widened to entry ∓ $1.00.
  - There is no ratio rescaling, because $1.00 is the engine's pre-existing XAU convention.
- **Daily break:** the XAU daily break is about 20:58–22:00 UTC in summer and 21:58–23:00 UTC in winter. The 20:00 UTC time exit and the existing entry block (20:30–24:00 UTC, and weekends) already lie before or around it, so no change is needed.
- **US-holiday early closes:** 54 weekdays in 2019-01..2025-10-09 have the last pre-20:00 bar before 19:55 UTC. These are MLK, Presidents', Memorial, Juneteenth, Independence, Labor, Thanksgiving and Christmas Eve sessions closing about 17:00–19:45 UTC.
  - Rule: if the session closes before 20:00 UTC and the next bar is after 20:00 UTC, the time exit is at the **open of the last M5 bar before the early close** (≤ 5 min before the close). The position is never carried over the break.
  - The trigger window on such days ends at the early close.

## Costs (Kai's file; engine, unchanged)
- **Spreads:** XAU session p90 = 12 / 11 / 10 points (Asia / London / NY; $0.12 / $0.11 / $0.10). NY-late ×1.5; the weekend/rollover spread is 40 points. Half the spread is charged at entry and half at exit.
- **Commission:** $3.50 per lot per side, 100 oz per lot ($0.07/oz round trip).
- **Slippage:** $0.05/oz per side.
- **Swap:** −57.03 / +39.77 points per lot per night (long/short), Wednesday ×3. It applies only if a position crosses rollover, which the time exit normally prevents.
- **Sensitivity:** costs ×1 / ×1.5 / ×2.

## Window, risk, statistics
- **Window:** 2019-01-01..2025-10-09 only. No XAU parameter is fitted, so the whole window is out-of-sample for XAU. **Decisive window = 2019-01-01..2025-10-09.** 2021-01..2025-10-09 is reported for information, to compare with the USDJPY walk-forward span.
- **Risk:** flat 1% risk per trade.
- **Trials:** 1 strategy trial (XAUUSD, ('B2', 0.5, 'opp') + F2) plus 4 IQ hit-rate trials, logged in results/trials.csv. Bonferroni (one-sided 5%) and the deflated Sharpe are recomputed with analyze.py.

## Pass bar (all required)
- Positive expectancy (net R at 1x) in every calendar year 2019–2025 (2025 = Jan..Oct 9).
- PF ≥ 1.2 at 1x AND > 1.0 at 1.5x.
- ≥ 300 trades.
- Max DD ≤ 20% (closed-trade equity at 1% per trade).
- Worst losing streak ≤ 12.
- No martingale, grid or averaging (structurally satisfied).
- t-stat versus the Bonferroni threshold is reported; it is not part of the bar, consistent with earlier tracks.

## Holdout gate
- Run the untouched holdout 2025-10-10..2026-10-09 ONCE, ONLY if the full bar is met:
  - same frozen rules, on Dukascopy XAUUSD M1;
  - the IC MT5 export (data/ic-mt5-2026-10-10) used as a price cross-check of entries and exits;
  - write results/HOLDOUT_USED_REB_H4_XAU.
  - Holdout reading: PF ≥ 1.0 at 1x and positive expectancy = "consistent"; otherwise "not confirmed". No re-runs.
- If the bar is not met, the holdout is NOT run.

## IQ hit-rate check (numbers only; no IQ Option access)
- **Signals:** the same XAU REB-H4 signals.
- **Entry instant:** the first M1 bar inside the M5 fill bar reaching the entry price. Strike = entry price.
- **Expiry:** T ∈ {5, 15, 30, 60} min. Expiry price = M1 mid open at entry_minute + T, or the next M1 bar within 5 min; otherwise the signal is dropped and counted.
- **Outcome:** win only if the price moved strictly in the trade direction. Ties count as losses and are reported.
- **Statistics:** count, raw hit rate, Wilson 95% lower bound per expiry.
- **Decision:** "clears" a breakeven only if the Wilson LB ≥ 55.6% / 54.1% / 53.5% (80 / 85 / 87% payout). Informational; no holdout.
