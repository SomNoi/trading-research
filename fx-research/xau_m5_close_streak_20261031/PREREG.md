# PREREG xau_m5_close_streak_20261031 (fleet xau-m5-close-streak-20261031) — Round 9
Written 2026-10-31 (ICT) before any backtest.
Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv (IC MT5 BID). Cost $0.28/oz RT. Split: first 60% bars IS, last 40% OOS.
streak_up[t]=streak_up[t-1]+1 if close[t]>close[t-1] else 0; streak_down mirrors. Equal close resets both.
Signal: fire once at bar t where streak_up==k exactly (or streak_down==k). No size/ATR requirement on the streak (distinct from R3 ATR impulse κ·ATR over 3 bars).
CONT: enter in streak direction at open[t+1]. FADE: enter against it.
k in {3,5,8}. ATR gate: any, or Q4 = ATR14 Wilder causal pct rank >=75 over trailing 5520 bars at t. Session = any (frozen).
Exit: SL $3.5, TP $5.25 (1.5R), time stop at close of 5th bar. SL wins ties. One position at a time.
Grid 12 = Arm{CONT,FADE} x k{3,5,8} x ATR{any,Q4}.
Pass (OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sens PF>1 for SL{3,4}xR{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Else ไม่เจอ. N_TRIALS +12 (2881->2893).
