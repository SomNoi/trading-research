# PREREG — xau_h1_m5_structure_20261031 (fleet task xau-h1-m5-structure-20261031)
Source: IC MT5 BID XAUUSD M5 `/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv` (2025-05-14..2026-10). Research only.
Written and hashed BEFORE any backtest run.

## H1 build
Resample M5 -> H1, label=left, closed=left. H1 bar with open T is usable at M5 bars with open >= T+1h (fully closed). Incomplete hours (<12 M5 bars) still used (market data gaps); no forward info.

## H1 structure (locked)
- Fractal swing high at j: H[j]>H[j-1] and H[j]>H[j+1]; low mirror. Confirmed at close of j+1 (usable from H1 bar j+2 open).
- Keep last two confirmed SH (sh1 latest, sh0 prior) and SL (sl1, sl0). State = BULL if sh1>sh0 and sl1>sl0; BEAR if sh1<sh0 and sl1<sl0; else NEUTRAL.
- Evaluated on each H1 close k, using swings confirmed at or before close k:
  - Bull BOS: state BULL and C[k] > sh1, first close beyond that swing. Bear BOS mirror (state BEAR, C<sl1).
  - Bear CHoCH: state BULL and C[k] < sl1 (protecting HL). Bull CHoCH: state BEAR and C[k] > sh1. Each swing triggers at most once.
- Arm BOS_cont: bias=+1 after bull BOS, held until a bear CHoCH (bias=0) or bear BOS (bias=-1); mirror for short.
- Arm CHoCH_flip: after CHoCH in direction d, bias=d for the next 12 H1 bars, cancelled early by any opposite BOS/CHoCH.

## M5 triggers (on completed M5 bar i; bias must be nonzero and equal trigger direction)
- ENGULF: exact rule of `engulf_watch/bt_week.py` lines 26–28 (T1 or T2): long = green[i] & red[i-1] & C[i]>H[i-1]; short = red[i] & green[i-1] & C[i]<L[i-1].
- M5_microBOS: same 3-bar fractal on M5, confirmed at close of i+1. Long when C[i] > latest confirmed M5 swing high (first close beyond it); short mirror with latest confirmed M5 swing low.

## Exits
- E1: SL $3.5, TP 1.5R ($5.25).
- E2: SL 1.5*ATR14(M5, Wilder, at signal bar), TP 1.5*SL.
- Max hold 288 M5 bars (24h), exit at close. SL checked before TP on the same bar (worst case).

## Gate
Session (entry bar open time, ICT=UTC+7): any vs LDN(14:00–19:00) ∪ NY(19:30–23:30).

## Grid
2 arms x 2 triggers x 2 exits x 2 sessions = **16 trials**. PIN not used. No RSI. N_TRIALS 2735 -> 2751, Z_BONF = norm.ppf(1-0.05/2751).

## Mechanics
Entry = next M5 open after signal bar. One position at a time (signals while in a trade ignored). 0.01 lot = $1 per $1 move. Cost $0.28 RT per trade; also 1.5x ($0.42).
Split: chronological by M5 bar index, first 60% IS / last 40% OOS (trade assigned by entry bar). Nothing tuned; IS reported for context only.

## Pass (all, on OOS)
PF>=1.25; expectancy>0; n>=150; PF>1.0 at 1.5x cost; MDD<=20% at 1% risk/trade (compounded R) OR MDD<25% of net profit; worst losing streak <=12; sensitivity: entry delayed +1 bar (−1 bar would be lookahead, not tested) and SL ±$0.5 (E2: ATR-SL ±$0.5, TP stays 1.5x SL) each keep PF>1.15.
Else verdict **ไม่เจอ**.
