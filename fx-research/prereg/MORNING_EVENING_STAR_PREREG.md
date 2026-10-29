# MORNING_EVENING_STAR_PREREG — Track B (task morning-evening-star-20261029)
Locked BEFORE any signal counting / stats. Source: Dukascopy free feed (mid), not IC MT5.
Symbol XAUUSD, M5 = resample('5min', left/left) of engine.load_m1 M1, filtered m1.index < 2025-10-10 UTC (engine.HOLDOUT_START; never loaded beyond).

## Patterns (3-bar star, signal completes on bar i; bars i-2, i-1, i)
range_j=h-l (must be >0 on all three bars); body_j=|c-o|; br=body/range; mid_j=(h+l)/2
- MORNING (+1): c[i-2]<o[i-2] AND br[i-2]>=0.5; br[i-1]<=0.3 AND mid[i-1]<mid[i-2]; c[i]>o[i] AND br[i]>=0.5 AND c[i]>=(o[i-2]+c[i-2])/2
- EVENING (-1): c[i-2]>o[i-2] AND br[i-2]>=0.5; br[i-1]<=0.3 AND mid[i-1]>mid[i-2]; c[i]<o[i] AND br[i]>=0.5 AND c[i]<=(o[i-2]+c[i-2])/2
- Conflict: both are mutually exclusive by construction (candle1 color). If both ever fire: evening if c[i]<o[i] else morning.
- MES_V0: no trend filter
- MES_V1: ema5=EMA(close,5) (engine.ema); slope=ema5[i]-ema5[i-5]; morning needs slope<0, evening needs slope>0

## Eligibility
Entry = open of bar i+1. Skip if entry_blocked(t[i+1]) (>=20:30 UTC or Sat/Sun), t[i+1]-t[i]!=5min, or bars i+1..i+24 not contiguous.
Each set split chronologically on its own eligible signals: first 70% discovery, last 30% internal holdout.

## Measurement / Exits / Costs — identical to CLASSIC_CANDLES_PREREG
Hit +1,+3,+6,+12,+24; MFE/MAE/MAE-before-peak on M1 over 24 M5 bars (p50/p80).
COST=$0.28/oz RT; sensitivity 1x/1.5x/2x. One position at a time; SL before TP; else time exit close bar i+24.
- E1: SL=TP = disc winners' mae_before_peak p80 + $0.30
- E2: SL=k*ATR14(M5) at bar i, TP=1.5*SL, k in {1.0,1.5}; freeze best disc net PF (tie -> higher mean net)

## Trials: 2 sets x 3 exits = 6 discovery trials (results/trials.csv). No other variants.

## Pass bar (all required, internal holdout OOS)
Net expectancy >0 in every OOS calendar year (or 4/5), PF>=1.2 OOS and >1.0 at 1.5x cost, >=300 OOS trades, max DD<=20% at 1% risk, worst losing streak<=12. Else NO EDGE. Not a live signal.
