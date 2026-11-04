---
name: siw-star-in-wick
description: Use when detecting, backtesting, or alerting the SIW (Star-in-Wick / engulf) XAUUSD M5 entry technique, applying or tuning its exits (current v4 = SL $10 / TP $20 cap / close after 10 min; older fixed and v3), the SIW Alert app (SomNoi/siw-alert), or porting it to Pine/MQL5. Research and alerts only, never live orders.
---
# SIW v2 — Star-in-Wick XAUUSD M5

Code: GitHub SomNoi/trading-research `fx-research/siw/` (siw.py, exit_v4.py, exit_v3.py, SIW.pine, SIW.mq5, SPEC.md). App: SomNoi/siw-alert (engine/, Pages https://somnoi.github.io/siw-alert/, ntfy push, mt5/ EA webhook sketch). Research only: no live trading and no order sending. MQL5 files only raise alerts / POST JSON.

## Entry rules (sell; buy is the mirror image)
Decide on CLOSED bars only. L = confirm bar (the trader's listed time). Entry = OPEN of L+1.
1. Direction filter: if EMA21 < EMA55 at L, take sells only. If EMA21 > EMA55, take buys only.
2. Pattern at L, any one of these (modes `abc`):
   - A: L is a pin bar (upper wick ≥50% of range, body ≤35%), or L has a small body (≤40%) inside L-1's upper wick (±$0.30).
   - B: engulf. L is red and L-1 is green, open(L) ≥ close(L-1)−0.10, and close(L) ≤ open(L-1)+0.10.
   - C: L-1 is a pin or a star-in-wick, and L closes red.
3. Leg filter: ext = highest high of the last 12 bars − close(L). If ext > $10, skip. Optional zone filter ext ≤ $3 (off).
4. Dedupe: research = 1 (off); the app uses 3 bars (same direction) to avoid repeated pushes.

## Exit v4 (CURRENT, user decision 2026-11-04)
- SL $10, TP $20 (safety cap) from entry; close by time at the CLOSE of bar L+2 (10 min after entry at open of L+1), whichever comes first.
- Bar by bar over L+1 and L+2: SL checked before TP (worst case); a gap through a level fills at that bar's open.
- Clock: confirm bar L opens at T → entry T+5m → time exit T+15m (ICT; MT5 server = ICT−4h during US DST, ICT−5h otherwise).
- Cost $0.28 per 0.01 lot; $ moves are per 0.01 lot (1 oz).
- Older exits kept for comparison: fixed TP $10/SL $5 (timeout 48); v3 SL $5/TP $20 + trail after 15 min.

## Results v4 (Dukascopy BID, 2026-10-23 → 2026-11-04 11:00 ICT, IN-SAMPLE, small n)
| set | n | win | total $ | avg | worst |
|---|---|---|---|---|---|
| all SIW v2 sells | 253 | 55% | +103.30 | +0.41 | −10.28 |
| all SIW v2 buys | 211 | 49% | −6.51 | −0.03 | −10.28 |
| all SIW v2 | 464 | 52% | +96.79 | +0.21 | −10.28 |
| his 20 picks | 20 | 90% | +65.07 | +3.25 | −1.63 |
| his 2 buys Nov 4 (06:45, 09:30 ICT) | 2 | 50% | +3.90 | +1.95 | −3.41 |
459/464 trades exit on time; SL/TP rarely hit within 10 min. Buys are flat/negative across all signals; sells carry the edge. His hand picks beat the mechanical set: discretion is doing work the rules don't capture. See exit_v4.md.

## Run
```
python3 siw.py duka_xau_m5_bid_refreshed.csv [--from 2026-10-29] [--to 2026-11-05] [--modes abc] [--zone 3] [--touch] [--exit v4|v3|fixed]
python3 exit_v4.py   # regenerates exit_v4.md/csv
```
CSV columns: t (ms UTC), o, h, l, c. Server time = UTC+3 before Nov 1 2026 and UTC+2 after. ICT = UTC+7.
Pine: SIW.pine strategy() Exit input fixed/v3/v4 (default v4; use process_orders_on_close=true for the time exit). TradingView may fill TP before SL within a bar, so results can be more optimistic than Python's.

## Data caveat
Dukascopy BID M5 runs about +$1.5 above the IC Markets feed, so absolute levels differ while shapes mostly match. Some bars differ, and the pattern can flip on a broker's own feed. Revalidate on the broker's data before trusting any signal. ~1.5 weeks of data is not an edge: report results as in-sample and overfit-prone.
