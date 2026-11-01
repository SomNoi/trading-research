# R218 PREREG — Break PDH/PDL then first retest CONT, IC BID, 3R
Data: IC BID XAUUSD_M5 (data/ic-mt5-2026-10-10). Label IC BID.
PDH/PDL = high/low of prior UTC calendar day with data. BREAK: first M5 bar of the day (from 00:00 UTC) whose CLOSE > PDH (PDH level) / < PDL (PDL level) — locked.
RETEST: first later same-day bar with low ≤ PDH (PDH) / high ≥ PDL (PDL); no wick-beyond/sweep requirement. CONT in break direction (PDH→long, PDL→short), enter next bar open.
SL $2, TP $6, both-hit same bar → SL. Time stop: close of bar Hold (T4=20m, T8=40m). Cost $0.28. R=(pnl−0.28)/2. 1 trade/day/level.
Grid 16: Level{PDH,PDL} × Hold{T4,T8} × Day{any,MonTue} × SessEntry{any_after_break, LDN∪NY retest bar 07:00–20:59 UTC}.
Split 60/40 by calendar day. Z one-sided on OOS mean R. MT N 6090→6106; Bonferroni at N=6106.
Pass: OOS E>0, z ≥ Z_BONF, n≥100. Else ไม่เจอ. Distinct from R94 (first-touch, no break), R117 (sweep/reject).
