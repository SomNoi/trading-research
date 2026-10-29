# REB-H4 on XAUUSD: independent pre-registered OOS test: REPORT

**Verdict: FAIL (years,pf,dd). The holdout was NOT run and stays unused.**

- Pre-registration: prereg/REB_H4_XAU_PREREG.md (sha256 eeadef45d74c…, registered 2026-10-11T13:34:23Z = 20:34 ICT), written before any XAU REB/B2 run.
- Rules are the USDJPY V2 / handoff setting, unchanged: f = 0.5, opposite-level SL, H4 swing filter F2, time exit 20:00 UTC; XAU minimum stop $1.00/oz.
- 53 US-holiday early-close days used the pre-registered rule (exit at the open of the last M5 bar before the close); 0 entries in the last pre-close bar were dropped.
- Code check: with the early-close rule off, the entries equal trackB.b2_range_bo exactly: True.
- Costs: Kai's file (XAU p90 12/11/10 points, $3.50/lot/side, $0.05/oz/side slippage, swap with Wednesday ×3). Flat 1% risk.
- Multiple testing: 645 trials in total (5 new); Bonferroni one-sided 5% t threshold = 3.78.

## Results (after costs; gross/cost/swap columns in $/oz per trade)

| set                          |   n |   trades_per_month |   win_pct |   pf_1x |   pf_1_5x |   pf_2x |   exp_R |   maxdd_pct |   worst_streak |   tstat | years_pos   |   gross_usd_oz |   cost_usd_oz |   swap_usd_oz |   avg_risk_usd_oz |   dsr_strict |   dsr_pooled | passes   | failed      |
|:-----------------------------|----:|-------------------:|----------:|--------:|----------:|--------:|--------:|------------:|---------------:|--------:|:------------|---------------:|--------------:|--------------:|------------------:|-------------:|-------------:|:---------|:------------|
| DECISIVE 2019-01..2025-10-09 | 382 |               4.7  |      41.1 |   1.026 |     0.979 |   0.935 |   0.01  |       -23.7 |              9 |    0.14 | 4/7         |          0.281 |         0.294 |             0 |             18.86 |            0 |            0 | False    | years,pf,dd |
| info 2021-01..2025-10-09     | 272 |               4.75 |      44.1 |   1.272 |     1.221 |   1.174 |   0.098 |       -12   |              7 |    1.1  | 4/5         |          0.459 |         0.294 |             0 |             20.54 |            0 |            0 | False    | years,n     |

Exit reasons (1 = SL, 3 = time/early close): {3: 276, 1: 106}. Longs 230, shorts 152.

## Per year (1x)

|    y |   n |   exp_R |   sum_R |   gross_usd_oz |   cost_usd_oz |
|-----:|----:|--------:|--------:|---------------:|--------------:|
| 2019 |  50 |  -0.3   | -15.022 |         -0.693 |         0.294 |
| 2020 |  60 |  -0.133 |  -7.967 |          0.287 |         0.292 |
| 2021 |  51 |   0.07  |   3.545 |          0.291 |         0.294 |
| 2022 |  59 |   0.307 |  18.107 |         -0.616 |         0.294 |
| 2023 |  63 |   0.036 |   2.289 |          1.841 |         0.292 |
| 2024 |  65 |  -0.011 |  -0.74  |          2.433 |         0.294 |
| 2025 |  34 |   0.105 |   3.579 |         -3.757 |         0.294 |

## IQ hit-rate check (numbers only; no IQ Option access)

Entry = first M1 bar reaching the entry price inside the fill bar; strike = entry price. Expiry = M1 mid open at entry + T. Ties count as losses.

|   expiry_min |   n |   wins |   ties |   dropped |    hit |   wilson_lo |   wilson_hi |    ev85 | clears_55_6   | clears_54_1   | clears_53_5   |
|-------------:|----:|-------:|-------:|----------:|-------:|------------:|------------:|--------:|:--------------|:--------------|:--------------|
|            5 | 382 |    184 |      0 |         0 | 0.4817 |      0.432  |      0.5317 | -0.1089 | False         | False         | False         |
|           15 | 382 |    186 |      0 |         0 | 0.4869 |      0.4372 |      0.5369 | -0.0992 | False         | False         | False         |
|           30 | 382 |    184 |      0 |         0 | 0.4817 |      0.432  |      0.5317 | -0.1089 | False         | False         | False         |
|           60 | 382 |    173 |      0 |         0 | 0.4529 |      0.4037 |      0.503  | -0.1622 | False         | False         | False         |

**Any Wilson LB clearing a breakeven (55.6 / 54.1 / 53.5%)? NO.**

## Notes
- **Why it fails:**
  - The decisive window has PF 1.026 at 1x and 0.979 at 1.5x. Max DD is −23.7%, and 2019, 2020 and 2024 are negative.
  - Average gross is $0.28/oz per trade against a cost of $0.29/oz; average risk is $18.9/oz. The edge is roughly zero before costs.
  - The 2021+ subset (PF 1.27, n 272) is information only. It falls short of 300 trades and has 2024 negative. The pre-registration fixed 2019–2025 as decisive because no XAU parameter was fitted.
- **Early-close detection:** the pre-registration counted 54 early-close weekdays. The coded rule (next bar > 60 min after 20:00 UTC and last bar > 5 min before 20:00) triggered on 53 of them. The one day not caught resumes trading within 60 min of 20:00, so its normal 20:00 exit is valid.
- **analyze.py's generic report:** results/reports/REB_H4_XAU_XAUUSD.md applies its default ">5 years: 4/5 allowed" year rule. The pre-registered rule (every year positive) governs here. Both verdicts are FAIL.
- **Holdout:** not run. results/HOLDOUT_USED_REB_H4_XAU was not created.
