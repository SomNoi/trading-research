# fx-research INDEX — access map of finished candidates/studies
Built 2026-10-29 (ICT) by FX-Research, task classic-candles-20261029-A. Sources: STATUS.md, NOTES.md, results/prereg_hashes.txt, report headlines, results/ranked_oos.csv. No system was re-run.

## Global facts
- **Overall: 0 systems pass the full pass bar.** No finalist, so no holdout run was ever authorised.
- N_TRIALS = **925** (results/multiple_testing.json; Bonferroni z ≈ 3.87).
- HOLDOUT_START = **2025-10-10 UTC** (scripts/engine.py). It was never used for selection. Exception: mae-pla used its own separate holdout trial; engulf maemfe uses an internal discovery/holdout split before 2025-10-10.
- Data: Dukascopy M1 **mid**, which is **not the same as IC MT5** (IC bid ≈ −$0.04 vs mid on XAU; see results/dukascopy_vs_ic.md). IC export may be used only as a cross-check.
- Cost model: Kai's IC model (p90 session spreads, $3.50/lot/side, slippage, swaps) in scripts/engine.py + IC_COSTS_FROM_KAI_20261011.md. XAU ad-hoc scripts use about $0.28/oz RT.
- Meta pointers: REPORT.md (top-level report + addendum), STATUS.md (run log/updates), NOTES.md (prior work, CHoCH, Kaze, data/cost history).
- PF columns are walk-forward OOS at 1x cost (after costs) unless stated otherwise.

## Track 1 — families 1–6 (results/reports/{fam}_{SYM}.md; 4–5 symbols each)
| short name | path | symbol/TF | method | verdict | key metric (OOS PF min–max) | prereg |
|---|---|---|---|---|---|---|
| 1_donchian | results/reports/1_donchian_*.md | EU/GU/UJ/AU/XAU | Donchian channel breakout | FAIL | 0.69–1.28, 0 passes | – (pre-prereg; trials.csv) |
| 2_asian_mr | results/reports/2_asian_mr_*.md | 5 sym | Asian-range mean reversion | FAIL | 0.68–0.81, 0 passes | – |
| 3_session_bo | results/reports/3_session_bo_*.md | 5 sym | session breakout | FAIL | 0.89–1.26, 0 passes | – |
| 4_kaze | results/reports/4_kaze_*.md | 5 sym, M5/M1 | Kaze EMA9/21 M5 trend + M1 pullback cross (lookahead fixed) | FAIL | 0.80–0.95, 0 passes | – |
| 5_tsmom | results/reports/5_tsmom_*.md | 5 sym | time-series momentum | FAIL | 0.82–1.21, 0 passes | – |
| 6_fx_seasonality | results/reports/6_fx_seasonality_*.md | 4 FX | calendar seasonality | FAIL | 0.88–0.98, 0 passes | – |

## Track 2 — families 7–11 (summary: results/reports/TRACK2_SUMMARY.md, "0 of 24 pass")
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| 7_orb_tokyo | results/reports/7_orb_tokyo_*.md | 5 sym | Tokyo opening-range breakout | FAIL | PF 0.70–0.96 | – |
| 8_orb_frankfurt | results/reports/8_orb_frankfurt_*.md | 5 sym | Frankfurt ORB | FAIL | PF 0.91–1.00 | – |
| 9_fix_flow | results/reports/9_fix_flow_*.md | 5 sym | London-fix / month-end flow | FAIL | PF 0.59–1.04 | – |
| 10_xpair_residual | results/reports/10_xpair_residual_*.md | 4 FX | cross-pair residual reversion | FAIL | PF 0.71–0.85 | – |
| 11_news_shock | results/reports/11_news_shock_*.md | 5 sym | news-shock fade/follow | FAIL | PF 0.69–0.83 | – |

## Track 3 — Kai techniques (results/reports/track3/; prereg TRACK3_DEFINITIONS e563e30f, T06_T09_LOOSE 194b7e9b)
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| T01 SMC sweep | track3/T01_smc_sweep_REPORT.md | 5 sym | SMC/ICT liquidity sweep-reclaim | FAIL (CLEAR) | PF 0.73–0.80 | e563e30f |
| T06 AsiaBreak | track3/T06_asia_break_REPORT.md | 5 sym | Asia-range break + retest | FAIL (CLEAR) | PF 0.61–0.76 | e563e30f |
| T06 loose L1/L2/L3 | track3/T06_T09_LOOSE_REPORT.md | 5 sym | tol50 / Tokyo / no-prev variants | FAIL | PF 0.61–0.69; 0/35 pass (with T09) | 194b7e9b |
| T08 MultiTF | track3/T08_multitf_REPORT.md | 5 sym | multi-TF confluence | FAIL (CLEAR) | PF 0.70–0.82 | e563e30f |
| T09 VSA (+L1/L2/L3) | track3/T06_T09_LOOSE_REPORT.md; reports/T09_*.md | 5 sym | volume-spread analysis; vol12/body40/ext5 variants | FAIL | PF 0.57–0.72 | 194b7e9b |
| T15 Preda-v5 | track3/T15_preda_v5_REPORT.md | XAUUSD | Preda v5 rules | FAIL (CLEAR) | PF 0.86 | e563e30f |

## Track A / Track B (prereg TRACK_A_B_PREREG 7ee2d001)
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| Track A A1–A6 | results/reports/TRACKA_REPORT.md | 13 sym pooled, HTF | trend/breakout/momentum/carry pooled | FAIL (CLEAR) | PF 0.64–0.96, 0/6 | 7ee2d001 |
| Track B B1 ldn_mom | results/reports/B1_ldn_mom_EURUSD.md | EURUSD M5 | London momentum | FAIL | PF 1.08 | 7ee2d001 |
| Track B B2 range_bo | results/reports/B2_range_bo_USDJPY.md | USDJPY M5 | range-expansion breakout | **near-miss** | PF 1.28/1.20/1.13, n 996, DD −31%, 2023 neg, t 1.79 | 7ee2d001 |
| Track B B3 overnight | results/reports/B3_overnight_USDJPY.md | USDJPY M5 | overnight drift | FAIL | PF 1.07 | 7ee2d001 |
| Track B B4 rsi2 | results/reports/TRACKB_REPORT.md | FX M5 | RSI2 trend pullback | FAIL (IS gate) | – | 7ee2d001 |

## NYBO and REB family
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| NYBO M15/4h | results/reports/NYBO_M15_4h_prereg_REPORT.md | 5 new pairs M15 | NY 4h-range breakout | FAIL (CLEAR) | pooled PF 0.904; 0/5 pairs | 50729e0d |
| REB V1/V2/V3 | results/reports/USDJPY_REB_HTF_REPORT.md (+REB_V*_USDJPY.md) | USDJPY M5 | B2 REB + HTF filters | FAIL (CLEAR); **near-miss** V3/V2 | V3 PF 1.56 n 207; V2 PF 1.31 n 272 (<300) | 0792ebd5 |
| REB-H4 XPAIR | results/reports/REB_H4_XPAIR_REPORT.md | EU/GU/AU | REB-H4 cross-pair OOS | FAIL (CLEAR) | pooled n 895, PF 0.90 | ec2aecc3 |
| REB-H4 binary | results/reports/REB_H4_BINARY_FEASIBILITY.md | pooled | fixed-payout binary arithmetic | FAIL (not feasible) | Wilson LB 46.3% vs breakeven 53.5–55.6% | fe461e9a |
| REB-H4 XAU | results/reports/REB_H4_XAU_REPORT.md | XAUUSD | REB-H4 on gold | FAIL | n 382, PF 1.03/0.98/0.94, t 0.14 | eeadef45 |
| REB-H4 demo handoff | handoff/REB-H4/README.md | USDJPY | MQ5 EA + spec for Kai demo forward-test | demo only — **NOT a pass** | n 272, t 1.09 | – |

## XAU-named studies (each distinct study)
| short name | path | TF | method | verdict | key metric (after cost) | prereg |
|---|---|---|---|---|---|---|
| XAU_EMA55_PB | results/reports/XAU_EMA55_PB_REPORT.md | M5 | EMA55 pullback long/short | NO EDGE | n 1154, PF 0.69 (0.92 gross) | ba1f4a38 |
| XAU_EMA55_HTF | results/reports/XAU_EMA55_HTF_REPORT.md | HTF | EMA55 PB higher TF | NO EDGE | n 306, PF 0.93 | 0d74831b |
| XAU_SWINGBO + blind read | results/reports/XAU_BLINDREAD_SWINGBO_REPORT.md | M5/H1 | Kai swing-high breakout | NO EDGE | n 1026, PF 1.009, +0.003R | d05e0009 |
| XAU_SOX (v1/v2) | results/reports/XAU_SOX_REPORT.md | M5 | session-open expansion scalp | NO EDGE | v2 n 215, PF 0.70 | 5ff6f1bb / 41fce6b4 |
| XAU_ADR | results/reports/XAU_ADR_REPORT.md | D/M1 | daily-range exhaustion | FAIL / NO EDGE | n 1086, PF 0.92 | 22951dde |
| XAU_FUZZY | results/reports/XAU_FUZZY_REPORT.md | M5 | fuzzy-pattern scalp | NO EDGE | n 974, PF 0.75, −$0.33/tr | ecede349 |
| XAU_CLOSEBREAK_TP5 | results/reports/XAU_CLOSEBREAK_TP5_REPORT.md | M5 | close-break (engulf T1/T2), TP $5 | NO EDGE | −$0.24 to −$0.50/tr | – |
| XAU_SL2_TP5 | results/reports/XAU_SL2_TP5_REPORT.md | M5 | close-break SL $2/TP $5 | NO EDGE | win 31.5% vs BE 32.6% | – |
| XAU_ENGULF_MFE_MAE | results/reports/XAU_ENGULF_MFE_MAE_REPORT.md | M5 | MFE/MAE of close-break signals | vocab-only (descriptive) | – | – |
| XAU_ENGULF_20261015 | results/reports/XAU_ENGULF_20261015_REPORT.md | M5 | one-day engulf scan | vocab-only (descriptive) | – | – |
| XAU_SMC_STRUCT | results/reports/XAU_SMC_STRUCT_REPORT.md | M5 | fuzzy SMC structure continuation | NO EDGE | 0 variants net+ IS | – |
| XAU_SMC_STRUCT_HTF | results/reports/XAU_SMC_STRUCT_HTF_REPORT.md | H1/H4 | same, higher TF | NO EDGE | gross ≈ 0R; H4 n 86/39 t≈0.6 | – |
| XAU_HINDSIGHT_MINE | results/reports/XAU_HINDSIGHT_MINE_REPORT.md | M5 | hindsight pattern mine | LOOKAHEAD (IS); OOS NO EDGE | OOS hit 46.7–49.9%, −0.12 to −0.17R | – |
| XAU_BIAS_DEMO | results/reports/XAU_BIAS_DEMO_REPORT.md | M5 | deliberate bias demo | LOOKAHEAD (not a strategy) | honest PF 0.19 | – |
| Oracle daily range | REPORT_oracle_daily_range_xau_1m.md (= oracle_daily_range_xau_1m_REPORT.md) | D/M1 | perfect-foresight H−L | **LOOKAHEAD — NOT a strategy** (upper bound) | – | – |

## Other study folders
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| Engulf watch | engulf_watch/README.md, bt_week_20261017.md | XAU M5 | live engulf T1/T2 watcher + one-week BT | vocab-only (descriptive, 1 wk IS) | – | – |
| Engulf MAE/MFE | engulf_watch/maemfe/REPORT.md | XAU M5 | engulf T1/T2 SL/TP brackets from MAE/MFE | NO EDGE | 62,599 signals; gross ≈ 0, win 4–6 pts below BE | d35aa556 |
| Mae-pla | mae-pla/REPORT.md | XAU H1/H4 | Mae Pla Pak Ka Khiao book patterns | FAIL | OOS PF 0.87 (n 2762) / 0.97 (n 443); holdout 0.76 / 0.00 | 7b505ab5 |
| ACME full | acme-9step/REPORT_v1_toovague.md | XAU | ACME TRADERIST 9-step | TOO-VAGUE | – | – |
| ACME-8 entry-only | acme-9step/REPORT.md | XAU H4/D1 | user's 8 rules + fixed SL | FAIL | n 12, PF 0.27 | 776e7039 |
| SMC structure | smc_structure/REPORT.md, EXEC_SUMMARY.md | XAU | SMC vocabulary (swings/BOS/CHoCH/OB/FVG) | vocab-only | – | – |
| SMC week H1 | smc_structure/week_20261026/ | XAU H1 | weekly structure count | SUPERSEDED (SUPERSEDED.txt) | – | – |
| SMC week M1 | smc_structure/week_20261026_m1/EXEC_SUMMARY.md | XAU M1 | SELL packages + H1 candles | vocab-only (NOT an edge) | 6 packages, 5 went with sell | – |
| CHoCH (archive) | NOTES.md §CHoCH → /workspace/choch-research (ct/backend-choch) | XAU M5 BID | CHoCH + 62% retrace limit, 2R | FAIL (≈ breakeven; first 70% negative) | S25: −0.095R / +0.03R; 1 yr data | locked defs (archive) |
| xau_research (archive) | NOTES.md §Prior XAUUSD → /workspace/xau_research/REPORT.md | XAU M1 | 888 rule combos + LightGBM | NO EDGE | median PF ≈ 1.01 | – |

## Prereg → report match
All 15 prereg/*.md have a matching report: NYBO→NYBO report; TRACK3_DEFINITIONS→track3/*; T06_T09_LOOSE→T06_T09_LOOSE_REPORT; TRACK_A_B→TRACKA/TRACKB; USDJPY_REB_HTF; REB_H4_XPAIR/BINARY/XAU; XAU_EMA55_PB(+HTF); XAU_SWINGBO→BLINDREAD_SWINGBO; XAU_SOX(+V2)→XAU_SOX_REPORT; XAU_ADR; XAU_FUZZY. Folder preregs: engulf_watch/maemfe/MAEMFE_PREREG.md, mae-pla/prereg_MAEPLA.md, acme-9step/prereg_hash.txt.

## Classic candle patterns — NEVER a dedicated standalone study
| pattern | dedicated study? | note |
|---|---|---|
| **Pin bar / hammer / shooting star** | YES (2026-10-29) | classic_candles/ — FAIL / NO EDGE (was NEVER before this study; mae-pla PAT1 alone did not count) |
| **Doji** | YES (2026-10-29) | classic_candles/ — FAIL / NO EDGE |
| **Inside bar** | YES (2026-10-29) | classic_candles/ — FAIL / NO EDGE |
| **Morning star / evening star** | YES (2026-10-29) | classic_candles/MES_REPORT.md — FAIL / NO EDGE (was NEVER before this study) |
| Engulfing | YES | engulf_watch, maemfe (NO EDGE), XAU_CLOSEBREAK_TP5 / SL2_TP5 (NO EDGE), MFE_MAE + 2026-10-15 scan (descriptive) |

## Classic candles study (Track B, 2026-10-29) — DONE after catalog
| short name | path | symbol/TF | method | verdict | key metric | prereg |
|---|---|---|---|---|---|---|
| Classic pin/inside/doji | classic_candles/REPORT.md | XAUUSD M5 | Pin V0/V1, inside bar, doji; hit-rate horizons + MFE/MAE; 1R:1R & ATR exits after $0.28 cost | **FAIL / NO EDGE** (all 4 sets) | hold PF E1 0.77–0.83, E2 0.84–0.86; hit≈50%; MFE≈MAE ~$3.5 | fbbf03ee… (CLASSIC_CANDLES_PREREG) |
| Classic EXEC | classic_candles/EXEC_SUMMARY.md | — | short summary | FAIL | 12 trials added; N_TRIALS now 937 | frozen fc8de240… |

| Morning/evening star | classic_candles/MES_REPORT.md | XAUUSD M5 | MES_V0 (no filter), MES_V1 (EMA5 prior-trend); 3-bar star, midpoint-substitute for gap | **FAIL / NO EDGE** (both sets) | hold PF E1 0.76–0.79, E2 0.79–0.80; hit≈49%; MFE≈MAE ~$3.5 | 665bca26… (MORNING_EVENING_STAR_PREREG) |
| MES EXEC | classic_candles/MES_EXEC_SUMMARY.md | — | short summary | FAIL | 6 trials added; N_TRIALS now 943 | frozen 37a71cc2… |

All classic candle patterns in this catalog (pin, doji, inside, morning/evening star, engulfing) have now been studied: all NO EDGE.
| Combo MTF (H1 EMA55 bias + M5 PIN/ENGULF ± RSI14) | combo_mtf/REPORT.md | XAUUSD M5/H1 | PIN_F0/F1, ENGULF_F0/F1 × E1/E2 | **FAIL / NO EDGE** (all 4) | hold PF 0.72–0.85; hit≈50%; stacking did not help | c4a31bd3… (COMBO_MTF_PREREG) |
| xau_m1_edge_20261030 | xau_m1_edge_20261030/report.md | XAU M1 | 25 human-behavior hyps (sweep/exhaustion/session-open/MR), SL3.5 TP1.5R, $0.65 cost | FAIL (NO EDGE) | OOS PF 0.47–0.83, 0/25 pass | xau_m1_edge_20261030/PREREG.md |
| xau_m1_edge_20261030_cost028 | xau_m1_edge_20261030_cost028/report.md | XAU M1 | same 25 hyps, $0.28 cost | FAIL (NO EDGE) | best OOS PF 1.02 (PDL fake, n=253, sens fail), 0/25 pass | PREREG_COST028.md |
| xau_m5_edge_20261030_cost028 | xau_m5_edge_20261030_cost028/report.md | XAU M5 | same 25 hyps, M5 thresholds, $0.28 cost | FAIL (NO EDGE) | best OOS PF 1.09 (LDN FVG, n=350, sens fail), 0/25 pass | xau_m5_edge_20261030_cost028/PREREG.md |
| xau_m15_edge_20261030_cost028 | xau_m15_edge_20261030_cost028/report.md | XAU M15 | same 25 hyps, M15 thresholds, $0.28 cost | FAIL (NO EDGE) | best OOS PF 1.13 (Asia drive, n=171, sens fail), 0/25 pass | xau_m15_edge_20261030_cost028/PREREG.md |
| xau_h1_edge_20261030_cost028 | xau_h1_edge_20261030_cost028/report.md | XAU H1 | same 25 hyps, H1 thresholds, SL3.5 TP1.5R, $0.28 cost | FAIL (NO EDGE) | best OOS PF 1.17 (EQL sweep, n=85, sens fail), 0/25 pass | xau_h1_edge_20261030_cost028/PREREG.md |
| ic_mt5_xau_edge_20261030 | ic_mt5_xau_edge_20261030/report.md | XAU M5+M1 (IC MT5 BID) | same 25 hyps, $0.28, IS60/OOS40 | FAIL (NO EDGE) | best n>150 OOS PF M5 0.86 / M1 0.97, 0/50 pass; +COVERAGE.md, DEALS_SUMMARY.md | ic_mt5_xau_edge_20261030/PREREG.md |
| 2026-10-31 | m5_shape_edge_overnight_20261031 | XAUUSD M5 3–5 bar shape clusters+codes, 370 patterns/360 BT | **ไม่เจอ** — 0 pass, median OOS PF 0.76 | m5_shape_edge_overnight_20261031/exec_run_A_7030/EXEC_SUMMARY.md (run A; a parallel 60/40 prereg run may exist in the root of the same folder) |
| m5_shape_edge_overnight_20261031 | m5_shape_edge_overnight_20261031/HANDOFF_FOR_10AM.md | XAU M5 IC MT5 | shape clusters w3-5 sim .85/.90 + bar-sequences, $0.28 | FAIL (ไม่เจอ) | A 0/360, B 0/440; B best OOS PF 1.19 n=163 sens fail | m5_shape_edge_overnight_20261031/PREREG.md |
