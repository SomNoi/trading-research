# XAU SOX v2: amendment to prereg/XAU_SOX_PREREG.md (registered BEFORE any v2 run)

## Why there is an amendment
- The v1 quiet test compared the 6 pre-window bars' mean range with the continuous M5 ATR14 at the bar before the window.
- Those same 6 bars make up almost half of ATR14's effective window, so the ratio sits at about 1.0 (London median 1.07). Only 0.3% of windows passed.
- v1 produced 5 candidate windows in 2019–2025 (4 trades in the best case), so it fails the ≥ 300-trades bar outright. v1 is reported as run, and its 20 trials stay logged.
- The brief asked for the quiet test "measured with prior-day context". v1 did not capture that, which is a definition error on our side.
- Disclosure: v1's outcome on those 4–5 trades was seen, and is irrelevant to v2. No v2 statistic was looked at before this registration, including the pass rate of the new quiet test.

## v2 change (the only change)
- **Quiet pre-open:**
  - D_ATR = the mean M5 true range over ALL M5 bars of the most recent PREVIOUS UTC calendar day with ≥ 100 M5 bars (i.e. the prior trading day; weekends are skipped).
  - Condition: the mean (high − low) of the 6 bars immediately before the window < 0.7 × D_ATR.
  - The threshold 0.7 is unchanged and not tuned.
- **Everything else is identical to v1:**
  - windows (fixed UTC);
  - expansion bar > 1.5 × ATR14[i−1] (continuous ATR), with the close in the top/bottom 25%;
  - first qualifying bar per window only;
  - spread filter;
  - entry {close, stop} × trend {none, h1} × exit {A, B, C, D, E} = 20 variants;
  - SL = the bar's opposite end + $0.10, floor $3;
  - costs; walk-forward; finalist = the last window's choice;
  - pass bar, including net ≥ $0.30/oz per trade;
  - holdout gate.
- **Trials:** v2's 20 are logged in addition to v1's 20 (40 total for SOX).
