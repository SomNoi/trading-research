# IC Markets real costs (from Kai, read-only probe, 2026-10-11)
Account: DEMO 52946518 ICMarketsSC-Demo, Raw Trading Ltd, MT5 build 6230, USD, leverage 1:5000, hedging. No live account on Kai's box.
Commission: 3.50 USD per 1.00 lot per side (7.00 RT), least-squares over 3,290 deals. 0.01-lot deals show 0.04 due to rounding. FX bounded consistent with same rate.
Spread (tick-by-tick, 1h core per session, Mon 05 - Fri 09 Oct 2026; server UTC+3; ASIA 00-01 UTC, LONDON 08-09 UTC, NY 14-15 UTC):
sym,session,median_pts,p90_pts,USD_per_lot_median
EURUSD,ASIA,1,1,1.00
EURUSD,LONDON,1,1,1.00
EURUSD,NY,1,1,1.00
GBPUSD,ASIA,2,2,2.00
GBPUSD,LONDON,2,2,2.00
GBPUSD,NY,2,3,2.00
USDJPY,ASIA,1,2,0.63
USDJPY,LONDON,1,2,0.63
USDJPY,NY,1,2,0.63
AUDUSD,ASIA,1,1,1.00
AUDUSD,LONDON,1,1,1.00
AUDUSD,NY,1,1,1.00
XAUUSD,ASIA,11,12,11.00
XAUUSD,LONDON,8,11,8.00
XAUUSD,NY,7,10,7.00
Points: 1e-05 on 5-digit FX, 0.001 USDJPY, 0.01 XAUUSD. Weekend-close spreads are much wider (EURUSD 12, GBPUSD 44, USDJPY 33, AUDUSD 32, XAUUSD 40 pts): avoid/penalize rollover and weekend-open periods. Only 1h per session sampled; off-core hours (esp. rollover) not measured.
Swap (points, USD/lot/night): EURUSD -7.99/+1.31; GBPUSD -4.84/-3.19; USDJPY +5.19/-10.74 USD; AUDUSD -2.18/-4.82; XAUUSD -57.03/+39.77. Triple swap Wednesday.
Contract: FX 100000, XAUUSD 100; min lot 0.01, step 0.01; stops_level 0 (impose own min stop); filling IOC.
Slippage: XAUUSD last 120 market entries ~0 (quote-before-fill proxy; 2 of 120 adverse by 1 pt). Demo fills are likely optimistic vs live: keep slippage assumption >= 0.1 pip FX / $0.05 XAU per side and keep 1.5x/2x cost sensitivity.
