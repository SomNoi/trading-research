# CLASSIC_CANDLES_PREREG — Track B (task classic-candles-20261029-B)
Locked BEFORE any signal counting / stats. Source: Dukascopy free feed (mid), not IC MT5.
Symbol XAUUSD, M5 = resample('5min', left/left) of engine.load_m1 M1, filtered m1.index < 2025-10-10 UTC (engine.HOLDOUT_START; never loaded beyond).

## Patterns (signal on bar i, M5 OHLC)
range=h-l>0; body=|c-o|; uw=h-max(o,c); lw=min(o,c)-l
- PIN bull (+1): lw>=2*body AND uw<=0.5*body AND body/range<=1/3 AND c>=l+0.66*range
- PIN bear (-1): uw>=2*body AND lw<=0.5*body AND body/range<=1/3 AND c<=h-0.66*range
  (note: body=0 bars require uw<=0 resp. lw<=0 — rule applied literally)
  - PIN_V0: no trend filter
  - PIN_V1: ema5=EMA(close,5) (span, adjust=False); bull needs ema5[i]-ema5[i-5]>0, bear needs <0
- INSIDE: h[i]<h[i-1] AND l[i]>l[i-1]; dir=+1 if c[i-1]>o[i-1], -1 if c[i-1]<o[i-1]; doji mother (c==o) -> no signal
- DOJI: range>0 AND body/range<=0.1; dir=+1 if c>(h+l)/2 else -1 (measurement tag only)

## Eligibility
Entry = open of bar i+1. Skip if entry_blocked(t[i+1]) (>=20:30 UTC or Sat/Sun), t[i+1]-t[i]!=5min, or bars i+1..i+24 not contiguous (24*5min).
Each pattern set split chronologically on its own eligible signals: first 70% = discovery, last 30% = internal holdout.

## Measurement (per set, disc and hold)
- Hit rate at +1,+3,+6,+12,+24 M5 bars: hit = dir*(close[i+k]-entry)>0.
- MFE / MAE (total) / MAE-before-peak over 24 M5 bars, scanned on M1. Report p50/p80.

## Exits (frozen from discovery, then applied unchanged to holdout)
Cost COST=$0.28/oz round-trip deducted per trade (Kai IC model, same as maemfe). Sensitivity: net at 1x/1.5x/2x cost.
One position at a time (per set); SL checked before TP within the same M1 bar; else time exit at close of bar i+24.
- E1 (1R:1R): SL = discovery p80 of mae_before_peak among WINNERS (dir*(c[i+24]-entry)>0) + $0.30; TP = SL. Fixed $ distances.
- E2 (ATR): SL = k*ATR14(M5, engine.atr Wilder) at signal bar i; TP=1.5*SL; k in {1.0,1.5}; freeze k with best discovery net PF (tie -> higher mean net).
R per trade = net/SL distance (1% risk per trade, $10k non-compounded) for DD and streak.

## Trials (logged): 4 sets (PIN_V0, PIN_V1, INSIDE, DOJI) x 3 exit configs (E1, E2k1.0, E2k1.5) = 12 discovery trials.
No other variants. No martingale/grid/averaging.

## Pass bar (all required, internal holdout = OOS)
Net expectancy >0 in every OOS calendar year (or 4/5), PF>=1.2 OOS and >1.0 at 1.5x cost, >=300 OOS trades, max DD<=20% at 1% risk, worst losing streak<=12.
Otherwise verdict = NO EDGE. Not a live signal.
