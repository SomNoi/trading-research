# XAUUSD M5 EMA55 pullback (long + mirrored short): pre-registration

- Written BEFORE any result of this system was computed. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- No EMA55-pullback variant has been run on XAUUSD in this project before. Other XAU systems (breakouts, ORB, Kai techniques, REB-H4) all failed.
- **Data:** Dukascopy XAU/USD M1, bid+ask → mid OHLC plus bid/ask spread, resampled to M5, timestamps UTC. Window 2019-01-01..2025-10-09 23:59 UTC.
- **Holdout:** 2025-10-10..2026-10-09 is untouched. The user's "last 3 months" request falls inside our 12-month holdout.

## Definitions (long; the short is the exact mirror: highs↔lows, above↔below, + ↔ −)
All indicators use M5 mid prices and are computed on bar closes. Bar t = the "touch" (pullback) bar.
- **EMA:** E = EMA55(close) (pandas ewm span 55, adjust=False). ATR = ATR14 (Wilder).
- **Trend:** E[t] > E[t−10], AND close > E on each of the N bars t−N..t−1 (N ∈ {6, 12}).
- **Pullback / touch:** low[t] ≤ E[t] + X AND close[t] > E[t], with X ∈ {$0.00, $0.30, $0.50} (IC 1 point = $0.01).
- **Entry (must happen on bar t+1, which must start exactly 5 min after bar t; otherwise the setup lapses):**
  - `close`: if close[t+1] > high[t], enter long at close[t+1]. The position is live from bar t+2.
  - `stop`: buy-stop at high[t], valid for bar t+1 only. Filled if high[t+1] > high[t], at max(open[t+1], high[t]). On the fill bar only the SL can trigger; no TP on the fill bar.
- **Information set:** `close` uses bars ≤ t+1; `stop` uses bars ≤ t, because the order is placed at the close of t.
- **Swings:** a fractal k-k (k ∈ {2, 3}) swing low at bar j has low[j] strictly below the lows of the k bars on each side. It is confirmed at the close of bar j+k. Swing highs mirror this. "Latest swing" = the most recent swing confirmed within the information set.
- **Stop-loss:**
  - Candidates: (a) latest swing low − $0.10 buffer; (b) E − 1×ATR14 (at the last bar of the information set).
  - A candidate is valid if it is ≥ $1.00 below the entry price. For `stop`, the reference price is the order level high[t].
  - Pick the TIGHTER valid candidate (the higher one for longs). No valid candidate → skip.
  - Skip if the risk (reference entry − SL) > 2 × ATR14.
  - On a `stop` fill with a gap, the SL is unchanged and the risk is measured from the actual fill.
- **Exits (latest swing high = same fractal k and the same information set):**
  - **A** full take-profit at the latest swing high. Skip the trade if swing high ≤ the reference entry.
  - **B** 50% at the latest swing high (same skip rule). The WHOLE remaining position also trails: whenever a new swing low is confirmed after entry and (swing low − $0.10) > the current stop, the stop moves up to it. There is no breakeven move.
  - **C** take-profit at entry + 2R (R = entry − SL).
  - Common to all: SL is checked before TP within a bar. Gaps through SL/TP fill at the bar open.
  - **Weekend safety exit:** a position still open on the last M5 bar before the weekend close is closed at that bar's close. This rule was not in the brief and was added to avoid weekend-gap risk. There is no other time exit.
- **Spread filter:** skip if the Dukascopy bid/ask spread at the decision bar's close (bar t+1 for `close`, bar t for `stop`) is > 2 × its rolling median over the previous 288 M5 bars (1 day; spread_c, M1 last close in the bar).
- **Blocked hours:** no entries 20:30–24:00 UTC (rollover) and none on Saturday/Sunday. The entry time is the fill time (close of t+1 = start of t+2 for `close`; start of t+1 for `stop`).
- **XAU daily break** (about 20:58–22:00 UTC summer, 21:58–23:00 winter):
  - No bars exist in the break, so indicators run on consecutive bars across it.
  - A setup lapses if bar t+1 is not contiguous. Entries in the post-break hour fall inside the 20:30–24:00 block anyway.
  - Open positions are held through the break and pay the engine's rollover/weekend spread if they exit inside the block, plus swap.
- **One position at a time.** Signals while a position is open are ignored. No martingale, grid or averaging.
- **Sessions:** no session filter, i.e. trade all unblocked hours. Results by entry hour (ICT = UTC+7) are reported as information; they are not used for selection.

## Costs (Kai's file via engine; unchanged)
- **Spread:** p90 12 / 11 / 10 points by session; NY-late ×1.5; rollover/weekend 40 points. Half the spread is charged at entry and half at each exit leg.
- **Commission:** $3.50 per lot per side ($0.07/oz round trip).
- **Slippage:** $0.05/oz per side.
- **Swap:** −57.03 / +39.77 points per lot per night, Wednesday ×3, NY 17:00 rollover.
- **Sensitivity:** costs ×1 / ×1.5 / ×2.
- **Risk:** flat 1% risk per trade.
- **Exit B costs:** each 50% leg pays its own half exit spread and slippage. The commission total stays $0.07/oz.

## Grid (72 variants, all logged as trials)
N {6, 12} × X {0, 0.30, 0.50} × entry {close, stop} × fractal {2-2, 3-3} × exit {A, B, C}.

## Walk-forward and finalist
- **Windows:** engine.wf_windows: IS 24 months / OOS 6 months, 10 non-overlapping OOS windows stitched over 2021-01-01..2025-10-09.
- **Selection:** in each window, the variant with the best IS per-trade t-stat (net R at 1x, ≥ 30 IS trades) trades the next OOS window (engine.walk_forward).
- **Reporting:**
  - IS vs OOS per window.
  - Per variant: metrics on the full 2019–2025 sample (in-sample) and on the 2021..2025-10-09 span (not independent for a hand-picked variant).
  - The stitched WF OOS is the decisive result.
- **Finalist (single, frozen):** the variant chosen by the LAST IS window. It is reported with its own fixed-parameter result over the WF OOS span.

## Pass bar (on the stitched WF OOS; all required)
- Positive expectancy in every OOS calendar year 2021–2025.
- PF ≥ 1.2 at 1x AND > 1.0 at 1.5x.
- ≥ 300 OOS trades.
- Max DD ≤ 20% (closed-trade equity, 1% per trade).
- Worst losing streak ≤ 12.
- No martingale, grid or averaging.
- The t-stat versus Bonferroni (N_TRIALS from analyze.py after logging the 72) and the deflated Sharpe are reported.
- **Verdict wording:**
  - "edge" only if the bar is passed AND the holdout is consistent.
  - "needs more data" if the bar is passed but t < Bonferroni, or the holdout is not run.
  - "no edge" if the bar is failed.

## Holdout gate
- ONLY if the stitched WF OOS passes the full bar, run the frozen finalist ONCE on 2025-10-10..2026-10-09 (Dukascopy).
  - Use the IC MT5 export (data/ic-mt5-2026-10-10) as a price cross-check where it overlaps.
  - Report separately, plus the last-3-months slice 2026-07-10..2026-10-09.
  - Write results/HOLDOUT_USED_XAU_EMA55_PB.
  - Holdout reading: PF ≥ 1.0 at 1x with positive expectancy = "consistent".
- Otherwise the holdout is not run.

## Reference example (signal-detection check only; NOT used for selection or performance)
- **User example:** 2026-10-14 23:35 UTC touch bar (low about 4101.2), long trigger on the 23:40 UTC bar.
- **Data:** Dukascopy M1 2026-10-11..2026-10-15 04:00 UTC is fetched into data/refcheck/. This is post-holdout data and is not merged.
- **Check:** whether each N/X/entry variant flags it, with the entry block ON (spec) and OFF (diagnostic), and the reason if not. 23:35/23:45 UTC lies inside the 20:30–24:00 block. The example does not change the spec.
