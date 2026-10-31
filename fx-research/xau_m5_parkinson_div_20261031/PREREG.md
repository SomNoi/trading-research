# PREREG R12 xau_m5_parkinson_div_20261031 (fleet xau-m5-parkinson-div-20261031)
Data: IC MT5 BID XAUUSD_M5.csv (data/ic-mt5-2026-10-10). Split 60/40 by bar index. Cost $0.28 RT.
Features (bar i, causal): PK_W = sqrt(mean_W(ln(H/L)^2)/(4 ln2)); sigma_cc_W = std(ln(c/c[-1]), W); div = PK/(sigma_cc+1e-9).
Threshold: trailing 20d (5520 bars, min 2760) rolling quantile p of div, shifted 1 bar (excludes bar i).
Signal: ONE-SIDED high div only: div_i >= q_p. Last bar dir d=sign(c_i-o_i) (0 -> no trade).
Arms: FADE -> -d ; CONT -> +d. Grid Arm{FADE,CONT} x W{12,24} x pctl{80,90} x Sess{any, LDN∪NY 07:00-16:30 UTC} = 16.
Entry open[i+1]; SL $3.5, TP 1.5R, time exit 5 bars at close; no overlap.
PASS: OOS n>=150, PF>=1.25, E>0, PF@1.5x cost>1, sens(SL{3,4}xR{1.25,1.75}) min PF>1, MDD<=25% @1% risk, IS PF>1.
N_TRIALS 2914 -> 2930.
