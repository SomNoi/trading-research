# R219 Quiet Asia range -> first London break CONT — IC BID, 3R
Data: IC BID XAUUSD_M5 (ic-mt5-2026-10-10). Cost $0.28. SL $2 TP $6 (R=$2).
AsiaRange = H-L of 00:00-06:55 UTC bars. ATR14 = 14-day mean of daily (H-L) of prior days (no lookahead).
Quiet if AsiaRange <= theta*ATR14. LDN window 07:00-10:00 UTC (bar opens 07:00..09:55): first close > AsiaH (long) or < AsiaL (short) -> CONT, entry next bar open. 1 trade/day.
Grid: theta{0.5,0.8,1.0,1.2} x Hold{T4,T8} x Day{any,MonTue} = 16. Time exit at close of bar entry+H-1.
Split 60/40 by day. Z one-sided on OOS; Bonferroni N=6122 (6106+16). Distinct from R125 (any break), R168, R4 NR.
