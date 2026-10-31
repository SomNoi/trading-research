# Late-round REPORT digest R170–R191

## R171 — xau_m5_asia_midldn_20261031/REPORT.md

# R171 — Asia return → mid-London 10:00 UTC CONT/FADE (XAU M5)
DATA WARNING: SUBSTITUTE parquet-derived M5 (≠ IC BID). Cost $0.28.
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS. Days 2006, cut 2023-08-30. N 5394→5410, Z_BONF 4.282.
Best OOS: λ0.5 FADE T24 MonTue PF 0.951 E −0.091 t −0.41 n305 (IS PF 0.752).
CONT worst (OOS PF 0.65–0.78); FADE OOS 0.86–0.95. λ filter near non-binding (ATR14 is M5 ATR; 1175 vs 1133 days).
Related R65 (entry 07:00); distinct entry clock 10:00. Files: PREREG.md(sha,444), run.py, results.json.


## R172 — xau_m5_vol_impact_20261031/REPORT.md

# R172 — Rolling Spearman ρ(vol,|logret|) extreme CONT/FADE, XAU M5
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS (IS PF 0.59–0.80, OOS 0.75–0.91). Cut 2023-08-31. N 5410→5426, Z_BONF 4.283.
Best OOS: W40 q0.85 LOW_FADE LDN∪NY PF 0.910 E −0.127 t −1.13 n801 (IS PF 0.724; FULL t −3.57).
HIGH_CONT worse than LOW_FADE throughout; "volume confirms move" gives no continuation.
Related R6 tickvol climax, R81, R59 Amihud, R140 CVD; distinct (rank-corr, not level).
DATA WARNING: substitute parquet M5 ≠ IC BID; volume is weak tickvol proxy — ρ measures proxy, not true flow.
Note: in Sess=LDN∪NY cells, an out-of-session first signal consumes the regime's single entry (per prereg one entry/regime).


## R173 — xau_m5_asia_mid_touch_20261031/REPORT.md

# R173 AsiaMid first touch in London — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M5 ≠ IC BID. Cost $0.28. Split by day 60/40 at 2023-05-22. 1268 touch-days.
- All 16 cells E<0 IS and OOS. θ non-binding (AsiaRange always ≥1·ATR14(M5)) → 8 effective cells.
- Best OOS: FADE T12 from_above PF 0.891 E −0.179 t −0.82 n256 (IS 0.845).
- CONT worst: OOS PF 0.64–0.75, full t to −5.47; FADE OOS 0.78–0.89, also E<0.
- N 5426→5442, Z_BONF 4.284. See results.json.


## R174 — xau_m5_range_eff_20261031/REPORT.md

# R174 — Range-efficiency β (log|ΔC| ~ log(H−L)) extreme CONT/FADE, XAU M5
DATA WARNING: SUBSTITUTE parquet M1→M5 (≠ IC BID). Cost $0.28; split 2023-08-31 04:05 UTC (60/40).
Verdict: **ไม่เจอ 0/16**; all E<0 IS+OOS (IS PF 0.50–0.84, OOS 0.64–0.96).
β median 1.56 (W20) / 1.49 (W40).
Best OOS: W40 q0.90 LOW_FADE LDN∪NY PF 0.964 n=510 E −0.053 t −0.36 (IS 0.826, @$0.42 0.876); runner-up W40 q0.90 LOW_FADE any 0.958 n=917 (IS 0.722).
HIGH_CONT is the worst arm: W40 q0.90 IS 0.50–0.52, OOS 0.64–0.76. "Efficient" bars do not continue.
Related to path-asymmetry R164 / NR R4 / R134 but distinct (cross-sectional range→move elasticity). N 5442→5458, Z_BONF 4.284.
See results.json, PREREG.md (sha256 locked, chmod 444).


## R175 — xau_m5_hour_open_drive_20261031/REPORT.md

# R175 — XAU M5 hour-open drive (every UTC hour, minute==0) CONT/FADE
DATA WARNING: SUBSTITUTE parquet→M5, ≠ IC BID. Prereg sha in PREREG.sha256 (chmod 444).
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS; full t −12.5…−31.8 (λ gate near non-binding: n 23k→18.7k).
Best OOS: λ0.15 CONT T6 hours7–16 PF 0.825 E −0.296 t −7.01 n6690 (IS 0.700; @$0.42 0.754).
FADE OOS 0.72–0.78; CONT 0.75–0.83. Split 2023-08-31. N 5458→5474, Z_BONF 4.285.


## R176 — xau_m5_gk_pk_ratio_20261031/REPORT.md

# R176 GK/PK vol ratio extreme — XAU M5 (SUBSTITUTE data, ≠IC BID)
Verdict: ไม่เจอ 0/16. All cells E<0 IS and OOS @ $0.28; full t −4.65…−11.80.
Best OOS: W40 q0.80 HIGH_CONT LDN∪NY n=803 PF 0.907 E −0.14 t −1.19 (IS PF 0.624; @0.42 PF 0.823).
R median ≈1.00 (P10–P90 0.93–1.06 W20) — estimators rarely disagree much. Split 2023-08-31 04:05 UTC. N_TRIALS 5474→5490, Z 4.286.


## R177 — xau_m5_rs_cc_ratio_20261031/REPORT.md

# R177 REPORT — RS/CC vol ratio extreme, XAU M5 (SUBSTITUTE data ≠ IC BID)
Verdict: ไม่เจอ 0/16. All cells E<0 IS and OOS; full t −3.13…−12.09; @$0.42 OOS PF 0.61–0.81.
Best OOS: W40 q0.80 LOW_FADE LDN∪NY n781 PF 0.895 E −0.159 t −1.34 (IS PF 0.781).
R median ≈1.01–1.02 (p10–p90 0.78–1.34 W20). Split 2023-08-31. N 5490→5506 Z 4.286.
Related R176 GK/PK (0/16, best OOS 0.907) and R12 Parkinson vs ATR; RS≠GK — same dead outcome.


## R178 — xau_m5_h1_orb_20261031/REPORT.md

# R178 — Prior completed H1 opening-range break on M5 (CONT/FADE)
DATA WARNING: SUBSTITUTE M5 from parquet M1, ≠ IC BID. Cost $0.28 (+$0.42 check).
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS; full t −11.4…−24.7.
Best OOS: K2 FADE T12 LDN∪NY n9482 PF 0.851 E −0.279 t −7.25 (IS PF 0.827, @$0.42 0.786).
CONT worse (OOS PF 0.77–0.83); K2≈K3. First-pass bug (hour id unit) caught & fixed before final run; PREREG unchanged.
Related R19 (session-open ORB); distinct R116/R144. N 5506→5522, Z 4.287.


## R179 — xau_m5_h1_resid_break_20261031/REPORT.md

# R179 — M5 residual vs lagged completed H1 (resid-extreme CONT/FADE)
DATA WARNING: SUBSTITUTE M5 from parquet M1, NOT IC BID.
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS (full t −12.4…−29.7). Best OOS W24 λ1.5 FADE LDNNY PF 0.827 E −0.281 t −9.31 n12456 (IS 0.782, @$0.42 0.753). CONT OOS 0.765–0.797.
Split 2023-08-31 04:05 UTC. N 5522→5538 Z 4.288. Related R54/R161/R137. Details results.json.


## R180 — xau_m5_up_breadth_20261031/REPORT.md

# R180 up-close breadth extreme — ไม่เจอ 0/16
DATA SUBSTITUTE ≠ IC BID. Split 2023-08-31 04:05 UTC. N 5538→5554, Z 4.288.
All 16 E<0 IS+OOS (full t −10.7…−23.2). Best OOS: W12 q0.80 FADE LDNNY n6508 PF 0.848 E −0.232 t −5.75 (IS PF 0.713; @$0.42 0.768). CONT OOS PF 0.74–0.81.
Note: LOW used fixed 1−q_hi level per brief (not trailing low quantile). See results.json.


## R181 — xau_m5_week_mid_bo_20261031/REPORT.md

# R181 — Prior-week mid break CONT/FADE (XAU M5) — VERDICT: ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE from_parquet_m1/XAUUSD_M5.csv ≠ IC BID. Cost $0.28 (also $0.42). Split 60/40 by week, OOS from 2023-08-28.
- Trades ≈1/week, only weeks with a cross of prior-week Mid in window: n 119–135 IS / 65–78 OOS (any-ATR); Q4 32–44 OOS.
- CONT: IS PF 1.07–1.46 → OOS PF 0.19–0.47 (sign flip, collapses).
- FADE: IS PF 0.49–0.62 → OOS 0.85–1.61. Best OOS FADE MonTue T48 Q4 PF 1.611 E +1.01 n32 t1.32 but IS PF 0.489, full t −0.71 → fails IS gate & Z.
- Full-sample t all negative (−0.62…−2.35); Z_Bonf 4.288 (N 5538→5554). Regime flip IS↔OOS = no stable edge.


## R182 — xau_m5_wick_ratio_20261031/REPORT.md

# R182 — Extreme wick ratio CONT/FADE XAU M5 — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M1→M5, ≠IC MT5 BID.
All 16 cells E<0 IS and OOS (full t −7.0…−30.0). OOS PF 0.73–0.84. @$0.42 OOS PF 0.66–0.76.
Best OOS: θ0.60 λ0.5 FADE LDN∪NY PF 0.835 E −0.259 t −8.91 n12936 (IS PF 0.738, @$0.42 0.758).
CONT OOS PF 0.76–0.82; FADE 0.73–0.84 — neither direction of rejection has edge after $0.28.
N 5554→5570, Z_BONF 4.289. Split 2023-08-31 (60/40 by bar).


## R183 — xau_m5_vol_acf_20261031/REPORT.md

# R183 REPORT — Rolling lag-1 ACF of |r| extreme CONT/FADE (XAU M5) — DATA SUBSTITUTE ≠IC BID
Verdict: ไม่เจอ 0/16. All cells E<0 in IS and OOS (full t −6.49…−14.30). N 5570→5586, Z_BONF 4.290. Split 2023-08-31 (60/40 by bar).
Best OOS: W60 q0.80 HIGH_CONT any PF 0.830 E −0.253 t −4.62 n3425 (IS PF 0.682, @$0.42 0.750).
HIGH_CONT OOS PF 0.73–0.83; LOW_FADE OOS 0.76–0.81. Vol clustering regime carries no directional edge after $0.28.
Related R139 VoV / R132 Spearman ACF of returns / R170 jumps / R137 AR; |r| lag-1 ACF novel. Details: results.json.


## R184 — xau_m5_h4_mid_touch_20261031/REPORT.md

# R184 — Prior completed H4 mid first-touch CONT/FADE (XAU M5)
DATA WARNING: SUBSTITUTE from_parquet_m1 M5 ≠ IC BID. Cost $0.28 (also $0.42). Split 2023-08-31 04:05 UTC.
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS (full t −2.15…−9.30).
Best OOS: θ1.0 FADE T12 LDN∪NY PF 0.917 E −0.151 t −1.08 n726 (IS 0.873, @$0.42 0.846).
CONT OOS PF 0.75–0.86; FADE 0.81–0.92. N 5586→5602, Z≈4.29. See results.json.


## R185 — xau_m5_tickvol_slope_20261031/REPORT.md

# R185 — Rolling OLS slope of tickvol vs bar index (XAU M5) — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M5 (≠IC BID); volume = weak tickvol proxy.
All 16 cells E<0 IS and OOS @ $0.28 (full t −4.48…−12.75). Split 2023-08-31 04:05 UTC.
Best OOS: W40 q0.80 HIGH_CONT LDN∪NY PF 0.867 E −0.219 t −2.51 n1572 (IS PF 0.752; @$0.42 PF 0.791).
HIGH_CONT OOS PF 0.75–0.87; LOW_FADE OOS PF 0.78–0.83.
Related R6 (tickvol climax level) / R172 (vol-impact ρ) / R140 (CVD): slope≠level, also dead.
N_TRIALS 5586→5602, Z_Bonf 4.290. PREREG sha in PREREG.sha256 (chmod 444).


## R186 — xau_m5_day_gap_20261031/report.md

# R186 UTC day-open gap CONT/FADE — XAU M5 — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M5 (≠ IC BID). Cost $0.28. Split 60/40 by day, cut 2023-09-01. N=5618, Z_bonf 4.29.
Gap stats: median |Gap| $0.025, median |Gap|/ATR14 0.025; days ≥0.15 ATR 18.0%, ≥0.30 ATR 15.1% (n_days 2409). Large gaps mostly weekend reopen (first bar of Sunday 22/23 UTC); MonTue filter therefore tiny n (≤17 IS / ≤6 OOS).
Best OOS (n≥30): λ0.15 FADE T12/T24 any PF 0.74–0.78 E −0.44..−0.51. FADE IS λ0.30 T24 PF 1.147 E +0.18 → OOS PF 0.794 E −0.42 (decay). CONT all E<0 (full t −5.3…−6.0).


## R187 — xau_m5_ar_innov_20261031/REPORT.md

# R187 AR(k) innovation extreme — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M5 ≠ IC BID. Split 2023-08-31 (60/40). N 5618→5634, Z_Bonf 4.291.
All 16 cells E<0 IS+OOS (full t −11.8…−24.6). Best OOS: k2 λ2.0 CONT any PF 0.816 E −0.307 t −9.19 n10487 (IS 0.666; @$0.42 0.745).
FADE OOS PF 0.75–0.80; CONT OOS 0.79–0.82. k1≈k2; λ and session change little. Signals very frequent (~5–9/day), cost-dominated.


## R188 — xau_m5_asia_ldn_nybo_20261031/REPORT.md

# R188 — Asia∪London range break in NY open hour (XAU M5) — ไม่เจอ 0/16
DATA: SUBSTITUTE parquet M5 ≠ IC BID. Cost $0.28 (+$0.42 sens). Split 2023-09-01. N 5634→5650, Z_Bonf 4.292.
- 730 break days (first close beyond AL range in 12:00–13:00 UTC). Range/ATR14(M5) min 4.7, median 11.1 → θ{0.8,1.5} NON-BINDING: θ cells identical (effective 8 distinct cells).
- CONT: all E<0 IS+OOS; OOS PF 0.50–0.66, full t −2.35…−4.40.
- FADE: best OOS θ any FADE T24 MonTue PF 0.920 E −0.172 n90 (IS PF 0.990); FADE T24 any OOS PF 0.867 E −0.297 n259 (IS 1.008, only IS-positive cell, t 0.08).
- Verdict: no edge; mild breakout-failure lean (FADE>CONT) but sub-cost and OOS negative.


## R189 — xau_m5_body_streak_20261031/REPORT.md

# R189 XAU M5 body-color streak — ไม่เจอ 0/16
DATA WARNING: SUBSTITUTE parquet M5 ≠ IC BID. Split 2023-08-31 04:05 UTC. N 5650→5666, Bonf Z 4.293.
All 16 E<0 IS+OOS at $0.28 (full t −9.9…−37.3). Best OOS: K3 FADE T6 LDN∪NY PF 0.836 E −0.274 n12143 (IS 0.749, @$0.42 0.763).
CONT OOS PF 0.72–0.81; FADE 0.75–0.84. K5 no better than K3. Doji frac 0.18%.
vs R84: body color sign(C−O) ≠ close-to-close sign; same null — streaks carry no exploitable drift after cost.


## R190 — xau_m5_wick_mass_20261031/REPORT.md

# R190 — XAU M5 wick-mass residual (range ~ |body| rolling OLS) extreme CONT/FADE
DATA WARNING: SUBSTITUTE parquet M5 ≠ IC BID. Split 60/40 at 2023-08-31. Cost $0.28.
Verdict: ไม่เจอ 0/16. All cells E<0 in IS and OOS (full t −15.7…−30.3).
Best OOS: W40 q0.90 HIGH_FADE LDN∪NY — PF 0.810, E −0.335, t −9.39, n 9799 (IS PF 0.753; @$0.42 PF 0.743).
HIGH_FADE OOS PF 0.79–0.81; LOW_CONT OOS PF 0.77–0.80. W and q barely matter.
N 5666→5682, Z_BONF 4.294.


## R191 — xau_m5_halfhour_drive_20261031/REPORT.md

# R191 — Half-hour open drive (:00/:30), LDN∪NY 07–16 UTC
DATA WARNING: SUBSTITUTE from_parquet_m1 M5 ≠ IC BID.
Verdict: ไม่เจอ 0/16. All E<0 IS+OOS; full t −12.5…−24.7. Split 2023-08-31 04:05 UTC.
Best OOS: λ0.30 CONT T6 :00_only PF 0.827 E −0.294 t −6.22 n5401 (IS 0.710; @$0.42 0.756).
Both(:00+:30) OOS PF 0.75–0.81; FADE OOS 0.73–0.79. λ near non-binding (n 19.9k→16.0k).
NOTE: :00_only λ0.15 cells are identical to R175 hours7–16 cells (same signal set) — redundant trials; :30 adds nothing.
N 5682→5698 Z 4.294.

