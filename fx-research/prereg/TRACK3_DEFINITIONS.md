# Track 3 - Kai demo techniques: operational definitions (written BEFORE any backtest)

Sources checked:
- /workspace/xau_lab_review/xau_lab/tech/T01_smc_ict.py, T06_asia_break_retest.py and T08_multitf_confluence.py. This is Kai's lab code as reviewed on 2026-10-02. It may differ from the build that later ran on demo.
- /workspace/kai-skills/MULTI_TECH_DEMO_PASTE.txt (spec).
- KAI_PREDA_SETUP_V1/V2_PASTE.txt and KAI_T14_VERIFY_PASTE.txt (Preda setup that became T14/T15).
- No T15 source file was found anywhere on the box. HANDOFF.md (1 Oct) notes that the deployed lab added an EMA50-H4 filter to T01/T03/T06/T07/T08/T12/T15, plus a per-technique martingale (×2.1, reset after 5 losses, 0.01→0.19 lots). The martingale is NOT replicated.

Common to all techniques:
- Signals are computed on closed bars only. Entry is at the next bar's open, except T15, which uses a stop entry.
- 1 position at a time per technique and symbol.
- FLAT 1% risk per trade. No martingale, grid or averaging.
- Costs: IC_COSTS_FROM_KAI_20261011.md, via engine.py.
- Entries blocked 20:30–24:00 UTC and at weekends.
- Minimum stop: XAU $1 / FX 5 pips; tighter stops are widened and TP is scaled with them.
- Safety time-exit after 288 M5 bars (24 h) for T01/T06/T08, which have no time exit in the source.
- Walk-forward: IS 24 months / OOS 6 months; 10 non-overlapping OOS windows 2021-01-01..2025-10-09. Param chosen by IS t-stat.
- Holdout (>= 2025-10-10) is never loaded.
- Data and symbols:
  - XAUUSD on Dukascopy M1 mid, using the source's USD constants.
  - FX majors (EURUSD, GBPUSD, USDJPY, AUDUSD), T01/T06/T08 only, with "ATR-normalised" constants: each USD constant c becomes (c / 2.0) × ATR14(M5) at the signal bar. $2.0 is taken as a nominal XAU M5 ATR, fixed a priori and not fitted.
  - T15 is XAU-only: its $5 stop and EMA-tick structure are gold-specific.

## T01 SMC/ICT sweep-reclaim (magic 772001), M5 + H4
- H4 bars are built in UTC.
- BOS event: the last completed H4 close is above the max high of the previous 24 completed H4 bars (+1), or below their min low (−1).
- Bias modes (grid):
  - `src`: the event on the last completed H4 bar only, else 0. Buys are allowed if bias ≥ 0 and sells if ≤ 0, exactly as in the source.
  - `persist`: direction of the most recent BOS event. Buys only if +1, sells only if −1.
- Equal lows/highs: within the 12 closed M5 bars before the signal bar, two bar lows are within tol = $0.15. The level is the lowest such low (mirrored for highs).
- Signal bar: low < level, close > level, bullish, body ≥ $0.50 (mirrored for sells). Buys are checked first.
- SL = signal-bar low − $0.30. Distance is clamped to [$1, $4].
- TP (grid): 1R (source) or 2R (parent's description).
- "Structure confirm"/CHoCH and OB/FVG retest from the spec are NOT in the source code, so they are not added.
- Grid: 2 bias × 2 TP = 4 per symbol.

## T06 AsiaBreak retest (magic 772006), M5
- Asia range: M5 bars 23:00 (previous UTC day)–06:55 UTC (= 06:00–13:55 ICT). At least 20 bars are required.
- Signals 07:00–17:00 UTC (the ICT day; the source's "today" is the ICT date).
- Buy setup:
  - Break: one of the previous 19 closed bars closed above AH + $0.20.
  - Retest bar: low ≤ AH + $0.15, close > AH, and the previous bar's close > AH.
  - SL distance = entry − min(bar low, AH − $0.30), clamped to [$0.8, $3.0]. The engine minimum of $1 applies.
  - TP 1R.
- Sells are the mirror image.
- Grid: max trades/day {1, unlimited} × TP {1R, 1.5R} = 4.

## T08 MultiTF confluence (magic 772008), M15 + M5 + H4
- Bias: last completed H4 close vs EMA50 of completed H4 closes.
- M15 trigger on a closed M15 bar:
  - Buy: low < min low of the previous 10 M15 bars, close > that min, bullish, body ≥ $0.80.
  - Sell: the mirror image.
- M5 confirm: the last closed M5 bar, i.e. the last M5 inside the trigger M15 bar, closes in the trade direction.
- Layers = (bias agrees) + (M5 confirm agrees).
- Required layers (grid): ≥1 (source code) or 2 (strict, matching the parent's description "H4 bias + M5 confirm").
- SL = trigger extreme ∓ $0.20, clamped to [$1, $3.5]. TP 1R (grid also includes 1.5R).
- Grid: 2 × 2 = 4.

## T15 Preda-v5 (magic 772015), M1 XAUUSD
- Cross definition (grid):
  - A: close crosses EMA55.
  - B: EMA26 crosses EMA55.
  - The pullback count resets on every cross.
- Tracking after a bullish cross:
  - Peak = highest high since the cross.
  - A pullback starts when price retraces from the current peak by ≥ X. X is either 30% of the leg (cross close → peak) or 1 × ATR14(M1) (grid).
  - Pullback #k ends when a new peak above the previous peak is made. Pullbacks are counted 1, 2, 3...
- Exhaustion signal: a bar during pullback #1 or #2 (before a new peak) that is any of:
  - a pin bar: lower wick ≥ 50% of range and body ≤ 30% of range;
  - an inside bar;
  - the 3rd consecutive bar of decreasing range.
- Entry: buy-stop at the signal-bar high, valid for the next bar only.
- SL = EMA55 − $5.00 at the signal bar.
- TP = current peak. Skip if TP distance < 0.5 × SL distance.
- Timeout 60 M1 bars.
- Freshness (grid): signal within 60 bars of the cross, or unlimited.
- Bearish is the mirror image.
- Grid: 2 × 2 × 2 = 8.

## MCM1 (magic 20260716)
Source lost; not backtested (noted only).

## Pass bar
Unchanged from the main study: positive every OOS year (or 4 of 5 years); PF ≥ 1.2 at 1x and > 1.0 at 1.5x; ≥ 300 OOS trades; DD ≤ 20%; streak ≤ 12. Also reported: DSR (strict/pooled) and the Bonferroni t threshold.
