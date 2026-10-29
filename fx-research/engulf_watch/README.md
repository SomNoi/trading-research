# XAUUSD M5 close-break engulf watcher (read-only research, no trading)
**Source:** Dukascopy free feed (mid = (bid+ask)/2), **not IC MT5**. IC prices differ slightly (a few cents to tens of cents), so bar colours and breaks can occasionally differ from IC charts.

## Run (idempotent, safe to repeat; a lock file prevents overlapping runs)
    cd /workspace/fx-research && .venv/bin/python engulf_watch/watch.py
Options:
- `--hour "2026-10-16 13"` sets the Thai hour to summarise. The default is the last fully closed Thai hour.
- `--days 4` sets how far back to fetch on the first run.
- `--no-fetch` reuses the cached data.

JSON goes to stdout (log lines go to stderr). It is also saved to `last_summary.json` and `summaries/summary_YYYYMMDD_HH.json`.

## Data
- Fetch window: the throttled `scripts/fetch_dukascopy2.fetch_month` pulls XAU/USD M1 bid and ask, from (cached end − 3h), or now − 4 days on the first run, up to now.
- Cache: `data/XAUUSD_M1_recent.parquet`, keeping about 10 days. This is separate from the research data.
- M5 bars: UTC buckets (label left). Only **completed** bars are used, meaning bar end ≤ last M1 + 1 min. Times are displayed in ICT (UTC+7).
- Feed lag: recorded per run in `data_lag` and in `state.json` (`lag_history_min`). On 2026-10-16 the minute endpoint lagged by under 1 minute. Hourly archive files on Dukascopy's other endpoints can lag more, and lag looks large whenever the market is closed.

## Signal rules (completed M5 bars, no size filter)
- **BUY T1:** previous bar red (close<open), current bar green, and current close > previous HIGH.
- **BUY T2:** previous 2 bars red, current green, and close > max HIGH of those 2.
- **SELL T1 / T2:** the mirror (previous 1 or 2 green bars, current red, close < LOW / min LOW of the 2).
- **Both T1 and T2:** recorded once as **T2**, with `both_T1_T2=True`.
- Doji bars (close == open) are neither red nor green.
- Entry = signal bar close. `signal_time` = bar **close** time.

## signals.csv columns
- **Signal fields:** signal_time_thai, side, type, entry, bar_range_usd, bar_range_pts (1 pt = $0.01), both_T1_T2, source, signal_time_utc.
- **Key:** (signal_time_utc, side, type). A key is never duplicated, and the file is rewritten atomically (tmp + rename).
- **Outcome fields:** blank until 24 subsequent M5 bars have closed. Bars are counted in sequence, so weekend and break gaps are skipped and do not count.
  - **direction:** sign of (close of bar 24 − entry) in the signal's favour. `signal_way` if >0, `against` if <0, `flat` if exactly 0. Flat counts as not signal-way in percentages.
  - **close24:** close of bar 24.
  - **run_usd / run_pts:** max favourable excursion from entry over bars 1..24, using highs for BUY and lows for SELL; floored at 0.
  - **against_usd / against_pts:** max adverse excursion, floored at 0.
  - **cont_bars:** number of consecutive bars right after the signal that each make a higher high than the bar before (lower low for SELL). The first comparison is against the signal bar.
  - **bars_to_peak:** bar index (1..24) of the max favourable excursion. If tied, the first occurrence counts. 0 if run = 0.
  - **first:** which extreme came first, `run` or `against`. `same_bar` if both extremes fall in the same bar, since M5 cannot order them. `none` if both are 0.
  - **outcome_filled_utc:** when the outcome was filled.

## Summary JSON
- signals_in_hour: bars closing in (H:00, H+1:00] ICT.
- completed_since_last_run: outcomes filled this run that were not reported before; this is tracked in state.json.
- today_ict: running totals for the Thai calendar day, covering signals with outcomes.
- market_open / market_status:
  - Weekend close runs from Friday server midnight (21:00 UTC during US DST, otherwise 22:00 UTC; Sat 04:00/05:00 ICT) to Sunday at the same hour.
  - A daily break of about 1 hour starts at the same time.
  - This is an approximation; holidays are not modelled.
- data_lag.

## Caveats
Descriptive only. No costs are included, and this is not a strategy test. Signals are counted after the fact on mid prices. The schedule is handled outside this script; there is no cron here.
