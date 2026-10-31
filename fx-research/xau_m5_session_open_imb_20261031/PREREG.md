# PREREG — xau-m5-session-open-imb-20261031
Data: IC MT5 BID XAUUSD M5 (/workspace/fx-research/data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv). Timestamps UTC; sessions fixed in ICT (UTC+7), no DST adjust.
- Session open bar0: LDN 14:00 ICT (07:00 UTC); NY 19:30 ICT (12:30 UTC). Max 1 trade/session/day.
- W=2 frozen. I=(close of bar1 − open of bar0)/ATR14_M5 at bar before bar0 (Wilder ATR, completed bars). Extreme |I|>=tau, tau∈{0.8,1.2}.
- ATR pct: rank of ATR14 at open vs ATR14 at same session-open bar over prior 20 trading days (needs 20). Q4 = pct>=75.
- Arms: CONT=sign(I), FADE=-sign(I). Entry open of bar2 (bar0 index+2).
- HTF F1: last completed H1 (resampled from M5) close vs EMA55 of H1 closes; trade dir must agree.
- Exit: SL $3.5, TP $5.25 (1.5R) intrabar (both hit same bar → SL), else exit at open of entry+5 bars. Cost $0.28/oz RT (0.01 lot). PnL $/oz.
- Grid (24): Session{LDN,NY} × Arm{CONT,FADE} × tau{0.8,1.2} × Filter{F0+ATRany, F1+ATRany, F0+ATRQ4}.
- Split: chronological 60/40 by bar time. No OOS tuning.
- Pass (all): OOS PF>=1.25, n_OOS>=150, E>0, PF@1.5x cost>1.0, OOS MDD<=30R... (MDD in $/oz <= 30×3.5), sensitivity entry±1 bar and SL±0.5 (TP 1.5R) all PF>1.15 on OOS.
- N_TRIALS 2751→2775; Z_BONF=norm.ppf(1-0.05/2775).
