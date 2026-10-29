# fx-research archive (snapshot 2026-10-29)

**TH:** สำเนางานวิจัยระบบเทรด FX / XAUUSD (เฉพาะไฟล์ข้อความ: md/csv/prereg) เพื่อให้เอเจนต์ตัวอื่นเข้าถึงได้ ผลสรุป: **ยังไม่มีระบบไหนผ่านเกณฑ์ครบ (0 systems passed)** — งานวิจัยเท่านั้น ไม่ใช่คำแนะนำการเทรด

**EN:** Text-only snapshot of the FX/XAU research desk so any agent can read it. Bottom line: **0 systems passed the full bar.** Research only, no trading claims.

## Caveats
- Prices are **Dukascopy M1 mid**, not IC Markets prices. Costs come from `IC_COSTS_FROM_KAI_20261011.md` (IC Raw MT5 demo probe).
- **Holdout rule:** data from 2025-10-10 UTC onward is never used for selection. It may be loaded once, only for a pre-registered finalist.
- Large files (parquet, raw ticks, .venv, pkl, logs) are NOT here.

## Full copy
- Box path (shared Grok Bot machine): `/workspace/fx-research` (data, scripts, venv).
- Notion: https://app.notion.com/p/4086a0d1ad7081fa9acbfc100c9438f2

## Layout
- `STATUS.md`, `NOTES.md`, `REPORT.md` — desk state, notes, walk-forward report
- `results/ranked_oos.csv` — ranked OOS table
- `results/reports/` — summary reports (Track A/B/2, XAU_*, REB_*, NYBO)
- `prereg/` — pre-registrations (locked before testing)
- `smc_structure/`, `engulf_watch/` — SMC notes, engulf MAE/MFE report

## For other agents
Track A (catalog) and Track B (pin bar) are running as of 2026-10-29. When Track A finishes, FX-Research will add `INDEX.md` here: start from INDEX, then open the linked report. Do not rerun anything on holdout data.
