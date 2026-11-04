---
name: siw-star-in-wick
description: Use when detecting, backtesting, or alerting the SIW (Star-in-Wick / engulf) XAUUSD M5 entry technique, tuning its exits (fixed TP/SL or v3 SL5/TP20 + trailing after 15 min), or porting it to Pine/MQL5. Research only, never live orders.
---
# SIW v2 — Star-in-Wick XAUUSD M5

Code: GitHub SomNoi/trading-research `fx-research/siw/` (siw.py, exit_v3.py, SIW.pine, SIW.mq5, SPEC.md). Research only: no live trading and no order sending. The MQL5 file only raises alerts.

## Entry rules (sell; buy is the mirror image)
Decide on CLOSED bars only. L = confirm bar (the trader's listed time). Entry = OPEN of L+1.
1. Direction filter: if EMA21 < EMA55 at L, take sells only. If EMA21 > EMA55, take buys only.
2. Pattern at L, any one of these (modes `abc`):
   - A: L is a pin bar (upper wick ≥50% of range, body ≤35%), or L has a small body (≤40%) inside L-1's upper wick (±$0.30).
   - B: engulf. L is red and L-1 is green, open(L) ≥ close(L-1)−0.10, and close(L) ≤ open(L-1)+0.10.
   - C: L-1 is a pin or a star-in-wick, and L closes red.
3. Leg filter: ext = highest high of the last 12 bars − close(L). If ext > $10, skip the trade. Optional zone filter: ext ≤ $3 (off by default).
4. Dedupe is 1 (off). Clustered signals are possible.

## Exits
- fixed: TP $10 / SL $5, timeout 48 bars.
- v3 (default recommendation, in-sample): SL $5 / TP $20. After 3 bars (15 min), switch to a trailing stop at best price since entry ∓ trail. The trail never loosens past the SL. Optional breakeven. Bar by bar; if SL and TP both fall in the same bar, count the SL. Best: trail $3 + BE.
- Cost: $0.28 per 0.01 lot. $ moves are per 0.01 lot (1 oz).

## Results (Oct 29 – Nov 3 2026, in-sample, small n, sells much stronger than buys)
| set | exit | n | win | net $ |
|---|---|---|---|---|
| all v2 sells | 15-min time exit | 148 | 59% | +137.84 |
| all v2 sells | v3 T3+BE | 148 | 49% | +145.80 |
| all v2 buys | v3 T3+BE | 81 | 35% | −15.07 |
| his 20 picks | v3 T5+BE | 20 | 80% | +90.95 |
See exit_v3.md for the full table. Consider running sells only.

## Run
```
python3 siw.py duka_xau_m5_bid.csv [--from 2026-10-29] [--to 2026-11-04] [--modes abc] [--zone 3] [--touch] [--exit v3 --trail 3 --be]
python3 exit_v3.py   # regenerates exit_v3.md/csv
```
CSV columns: t (ms UTC), o, h, l, c. Server time = UTC+3 before Nov 1 2026 and UTC+2 after. ICT = UTC+7.
Pine: SIW.pine is a strategy() with Exit input fixed/v3. TradingView may fill TP before SL within a bar, so its results can be more optimistic than Python's.

## Data caveat
Dukascopy BID M5 runs about +$1.5 above the IC Markets feed, so absolute levels differ while shapes mostly match. Some bars differ, and the pattern can flip on a broker's own feed. Revalidate on the broker's data before trusting any signal. One week of data is not an edge: report results as in-sample and overfit-prone.
