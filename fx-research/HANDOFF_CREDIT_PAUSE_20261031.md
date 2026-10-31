# HANDOFF — CREDIT PAUSE 2026-10-31 (~17:10 Asia/Bangkok)

**Status:** Hunt STOPPED by dr eggbot — user credits nearly full. No R192+. No demo. Resume only after user says so post credit-reset.

## Scoreboard
- **Latest round done:** **R191** `xau_m5_halfhour_drive_20261031` — ไม่เจอ 0/16 (best OOS PF 0.827 n=5401)
- **Rounds completed this standing hunt:** R1–R191 (all ไม่เจอ except R94 fragile watchlist)
- **N_TRIALS:** **5698**
- **Z_BONF:** **4.294** (one-sided Bonferroni α=0.05)
- **Robust passes:** **0**
- **Cost model:** $0.28 / 0.01 lot XAUUSD RT (also checked @$0.42)
- **Data:** SUBSTITUTE `data/from_parquet_m1/XAUUSD_M5.csv` (parquet M1→M5, Dukascopy-family mid) — **≠ IC BID**. Every post-wipe PREREG/REPORT labelled. See `RECOVERY.md`.

## R94 fragile watchlist ONLY (no demo)
- Folder: `xau_m5_pdh_pwh_or_20261031`
- PDH∪PWH MonTue H24 any — OOS PF 1.317 n=213 E+0.54; IS 1.126; @$0.42 1.226; t≈1.92 ≪ Z_BONF
- **Needs IC BID retest** before any demo consideration. Leave untouched until IC export returns.

## What needs IC BID retest
1. R94 PDH∪PWH MonTue longer-hold (only fragile candidate)
2. Full re-validation of any future survivor on true IC MT5 BID (current SUBSTITUTE cannot claim IC parity)
3. Prefer re-export IC M5/M1 under `data/ic-mt5-…` when Drive/box has it


## Closed shelves (afternoon/evening standing hunt, all ไม่เจอ on SUBSTITUTE)
- Jump intensity / clustering (R170)
- Asia→London timing + Asia mid-touch (R171/R173)
- Vol-impact Spearman / volume-proxy (R172)
- Range-efficiency / path-eff / Kaufman-ER cousins (R174)
- Hour-open drive / session-drive (R175)
- GK/PK + RS/CC vol-estimator ratios (R176/R177) — shelf CLOSED
- HTF-ORB prior-H1 OR (R178)
- M5↔H1 sync / residual (R179) — shelf CLOSED
- Up-breadth (R180 confirmatory of R78 — N rolled back)
- Week-mid BO (R181)
- Wick-ratio PA (R182)
- Vol-ACF |r| lag (R183); NY-lunch AM confirmatory SKIPPED (R153 intact)
- H4 mid touch (R184 confirmatory of R118 — N rolled back)
- Tickvol slope (R185)
- UTC day-gap (R186) — gap shelf CLOSED
- AR innovation (R187)
- Asia∪LDN → NY-hour BO (R188)
- Body-streak (R189)
- Wick-mass residual (R190)
- Half-hour drive (R191)
Plus many earlier shelves listed in INDEX (volume-flow, oscillators, FX-residual, pivots, compression, ACF/AR, calendar, VoV, CVD, prior-day, skew, Donchian, FVG, SMC, robust-slope, NY-range, info-theoretic, Asia KZ, R², vol-asym, VWAP-slope, multi-scale, daily-mid, Hurst, path-asym, session-impulse, calendar-direction, quiet→BO, MR-to-MA, etc.)


## Key paths
- Workspace: `/workspace/fx-research/`
- INDEX: `INDEX.md` (R1–R191)
- Catalog: `CATALOG_EXEC.md`
- Multiple testing: `results/multiple_testing.json` (N=5698)
- Recovery notes: `RECOVERY.md`
- This handoff: `HANDOFF_CREDIT_PAUSE_20261031.md`
- Data: `data/from_parquet_m1/XAUUSD_M5.csv` + `data/XAUUSD_M1.parquet`

## Round folders this session (dated 20261031)
Count xau_m5_*_20261031: **187**
Other *20261031* dirs: **8** (m5_motif5_novel_20261031, m5_shape_clusters_20261031, m5_shape_edge_overnight_20261031, xau_h1_donchian_20261031, xau_h1_m5_structure_20261031, xau_h1_orb_london_20261031, xau_m15_clv_mr_20261031, xau_m15_ema_ribbon_20261031)

Full xau_m5 list:
- `xau_m5_absorb_vol_20261031/`
- `xau_m5_adx_di_20261031/`
- `xau_m5_amihud_illiq_20261031/`
- `xau_m5_ao_saucer_20261031/`
- `xau_m5_ar_innov_20261031/`
- `xau_m5_aroon_cross_20261031/`
- `xau_m5_asia_kz_20261031/`
- `xau_m5_asia_ldn_hand_20261031/`
- `xau_m5_asia_ldn_nybo_20261031/`
- `xau_m5_asia_mid_touch_20261031/`
- `xau_m5_asia_midldn_20261031/`
- `xau_m5_asia_range_bo_20261031/`
- `xau_m5_asia_range_ldn_brk_20261031/`
- `xau_m5_atr_q_trans_20261031/`
- `xau_m5_atr_regime_lib_20261031/`
- `xau_m5_audusd_resid_20261031/`
- `xau_m5_bb_squeeze_20261031/`
- `xau_m5_beta_break_20261031/`
- `xau_m5_body_exh_20261031/`
- `xau_m5_body_streak_20261031/`
- `xau_m5_bop_extreme_20261031/`
- `xau_m5_breadth_mid_20261031/`
- `xau_m5_camarilla_20261031/`
- `xau_m5_cci_extreme_20261031/`
- `xau_m5_chandelier_20261031/`
- `xau_m5_close_streak_20261031/`
- `xau_m5_clv_streak_20261031/`
- `xau_m5_cmf_cross_20261031/`
- `xau_m5_cmo_extreme_20261031/`
- `xau_m5_comp_h1fade_20261031/`
- `xau_m5_comp_ldn_er_20261031/`
- `xau_m5_comp_montue_20261031/`
- `xau_m5_comp_pwh_dow_20261031/`
- `xau_m5_comp_rsi_willr_20261031/`
- `xau_m5_composite_q4_ldn_20261031/`
- `xau_m5_coppock_20261031/`
- `xau_m5_corr_regime_20261031/`
- `xau_m5_cvd_proxy_20261031/`
- `xau_m5_daily_pivot_20261031/`
- `xau_m5_day_gap_20261031/`
- `xau_m5_dd_du_ratio_20261031/`
- `xau_m5_dec_range_exp_20261031/`
- `xau_m5_demarker_20261031/`
- `xau_m5_displace_20261031/`
- `xau_m5_dow_drive_20261031/`
- `xau_m5_dpo_cross_20261031/`
- `xau_m5_dual_tf_rsi_20261031/`
- `xau_m5_elder_ray_20261031/`
- `xau_m5_eom_cross_20261031/`
- `xau_m5_eq_hl_tap_20261031/`
- `xau_m5_eurusd_resid_20261031/`
- `xau_m5_ewm_mom_20261031/`
- `xau_m5_feature_stump_20261031/`
- `xau_m5_fh_mid_20261031/`
- `xau_m5_fib_pd_20261031/`
- `xau_m5_fisher_xform_20261031/`
- `xau_m5_force_index_20261031/`
- `xau_m5_fractal_bo_20261031/`
- `xau_m5_frama_cross_20261031/`
- `xau_m5_fvg_fill_20261031/`
- `xau_m5_gann_hilo_20261031/`
- `xau_m5_gk_pk_ratio_20261031/`
- `xau_m5_h1_donch_mid_20261031/`
- `xau_m5_h1_h4_disagree_20261031/`
- `xau_m5_h1_orb_20261031/`
- `xau_m5_h1_resid_20261031/`
- `xau_m5_h1_resid_break_20261031/`
- `xau_m5_h1_streak3_20261031/`
- `xau_m5_h1_streak_entry_20261031/`
- `xau_m5_h1_vwap_mag_20261031/`
- `xau_m5_h1quiet_m5bo_20261031/`
- `xau_m5_h4_ema_pullback_20261031/`
- `xau_m5_h4_mid_20261031/`
- `xau_m5_h4_mid_touch_20261031/`
- `xau_m5_h4_open_mag_20261031/`
- `xau_m5_halfhour_drive_20261031/`
- `xau_m5_heikin_ashi_20261031/`
- `xau_m5_hod_lod_20261031/`
- `xau_m5_hour_open_drive_20261031/`
- `xau_m5_hour_resid_z_20261031/`
- `xau_m5_hour_sign_20261031/`
- `xau_m5_hull_ma_20261031/`
- `xau_m5_hurst_diff_20261031/`
- `xau_m5_hurst_reg_20261031/`
- `xau_m5_ichimoku_tk_20261031/`
- `xau_m5_inside_bo_20261031/`
- `xau_m5_intra_h1_beta_20261031/`
- `xau_m5_intraday_hl_bo_20261031/`
- `xau_m5_jump_fade_20261031/`
- `xau_m5_jump_intensity_20261031/`
- `xau_m5_kaufman_er_20261031/`
- `xau_m5_keltner_squeeze_20261031/`
- `xau_m5_killzone_h1_20261031/`
- `xau_m5_kst_cross_20261031/`
- `xau_m5_ldn_day_mom_20261031/`
- `xau_m5_ldn_drive_20261031/`
- `xau_m5_ldn_streak_20261031/`
- `xau_m5_linreg_chan_20261031/`
- `xau_m5_loud_asia_ldn_20261031/`
- `xau_m5_macd_cross_20261031/`
- `xau_m5_mass_index_20261031/`
- `xau_m5_mcginley_20261031/`
- `xau_m5_mfi_extreme_20261031/`
- `xau_m5_mi_lag1_20261031/`
- `xau_m5_micro_swing_20261031/`
- `xau_m5_min_of_hour_20261031/`
- `xau_m5_mom_persist_20261031/`
- `xau_m5_nr_breakout_20261031/`
- `xau_m5_nr_then_exp_20261031/`
- `xau_m5_ny_drive_20261031/`
- `xau_m5_ny_lunch_20261031/`
- `xau_m5_ny_orb_fail_20261031/`
- `xau_m5_ob_retest_20261031/`
- `xau_m5_open_gap_20261031/`
- `xau_m5_orb_fail_20261031/`
- `xau_m5_ou_halflife_20261031/`
- `xau_m5_outside_bar_20261031/`
- `xau_m5_overlap_imp_20261031/`
- `xau_m5_overnight_gap_20261031/`
- `xau_m5_ovn_inv_20261031/`
- `xau_m5_parkinson_div_20261031/`
- `xau_m5_pdh_cont_only_20261031/`
- `xau_m5_pdh_pwh_or_20261031/`
- `xau_m5_pdh_sweep_20261031/`
- `xau_m5_pdhl_levels_20261031/`
- `xau_m5_pdm_cross_20261031/`
- `xau_m5_pdo_cross_20261031/`
- `xau_m5_perm_entropy_20261031/`
- `xau_m5_ph4hl_levels_20261031/`
- `xau_m5_pwh_pwl_20261031/`
- `xau_m5_pwhl_levels_20261031/`
- `xau_m5_pwo_cross_20261031/`
- `xau_m5_qreg_slope_20261031/`
- `xau_m5_quiet_asia_ldn_20261031/`
- `xau_m5_r2_gate_20261031/`
- `xau_m5_range_eff_20261031/`
- `xau_m5_range_exp_20261031/`
- `xau_m5_range_pos_mr_20261031/`
- `xau_m5_range_skew_20261031/`
- `xau_m5_ret_acf_20261031/`
- `xau_m5_ret_entropy_20261031/`
- `xau_m5_ret_kurt_20261031/`
- `xau_m5_ret_skew_20261031/`
- `xau_m5_roc_extreme_20261031/`
- `xau_m5_round_number_20261031/`
- `xau_m5_rs_cc_ratio_20261031/`
- `xau_m5_rsi2_mr_20261031/`
- `xau_m5_schaff_stc_20261031/`
- `xau_m5_schaff_tc_20261031/`
- `xau_m5_semivar_20261031/`
- `xau_m5_sess_vote_20261031/`
- `xau_m5_sess_vpoc_20261031/`
- `xau_m5_session_open_imb_20261031/`
- `xau_m5_session_vwap_band_20261031/`
- `xau_m5_sma_resid_zx_20261031/`
- `xau_m5_spearman_acf_20261031/`
- `xau_m5_stoch_cross_20261031/`
- `xau_m5_supertrend_20261031/`
- `xau_m5_td_seq_20261031/`
- `xau_m5_tickvol_climax_20261031/`
- `xau_m5_tickvol_slope_20261031/`
- `xau_m5_tod_calendar_20261031/`
- `xau_m5_triple_barrier_20261031/`
- `xau_m5_trix_cross_20261031/`
- `xau_m5_tsi_cross_20261031/`
- `xau_m5_tsi_extreme_20261031/`
- `xau_m5_ultosc_20261031/`
- `xau_m5_up_breadth_20261031/`
- `xau_m5_usd_basket_resid_20261031/`
- `xau_m5_usdchf_resid_20261031/`
- `xau_m5_usdjpy_residual_20261031/`
- `xau_m5_var_ratio_20261031/`
- `xau_m5_vol_acf_20261031/`
- `xau_m5_vol_impact_20261031/`
- `xau_m5_vol_reject_20261031/`
- `xau_m5_vortex_cross_20261031/`
- `xau_m5_vov_atr_20261031/`
- `xau_m5_vwap_slope_20261031/`
- `xau_m5_week_mid_bo_20261031/`
- `xau_m5_week_open_20261031/`
- `xau_m5_weekend_gap_20261031/`
- `xau_m5_wick_mass_20261031/`
- `xau_m5_wick_ratio_20261031/`
- `xau_m5_willr_extreme_20261031/`
- `xau_m5_woodie_20261031/`
- `xau_m5_zscore_mr_20261031/`
- `xau_m5_zz_fibext_20261031/`

## Archive targets
- GitHub: `SomNoi/trading-research` → `fx-research/` (prioritize INDEX, CATALOG_EXEC, HANDOFF, multiple_testing, RECOVERY, PREREGs/REPORTs)
- Notion: FX Research archive parent `4086a0d1-ad70-81fa-9acb-fc100c9438f2`

## Standing rules on resume
- Silent to user; report EN to dr eggbot only
- Prefer ไม่เจอ over fake edges; prereg first; no martingale/grid
- Do not start rounds until user/dr eggbot says resume after credit reset
