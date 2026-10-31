# PREREG — xau_m5_tod_calendar_20261031 (fleet xau-m5-tod-calendar-20261031)
Round 7: TOD × weekday calendar seasonality, IS-locked buckets. No price patterns.
Data: IC MT5 BID XAUUSD_M5.csv (data/ic-mt5-2026-10-10). Split 60/40 by bar index (chrono).
Bucket = (weekday Mon–Fri 0–4, ICT hour 0–23) of bar open time in ICT (UTC+7). 120 candidate cells.
IS only: fwd_H[t]=close[t+H]-close[t]. Per bucket: n, mean, std, sign consistency = share of events with sign(fwd)==sign(mean).
IS gates (locked): n>=80; |mean|/ATR14_mean_IS(bucket) >= θ=0.05; sign consistency > 0.55.
Rank gated buckets by score (|mean| or |mean|/std), keep top K. Direction = sign(IS mean). Tag HINDSIGHT-SELECTED.
OOS: every bar with open in a selected bucket -> enter open[t+1] in locked dir; exit SL $3.5 / TP 1.5R ($5.25) / time stop H bars (close of H-th), SL first if both. One position. Cost $0.28 RT.
ATR Q4 filter: ATR14[t] >= IS 75th pct of ATR14.
Grid (16): H{3,5} × score{mean,mean/std} × K{3,5} × ATR{any,Q4}.
Pass (all OOS): PF>=1.25, n>=150, E>0, PF>1 at $0.42, sensitivity PF>1 for SL{3,4}×R{1.25,1.75}, MDD<=25% at 1% risk, IS PF>1. Else ไม่เจอ. If zero buckets pass IS gates for a cell -> 0 trades, fail.
N_TRIALS +16 (2849->2865).
