# PREREG xau-m5-session-vwap-band-20261031 (locked before results)
Data: IC MT5 BID XAUUSD_M5.csv. Times UTC; ICT=UTC+7. LDN 14:00-19:00 ICT (07:00-12:00 UTC), NY 19:30-23:30 ICT (12:30-16:30 UTC).
VWAP: session-anchored, TP=(H+L+C)/3 weighted by tick_volume (file has tick_volume; real_volume=0). Reset each session open.
d=(close-VWAP)/ATR14 (Wilder, M5, computed on all bars). Signal: first bar in session with |d|>=beta (bars after first 2 of session). One trade per session-day.
Arm MR: side=-sign(d); CONT: side=sign(d). TOD: any = whole session; early60 = signal bar within first 60m.
Entry next bar open; SL $3.5, TP $5.25 (1.5R), time stop close of bar 5; SL first if both hit in a bar. Cost $0.28 per 0.01 lot RT = $0.28 price-points per trade in $ per 0.01 lot (1 lot unit = $1/pt for 0.01lot).
Grid 16: Session{LDN,NY} x Arm{MR,CONT} x beta{1.0,1.5} x TOD{any,early60}. H=5, F0 frozen.
Split 60/40 chrono by date. PASS: OOS PF>=1.25, n>=150, E>0, PF>1 at 1.5x cost, sensitivity (beta±0.25 & H{3,4} all PF>1 OOS), MDD reported. No expansion after P&L.
