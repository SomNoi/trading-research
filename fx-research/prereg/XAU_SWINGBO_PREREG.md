# XAUUSD M5 swing-high breakout with H1 trend filter (Kai's idea): pre-registration

- Written BEFORE any run of this system. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- **Data:** Dukascopy XAU/USD M1 bid+ask → mid; M5 and H1 resampled in UTC. Window 2019-01-01..2025-10-09; the holdout (2025-10-10+) is untouched.
- **Costs:** Kai's IC file via the engine. p90 12/11/10 points; NY-late ×1.5; 20:30–24:00 UTC and weekend = 40 points; $3.50/lot/side; $0.05/oz/side slippage; swap with Wednesday ×3. Reported gross and at 1x/1.5x/2x.
- **Risk:** flat 1% per trade.

## Rules (long; the short is the exact mirror)
- **Swings:** M5 fractal 3-3 (strictly beyond the 3 bars on each side), confirmed at the close of bar j+3.
- **H1 trend:** on the last COMPLETED H1 bar (end ≤ the start of the current M5 bar), EMA55_H1 > its value 10 completed H1 bars earlier AND close_H1 > EMA55_H1.
- **Setup:**
  - SH = the latest confirmed M5 swing high (bar jh). The setup stays alive while no M5 bar after jh has traded ≥ SH + $0.10, i.e. the level is not yet broken.
  - A new confirmed swing high replaces the setup.
- **Pullback (dimension P):**
  - `swl`: a confirmed M5 swing low exists at a bar index > jh (a structural pullback after the swing high).
  - `ema`: some M5 bar after jh has low ≤ EMA55_M5 (EMA55 of M5 closes).
- **Entry:**
  - Buy-stop at SH + $0.10, working on M5 bar i if the setup is alive, the pullback is met, and the H1 trend is OK. All of these are evaluated with information up to the close of bar i−1.
  - Fill if high[i] ≥ level, at max(open[i], level). On the fill bar only the SL can trigger.
  - **Expansion variant (`exp`):** instead of the stop order, enter at the CLOSE of the breakout bar i, only if close[i] > level AND bar range (high − low) > 1.5 × ATR14_M5[i−1]. Live from bar i+1.
- **Stop:**
  - SL = PL − $0.10, where PL = the lowest low after jh up to bar i−1.
  - Minimum stop floor F ∈ {$1, $4}: if entry − SL < F, widen to F.
  - Skip if PL ≥ the level, or the stop is > 4 × ATR14_M5[i−1].
- **Spread filter (as before):** skip if the Dukascopy spread at bar i−1 > 2 × the rolling 1-day median.
- **Exits (dimension E; both trail the remaining position under each new confirmed M5 swing low − $0.10, never lowering the stop):**
  - `1R`: 50% at entry + 1R.
  - `psh`: 50% at the most recent confirmed swing high before SH whose price is > entry (the "prior swing high"). If none exists, use 2R.
  - The rest has no take-profit; trailing only.
  - Weekend safety exit at the last bar before the weekend close. SL is checked first within a bar; gaps fill at the open.
- **Blocks:** entries blocked 20:30–24:00 UTC and on weekends; the block stays ON. One position at a time; no martingale, grid or averaging.

## Grid (12 variants)
- P {swl, ema} × F {1, 4} × E {1R, psh} = 8 stop-order variants.
- Plus `exp` entry for P = swl × F {1, 4} × E {1R, psh} = 4.
- All 12 are logged as trials.

## Walk-forward, finalist, pass bar, holdout
- **Walk-forward:** engine.wf_windows (IS 24 months / OOS 6 months, 10 stitched non-overlapping OOS windows 2021-01..2025-10-09). Per window, the best IS t-stat (≥ 30 trades).
- **Finalist** = the LAST window's choice (frozen).
- **Pass bar on the stitched OOS:**
  - every OOS year positive;
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x;
  - ≥ 300 trades;
  - max DD ≤ 20%;
  - worst streak ≤ 12.
  - t vs Bonferroni and the DSR are reported.
- **Verdict:** "edge" only if it passes and the holdout is consistent; "needs more data" if it passes with t < Bonferroni; otherwise "no edge".
- **Holdout:** run 2025-10-10..2026-10-09 once, only for a passing finalist (write results/HOLDOUT_USED_XAU_SWINGBO). Otherwise it is not run.

## Blind-read rule (Part 1, applied to the refcheck window)
- At the close of the 2026-10-14 23:35 UTC bar, apply (a) these swing-breakout rules and (b) the earlier EMA55-pullback rules (prereg XAU_EMA55_PB) mechanically.
- Decision = BUY-STOP / SELL-STOP order or WAIT. Entry, SL and TP are as defined above; the entry block applies.
