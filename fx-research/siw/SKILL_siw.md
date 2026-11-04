---
name: siw-star-in-wick
description: Use when detecting, backtesting, or alerting the SIW (Star-in-Wick / engulf) XAUUSD M5 setup for Preda, running or handing over the xau-plan-watch routine, tuning its exits (v4 = SL $10 / TP $20 / time exit at close of L+2), or porting it to Pine/MQL5. Watch-only, never orders.
---
# SIW v5: Star-in-Wick XAUUSD M5 (watch-only)

**Read the full handbook first:** GitHub `SomNoi/trading-research/fx-research/siw/README_HANDBOOK.md`. Box copy: `/workspace/fx-research/siw_v2_20261104/README_HANDBOOK.md`.
Code: `siw.py` (same folders). Its header docstring repeats the rules, data URL, and timezones.

## Hard rules
- User: Preda (ส้มน้อย). Alerts are in **Thai**. **Never place or send orders.** Alerts are information, not advice. No proven edge (R247–R251, N_TRIALS 6670).
- Report every time in ICT and in MT5 server time (server = ICT−5h in winter / UTC+2, ICT−4h in summer).

## Rules (sell; buy is the mirror). Closed bars only. L = confirm bar, entry = open of L+1
1. EMA21 < EMA55 on M5 closes (500-bar warm-up) means sells only; EMA21 > EMA55 means buys only.
2. Pattern at L: A pin (opposite wick ≥50% of range, body ≤35%) or small body ≤40% inside L-1's wick; B engulfing in trend direction; C L-1 pin/star-in-wick and L closes in trend colour.
3. Leg: |close(L) − 12-bar extreme| ≤ $10.
4. Fresh-extreme K=5: set L-2..L must hold the extreme vs L-7..L-3 (SELL max high ≥ all ref highs; BUY min low ≤ all ref lows).
5. Dedupe: same direction within 3 bars is skipped.
6. Exit v4: SL $10, TP $20, time exit at close of L+2 (10 min). SL is checked before TP; a gap fills at the bar open.
Extras: MA-pullback ✅ tag (EMA21/55 touch + star/engulf/rejection, 1–4 bar pullback). Plan levels 3950/4000/4050/3860/4100.

## Data
Dukascopy XAU/USD BID M5 (≈ IC +$1.5), from `freeserv.dukascopy.com/2.0/?path=chart/json3...` with the Referer and User-Agent headers. Rows are newest first: `[t_ms_UTC,o,h,l,c,vol]`. Stale after 15 min: retry once, then fall back to Yahoo GC=F 5m (≈ +$12, levels only). Backtests use IC Markets BID CSVs.

## One cycle (routine xau-plan-watch, dr eggbot, every 15 min, weekdays 08:01–23:46 ICT)
1. Read `/workspace/fx-research/plan_watch_state.json`.
2. Run `python3 siw.py --live` (JSON lines).
3. Drop anything at or before `last_siw` and apply the dedupe. Check the ✅ tags and level crosses.
4. If something is new, send the Thai message (template in handbook §6) to dr eggbot, which delivers it. Otherwise stay silent.
5. Update the state file (schema in handbook §4).

## Backtest
`python3 siw.py --backtest data.csv [--from --to] [--exit v4|v3|fixed] [--no-fresh] [--k 5] [--dedupe 3]`. Report results as in-sample and overfit-prone. Pre-register new tests (follow the R249–R251 folder pattern).

## Open
Test an exit that holds until the first opposite-colour bar (the 10-min exit cut a winner on 2026-11-04 19:15 ICT). Agree on a confirm-time labelling convention. Decide whether to keep buys.
