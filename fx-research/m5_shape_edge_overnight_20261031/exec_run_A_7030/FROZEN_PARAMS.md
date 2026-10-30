# FROZEN_PARAMS
- Clustering: 12-d vector (O,H,L,C minus first open, divided by window H−L; for w=4/5 the vector is 16/20-d), L2-normalised, greedy leader cosine clustering. Configs: w3@0.85, w3@0.90, w4@0.85, w5@0.85. Clusters kept if ≥20 members.
- Bar features: body/range bins [<.33, <.66, ≥.66]; wick dominance (upper−lower > .2 → up-wick, < −.2 → low-wick, else balanced); direction C≥O.
- Code schemes: bodyXdir = body3*2+dir (0–5); wickXdir = wick3*2+dir (wick 0 = lower-dominant, 1 = balanced, 2 = upper-dominant). Sequence lengths 3, 4, 5. Patterns need ≥200 IS events.
- Forward returns: close-to-close at h = 1, 3, 5, 10 bars. Lift = IS P(up) / IS baseline P(up).
- Backtest candidates: top 40 by max |t| of IS mean return across h. Entry at the next bar's open after the pattern completes. SL ∈ {2, 3, 5} $, TP = SL × {1.3, 1.5, 2.0}. Time exit after 24 bars. If SL and TP hit in the same bar, SL counts. No overlapping trades. Cost $0.28 per trade per 1 oz (0.01 lot) round trip.
