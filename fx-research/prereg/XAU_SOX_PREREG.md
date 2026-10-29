# XAUUSD M5 session-open expansion scalp (SOX): pre-registration

- Written BEFORE any run. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- **Data:** Dukascopy XAU/USD M1 bid+ask → mid, M5/H1 in UTC. Window 2019-01-01..2025-10-09; the holdout (2025-10-10+) is untouched.
- **Costs:** Kai's IC file via the engine. Session p90 spread 12/11/10 points (Asia/London/NY; NY-late ×1.5; 20:30–24:00 UTC and weekend 40 points), half at entry and half at exit; $3.50/lot/side; $0.05/oz/side slippage; swap with Wednesday ×3. Sensitivity gross/1x/1.5x/2x.
- **Risk:** flat 1% per trade.

## Definitions (long; the short is the exact mirror)
- **Windows (fixed UTC, NO DST adjustment):** London 07:00–09:00 UTC; NY 12:30–14:30 UTC. A bar is in the window if its start is ≥ the window start and < the window end.
  - Note: in UTC terms the real cash opens move by 1 h with DST. We keep fixed UTC as instructed.
- **ATR14:** Wilder ATR14 on the continuous M5 series (bars from prior days included, i.e. prior-day context). Every use is of ATR at a bar that is already CLOSED.
- **Quiet pre-open:**
  - The 6 M5 bars immediately before the window start (London 06:30–06:55; NY 12:00–12:25) must all exist.
  - Their mean (high − low) < 0.7 × ATR14 at the close of the last pre-window bar.
  - Otherwise no trade in that window.
- **Expansion bar:** a bar i inside the window with (high − low) > 1.5 × ATR14[i−1] (ATR of the previous closed bar; no lookahead).
  - Close in the top 25% of its range ((close − low)/(high − low) ≥ 0.75) → long; bottom 25% (≤ 0.25) → short.
  - **Only the FIRST qualifying bar per window** (either direction) is considered. If it is rejected by the trend filter or the spread filter, there is no trade in that window; we do not look for a second bar.
- **Spread filter (as before):** skip if the Dukascopy spread at bar i > 2 × the rolling 1-day median.
- **Entry (dimension):**
  - `close`: enter at close[i]; live from bar i+1.
  - `stop`: buy-stop at high[i], valid on bar i+1 only; filled if high[i+1] > high[i], at max(open[i+1], high[i]); cancelled otherwise. On the fill bar only the SL can trigger.
- **Trend filter (dimension):**
  - `none`.
  - `h1`: EMA55 of H1 closes on the last COMPLETED H1 bar (end ≤ the expansion bar's close) > its value 10 completed H1 bars earlier for longs, < for shorts.
- **Stop-loss (single rule, fixed now):** SL = low[i] − $0.10 (the opposite end of the expansion bar plus a buffer). If entry − SL < $3.00/oz, widen to $3.00. There is no maximum.
- **Exits (dimension):**
  - **A:** TP at 1R.
  - **B:** TP at 1.5R.
  - **C:** 50% at 1R; the WHOLE remaining position trails under each new confirmed M5 fractal 3-3 swing low − $0.10 (confirmed at j+3; never lowered); no TP on the rest.
  - **D:** time stop. Exit at the close of the 6th bar after entry (bars entry+1..entry+6 for `close`; the fill bar counts as bar 1 for `stop`). The SL stays active; no TP.
  - **E (quick scalp):**
    - TP at entry + (est. cost + $1.00), where est. cost = the engine's 1x round-trip cost for the entry time (½ spread in + ½ spread out at the same session + 2 × slippage + commission).
    - Once a bar's high reaches entry + $0.60, the SL moves to entry (gross breakeven) from the NEXT bar on. This is a conservative intrabar assumption.
  - **All exits:** SL is checked before TP within a bar; gaps fill at the open; weekend safety exit.
- **Positions:** one at a time. No martingale, grid or averaging. Entries are never in 20:30–24:00 UTC (the windows lie outside it).

## Grid (20 variants; all logged as trials)
- entry {close, stop} × trend {none, h1} × exit {A, B, C, D, E}.
- Fixed to stay in budget:
  - BOTH windows are traded in every variant; London vs NY is reported separately, not selected.
  - Single SL rule (expansion-bar opposite end + $0.10, $3 floor).
  - Single quiet threshold (0.7) and expansion threshold (1.5×, top/bottom 25%).

## Walk-forward, finalist, pass bar, holdout
- **Walk-forward:** engine.wf_windows (IS 24 months / OOS 6 months, 10 stitched non-overlapping OOS windows 2021-01..2025-10-09). Per window, the best IS t-stat (≥ 30 IS trades).
- **Finalist** = the LAST window's choice.
- **Pass bar on the stitched OOS:**
  - every OOS year positive;
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x;
  - ≥ 300 trades;
  - max DD ≤ 20%;
  - worst streak ≤ 12.
  - **Plus the key metric:** net average $/oz per trade after 1x costs ≥ $0.30/oz, i.e. at least the cost per trade (states "clearly exceeds cost").
  - t vs Bonferroni and the DSR are reported.
- **Verdict:** "edge" only if it passes and the holdout is consistent; "needs more data" if it passes but t < Bonferroni; otherwise "no edge".
- **Holdout:** 2025-10-10..2026-10-09, once, finalist only, only if it passes; write results/HOLDOUT_USED_XAU_SOX. Otherwise it is not run.
