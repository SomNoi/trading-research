# PREREG xau_m5_nr_breakout_20261031 (fleet xau-m5-nr-breakout-20261031)
Written 2026-10-31 (ICT) before any backtest.
Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (IC MT5 BID). Cost $0.28/oz RT. Split: first 60% of bars = IS, last 40% = OOS.
NR-K: bar t with range[t]=h-l equal to min(range[t-K+1..t]), K in {4,7}. NR box = [low_t, high_t].
Break: the first bar b in t+1..t+3 that CLOSES above high_t (long) or below low_t (short). No break in 3 bars means no setup.
CONT: enter in the break direction at open[b+1].
FAILFADE: after a break at b, if bar b+1 or b+2 closes back inside [low_t, high_t], enter opposite the break at the next bar's open.
ATR gate: any, or Q4 = ATR14 (Wilder) causal pct rank >=75 within the trailing 5520 bars (~20d), measured at the decision bar.
Session: any, or LDN∪NY = decision bar in ICT 14:00-18:59 or 19:30-23:29 (UTC 07:00-16:29).
Exit: SL $3.5, TP $5.25 (1.5R), time stop at the close of the 5th bar after entry. SL wins any same-bar tie. One position at a time, so several trades a day are allowed.
Grid 16 = K{4,7} x Arm{CONT,FAILFADE} x ATR{any,Q4} x Sess{any,LDNNY}.
Pass (all OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sensitivity PF>1 for SL{3,4} x R{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Otherwise the verdict is ไม่เจอ. N_TRIALS +16 (2807->2823).
