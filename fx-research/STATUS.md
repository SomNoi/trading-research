# fx-research STATUS (Track A + USDJPY REB done 2026-10-11 ~14:28 ICT; no finalists)

## Data (read-only for reuse)
- **Dukascopy M1, mid prices** (`data/{SYM}_M1.parquet`):
  - UTC index; columns open/high/low/close (mid), spread_o, spread_c, volume.
  - Zero-volume bars are dropped. Coverage notes are in `data/{SYM}_coverage.json`.
  - EURUSD, GBPUSD, USDJPY, AUDUSD, XAUUSD: 2019-01-01 → 2025-10-09 23:59 UTC. Older runs downloaded raw data up to 2026-10-09 for these five, but every script truncates at the holdout on load.
  - EURJPY, GBPJPY, AUDJPY, USDCAD, USDCHF: 2019-01-01 → 2025-10-09 (downloaded with END=2025-10-10).
- **Raw monthly bid/ask files**: `data/raw/{SYM}/{bid,ask}_YYYY-MM.parquet`. They are merged by `scripts/build_data.py SYM...`.
- **NZDUSD / EURGBP / EURCHF**: DONE (2026-10-11 ~14:25 ICT by dr eggbot).
  - Fetcher had crashed on EURCHF (None row); patched `scripts/fetch_dukascopy2.py` and resumed. Log `results/fetch_eurchf_resume.log`.
  - Built with `.venv/bin/python scripts/build_data.py NZDUSD EURGBP EURCHF` → `data/{SYM}_M1.parquet` + coverage JSON through 2025-10-09.
- **H1 cache**: `data/htf/{SYM}_H1.parquet` for the original 10 symbols (pre-holdout). The 3 new symbols get H1 cache when Track A runs.
- **Rates**: `data/rates/IR3TIB01{US,EZ,GB,JP,AU,CA,CH,NZ}M156N.csv`. These are FRED OECD 3-month interbank rates, used for Track A's rate-based swaps.
- **IC MT5 export**: `data/ic-mt5-2026-10-10/` (true UTC; BID OHLC; spread in points, 0 = missing). It may be used only for the price-difference check (`results/dukascopy_vs_ic.md`) or as a cross-check inside a finalist's one-time holdout. Never use it for selection.
- **Kai demo deals**: `data/kai-demo/deals_52946518_alltime_20261011.csv` (inside the holdout; descriptive analysis only).
- **HOLDOUT**: `engine.HOLDOUT_START = 2025-10-10 UTC`. It has never been loaded in any backtest (the IC export is the only exception, as above). `results/HOLDOUT_USED_NYBO` does not exist.

## Engine and how to run
- **Python**: venv at `/workspace/fx-research/.venv` (system site-packages plus pyarrow and numba). Run with `.venv/bin/python` from `/workspace/fx-research`.
- **`scripts/engine.py`**:
  - Cost model; `load_m1`; `resample`; `atr`/`ema`.
  - `run_sim(sym, bars, sig, stop_entry, exitL, exitS)`:
    - Numba simulator, sequential (one position at a time).
    - SL is checked before TP; gaps fill at the open.
    - `sig` columns: ent_idx, ent_px, dir, sl, tp, tx.
  - `net_R`, `metrics`, `wf_windows` (IS 24 months / OOS 6 months, 10 non-overlapping OOS windows 2021-01..2025-10-09), `walk_forward` (picks the param with the best IS t-stat).
- **Strategy modules**:
  - `strategies.py`: families 1–6.
  - `strategies2.py`: Track 2 (families 7–11).
  - `strategies3.py`: Kai techniques T01/T06/T08/T15, the T06 loose variants and T09 with its variants.
  - `trackB.py`: B1–B4 with the IS gate.
  - `trackA.py`: A1–A6 pooled across 13 symbols. Written and smoke-tested on EURJPY; the full run was NOT started.
- **Runners**:
  - Walk-forward: `.venv/bin/python scripts/run_wf.py SYM... --strategies NAME,...`. Writes `results/wf`, `results/trades`, `results/regimes` and appends to `results/trials.csv`.
  - Reports: `.venv/bin/python scripts/analyze.py` writes `results/reports/{strat}_{SYM}.md`, `results/ranked_oos.csv` and `results/multiple_testing.json`.
  - Example: `FLEET_TASK=my-task nohup .venv/bin/python scripts/run_wf.py EURUSD --strategies 1_donchian > results/x.log 2>&1 &`
- **STOP convention**: create `/workspace/fx-research/STOP` to stop jobs.
  - Every runner checks it between steps, and the fetcher checks it before every request.
  - It is SHARED by the fetcher and the backtests, so to stop only a backtest, kill that backtest's PID instead.
  - Delete the file before restarting.
- **Fleet events**: `scripts/fleet.py`. Use `fx(type, summary, **kw)`. Events append to `/workspace/fleet/events/fx-research.jsonl`.

## Cost model
- **Source**: `IC_COSTS_FROM_KAI_20261011.md`, applied in `engine.py`.
- **Spreads**: p90 points by session.
  - asia 00–07, london 07–12 and NY 12–16 UTC use the file's values.
  - ny_late 16–20:30 is 1.5 × NY.
  - Rollover 20:30–24 and weekends use the weekend-close spread.
  - Half the spread is charged at entry and half at exit.
- **Pairs not in Kai's file** use proxy p90 spreads (points): EURJPY 7, GBPJPY 13, AUDJPY 8, USDCAD 5, USDCHF 7, NZDUSD 8, EURGBP 8, EURCHF 10. ny_late is 1.5× and rollover 15×.
- **Commission and slippage**: $3.50/lot/side ($7 RT), converted to quote currency. Slippage is 0.1 pip per side ($0.05 on XAU). Sensitivity is run at 1x / 1.5x / 2x via `net_R(mult)`.
- **Swaps**:
  - Kai's file for the five originals.
  - ic.com/eu values for EURJPY, GBPJPY, AUDJPY, USDCAD, USDCHF.
  - Counted per NY 17:00 rollover, with Wednesday ×3.
  - Track A instead uses rate-based swaps from FRED rates with a 1.5% markup.
- **Execution rules**: entries are blocked 20:30–24:00 UTC and on Saturday/Sunday. Minimum stop is 5 pips on FX and $1 on XAU; tighter stops are widened and TP is scaled to match.

## Trial log, multiple testing, prereg
- **Trial log**: `results/trials.csv`, one row per parameter set and symbol (Track A pooled systems: one row per pooled set). `analyze.py` de-duplicates rows and adds 37 pilot trials.
- **Multiple testing**: `results/multiple_testing.json` currently shows N_TRIALS = 584 and a Bonferroni t threshold of 3.76. It also holds the variance inputs for the deflated Sharpe. The DSR is computed per candidate by `analyze.py`.
- **Prereg**:
  - Specs go in `prereg/*.md`, written before testing.
  - Each file's sha256 and UTC timestamp are appended to `results/prereg_hashes.txt`, and the file is then made read-only (chmod a-w).
  - Files: NYBO_M15_4h_PREREG, TRACK3_DEFINITIONS, T06_T09_LOOSE_PREREG, TRACK_A_B_PREREG.

## Results so far (all: 0 passes of the full bar)
- `REPORT.md`: top-level report and addendum.
- `results/reports/`: per-candidate reports; also NYBO_M15_4h_prereg_REPORT.md, TRACK2_SUMMARY.md and TRACKB_REPORT.md.
- `results/reports/track3/`: T01, T06, T08, T15 and T06_T09_LOOSE.
- `results/kai_demo_analysis.md`, `results/dukascopy_vs_ic.md`.

## Unfinished
- **T06/T09 loose variants**: DONE. 0 of 35 pass.
- **Track B (M5 low-cost FX)**: DONE.
  - 3 of 12 system/symbol candidates passed the IS gate; 0 pass the full bar.
  - Near-miss: USDJPY B2, PF 1.28 / 1.20 / 1.13, 996 trades, DD −31%, 2023 negative.
- **Track A (higher-TF pooled)**: DONE 2026-10-11 ~14:28 ICT. CLEAR FAIL. 0 of 6 pooled systems pass (PF 0.64–0.96). No holdout. Report: `results/reports/TRACKA_REPORT.md`.
- **USDJPY REB + HTF filters**: DONE 2026-10-11 ~14:27 ICT. CLEAR FAIL. No finalist; holdout unused. Near-misses: V3 PF 1.56 n=207; V2 PF 1.31 n=272 (both fail ≥300). Report: `results/reports/USDJPY_REB_HTF_REPORT.md`.
- **IC re-run of finalists**: none, because there are no finalists. `scripts/nybo_prereg_test.py icdata` can read the IC export and refuses holdout-period data unless authorised.

## Update 2026-10-11 18:21 ICT: REB-H4 follow-ups
1. **Cross-pair OOS** (prereg REB_H4_XPAIR_PREREG.md, sha ec2aecc3): CLEAR FAIL.
   - Pooled EURUSD/GBPUSD/AUDUSD: n 895, PF 0.90, DD −98%.
   - The holdout was not run. Report: results/reports/REB_H4_XPAIR_REPORT.md.
2. **Demo handoff** in handoff/REB-H4/: SPEC.md, REB_H4.mq5 (not compiled, self-reviewed), signals_check.csv (matches the backtest), README.md.
3. **Binary feasibility** (prereg REB_H4_BINARY_PREREG.md, sha fe461e9a): NOT feasible.
   - Best pooled Wilson lower bound 46.3%, vs breakevens of 53.5–55.6%.
   - Report: results/reports/REB_H4_BINARY_FEASIBILITY.md.
- Trials 640; Bonferroni t 3.78. All holdouts are still unused.

## Update 2026-10-11 20:40 ICT: REB-H4 on XAUUSD (prereg REB_H4_XAU_PREREG.md, sha eeadef45)
- **FAIL:** n 382, PF 1.026 / 0.979 / 0.935, max DD −23.7%, 4/7 years positive, t 0.14. The holdout was NOT run.
- **IQ check:** the best Wilson LB is 43.7%, below every breakeven.
- Trials: 645; Bonferroni threshold t = 3.78.
- Report: results/reports/REB_H4_XAU_REPORT.md.

## Update 2026-10-15 11:30 ICT: XAU EMA55 pullback (prereg XAU_EMA55_PB_PREREG.md, sha ba1f4a38)
- **Verdict: NO EDGE.**
- **WF OOS:** n 1154, PF 0.69 at 1x, 0.92 gross. All 72 variants are negative after costs.
- **Holdout:** not run.
- **Trials:** 717; Bonferroni threshold t = 3.81.
- **Report:** results/reports/XAU_EMA55_PB_REPORT.md.
- **Reference example:** blocked by the 20:30–24:00 UTC entry block. With the block off it is flagged when X ≥ $0.30.
- **.venv:** missing again; recreated per the install checklist.

## Update 2026-10-15 11:40 ICT: XAU EMA55 HTF follow-up (prereg XAU_EMA55_PB_HTF_PREREG.md, sha 0d74831b)
- **Verdict: NO EDGE.**
- **WF OOS:** n 306, PF 0.93 at 1x (1.005 gross), DD −43.7R.
- **Cost drag:** costs per trade fell from about 0.17R to about 0.04–0.11R, but there is still no gross edge.
- **Rollover block:** keep it.
- **Holdout:** not run.
- **Trials:** 749; Bonferroni threshold t = 3.82.
- **Report:** results/reports/XAU_EMA55_HTF_REPORT.md.

## Update 2026-10-15 12:25 ICT: blind read + Kai swing-breakout (prereg XAU_SWINGBO_PREREG.md, sha d05e0009)
- **Swing breakout: NO EDGE.** WF OOS n 1026, PF 1.009 at 1x (1.21 gross), +0.003R per trade, DD −21.9R. The holdout was not run.
- **Blind read** (not truly blind): mechanical WAIT. Kai's plan would have hit its TP for +1.26R.
- **Trials:** 761; Bonferroni threshold t = 3.82.
- **Report:** results/reports/XAU_BLINDREAD_SWINGBO_REPORT.md.

## Update 2026-10-15 13:50 ICT: XAU session-open expansion scalp (prereg XAU_SOX 5ff6f1bb + amendment XAU_SOX_V2 41fce6b4)
- **Verdict: NO EDGE.**
- **v1:** degenerate. Only 5 windows qualified, because the quiet test used the continuous ATR.
- **v2** (quiet test vs prior-day ATR): WF OOS n 215, net −$0.53/oz per trade (gross −$0.25, cost $0.28), PF 0.70. All 20 variants are negative before costs.
- **Holdout:** not run.
- **Trials:** 801; Bonferroni threshold t = 3.84.
- **analyze.py:** now skips empty OOS files.
- **Report:** results/reports/XAU_SOX_REPORT.md.

## 2026-10-15 XAU ADR daily-range (prereg 22951dde): FAIL / NO EDGE
Part 1: only 36.8% of days within ±20% of ADR14; E≈ADR−X is worse than a constant 0.25×ADR baseline. Part 2: WF OOS n1086, PF 0.92/0.88/0.84, −104R DD, 1/5 years positive. N_TRIALS 819. Report results/reports/XAU_ADR_REPORT.md. Holdout unused.

## 2026-10-16 BIAS DEMO (deliberately biased, not a strategy): biased +$33.4/0.01lot vs honest -$128 (PF 0.19); OOS -$50. 2 BIAS_DEMO trials; report results/reports/XAU_BIAS_DEMO_REPORT.md

## 2026-10-16 XAU FUZZY (prereg ecede349): NO EDGE. 96 IS configs all net<0 on 2022 val; finalist OOS 974 tr, net -$0.33/tr, PF 0.75, all years neg. N_TRIALS 917. Holdout unused.


## CREDIT PAUSE 2026-10-31 ~17:10 ICT
Hunt stopped at R191 / N_TRIALS 5698. See HANDOFF_CREDIT_PAUSE_20261031.md. No new rounds until resume.
