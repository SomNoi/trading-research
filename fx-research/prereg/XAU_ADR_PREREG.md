# XAUUSD daily-range ("ADR") hypothesis: pre-registration (Part 1 definitions + Part 2 trading test)

- Written BEFORE any daily-range statistic or backtest was computed. The sha256 and UTC timestamp are in results/prereg_hashes.txt.
- **Data:** Dukascopy XAU/USD M1 bid+ask → mid (UTC), 2019-01-01..2025-10-09. The holdout (2025-10-10+) is untouched.

## Day definition (both parts)
- **Primary:** IC server day. Server time = UTC+3 while US DST is in effect (at that instant), otherwise UTC+2. The server day = the server calendar date, so day boundaries fall at 21:00 UTC (summer) / 22:00 UTC (winter).
  - XAU's daily break (about server 23:58–01:00) sits at the boundary, so the day open = the open of the first M1 bar of the server day (about 01:00 server).
- **Sunday stub rule:** bars whose server date is a Saturday or Sunday are merged into the following Monday.
  - With server = UTC+2/+3, the Sunday 22:00/23:00 UTC open is already Monday 00:00/01:00 server, so we expect no stubs. We report the count.
- **Short days:** a server day with < 18 h of M1 bars (US-holiday early closes, Christmas/New Year, data gaps) is a SHORT day.
  - Short days are excluded from all statistics, from ADR computation, and from trading.
- **Secondary (note only):** a fixed 21:00 UTC boundary (= the user's 04:00 ICT; equals server midnight in summer). Range and ADR-fit stats are reported for comparison.
- **ADR_n:** the mean daily range (high − low, $/oz) of the PREVIOUS n non-short days (n = 14 and 20). Days with fewer than n prior days are dropped.

## Part 1 (descriptive, in-sample 2019-01..2025-10-09; no trials)
- **Statistics:**
  - daily range: median, IQR, by year;
  - range/ADR14 and range/ADR20: quantiles;
  - share of days within ±20% of ADR14 / ADR20.
- **First move:** with T = 0.15 × ADR14, the side (above/below the open) whose excursion from the open FIRST reaches T, on M1 bars.
  - If both are reached in the same M1 bar, the day is "ambiguous" and excluded (count reported).
  - If neither side reaches T, the day is "no first move" (count reported).
  - X = the day's maximum excursion on the first-move side (whole day). E = the maximum excursion on the opposite side (the "extension").
- **Hypothesis test:** E ≈ ADR14 − X.
  - Reported: Pearson and Spearman correlation of E vs (ADR14 − X); median absolute error ($ and % of ADR); share within ±20% of the prediction.
  - **Baselines:** (a) E ≈ c × ADR14, where c = the median E/ADR14 over 2019–2020, with errors evaluated on 2021–2025-10-09; the hypothesis is also evaluated on 2021–25. (b) E ≈ 0 ("no extension").
  - Identity note: X + E = the day range whenever the open lies inside the range. So the hypothesis equals "range ≈ ADR", and its errors are the same as the range-vs-ADR errors.
- **Failure days:** X < 0.5 × ADR14, i.e. the first move stalled before half an ADR. Same stats conditioned on these days.

## Part 2: tradable test (walk-forward; trials logged)
- **Signals on M15 bars** (server day, mid prices); execution simulated on M5 bars.
- **Trigger:** the first M15 bar of the day whose high ≥ O + k×ADR14 (up excursion) or low ≤ O − k×ADR14 (down excursion), k ∈ {0.15, 0.25, 0.35}.
  - If one bar hits both levels, the day is skipped. Only the first triggered side is used.
- **Excursion extreme:** EXT = the running maximum high (up case) from the open through the current M15 bar.
- **Failure confirmation (dimension C), evaluated on M15 closes after the trigger bar (including the trigger bar's close):**
  - `rt50`: the first M15 close ≤ O + 0.5 × (EXT − O), i.e. back toward the open by half the excursion so far.
  - `sw`: an M15 fractal 2-2 swing high is confirmed (at bar j+2) whose high equals EXT (the day's extreme so far), AND the confirming bar's close < that swing bar's low.
  - Mirror for down excursions.
- **Entry:** at the close of the confirming M15 bar, AGAINST the excursion (short after an up excursion). One trade per day; no re-entry.
- **Take-profit (dimension P):** TP = O − p × (ADR14 − X_e) for the short (mirror for long), p ∈ {0.50, 0.75, 1.00}, where X_e = EXT − O at entry. Skip if TP is not beyond the entry.
- **Stop:** SL = EXT + $0.10, floor $3.00/oz (widen if closer). No maximum.
- **Time exit:** at the close of the last M5 bar of the server day (before the daily break). Weekend/holiday covered.
- **Blocks:** entries blocked 20:30–24:00 UTC (rollover block ON) and on weekends; short days are not traded.
  - The first 1–3 hours of the server day (22:00/23:00–24:00 UTC) are therefore not tradable.
- **Grid:** k (3) × C (2) × P (3) = 18 variants, all logged.
- **Costs:** Kai's IC file via the engine (session p90 12/11/10 points; NY-late ×1.5; 20:30–24:00 UTC 40 points; $3.50/lot/side; $0.05/oz/side slippage; swap with Wednesday ×3). Sensitivity gross/1x/1.5x/2x. Flat 1% risk.
- **Walk-forward:** engine.wf_windows (IS 24 months / OOS 6 months, 10 stitched non-overlapping OOS windows 2021-01..2025-10-09). Per window, the best IS t-stat (≥ 30 trades).
- **Finalist:** the last window's choice.
- **Pass bar on the stitched OOS:**
  - every OOS year positive;
  - PF ≥ 1.2 at 1x and > 1.0 at 1.5x;
  - ≥ 300 trades;
  - max DD ≤ 20%;
  - worst streak ≤ 12.
  - t vs Bonferroni and the DSR are reported.
- **Verdict:** "edge" only if it passes and the holdout is consistent; "needs more data" if it passes with t < Bonferroni; otherwise "no edge".
- **Holdout:** 2025-10-10..2026-10-09, once, finalist only, only if it passes; write results/HOLDOUT_USED_XAU_ADR.
