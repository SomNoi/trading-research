# PREREG — XAUUSD M5 bar-shape edge hunt (overnight 2026-10-31)
Task: m5-shape-edge-overnight-20261031. Research only; no live trading; no martingale/grid/hedge; every trade has SL.
Data: IC Markets MT5 BID export `/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv` (~99,964 bars, 2025-05-14→2026-10-09 UTC).
Split: bars sorted by time; IS = first 60% of bars (index < floor(0.6*N)); OOS = rest. A signal belongs to IS/OOS by its signal bar t (last bar of window); IS trades whose exit falls in OOS are kept in IS.
Note: `prior_partial_descriptive/` holds a pre-prereg, full-sample, no-trading clustering run (descriptive only, not used for selection).

## A) Shape clustering
- Windows of L∈{3,4,5} bars, sliding step 1. ref=open of bar1; rng=max(H)-min(L) over window; skip rng==0. Features per bar [(O-ref)/rng,(H-ref)/rng,(L-ref)/rng,(C-ref)/rng] → 4L vector.
- Cosine sim thresholds 0.85 and 0.90 (6 configs total).
- Greedy in time order on IS windows only: assign to FIRST (creation order) prototype with sim≥thr, else new prototype. Prototypes never update. Keep clusters with IS member_count ≥ 20.
- OOS windows: assign to FIRST kept IS prototype with sim≥thr (creation order); else unassigned. No new prototypes on OOS.
- Candidates: top 30 kept clusters by IS count per config (≤180). Implied direction = sign(prototype last-bar C feature) (net window move); if 0 → skip.
- Overlapping signals: one position at a time per candidate; signals during open trade skipped.

## B) Per-bar shape path
Bar class (r=H-L, body=|C-O|, uw=H-max(O,C), lw=min(O,C)-L, medr = median r of previous 20 bars, shifted, no lookahead):
1. r==0 or body/r<0.10 → doji
2. lw/r≥0.60 and body/r≤0.30 → pin_bull; uw/r≥0.60 and body/r≤0.30 → pin_bear
3. body/r≥0.60 and r≥medr → big_bull (C>O) / big_bear (C<O)
4. else weak_bull (C>O) / weak_bear (C<O)
- Sequences of length 3,4,5 ending at bar t. Forward dir = sign(close[t+N]-close[t]), N∈{1,3,5,10}; also mean return. Full contingency tables (IS and OOS separately) stored; lift = P(up|seq) - baseline P(up) (baseline on same split).
- Candidates: sequences with IS n≥100, ranked by |lift| at N=3 on IS; top 40 overall. Implied direction = sign(IS lift N=3).

## C) Backtest (all candidates, both modes predeclared)
- Modes: continuation (trade implied direction) and mean-reversion (opposite). Trials = candidates × 2.
- Entry at open of bar t+1. SL $3.5 price; TP 1.5R = $5.25; time stop: exit at close of 25th bar held. Same-bar SL & TP → SL first. Cost $0.28 per trade (0.01 lot RT) in $/oz.
- All-hours only (session gate skipped for cost/time; declared here).
- Metrics per IS and OOS: n, PF, WR, net, maxDD.
- PASS (OOS): PF>1.25 AND WR>48% (R:R 1.5≥1.3) AND maxDD<25% of OOS net AND n>150 AND sensitivity: entry delay +1,+2 bars and −1,−2 bars (signal bar shifted earlier = enter at open of t−1/t: −k interpreted as entry at open of bar t+1−k, i.e. inside the window; flagged as robustness probe only) and SL 3.0/4.0 (TP stays 1.5R) all OOS PF>1.15.
- Multiple testing: N_TRIALS += total trials; Z_BONF=norm.ppf(1-0.05/N). Report OOS t-stat of mean trade.
