# xau_m5_nr_breakout_20261031: ไม่เจอ
Fleet: xau-m5-nr-breakout-20261031. Data: IC MT5 BID XAUUSD M5, 99,964 bars. IS is 60%; OOS starts 2026-03-19 10:05 ICT. Cost is $0.28 RT. The spec is in PREREG.md (sha256 in PREREG.sha256, chmod 444).
- 0/16 cells pass. All 16 cells have OOS PF < 1 and IS PF < 1.
- Best OOS: NR7 FAILFADE, ATR Q4, any session. PF 0.87, n=371, E −$0.29/trade, WR 40%, MDD 36%, IS PF 0.83.
- Best high-frequency cell: NR7 CONT, any/any. PF 0.85, n=4079 (~28/day), MDD 98%.
- The LDN∪NY session gate makes results worse in every pairing. The Q4 ATR gate does not lift any cell above 0.88.
- Both CONT and FAILFADE lose. The breakout of a compression bar does not carry direction over a 5-bar hold after $0.28.
Distinction: NR-K uses minimum range over K bars, not containment (inside bar). Entry is on a close-confirmed break within 3 bars. This is not R1 open imbalance, R2 VWAP, or the R3 3-bar impulse.
Files: main.py, results/summary.csv, results/best_equity.png. N_TRIALS 2807→2823.
