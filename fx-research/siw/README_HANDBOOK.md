# SIW XAUUSD M5 Alert System: Handbook (v5, 2026-11-04)

Read this first if you are taking over the SIW alert job. It explains what we run, how, and why, so you can run it the same way.

## 1. The user
- Preda (nickname ส้มน้อย). Trades XAUUSD by hand on MT5 (IC Markets). Writes in Thai; **every alert goes out in Thai**.
- **Watch-only.** We never place, modify, or suggest-and-execute orders. We detect, alert, and research. Nothing else.
- He judges setups by eye. His hand picks beat the mechanical rules, so present alerts as information and don't oversell them.

## 2. Rule spec (live, as of 2026-11-04 19:07 ICT)
Use closed M5 bars only. **L = confirm bar.** Entry = OPEN of L+1. Rules are written for a sell; a buy is the mirror image.

| # | Rule | Detail |
|---|---|---|
| 1 | Direction | EMA21 vs EMA55 of M5 closes (warm-up 500 bars). EMA21 < EMA55 means sells only; EMA21 > EMA55 means buys only. |
| 2 | Pattern at L (any one) | **A**: pin (wick on the trend-opposite side ≥50% of range, body ≤35%), or small body ≤40% sitting inside L-1's wick (±$0.30). **B**: engulfing in the trend direction (tol $0.10). **C**: L-1 is a pin or star-in-wick and L closes in the trend colour. |
| 3 | Leg filter | \|close(L) − 12-bar extreme\| ≤ $10 (12-bar high for a sell, 12-bar low for a buy). |
| 4 | Fresh-extreme (R251, K=5) | Set = bars L-2..L, reference = L-7..L-3. SELL: max high of the set ≥ every high in the reference. BUY: min low of the set ≤ every low in the reference. Order inside the set does not matter. This is the user's eye rule ("the wick made a new extreme"). |
| 5 | Dedupe | Skip a same-direction SIW within 3 bars of the last one alerted. |
| 6 | Exit v4 | SL $10, TP $20, time exit at the CLOSE of L+2 (10 min after entry). First hit wins. Check bar by bar with SL before TP (worst case). A gap through a level fills at that bar's open. |
| 7 | MA-pullback ✅ tag | A 1–4 bar pullback that touches EMA21/55, then a shooting star, engulfing, or MA-rejection in the trend direction. Tagged ✅ in the alert. |
| 8 | Plan levels | Alert when price crosses 3950 / 4000 / 4050 / 3860 / 4100 (the `levels` field in the state file). |

Clock: if confirm bar L opens at T, entry is at T+5m and the time exit is at T+15m.

## 3. Data sources and offsets
| Source | Use | Offset |
|---|---|---|
| Dukascopy XAU/USD BID M5 (free, no key) | live, primary | ≈ IC BID **+$1.5** |
| Yahoo `GC=F` 5m (futures) | fallback only, levels only | ≈ IC **+$12**; don't run pattern rules on it |
| IC Markets BID M5 history (CSV on box) | backtests | reference feed (user's broker) |

Dukascopy call:
```
curl -s -H "Referer: https://freeserv.dukascopy.com/" -A "Mozilla/5.0" \
 "https://freeserv.dukascopy.com/2.0/?path=chart/json3&instrument=XAU/USD&offer_side=B&interval=5MIN&splits=true&stocks=true&limit=500&time_direction=P&timestamp=<now_ms>&jsonp=_cb"
```
Strip `_cb(` … `)`. Rows are `[t_ms_UTC, o, h, l, c, vol]`, **newest first**. The newest row may still be forming, so drop it unless t+5min ≤ now. If the newest closed bar is more than 15 min old, retry once, then fall back to Yahoo.

Times: always report **ICT (Asia/Bangkok, UTC+7)** and **MT5 server time**. Server = ICT−5h in winter (UTC+2, since 2026-11-01) and ICT−4h in summer (UTC+3).

## 4. One cycle, step by step (what the routine does every 15 min)
1. Read the state file `/workspace/fx-research/plan_watch_state.json`.
2. Fetch Dukascopy (section 3). Check staleness and keep closed bars only.
3. Run `python3 /workspace/fx-research/siw_v2_20261104/siw.py --live --since-min 30`. Line 1 of the JSON output is the summary (source, last closed bar, trend). Each line after that is one signal.
4. Drop any signal whose `confirm_ict` is ≤ `last_siw.confirm_ict` (already alerted). Apply the 3-bar dedupe against it too.
5. Check the MA-pullback ✅ tag and the plan-level crosses against `levels` and `fired`.
6. If something is new, write the Thai message (section 6) and hand it to dr eggbot. If nothing is new, **stay silent** (no message).
7. Update the state file: `last_check`, `source`, `last_checked_candle`, `last_siw`, `tagged`, `siw_skipped` (reason for each rejected candidate), `fired`, `asof_price`, `notes`.

Expected latency: alerts can lag 15–20 min behind the bar (15-min schedule plus the bar close). Say so if the user asks.

### State file schema (`plan_watch_state.json`)
```
plan            str   current plan name
asof_price      float last price seen
market          "open"|"closed"
levels          {name: price}            plan levels to watch
fired           {name: "time ICT price"} levels already alerted
last_check      "YYYY-MM-DD HH:MM ICT"
source          str   feed + bar used
last_checked_candle str
last_siw        {dir, confirm_ict, kind, entry, sl, tp, time_exit_ict, leg_dist, fresh_extreme, result}
tagged          [str] MA-pullback ✅ tags already sent
siw_skipped     [str] rejected candidates + reason (audit trail)
notes           str   running log
```

## 5. Tools used
- **Shell** on the box, with `curl`, `python3`, `pandas`, and `numpy`.
- **Code**: `siw.py` (this folder). Also `exit_v4.py`, `exit_v3.py`, `SIW.pine`, `SIW.mq5` (alert only), and `SPEC.md`.
- **Skill**: `siw-star-in-wick` (SKILL.md points here).
- **Routine**: `xau-plan-watch`. Runs every 15 min on weekdays, 08:01–23:46 ICT, inside the **dr eggbot** bot. The run is isolated: it hands the Thai text to dr eggbot, and dr eggbot sends it to the user.
- **GitHub**: `SomNoi/trading-research`, folder `fx-research/siw/` (code and research). App: `SomNoi/siw-alert`.

## 6. Alert message template (Thai)
```
🔔 SIW {ขาย|ซื้อ} XAUUSD M5 ({kind})
แท่งยืนยัน {confirm_ict} ICT / {confirm_srv} เวลา MT5
เข้า: เปิดแท่งถัดไป {entry_ict} ICT (~{entry})
SL {sl} | TP {tp} | ออกตามเวลา {time_exit_ict} ICT (10 นาที)
เทรนด์ EMA21{<|>}EMA55 | ห่างจุดสุดขา ${leg_dist} | fresh-extreme ผ่าน (K=5)
{✅ MA-pullback ถ้ามี}
ราคา Dukascopy BID (≈ IC +$1.5) · แจ้งเตือนเท่านั้น ไม่ได้ส่งออเดอร์ · ยังไม่พิสูจน์ edge
```
Plan level: `📍 ราคาแตะ {level} ({name}) เวลา {ICT} ICT / {srv} MT5 · ราคา {price}`

## 7. Research history (all watch-only, none proved an edge)
| Round | What | Result | Link |
|---|---|---|---|
| R247–R248 | SIW v2 baseline and exit tuning on Dukascopy (v3, v4) | small-n, in-sample only | [exit_v4.md](exit_v4.md), [exit_tuning.md](exit_tuning.md) |
| R249 | SIW v2 + v4 on 17 months of IC history | no edge | [r249_ic](r249_ic/EXEC_SUMMARY.md) |
| R250 | template matching of his picks | no edge | [r250_template](r250_template/EXEC_SUMMARY.md) |
| R251 | fresh-extreme filter K=5/6 | 0/12 cells pass. SELL K=5 OOS E +$0.09/0.01 lot but IS −$0.32, so it is noise. BUY is worse. | [r251_fresh_extreme](r251_fresh_extreme/EXEC_SUMMARY.md) |

Cumulative N_TRIALS = 6670. Follow-through: about 50% of signals get 0 bars of continuation. The filter is live because the user asked for it (it is his eye rule), not because it proved an edge.

## 8. Open questions / next tests
1. **Exit "hold until first opposite-colour bar"**: the 10-min time exit cut a winning buy early on 2026-11-04 19:15 ICT. Pre-register and test it on IC history.
2. Signal timestamp labelling: the routine logged the 19:15 alert as confirm 19:15. `siw.py --live` labels the same trade as confirm 19:10 / entry 19:15. Agree on one convention (code: L = confirm bar's OPEN time).
3. BUY side is consistently weaker. Should buys be alerted at all?
4. The pattern can flip on IC's own feed versus Dukascopy. Do we need an IC live feed?
5. What do his discretionary picks capture that the rules don't (R250 found no template)?

## 9. Quick commands
```
python3 siw.py --live                         # new signals, JSON lines (last 30 min)
python3 siw.py --live --since-min 600         # look back further
python3 siw.py --backtest ic_or_duka.csv --exit v4 --dedupe 3   # fresh filter ON by default
python3 siw.py --backtest data.csv --no-fresh # pre-R251 baseline (Duka 10/23–11/04: n=464, +$96.79)
```
