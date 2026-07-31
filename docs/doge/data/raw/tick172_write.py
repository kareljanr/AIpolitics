# -*- coding: utf-8 -*-
"""Tick 172: Vivaqua SC Rapport Financier 2024 — Brussels water intercommunale L5."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T07:25:00Z"
TICK = 172
UNIT = "rq_167"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


append_lines(
    DATA / "sources.csv",
    [
        "src_vivaqua_rf_2024,Vivaqua SC Rapport Financier 2024 comptes annuels,"
        "https://rapport.vivaqua.be/wp-content/uploads/2025/06/VIVAQUA-Rapport-Financier-2024-1.pdf,"
        "Vivaqua,2026-07-28,official_annual_report,"
        '"CA 325.9m ventes 469.7m op profit 25.7m net loss 0.86m; assets 1.804bn equity 559m; '
        'subsides capital net 127.8m (public 26.7m+Modave 0.8m third-party 100.3m); LT debt 1.021bn; '
        'MFC path 16.2-28.7m/yr 2022-26; BCR EIB guarantee 206.6m; no dividend IPM; FTE 1262; tick172"',
    ],
)

# Update entity vivaqua row
replace_line_startswith(
    DATA / "entities.csv",
    "vivaqua,",
    "vivaqua,Vivaqua SC,Vivaqua,Brussels water production distribution sanitation intercommunale,"
    "intercommunale,brussels_gov,bi,https://www.vivaqua.be,,"
    "Brussels,"
    "CA 326m 2024 net loss 0.86m; assets 1.8bn equity 559m LT debt 1.02bn; no dividend (IPM); "
    "BCR finops capital path 180m; MFC tariff self-finance; dual Aquafin/SPGE water stack; tick172",
)

append_lines(
    DATA / "budgets.csv",
    [
        "bud_vivaqua_ca_2024,vivaqua,2024,325924635,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua chiffre d'affaires 325.925m 2024 (users 303.1m wholesale 41.8m FRT -20.6m)",
        "bud_vivaqua_ca_2023,vivaqua,2023,333958120,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua CA 333.958m 2023",
        "bud_vivaqua_ventes_2024,vivaqua,2024,469749318,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua ventes et prestations 469.749m 2024 (incl production immobilisee 114.1m)",
        "bud_vivaqua_ventes_2023,vivaqua,2023,448726844,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua ventes et prestations 448.727m 2023",
        "bud_vivaqua_prod_immob_2024,vivaqua,2024,114137080,,,outturn,src_vivaqua_rf_2024,strong,"
        "Production immobilisee 114.137m 2024 (assain 72.8m dist 24.1m prod 14.6m)",
        "bud_vivaqua_op_profit_2024,vivaqua,2024,25734873,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua benefice d'exploitation 25.735m 2024",
        "bud_vivaqua_op_profit_2023,vivaqua,2023,10820913,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua op profit 10.821m 2023",
        "bud_vivaqua_net_result_2024,vivaqua,2024,-860069,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua perte de l'exercice -0.860m 2024 (mainly FRT 2022-23 charge 20.646m)",
        "bud_vivaqua_net_result_2023,vivaqua,2023,-16561171,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua net loss -16.561m 2023",
        "bud_vivaqua_assets_2024,vivaqua,2024,1803925994,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua total actif 1.804bn EOY 2024",
        "bud_vivaqua_equity_2024,vivaqua,2024,559497068,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vivaqua capitaux propres 559.497m EOY 2024",
        "bud_vivaqua_subsides_capital_2024,vivaqua,2024,127774095,,,outturn,src_vivaqua_rf_2024,strong,"
        "Subsides en capital net 127.774m (public BCR nets 26.7m + Modave 0.8m + tiers 100.3m)",
        "bud_vivaqua_subsides_public_cumul_2024,vivaqua,2024,26656000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Subsides publics cumules nets reseaux distribution+assainissement RBC 26.656m",
        "bud_vivaqua_lt_fin_debt_2024,vivaqua,2024,1021261856,,,outturn,src_vivaqua_rf_2024,strong,"
        "Dettes financieres a plus d'un an 1.021bn EOY 2024",
        "bud_vivaqua_total_dettes_2024,vivaqua,2024,1214755927,,,outturn,src_vivaqua_rf_2024,strong,"
        "Total dettes 1.215bn EOY 2024",
        "bud_vivaqua_personnel_2024,vivaqua,2024,146156676,,,outturn,src_vivaqua_rf_2024,strong,"
        "Remunerations charges sociales pensions 146.157m 2024",
        "bud_vivaqua_fte_2024,vivaqua,2024,1262,,,outturn,src_vivaqua_rf_2024,strong,"
        "Effectif moyen ETP 1262.1 2024 (headcount 1287)",
        "bud_vivaqua_hydria_assain_2024,vivaqua,2024,34965000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Redevances assainissement regional Hydria (ex-SBGE) 34.965m 2024",
        "bud_vivaqua_frt_charge_2024,vivaqua,2024,20646000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Fonds regulation tarifaire 2022-23 charge in CA 20.646m 2024",
        "bud_vivaqua_mfc_2024,vivaqua,2024,24672000,,,budgeted,src_vivaqua_rf_2024,strong,"
        "Marge de Financement Consentie Brugel 24.672m in tariffs 2024",
        "bud_vivaqua_mfc_2025,vivaqua,2025,28687000,,,budgeted,src_vivaqua_rf_2024,strong,"
        "MFC Brugel 28.687m 2025 (path 2022-26: 16.2/21.6/24.7/28.7/27.8m)",
        "bud_vivaqua_mfc_2026,vivaqua,2026,27797000,,,budgeted,src_vivaqua_rf_2024,strong,"
        "MFC Brugel 27.797m 2026",
        "bud_vivaqua_bei_guarantee_2024,vivaqua,2024,206606048,,,outturn,src_vivaqua_rf_2024,strong,"
        "Garantie RBC pour BEI hors bilan 206.606m EOY 2024 (323.6m 2023)",
        "bud_vivaqua_subside_reg_deferred_2024,vivaqua,2024,15440000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Solde subsides regionaux BEI ratio residual deferred 15.440m EOY 2024",
        "bud_vivaqua_pension_gap_hydralis_2024,vivaqua,2024,146990492,,,outturn,src_vivaqua_rf_2024,strong,"
        "Sous-couverture engagements pension Hydralis hors bilan 146.990m (coverage 83.8pct)",
        "bud_vivaqua_users_rev_2024,vivaqua,2024,303060000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vente eau+services usagers bruxellois 303.060m 2024",
        "bud_vivaqua_wholesale_2024,vivaqua,2024,41793000,,,outturn,src_vivaqua_rf_2024,strong,"
        "Vente eau en gros autres operateurs 41.793m 2024",
    ],
)

append_lines(
    DATA / "commitments.csv",
    [
        "cmt_vivaqua_utility_2024,Vivaqua Brussels water utility outturn 2024,"
        "vivaqua,Brussels households communes wholesale,Vivaqua SC regulated water intercommunale,"
        "2006-01-01,2024,2026,325924635,"
        '"{""ca_2024"":325924635,""ventes_2024"":469749318,""op_profit"":25734873,""net_loss"":-860069,'
        '""assets"":1803925994,""equity"":559497068,""lt_debt"":1021261856,""subsides_capital_net"":127774095,'
        '""public_subsides_cumul"":26656000,""mfc_2024"":24672000,""mfc_2025"":28687000,""mfc_2026"":27797000,'
        '""bei_guarantee_rbc"":206606048,""hydria_assain"":34965000,""frt_charge"":20646000,'
        '""pension_gap_hydralis"":146990492,""fte"":1262,""no_dividend"":true,""tax_regime"":""IPM""}",'
        "0,active,https://rapport.vivaqua.be/wp-content/uploads/2025/06/VIVAQUA-Rapport-Financier-2024-1.pdf,"
        "Potable water production distribution sanitation Brussels,"
        "Confirm BCR finops 180m cash-by-year vs accounts; dual unit cost vs Aquafin/SPGE,"
        "src_vivaqua_rf_2024,strong,Bruxelles>Intercommunale>Vivaqua,"
        "tick172 RF2024; dual with Aquafin VL + SPGE WAL wastewater; capital path still medium via CoA/press",
        "cmt_vivaqua_mfc_path,Vivaqua Brugel Marge Financement Consentie 2022-2026,"
        "vivaqua,Vivaqua users via tariffs,Brugel tariff methodology MFC self-finance CAPEX,"
        "2022-01-01,2022,2026,118961000,"
        '"{""2022"":16237000,""2023"":21568000,""2024"":24672000,""2025"":28687000,""2026"":27797000,'
        '""sum_path"":118961000,""note"":""in regulated tariffs not separate budget line""}",'
        "0,active,https://rapport.vivaqua.be/wp-content/uploads/2025/06/VIVAQUA-Rapport-Financier-2024-1.pdf,"
        "Tariff-financed investment margin reduce extra borrowing,"
        "Publish annual MFC vs CAPEX realised and unit cost water,"
        "src_vivaqua_rf_2024,strong,Bruxelles>Brugel>Vivaqua>MFC,tick172 path from RF evaluation rules",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_vivaqua_bru_water,Vivaqua Brussels water utility CA ~326m 2024,"
        "Brussels,ops,Bruxelles>Intercommunale>Vivaqua,325924635,1629623175,"
        "CA 325.9m 2024 strong RF; assets 1.8bn LT debt 1.02bn; MFC ~25-29m/yr; no dividend IPM; "
        "BCR EIB guarantee 207m; dual water stack with Aquafin/SPGE,"
        "strong,src_vivaqua_rf_2024,Brussels households communes,Essential water utility,"
        "Core public service; tariff+MFC+limited public capital; pension Hydralis gap ~147m off-BS,"
        "2,7.5,5,5.0,"
        "Publish dual unit-cost BE water; BCR capital cash calendar; open L5 investment lists,"
        "seed,,tick172",
        "lb_vivaqua_mfc_tariff,Vivaqua Brugel MFC tariff self-finance path ~119m 2022-26,"
        "Brussels,ops,Bruxelles>Brugel>Vivaqua>MFC,24672000,118961000,"
        "MFC 24.7m 2024 / 28.7m 2025 / 27.8m 2026 in regulated tariffs; sum path ~119m,"
        "strong,src_vivaqua_rf_2024,Water users Brussels,CAPEX autofinance reduce debt,"
        "Not a subsidy line but tariff markup; transparency on CAPEX yield,"
        "3,6.0,5,4.8,"
        "Publish MFC vs realised investment and bill impact,"
        "seed,,tick172",
    ],
)

# Research queue: close rq_167, spawn rq_168
replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_167,",
    "rq_167,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV FPS taxex other large FOI-adjacent) '
    'if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_interco_dividends_l5,2026-07-28T07:05:00Z,2026-07-28T07:25:00Z,"
    '"tick172: Vivaqua RF2024 CA 325.9m ventes 469.7m net -0.86m assets 1.8bn LT debt 1.02bn MFC path '
    '119m 2022-26; no dividend; BCR EIB guarantee 207m; spawn rq_168"',
)

append_lines(
    DATA / "research_queue.csv",
    [
        "rq_168,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        '"Prefer public primary fills (Antwerp register Mons BI2026 De Lijn JV ORES/RESA FPS taxex other large '
        'FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
        ",2026-07-28T07:25:00Z,,"
        '"Spawned tick172 after Vivaqua RF2024; rq_116 SWA deferred Oct-Dec 2026"',
    ],
)

# FOI note update for interco gap
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_interco_dividends_l5,",
    "gap_interco_dividends_l5,BE>Intercommunales>dividends_public_transfers,fluvius,"
    "Municipal dividends Fluvius DSOs 2023-2026; VL PMV equity cash schedule max 1.56bn; "
    "Aquafin public vs tariff split; SPGE OAA top-20; Vivaqua BCR capital cash calendar vs RF2024,"
    "Entity totals strong (Vivaqua CA 326m no dividend IPM tick172; Fluvius/Sibelga filled); "
    "L5 municipal cash + BCR 180m calendar still opaque,6,"
    "Fluvius PMV / Team Openbaarheid + SPGE Aquafin SPRB Vivaqua,"
    "openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
    "docs/doge/foi/drafts/gap_interco_dividends_l5.md,ready,2026-07-27,,,,,"
    "cmt_fluvius_eg_public_utility,lb_fluvius_public_utility,2026-07-27T23:35:00Z,2026-07-28T07:25:00Z,"
    "tick150+172 Vivaqua RF filled; residual L5 dividends+BCR capital calendar human send",
)

# loop_state
replace_line_startswith(
    DATA / "loop_state.csv",
    "main,",
    "main,continuous,hole_fill,2026-07-28T07:25:00Z,rq_167,172,no,"
    '"Scheduler 60s. Next prio5 rq_168 hole-fill Antwerp/Mons/De Lijn/ORES/taxex; rq_116 SWA deferred. '
    'FOI ready human send. tick172 Vivaqua RF2024 CA 326m."',
)

# loop_log append
log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **Vivaqua SC Rapport Financier 2024**)
- Found (strong primary annual accounts, RSM audit unqualified):
  - **CA EUR 325.925m 2024** (333.958m 2023) · ventes/prestations **469.7m** · op. profit **25.7m** · **net loss −0.86m** (FRT 2022–23 charge **20.6m**).
  - Users Brussels **303.1m** · wholesale **41.8m** · production immobilisée **114.1m** (assain **72.8m**).
  - Assets **1.804bn** · equity **559.5m** · LT fin. debt **1.021bn** · total dettes **1.215bn**.
  - **Subsides en capital net 127.8m** (public nets **26.7m** + Modave **0.8m** + tiers **100.3m**).
  - **MFC Brugel path** 2022–26: **16.2 / 21.6 / 24.7 / 28.7 / 27.8m** (sum ~**119m** in tariffs).
  - Hydria assainissement **35.0m** · BCR **BEI guarantee 206.6m** · Hydralis pension gap **147.0m** off-BS (cover **83.8%**).
  - **No dividend** (IPM tax regime — profits to immunised reserves only). FTE **1 262**.
  - Dual water stack: **Vivaqua BCR** + **Aquafin VL** + **SPGE WAL** (+ Hydria regional sanitation).
- Mons BI2026 / Antwerp bulk register still not newly filled.
- Wrote: sources 1; entity update; budgets 27; cmt 2; lb 2; FOI gap_interco note; rq_167=done; seeded **rq_168**.
- FOI: residual L5 municipal dividends + BCR 180m capital cash calendar human send.
- Next: prio5 **rq_168**; deferred **rq_116** SWA.
"""
text = log.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
log.write_text(text + entry, encoding="utf-8", newline="\n")

print(f"tick{TICK} write OK unit={UNIT}")
