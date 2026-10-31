# RECOVERY.md — workspace wipe 2026-10-31 ~14:15 ICT

Written: 2026-10-31 14:17 ICT by FX-Research after wipe + dr eggbot restore authorization.

## What happened
- Mid-hunt, `/workspace/fx-research/` lost most late round folders, IC MT5 CSV tree (`data/ic-mt5-2026-10-10/`), scripts/engine.py, and `.venv`.
- Early standing-order report folders (≈R3–R12) + INDEX/CATALOG/multiple_testing.json survived or were restored from GitHub tip `d03cd3a`.
- Drive had **no** `ic-mt5-2026-10-10` zip. ea-lab `XAUUSD_M5.csv` is Yahoo GC=F proxy — **not used**.

## Data restore (ACTIVE FEED for R33+)
- Source file: `data/XAUUSD_M1.parquet` (2755872 M1 bars, 2019-01-01 → 2026-10-09 UTC).
- Coverage (`data/XAUUSD_coverage.json`) labels series as **raw bid** aggregation (Dukascopy-family), **≠ IC Markets BID**.
- Rebuilt M5: `data/from_parquet_m1/XAUUSD_M5.csv` — **551494** bars.
- SHA256(M5 CSV): `b4f61d541ef82297245bb8befb708871d37a607992e5a3149fe0d968e4e7d114`
- Label required on every new PREREG/REPORT/EXEC: **SUBSTITUTE mid/bid Dukascopy-family ≠ IC BID**. Cost still $0.28/0.01 lot RT.
- USDJPY: `data/raw/USDJPY/` bid/ask month parquets present if needed for cross-asset rounds.

## Scoreboard R1–R33 (presence after recovery)
| R | folder | method | disk | verdict (prior) |
|---|---|---|---|---|
| 1 | `m5_motif5_novel_20261031` | 5-bar motif hindsight | LOST | ไม่เจอ |
| 2 | `xau_h1_m5_structure_20261031` | H1 BOS/CHoCH + M5 | LOST | ไม่เจอ |
| 3 | `xau_m5_session_open_imb_20261031` | session open imb | PRESENT | ไม่เจอ |
| 4 | `xau_m5_session_vwap_band_20261031` | session VWAP bands | PRESENT | ไม่เจอ |
| 5 | `xau_m5_atr_regime_lib_20261031` | ATR regime libraries | PRESENT | ไม่เจอ |
| 6 | `xau_m5_tickvol_climax_20261031` | tickvol climax (NR superseded) | PRESENT | ไม่เจอ |
| 6 | `xau_m5_nr_breakout_20261031` | NR-K breakout (pre-pivot) | PRESENT | ไม่เจอ |
| 6 | `xau_m5_composite_q4_ldn_20261031` | composite Q4+LDN | PRESENT | ไม่เจอ |
| 7 | `xau_m5_tod_calendar_20261031` | TOD calendar | PRESENT | ไม่เจอ |
| 8 | `xau_m5_h4_ema_pullback_20261031` | H4 EMA pullback | PRESENT | ไม่เจอ |
| 9 | `xau_m5_close_streak_20261031` | close streak | PRESENT | ไม่เจอ |
| 10 | `xau_m5_feature_stump_20261031` | feature stump | PRESENT | ไม่เจอ |
| 11 | `xau_m5_usdjpy_residual_20261031` | USDJPY residual | PRESENT | ไม่เจอ |
| 12 | `xau_m5_parkinson_div_20261031` | Parkinson divergence | PRESENT | ไม่เจอ |
| 13 | `xau_m5_corr_regime_20261031` | corr regime | PARTIAL | ไม่เจอ |
| 14 | `xau_m15_clv_mr_20261031` | M15 CLV MR | LOST | ไม่เจอ |
| 15 | `xau_m5_range_pos_mr_20261031` | range position MR | LOST | ไม่เจอ |
| 16 | `xau_m5_mom_persist_20261031` | momentum persistence | LOST | ไม่เจอ |
| 17 | `xau_m5_overnight_gap_20261031` | overnight gap | LOST | ไม่เจอ |
| 18 | `xau_m5_bb_squeeze_20261031` | BB squeeze | LOST | ไม่เจอ |
| 19 | `xau_h1_orb_london_20261031` | H1 London ORB | LOST | ไม่เจอ |
| 20 | `xau_m5_rsi2_mr_20261031` | RSI2 MR | LOST | ไม่เจอ |
| 21 | `xau_m5_dual_tf_rsi_20261031` | dual TF RSI | LOST | ไม่เจอ |
| 22 | `xau_m5_keltner_squeeze_20261031` | Keltner squeeze | LOST | ไม่เจอ |
| 23 | `xau_m5_macd_cross_20261031` | MACD cross | LOST | ไม่เจอ |
| 24 | `xau_m5_stoch_cross_20261031` | Stochastic cross | LOST | ไม่เจอ |
| 25 | `xau_m5_daily_pivot_20261031` | daily pivots | LOST | ไม่เจอ |
| 26 | `xau_m5_supertrend_20261031` | Supertrend | LOST | ไม่เจอ |
| 27 | `xau_m5_ichimoku_tk_20261031` | Ichimoku TK | LOST | ไม่เจอ |
| 28 | `xau_m5_round_number_20261031` | round numbers | LOST | ไม่เจอ |
| 29 | `xau_m5_adx_di_20261031` | ADX DI | LOST | ไม่เจอ |
| 30 | `xau_m5_cci_extreme_20261031` | CCI extreme | LOST | ไม่เจอ |
| 31 | `xau_m15_ema_ribbon_20261031` | M15 EMA ribbon | LOST | ไม่เจอ |
| 32 | `xau_h1_donchian_20261031` | H1 Donchian | LOST | ไม่เจอ |
| 33 | `xau_m5_heikin_ashi_20261031` | Heikin Ashi streak | RUNNING | (in progress) |

## N_TRIALS
- Restored `results/multiple_testing.json` ends at **N_TRIALS=2930** (through R12 / Parkinson notes).
- Pre-wipe claim was ~3250 after R32. Difference ≈ R13–R32 trial adds — **not reconstructed into JSON** (no invented OOS metrics).
- R33+ will continue incrementing from restored 2930.

## Policy (dr eggbot)
- Do **not** mass re-run R13–R32.
- Append INDEX rows for lost rounds as ไม่เจอ path-only (no fabricated PF/n).
- Resume hunt R33+ on parquet M5 SUBSTITUTE; prefer IC re-export later if it reappears.
- R1–R32 remain ไม่เจอ (prior IC or prior local runs).

## Recovered from GitHub
- Tip `d03cd3a` / SomNoi/trading-research: INDEX, CATALOG, R1–R12-ish EXEC/PREREG/report files.
- Notion digest R1–R12 still valid for human summary.

