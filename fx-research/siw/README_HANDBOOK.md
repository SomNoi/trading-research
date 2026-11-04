# SIW XAUUSD M5 alerts: handbook (rules v6 + exit v7, 2026-11-05)

Read this before you touch the SIW job. I'll explain the rule, why each piece is there, and walk you through today's chart so you can check the code yourself.

## 0. Ground rules
- The user is Preda (ส้มน้อย). He trades XAUUSD by hand on MT5 (IC Markets) and writes in Thai. **All alerts go out in Thai.**
- **Watch-only.** We never place or change orders. We detect, alert, and research.
- He reads charts well by eye. The code is our best copy of what he sees, not something to sell him. Never claim an edge (see §6).

## 1. The v6 rule in one breath
"In an uptrend, after a red pullback bar, a pin or a green engulfing bar that makes a fresh low = buy signal." Sells are the mirror.

## 2. Each piece and why it's there
| # | Piece | Exact rule (buy; sell mirrors) | Why |
|---|---|---|---|
| 1 | Trend | EMA21 > EMA55 on M5 closes means buys only | We only trade pullbacks with the trend. Same as v5. |
| 2 | Pullback | Bar **L-1** is red, any size | Something has to pull back before we can buy the dip. Preda accepts strong and weak pullbacks, so v6 dropped the old "bodies must shrink" idea. |
| 3 | Signal bar L | **PIN**: lower wick ≥ 50% of range, body ≤ 40%, any colour. **ENG**: green L whose body engulfs red L-1's body exactly (open(L) ≤ close(L-1), close(L) ≥ open(L-1), no tolerance) | A pin means sellers pushed price down and got rejected. An engulfing bar means buyers erased the whole pullback bar. |
| 4 | Fresh extreme | Set = L-1..L. The set's lowest low must be ≤ every low of the **K bars before the set** | The wick has to make a new local low. Without that it's just noise in the middle of a range. |
| 5 | K tag | Test K=10 and K=5. **K10** = fresh against the previous 10 bars (stronger, and implies K5). **K5** = fresh against 5 only. Fails 5 = no signal | Preda wants to see both. K10 shows fewer, cleaner extremes. K5 adds more marginal ones. |
| 6 | Dedupe | Same side on two bars in a row: keep the **later** one | The second bar is the better-confirmed version of the same idea. Live, the first one may already have been alerted. The later one then counts as an update. |
| 7 | **Exit v7 (default since 2026-11-05)** | Entry = open of L+1. **SL = structure**: BUY = lowest low of L-1..L, SELL = highest high of L-1..L. **If the SL is more than $8 from entry, skip the signal** (also skip if entry already gapped past it). TP $20, otherwise close at the **CLOSE of L+2** | Preda approved this. The stop sits where the idea is wrong (below the wick), not at an arbitrary $10. A wide wick means a stop too big for the setup, so we don't take it. Don't change it without the user. |
| 7b | Exit v4 (old, `--exit v4`) | SL $10 fixed, TP $20, close of L+2 | Kept for comparison only. |

v6 removed some v5 pieces: the leg filter (≤ $10 from the 12-bar extreme), the star-in-wick variant, mode C, and the 3-bar fresh set. `leg_dist` is still printed for information.

## 3. Time convention (people get this wrong)
- **Bars are named by their OPEN time.** "19:00 BUY PIN" means the bar that opened at 19:00 MT5 and closed at 19:05.
- Entry is at the open of L+1 (L+5 min). The time exit is at the close of L+2 (L+15 min).
- Always report **ICT (UTC+7)** and **MT5 server** time. Server time is UTC+2 when the US is on standard time (now, since 2026-11-01, so ICT−5h) and UTC+3 during US DST (ICT−4h). The code works this out from the US DST calendar.

## 4. Worked examples from 3–4 Nov 2026 (Dukascopy BID, MT5 times)
`python3 siw.py --backtest duka_v6_verify.csv --from "2026-11-03 18:00"` reproduces Preda's reviewed list exactly:

| MT5 (bar open) | Side | Kind | Tag | Why it fires |
|---|---|---|---|---|
| 11-03 19:00 | BUY | PIN | K10 | 18:55 was red. 19:00 is a green pin. The 18:55–19:00 low 3925.92 is the lowest in 10 bars. 18:55 also qualified (red pin), but the 19:00 bar replaced it (dedupe) |
| 22:30 | SELL | ENG | K5 | fresh against 5 bars, not 10 |
| 23:45 | SELL | ENG | K10 | |
| 23:55 | SELL | PIN | K10 | upper wick 50%, body 38%. Under v5's 35% body cap this was not a pin, which is why v6 uses 40% |
| 11-04 01:05 | SELL | ENG | K10 | |
| 01:30 | BUY | PIN | K5 | |
| 01:45 | BUY | ENG | K10 | |
| 02:25 | BUY | PIN | K5 | a red pin is fine |
| 04:30 | BUY | ENG | K10 | |
| 06:00, 06:35 | BUY | ENG | K5 | |
| 11:40 | BUY | PIN | K5 | |
| 14:10 | BUY | PIN | K10 | |

Two checks a junior should run:
- **02:40 BUY is not a signal.** It looks like an engulfing bar, but it opened at 3921.01, $0.04 above the 3920.97 close of red 02:35. v6 engulfing has zero tolerance.
- **15:15 BUY (rejected by Preda) must not appear.** It doesn't.

Exit v7 on the extended file (`python3 siw.py --backtest r253_chase/duka_v6_verify_ext.csv`, 11-03 → 11-04): 23 signals, **2 skipped** (11-03 23:55 SELL: weekend-style gap made SL $8+ away; 11-04 16:30 BUY: wick too long), 21 trades, 52% win, **+$24.00 net** (v4 on the same file: 23 trades, +$23.78). `--exit v4` output is byte-identical to the v6 script. Two days, in-sample, proves nothing.

Totals for the day (exit v4, original list): K5+K10 = 13 signals, +$26.82 gross (+$23.18 net of $0.28 each). K10 only = 7 signals, +$13.64 gross (+$11.68 net). That is one day, in-sample, and proves nothing.

## 5. Running it
```
python3 siw.py --live --since-min 30          # JSON: header, then one line per signal: dir, kind, k_tag, ICT/MT5 times, entry, sl, sl_dist, tp, skip, skip_reason
python3 siw.py --live --exit v4               # old $10 SL numbers
python3 siw.py --live --since-min 30 --k 10   # K10 only
python3 siw.py --backtest data.csv [--from ..] [--to ..] [--k 10] [--no-fresh] [--dedupe 0]
```
Live data comes from Dukascopy BID (≈ IC BID + $1.5). If it goes stale, retry once and then fall back to Yahoo GC=F, which is good for levels only. CSV columns are t,o,h,l,c with t in ms UTC. The previous code is in `siw_pre_v7.py.bak` (v6, exit v4) and `siw_pre_v6.py.bak`. In live JSON, `sl_dist`/`tp` are measured from the L+1 open when known, otherwise from L's close, so recheck against the real fill. **If `skip` is true, the alert should say "skipped: SL > $8", not give a trade.**

## 6. Long-sample backtest (R252, IC Markets MT5 BID M5, 2025-05-14 → 2026-10-09, ~17 months, 365 trading days)
Exit v4, $0.28 cost, 0.01 lot ($1 per $1 move). IS = first 70% of the time span, OOS = last 30%. Every K tag and side is negative in both IS and OOS. Full table: `r252_v6_backtest/results.csv`, trades: `trades.csv`.

| Tag | Side | n | /day | win | E$/trade | PF | IS E / OOS E | maxDD $ |
|---|---|---|---|---|---|---|---|---|
| K10 | BUY | 1832 | 5.02 | 41.4% | −0.68 | 0.64 | −0.55 / −0.99 | 1256 |
| K10 | SELL | 1634 | 4.48 | 44.4% | −0.57 | 0.71 | −0.66 / −0.39 | 976 |
| K5 | BUY | 1003 | 2.75 | 47.4% | −0.26 | 0.86 | −0.19 / −0.45 | 327 |
| K5 | SELL | 906 | 2.48 | 41.1% | −0.63 | 0.70 | −0.54 / −0.78 | 578 |

Tell the user what the numbers say and nothing more. This is an alert system for his eye, not a strategy.

### 6b. Exit v7 on the same IC data, and martingale (R255, `r255_martingale/`)
v7, trades one at a time (signals skipped while a trade is open), $0.28/0.01: n = 4743, 631 skipped for SL > $8, win 39.4%, **−$0.42/trade** (IS −0.33, OOS −0.61). Fixed 0.01 lot loses about $1,990 over 17 months. Longest losing run = 20 trades.

Martingale does not fix a negative expectancy. It only changes how you lose. Classic x2 (base 0.01, caps 5/7/10/unlimited) ruined **every** account ($500/$1000/$5000) inside the IS window, mostly in the first weeks. Anti-martingale (cap 3) just loses faster than fixed. See `r255_martingale/README.md`. If Preda asks about martingale, show him that table.
