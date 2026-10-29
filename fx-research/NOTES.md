# fx-research NOTES (started 2026-10-11, ICT)

Research/backtest only. No trading, no MT4/MT5/cTrader install, no broker login.
Install checklist (/home/box/agent-data/workflows/bot-install-checklist/SKILL.md) followed: disk 126G total / 108G free (10-11% used);
web layer (443) OK to pypi.org + freeserv.dukascopy.com. Installed only Python libs (pyarrow, numba) into a private venv
/workspace/fx-research/.venv (--system-site-packages; ~0.2 GB) so the shared system Python is untouched. No trade ports needed.

## Step 1 - Prior work (archive /workspace/bot-archive-20261011, read 2026-10-11)
Files read: INDEX.md; JOBS.md of nick-fury, forex-xauusd (ฟอเร็กซ์/Aura), jarvis, architect/backend/adversary/tool-runner/ux (code-team);
forex-xauusd automations/*.json + memory; nick + jarvis memory logs; /workspace/ea-lab-v0/scan_kaze_yahoo.py;
/workspace/code-team/{RESEARCH.md,decisions.tsv,tasks.json}; /workspace/choch-research (branch ct/backend-choch, reports/);
/workspace/xau_research/REPORT.md + ic_costs.py.

### Kaze definition (as actually coded in the archive)
Source: /workspace/ea-lab-v0/scan_kaze_yahoo.py (Forex bot "Gold/Aura", 2026-09-06), also Nick memory: "M5 Trend + M1 Pullback + EMA Cross
Confirmation (+ SMC/CHoCH/OB as context only)".
- EMA9 / EMA21 on both M5 and M1 closes.
- M5 trend up = EMA9>EMA21 on the last 3 M5 bars (down = mirror).
- M1 trigger long = EMA9 crosses above EMA21 on this M1 bar AND M5 trend up AND pullback: any of the previous 8 M1 bars had low < EMA9 (short mirror: high > EMA9).
- EA v0 risk params locked in EA Lab (2026-09-05): lot 0.01, SL 200 points, TP 400 points (1:2), max 2 positions, no daily loss breaker.
  On XAUUSD (2-digit) 200 points = $2.00, TP = $4.00.
- NOTE: the archive scanner joined each M1 bar to the M5 bar whose OPEN time <= M1 time, i.e. the still-forming M5 bar (up to 4 min lookahead).
  This repo fixes it: only M5 bars CLOSED at/before the M1 bar close are used.
- Kaze was never backtested with PnL in the archive: only a 152-signal list (Yahoo GC=F futures, ~28 Aug-5 Sep 2026, 1 week, M1 ~5 days).
- On 2026-09-06 the user switched the gold alerts AWAY from Kaze to SMA55 x SMA400 on M1 (TradingView OANDA:XAUUSD) + H1 engulfing; both routines paused since 13 Sep.
- "Kaze" is ALSO the name of the home-PC Hermes agent (separate from the trading system) - don't confuse.

### Prior XAUUSD results (xau_research, Dukascopy M1 mid, 2024-01 -> 2026-09, report 2026-10-04)
- 888 rule combos (8 trend filters x 14 entries x 8 exits) + LightGBM. Median PF before cost ~1.01 => essentially no edge.
- Pass criterion (PF>=1.10 on both test May-Sep 2026 and holdout 2024) at cost $0.35/oz: 0 strategies; at IC costs $0.14/0.19/0.20/0.25: 0 strategies.
- Best "near miss": H4 EMA50/200 filter + Kaze (their variant: M5 EMA20>50 + M1 pullback to EMA50 within 10 bars + M1 EMA9/21 cross),
  SL 2xATR14(M5) + 1R trail, max hold 8h: PF 2024/2025/val/test = 1.04/1.14/1.13/1.07 at $0.20 cost; ~+0.03-0.05R/trade; edge ~0 at $0.25+.
- Profits almost entirely from LONG side (2024 long PF ~1.17, short ~0.70) => gold bull-market beta, not skill.
- Tight stops (1xATR) lose: cost eats 0.1-0.3R/trade. London breakout of Asia range: PF 1.41 in 2025, 0.60-0.71 in 2026 (regime-specific).
  NY ORB: few trades, unstable. VWAP revert / M1 spike fade: PF<1. LightGBM overfit (train PF 1.36 -> test 1.02, 2024 0.93).

### CHoCH (code-team T19/T20, 2026-10-05; /workspace/choch-research branch ct/backend-choch)
- Definition locked before results: XAUUSD M5 (Dukascopy BID 2025-10-01..2026-09-30), fractal 3/3 swings, HH+HL / LH+LL structure,
  CHoCH = close beyond last confirmed swing against the structure; limit entry at 62% retrace of impulse, valid 24 bars;
  SL = origin -/+ $0.20; TP = 2R; ambiguous bars = SL. Spread S = 6/12/25 points (no commission).
- Results (fills, %TP; breakeven at 2R = 33.3%):
  S6:  first70% 527 fills, 31.5% TP (-29R => -0.055R/trade); last30% 203 fills, 36.0% TP (+16R => +0.08R/trade)
  S25: first70% 524 fills, 30.2% TP (-50R => -0.095R/trade); last30% 204 fills, 34.3% TP (+6R => +0.03R/trade)
  => around breakeven, first 70% negative; ~5.5 CHoCH/day; median R = -1. Adversary passed the code (no lookahead found).
  Open question in archive: user never answered "compute net P/L?". Only 1 year of data.

### Other lessons (Nick / Jarvis / Forex)
- Broker feed: MT5 via Wine installed then removed (~2.4 GB) because IC Markets trade/feed ports are blocked on this box => use Dukascopy/Yahoo/CSV.
  Yahoo GC=F is a FUTURES contract (contango offset vs spot) and only ~5 days of M1 - not usable for multi-year M1 research.
- Drive "TradingSystem_v5"/XAUUSD_EA.mq5 backtest was bogus (WR 92.6%, equity ~1e244, avg_bars=1) => sanity-check equity curves and bars-held.
- Kai's XAUUSD lab "EMA50_MG_v1": H4 EMA50 filter improved an 814-trade backtest from -210.59 to +22.42 (thin), then a x2.1 MARTINGALE
  reset after 5 losses (lot 0.01->0.19) was layered on top - martingale does not create edge; treat as a risk red flag.
- IQ Option binary-option work (roundfade5 etc.) is a different product (fixed payout) - not reused here. demo_bot P/L file (+$51.46)
  disagreed with the actual account (-$17.80) => reconcile backtest/journal against broker statements.
- Archive data issues: Dukascopy 1m files contain zero-volume filler bars during closures (drop them); holiday gaps (US Thanksgiving,
  Christmas, Juneteenth, July 4: gold stops ~17:00-19:30 UTC); one weekday with no XAU data (2026-04-03, Good Friday);
  Dukascopy XAU spread ~$0.25-0.70 is far wider than IC Raw; previous downloads hit transient errors/429 -> throttle + resume.

## Step 2 - Data (done 2026-10-11)
- Dukascopy M1 BID+ASK, 2019-01-01 22:00 -> 2026-10-09 20:59 UTC, 5 symbols, ~2.76-2.89M M1 bars each (data/*_M1.parquet, raw monthly in data/raw/).
- Downloaders: scripts/fetch_dukascopy.py (dukascopy-python; it hung with no timeout after ~45% and hit HTTP 429 when 5 ran in parallel) ->
  scripts/fetch_dukascopy2.py (sequential, 2 s throttle, 30s->900s backoff, 90 s hard deadline per request, STOP-aware, resumable). Final run: 0 x 429.
- Cleaning: scripts/build_data.py (inner-join bid/ask, mid OHLC, spread_o/spread_c, drop zero-volume bars). Gaps are in data/*_coverage.json.

## Cost model history
- v1 (morning): IC public pages. Raw MT $3.50/side ($7 RT): icmarkets.com/global/en/trading-accounts/overview (also lists new Raw Pro $1.5/side with $5k minimum, Raw Pro+ $1.0/side with $100k minimum).
  Spread table at icmarkets.com/global/en/trading-pricing/spreads looks inconsistent for majors (Raw avg 0.01-0.04 vs headline "EURUSD avg 0.1 pips").
  ic.com/eu spreads-and-swaps shows Raw avg EURUSD 0.06, GBPUSD 0.26, USDJPY 0.22, AUDUSD 0.10, XAU $0.08, plus swaps. Checked 2026-10-11. Results in results/old_costv1/ (superseded).
- v2 (current): IC_COSTS_FROM_KAI_20261011.md (broker demo probe), p90 spreads. See scripts/engine.py and REPORT.md.

## Step 3 - Results: see REPORT.md, results/ranked_oos.csv, results/reports/*.md, results/trials.csv, results/robust_usdjpy_nybo.csv.
Caveat: the archive's xau_research and CHoCH work already looked at XAU 2024-2026, which overlaps the reserved holdout. Any XAU idea that came from that work is
not fully holdout-clean.

## 2026-10-11 follow-ups
- Fixed a Track-2 crash in fix_flow (tz-naive month-end) by using a cumcount-based last-2-business-days flag. analyze.py de-duplicates trials on (phase, strategy, symbol, param).
- IC MT5 export:
  - No time shift.
  - IC bid sits between Dukascopy bid and mid: +0.15 to +0.40 pip vs bid, −0.12 to −0.23 vs mid; XAU +$0.26 vs bid, −$0.04 vs mid.
  - Outliers are at the 21:00 UTC rollover.
  - MT5 bar spread is a min/snapshot, not a p90; keep Kai's p90.
- nybo_prereg_test.load_ic now reads the time_utc format. icdata mode refuses holdout-period data unless the NYBO holdout was authorised; it never will be, because NYBO failed.
- Track 3 sources: /workspace/xau_lab_review/xau_lab/tech/T01, T06, T08. No T15 source exists.
- HANDOFF.md (1 Oct) says the deployed lab added an EMA50-H4 filter plus a ×2.1 martingale (reset after 5 losses). That martingale was not replicated.
