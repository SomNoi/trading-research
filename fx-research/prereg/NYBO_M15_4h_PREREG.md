# PRE-REGISTRATION: NYBO M15 / 4h pre-range (New York open breakout) - contamination-safe out-of-sample test
Registered: 2026-10-11T04:02:10Z (UTC). Author: Grok Bot executor for Preda Wisetsuntonr. Research only - no trading, no broker logins.
This file is frozen once its sha256 is written to results/prereg_hashes.txt. No edits afterwards. No parameter tuning: every parameter below is fixed.

## Origin (honest disclosure)
The variant (M15 bars, 4h pre-range) was found in results/robust_usdjpy_nybo.csv by looking at USDJPY 2021-01..2025-10-10. That span (and the
USDJPY 2019-2020 walk-forward in-sample) is therefore USED for selection. USDJPY 2019-01..2025-10-09 is excluded from this test.
EURUSD, GBPUSD, AUDUSD and XAUUSD were also seen in the walk-forward (NYBO family chosen on USDJPY only, other symbols failed), so they are also excluded.

## Exact rule (fixed)
- Data: Dukascopy M1 BID+ASK, mid = (bid+ask)/2, zero-volume bars dropped, resampled to M15 bars (UTC, label=left, closed=left). Fetched by
  scripts/fetch_dukascopy2.py with END=2025-10-10 (no bar at/after 2025-10-10 00:00 UTC is downloaded or loaded for the new pairs).
- Session: New York open = 08:00 America/New_York (DST-aware). For each NY business day (Mon-Fri):
  - Pre-range = M15 bars with open time in [open-4h, open) i.e. 04:00-08:00 NY. Require >= 80% of the 16 bars present, else skip the day.
    hi = max(high), lo = min(low). Skip if hi <= lo.
  - Breakout window = bars with open time in [08:00, 11:00) NY. Scan bars in order; first bar with high >= hi -> LONG, first with low <= lo -> SHORT.
    If one bar touches both levels -> skip the day. At most one trade per day.
  - Entry: stop-entry fill at max(bar open, hi) for long, min(bar open, lo) for short (gap fills at the open).
  - Stop: opposite range edge (long SL = lo, short SL = hi). On the fill bar only the SL may trigger.
  - Minimum stop distance (broker stops_level = 0): JPY pairs 0.05 (5 pips); USDCAD/USDCHF 0.0005 (5 pips); USDJPY 0.05. Tighter stops widened to the minimum.
  - No take-profit. Exit at the open of the first M15 bar at/after 16:00 America/New_York, or at the SL (SL first if a bar touches it; gaps through SL fill at the open).
  - Entry block (engine): no entries 20:30-24:00 UTC or Sat/Sun (not binding for this rule).
  - Simulator: scripts/engine.py simulate()/run_sim() as of this registration (one position at a time).
- Sizing: 1% of a $10,000 reference account risked per trade (1R = |entry - SL|), non-compounded. No martingale/grid/averaging/size-up.

## Costs (fixed)
- Commission $3.50/lot/side ($7 RT) per IC_COSTS_FROM_KAI_20261011.md, converted to quote currency: xxxJPY = 7e-5 x USDJPY rate (USDJPY mid from Dukascopy at entry time;
  if missing, 7e-5 x price/1.10 is NOT used - nearest previous USDJPY close is used), USDCAD/USDCHF/USDJPY = 7e-5 x price.
- Spreads: Kai's file covers USDJPY only among these symbols: USDJPY uses it exactly (p90 2/2/2 points; 16:00-20:30 UTC 1.5x NY; 20:30-24:00 UTC & weekend 33 points).
  New pairs are NOT in Kai's file -> conservative proxy = 2 x IC published Raw average (ic.com/eu/en/trading-pricing/spreads-and-swaps, retrieved 2026-10-11),
  rounded up to whole points, same value for asia/london/ny buckets; 16:00-20:30 UTC = 1.5x; 20:30-24:00 UTC & weekend = 15x:
  EURJPY avg 0.31 pip -> 7 pts; GBPJPY 0.65 -> 13 pts; AUDJPY 0.40 -> 8 pts; USDCAD 0.23 -> 5 pts; USDCHF 0.34 -> 7 pts (points: 0.001 JPY, 0.00001 others).
  Half the spread at entry + half at exit (by UTC time of each fill).
- Slippage 0.1 pip per side on every fill. Swaps: none (all trades close 16:00 NY, before the 17:00 NY rollover).
- Sensitivity: spread+commission+slippage x1.5 and x2.

## Symbols and windows
- Primary test: EURJPY, GBPJPY, AUDJPY, USDCAD, USDCHF, trades entered 2021-01-01 .. 2025-10-09 (UTC). Supplementary (reported, not in criteria): 2019-01-01 .. 2020-12-31.
- One-time holdout (only if "holds up"): USDJPY trades entered 2025-10-10 .. 2026-10-09 (data already on disk, never loaded so far).

## "Holds up" criteria (ALL must hold, on 2021-01..2025-10-09, 1x costs unless stated)
1. PF > 1.10 on at least 3 of the 5 new pairs.
2. Pooled PF (all trades of the 5 pairs, each trade 1% risk) >= 1.20.
3. Pooled PF > 1.00 at 1.5x costs.
4. Pooled expectancy > 0 in every calendar year 2021, 2022, 2023, 2024, 2025 (partial).
5. Per-pair max drawdown <= 20% and worst losing streak <= 12 on at least 3 of the 5 pairs.
If any fails -> NYBO is a clear FAIL and stops here (no holdout run).

## Holdout evaluation (only if it holds up)
USDJPY, same fixed rule and cost model, trades 2025-10-10..2026-10-09, run once. Reported against the standing pass bar items that are measurable on one year:
expectancy > 0, PF >= 1.2 at 1x and > 1.0 at 1.5x, max DD <= 20%, worst streak <= 12 (trade count ~240 < 300 is noted, not failed).

## Trials
This test counts as 1 new trial per pair (5) in results/trials.csv (+1 if the holdout is run).
