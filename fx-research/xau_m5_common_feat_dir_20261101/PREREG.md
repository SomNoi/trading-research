# R236 PREREG — XAU M5 shared pre-entry features for DIRECTION on large-move 2-bar pairs (IC BID, cost $0.28)
Written 2026-11-01 ~22:30 ICT before any outcome scoring. Data: data/ic-mt5-2026-10-10/csv/XAUUSD_M5.csv. Builds on R233–R235 (size≠direction).
Split 60/40 by unique trading day (same as R235). Contiguous 5m bars required. Hours UTC.
## Entries
- B2: features known at bar1 close; entry bar2 OPEN; ref color = col1; CONT = trade in col1 direction. Pair family (for consistency check) = col1×col2 ∈ {GG,GR,RG,RR} (ex-post, IS analysis only).
- B3: features known at bar2 close (bar1+bar2); entry bar3 OPEN; ref color = col2; CONT = col2 direction. Family = col1×col2 (known pre-entry).
## Candidate features (pre-entry only; for B3 computed on bar2 plus F_same, F_s21)
hour, sess(LDN 07-12 / NY 13-19 / other), tvr=tickvol/SMA20, rng/ATR14, bf=body/rng, uw=upper wick/rng, lw=lower wick/rng, wick_with = wick on ref-color side (signed-aware: upper for G, lower for R)/rng, wick_against, streak = prior same-color run length incl. ref bar, dPDH=(PDH−C)/ATR, dPDL=(C−PDL)/ATR (prior UTC day), moh bucket (minute//15). B3 extra: same=col1==col2, s21=rng2/rng1.
## Selection (IS only)
Selection sample = IS bars where target bar (bar2 for B2, bar3 for B3) has |body|≥$5 OR range≥$5 (ex-post, selection only).
Per feature: IS quintile bins (categoricals as-is). CONT hit = sign(target C−O)==ref color. Score = max over bins with n≥200 of |hit−0.5| on pooled sample, kept only if same sign of (hit−0.5) in ≥3 of 4 families for that bin. Top feature F1 bin → G1; G2 = G1 AND best consistent bin of F2 (second-ranked, same bin-sign arm). Arm direction NOT fixed by selection: both CONT and FADE are tested.
Locked gates written to setups_IS.json (chmod 444) before OOS BT.
## Backtest (16 cells): Entry{B2,B3} × Arm{CONT,FADE} × (TP,SL){(5,4),(10,5)} × Gate{G1,G2}. Applied to ALL bars satisfying gate (no ex-post size filter). Exit SL/TP/close of entry bar; same-bar both → SL first. Cost 0.28.
Soft PASS: OOS PF>1.25, n_OOS>150, IS E>0, OOS E>0. Z one-sided vs Z_BONF(N=6378+16=6394). Direction ~50% → ไม่เจอ.
Report: direction hit IS/OOS with vs without gates (all bars and big-target bars), P(range≥5) lift.
