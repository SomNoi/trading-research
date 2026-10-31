# Report — Round 5 composite

**ไม่เจอ**. 0/10 pass. Best OOS PF 1.15 (EXH_FADE κ0.8 early60, n=15, IS 0.76). Best n≥150: VWAP_MR β1.0 full_LDN PF 0.74 (n=276, IS 0.78). 9/10 cells OOS PF<1. N_TRIALS 2823→2833.

```
trial,IS_n,IS_PF,OOS_n,OOS_PF,OOS_E,OOS_PF_042,sens_minPF,OOS_MDD,PASS
VWAP_MR_b1.0|full_LDN,522,0.781,276,0.741,-0.619,0.694,0.639,60.9,False
VWAP_MR_b1.0|early60,81,0.678,24,0.939,-0.134,0.88,0.756,6.9,False
VWAP_MR_b1.5|full_LDN,389,0.767,208,0.718,-0.68,0.673,0.614,48.8,False
VWAP_MR_b1.5|early60,37,0.545,8,0.789,-0.499,0.739,0.635,4.3,False
NR7_FAILFADE|full_LDN,85,0.848,50,0.584,-1.068,0.547,0.499,17.5,False
NR7_FAILFADE|early60,22,0.733,5,0.329,-2.03,0.308,0.0,3.2,False
EXH_FADE_k0.8|full_LDN,125,0.733,54,0.773,-0.539,0.725,0.768,11.3,False
EXH_FADE_k0.8|early60,32,0.763,15,1.15,0.303,1.078,0.762,3.2,False
EXH_FADE_k1.2|full_LDN,85,0.903,36,0.939,-0.134,0.88,0.756,6.9,False
EXH_FADE_k1.2|early60,22,0.816,10,0.563,-1.155,0.528,0.453,4.7,False
```

How it differs from R2/R3/R4: R2 tested VWAP bands MR+CONT over several sessions without an ATR gate. R3 tested impulse CONT/FADE in Q1/Q4 over LDN∪NY. R4 tested NR4/NR7 CONT/FAILFADE with ATR any/Q4 over any session or LDN∪NY. R5 keeps only the fade/MR side of each trigger, forces Q4+London-only on all three arms, and adds an early-60m TOD level. EXH uses a 50% reclaim confirmation, not a direct fade.

Chart: results/oos_equity.png
