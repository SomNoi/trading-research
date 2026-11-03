# R248 Step 1 — Dissection of 2026-11-03 09:55 ICT bar (SUBSTITUTE data)
Source: Yahoo chart API GC=F 5m (COMEX gold futures, **not IC BID spot**; futures carry a basis/offset vs spot, so absolute levels are not comparable to IC). Pulled 2026-11-03 ~11:10 ICT; data to 03:59:45 UTC, so the 03:55 bar may be partial. Raw: gc_m5_raw.csv, gc_m5_window_with_emas.csv, dissect_raw.txt.
Time: 02:55 UTC = 09:55 ICT = 04:55 IC server (winter UTC+2) = IC CSV label 01:55.

## Target bar: matches the brief
02:55 UTC: O 3957.4, H 3961.0, L 3955.3, C 3955.7. Body 1.70, range 5.70 (1.25×ATR14, ATR14 = 4.56). Body/range 0.30. Upper wick 3.60 (2.1× body). Lower wick 0.40. Close position 0.07 of range.
**Bearish engulfing: yes.** O 3957.4 ≥ prior C 3957.0, and C 3955.7 ≤ prior O 3956.4. Body is 2.83× the prior body.

## Prior 5 bars (UTC / ICT)
| UTC | ICT | O | H | L | C | note |
|---|---|---|---|---|---|---|
|02:30|09:30|3956.9|3957.5|3952.8|3953.1|big bear, body/rng 0.81|
|02:35|09:35|3953.0|3954.6|3951.2|3952.9|doji 0.03|
|02:40|09:40|3952.7|3956.5|3952.0|3954.5|bull, higher high|
|02:45|09:45|3954.6|3958.1|3954.2|3955.8|bull, higher high, uw 1.9×body|
|02:50|09:50|3956.4|3960.3|3956.4|3957.0|**shooting star: yes** (uw 3.3 = 5.5× body, close pos 0.15), higher high|
So there were 3 consecutive higher highs (pullback up), then a star, then the engulfing bar.

## EMAs at signal bar (close-based EMA, GC 5m)
| pair | fast | slow | fast<slow | bars since cross | slope3 fast / slow | H−fast | H−slow | C−fast | C−slow |
|---|---|---|---|---|---|---|---|---|---|
|9/21|3955.67|3957.11|yes|16|+0.46 / −0.31|+5.33 (1.17A)|+3.89 (0.85A)|**+0.03**|−1.41 (−0.31A)|
|10/20|3955.77|3957.01|yes|15|+0.32 / −0.30|+5.23 (1.15A)|+3.99 (0.88A)|−0.07|−1.31 (−0.29A)|
|20/50|3957.01|3958.41|yes|10|−0.30 / −0.29|+3.99 (0.88A)|+2.59 (0.57A)|−1.31 (−0.29A)|−2.71 (−0.59A)|
|5/20|3955.60|3957.01|yes|17|+1.26 / −0.30|+5.40 (1.18A)|+3.99 (0.88A)|**+0.10**|−1.31 (−0.29A)|
- The high pierced **above** both EMAs in every pair. It did not just come within $1; it went 2.6–5.4 $ above.
- The close is below both EMAs only for 20/50, and barely for 10/20. For 9/21 and 5/20 the close sits on or just above the fast EMA, so the R247 "close below both" rule would reject those pairs.
- 20/50 is the cleanest: both EMAs slope down, and the cross was 10 bars earlier.

## Swing / session context
- Asia session, 2h55m after the 22:00 UTC daily open (3960.5). Session high 3974.5 at 00:35, low 3950.9 at 02:10.
- Swing highs (fractal) step lower: 3974.5 → 3972.6 → 3969.5 → 3963.1 → 3958.4 (02:25). The signal high of 3961.0 is above the last minor swing high (3958.4) but below the prior one (3963.1). It is a lower high vs the 01:50 swing and 13.5 below the session high.
- Prior swing low: 3950.9 (02:10). Signal close is 4.8 above it.
- Previous day (11-02) range: 3900.0–3980.8.

## Next 12 bars (entry = 03:00 open 3955.5)
- Max high 3956.0, so adverse excursion was only $0.5. Min low 3933.7, so favorable excursion was $21.8.
- Drop at 30m (close 03:25): $8.4. Drop at 60m (close 03:55, possibly partial): $19.7.
- SL 3961.3 → R = 5.8. TP1.5R 3946.8 was hit by 03:20–03:25; TP2R 3943.9 was hit at 03:30. **Winner under every exit.**
