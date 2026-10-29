# XAUUSD EMA55 pullback, higher-timeframe follow-up (cost-drag fix): pre-registration

- Written BEFORE any run of these variants. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- This follows prereg/XAU_EMA55_PB_PREREG.md (sha ba1f4a38). That M5 grid of 72 variants was NO EDGE: gross ≈ 0 and costs ≈ 0.17R per trade at a median stop of about $1.75/oz.
- **Data:** Dukascopy XAU/USD M1 bid+ask → mid; M5/M15/H1/H4 resampled in UTC (H4 anchored 00:00 UTC). Window 2019-01-01..2025-10-09; the holdout is untouched.

## Reused unchanged from the previous prereg
- **Indicators:** EMA55 on close; ATR14 (Wilder).
- **Trend:** EMA55[t] > EMA55[t−10] AND N consecutive closes on the trend side before the touch bar.
- **Touch rule:** low ≤ EMA + X and close > EMA (short mirrored).
- **Trigger:** the next bar must be contiguous.
- **Swings:** fractal swings confirmed at k bars after the swing; SL buffer $0.10.
- **Exits:** A = full TP at the latest confirmed swing high (skip if ≤ entry); B = 50% at that swing high, with the whole remaining position trailed under each new confirmed swing (±$0.10); C = 2R.
- **Other rules:** SL is checked first within a bar; gaps fill at the open; weekend safety exit at the last bar before the weekend close; one position at a time.
- **Spread filter:** Dukascopy spread > 2 × the rolling 1-day median → skip.
- **Blocked entries (default):** 20:30–24:00 UTC and weekends.
- **Costs:** engine/Kai, unchanged. p90 12/11/10 points; NY-late ×1.5; **20:30–24:00 UTC and weekend = Kai's rollover/weekend-close spread of 40 points** (Kai's file, NOT Dukascopy). $3.50/lot/side; $0.05/oz/side slippage; swap with Wednesday ×3. Sensitivity 1x/1.5x/2x and gross (0x).
- **Risk:** flat 1% per trade.

## Fixed this time (dimensions that did not matter in the 72-variant grid; nothing is re-gridded)
- **N = 6.** N=6 vs 12 made no consistent difference.
- **Entry = `close`:** next-bar close > touch-bar high, enter at that close. Close entries had slightly better gross than stop entries.
- **Fractal = 3-3.** Slightly better gross than 2-2.
- **X = 0.10 × ATR14 of the entry timeframe** (at the touch bar). This is a scale-free replacement for the $0/$0.30/$0.50 dollar grid.

## Family 1: same rules on a higher entry TF (6 variants)
- **Entry TF {M15, H1} × exit {A, B, C}.** All indicators, swings and trailing are on that TF.
- **SL:** the tighter valid candidate of (latest swing low − $0.10) and (EMA − 1×ATR14); valid if ≥ $1.00 below the entry; skip if risk > 2×ATR14 (same rule as before).

## Family 2: H1 trend filter + lower-TF pullback entry, with HTF-sized stops (24 variants)
- **Entry TF {M5, M15}:** the full EMA55 pullback rules above on that TF.
- **Filter {H1, H1+H4}:**
  - H1 = the last COMPLETED H1 bar j (end ≤ the decision time, i.e. the close of the trigger bar) has EMA55_H1[j] > EMA55_H1[j−10] AND close_H1[j] > EMA55_H1[j].
  - H1+H4 = the same condition also on the last completed H4 bar.
  - Shorts are mirrored. No lookahead.
- **Stop {h1atr, h1swing}:**
  - h1atr: SL = entry − 1.0 × ATR14_H1[j].
  - h1swing: SL = latest confirmed H1 swing low (3-3, confirmed by the decision time) − $0.10.
  - Both: if the distance is < $4.00, widen to $4.00; skip if the distance > 3 × ATR14_H1[j].
- **Exits {A, B, C}** use H1 structure:
  - A/B take profit at the latest confirmed H1 swing high (skip if ≤ entry).
  - B trails under new confirmed H1 swing lows (applied at the entry-TF bar where that H1 bar completes).
  - C = 2R.
- The median stop in $/oz is reported; the target is ≥ $4–5.

## Walk-forward and finalist
- **Grid:** 30 variants (6 + 24), entry block ON. engine.wf_windows (IS 24 months / OOS 6 months, 10 non-overlapping stitched OOS windows 2021-01..2025-10-09). Per-window choice = best IS t-stat (≥ 30 IS trades) across all 30.
- **Finalist** = the variant chosen by the LAST IS window (frozen).
- **Pass bar on the stitched WF OOS:**
  - every OOS year positive;
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x;
  - ≥ 300 trades;
  - max DD ≤ 20%;
  - worst streak ≤ 12;
  - no martingale.
  - t versus Bonferroni and the DSR are reported.
- **Verdict:** "edge" only if it passes AND the holdout is consistent; "needs more data" if it passes but t < Bonferroni or the sample is small; otherwise "no edge".

## Rollover-block dimension (explicit; counted as trials)
- The finalist is re-run with the entry block OFF (entries allowed 20:30–24:00 UTC; weekends stay blocked). Those entries pay Kai's 40-point rollover spread in the cost model, and exits there pay it too.
- Same for the best Family-1 and best Family-2 variant by full-period IS t-stat if they differ from the finalist. At most 3 extra trials.
- Results are reported by entry window: 20:30–24:00 UTC vs the rest, and by ICT hour.
- **Recommendation rule:** keep the block unless the 20:30–24:00 subset has positive expectancy at 1.5x costs with ≥ 100 trades. Information only; it never changes the finalist.

## Holdout gate
- ONLY if the stitched WF OOS passes the full bar: run the frozen finalist ONCE on 2025-10-10..2026-10-09.
  - Report separately, plus the last-3-months slice.
  - Write results/HOLDOUT_USED_XAU_EMA55_PB_HTF.
- Otherwise the holdout is not run.

## Trials
- 30 grid trials + up to 3 block-OFF trials, appended to results/trials.csv.
- Bonferroni and DSR are recomputed with analyze.py.
