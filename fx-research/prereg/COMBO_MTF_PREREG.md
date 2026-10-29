# COMBO_MTF_PREREG — task combo-mtf-20261029
Locked BEFORE any signal counting / stats. Source: Dukascopy free feed (mid), not IC MT5.

**Question:** Alone, pin/doji/inside/engulf/morning-evening have no edge. Does stacking HTF bias + LTF classic candle ± RSI help?

- Symbol: XAUUSD. Source: Dukascopy free feed (mid), not IC MT5.
- **Entry TF:** M5 = resample 5min left/left of M1 with index < HOLDOUT_START.
- **Bias TF:** **H1** (completed bars only). Bias indicator: EMA55 on H1 close (engine.ema span=55). At M5 bar i, use the last H1 bar whose open time ≤ M5 open and which is **fully closed** before the M5 bar's close (no lookahead: H1 bar ending at/before t5[i]).
  - Bull bias: H1 close > EMA55(H1)
  - Bear bias: H1 close < EMA55(H1)
  - Equal → no trade.
  - Implementation: H1 = resample('1h', left/left) of the same M1 (dropna); H1 bar with open T ends T+60min; for M5 bar i (open t5[i], close t5[i]+5min) take the last H1 bar with T+60min ≤ t5[i]+5min (merge_asof backward). No H1 bar available / EMA NaN → no trade.
- **LTF candles (exactly 2 types):**
  1) **PIN** = classic_candles PIN_V0 rules (bull pin +1 / bear pin -1).
  2) **ENGULF** = maemfe T1|T2 (T2 precedence): bull engulf +1, bear -1.
- **Signal:** candle direction must **agree** with H1 bias. Else skip.
- **Optional filter (exactly 2 levels):**
  - F0: no RSI filter
  - F1: RSI(14) on M5 (Wilder; use standard: avg gain/loss ewm alpha=1/14). Bull signal only if RSI[i] ≤ 40; bear only if RSI[i] ≥ 60.
- **Sets (4):** PIN_F0, PIN_F1, ENGULF_F0, ENGULF_F1. (Each already requires HTF agreement.)
- **Exits (3, same as classic candles):** E1 1R:1R from disc winners' mae_before_peak p80 + $0.30; E2 k∈{1.0,1.5}×ATR14(M5), TP=1.5×SL, freeze best disc PF.
- **Trials = 4×3 = 12** (≤24). No other variants. No martingale.

Eligibility / split / costs / pass bar: identical to CLASSIC_CANDLES_PREREG (entry next open, entry_blocked, contiguous 5min + 24-bar window, COST=$0.28/oz RT, 1x/1.5x/2x, chron 70/30, hit +1/+3/+6/+12/+24, MFE/MAE on M1, one pos at a time, SL before TP).

## Pass bar (copied from CLASSIC_CANDLES_PREREG; all required, internal holdout = OOS)
Net expectancy >0 in every OOS calendar year (or 4/5), PF>=1.2 OOS and >1.0 at 1.5x cost, >=300 OOS trades, max DD<=20% at 1% risk, worst losing streak<=12.
Otherwise verdict = NO EDGE. Not a live signal.
