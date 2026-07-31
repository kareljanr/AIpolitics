# -*- coding: utf-8 -*-
"""Tick 152: rq_144 Charleroi BI2026 official PDF + named ASBL L5 from cahier ordinaire."""
from pathlib import Path
import re

ROOT = Path("docs/doge")
DATA = ROOT / "data"
UTC = "2026-07-28T00:15:00Z"
TICK = 152
UNIT = "rq_144"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n".join(lines) + "\n", enc)


def replace_row(path: Path, key_prefix: str, new_row: str) -> None:
    text, enc = read_text(path)
    lines = text.splitlines()
    out = []
    replaced = False
    for ln in lines:
        if ln.startswith(key_prefix + ",") or ln.startswith(key_prefix):
            # match id at start of CSV row
            if ln.split(",", 1)[0] == key_prefix:
                out.append(new_row)
                replaced = True
                continue
        out.append(ln)
    if not replaced:
        out.append(new_row)
    write_text(path, "\n".join(out) + "\n", enc)


# --- sources ---
append_lines(DATA / "sources.csv", [
    'src_charleroi_synthese_bi2026,Charleroi Rapport de synthese budget initial 2026 eComptes SPW,https://www.charleroi.be/assets/files/Rapport-de-synthese-du-budget-initial-2026.pdf,Ville de Charleroi / SPW eComptes,2026-07-28,official_budget,"Ord dep propre 577.89m gen 582.52m; personnel 189.70m fct 48.22m transferts 240.30m dette 99.15m; Oxygene last tranche 48.6m; invest borrow limit 20m; FERI grandes villes"',
    'src_charleroi_cahier_ord_bi2026,Charleroi Cahier service ordinaire apres reformation BI2026,https://www.charleroi.be/assets/files/Cahier-du-service-ordinaire-apres-reformation.pdf,Ville de Charleroi,2026-07-28,official_budget,"271p article-level; named ASBL L5 culture sport social; ZPL 82.9m CPAS 93.2m Tibi ~31.5m ZOHE 8.1m RCA 3.86m PBA 1.34m"',
    'src_charleroi_synthese_bi2024,Charleroi Rapport de synthese budget initial 2024,https://www.charleroi.be/assets/files/4.-Rapport-de-synthese-du-budget-initial-2024.pdf,Ville de Charleroi,2026-07-28,official_budget,"Named ASBL table BI2024: PBA 1.34m CCR 0.73m Parc Sports 0.74m; CPAS 88.0m ZPL 87.4m Tibi 34.2m"',
])

# --- budgets: replace weak press rows + add official ---
# Update totals to official strong
replace_row(
    DATA / "budgets.csv",
    "bud_charleroi_rev_own_2025",
    "bud_charleroi_rev_own_2025,city_charleroi,2025,580698870.25,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2025 ord recettes exercice propre from BI2026 synthese comparative table",
)
replace_row(
    DATA / "budgets.csv",
    "bud_charleroi_transfers_4p_2026",
    "bud_charleroi_transfers_4p_2026,city_charleroi,2026,240303135.19,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 depenses transferts ord 240303135.19; -10.85m vs BI2025; 4P-heavy block",
)
replace_row(
    DATA / "budgets.csv",
    "bud_charleroi_budget_total_2026",
    "bud_charleroi_budget_total_2026,city_charleroi,2026,577887103.70,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 ord total exercice propre dep=rec 577887103.70 (not press 567m); gen 582521211.12",
)
replace_row(
    DATA / "budgets.csv",
    "bud_charleroi_invest_borrow_2026",
    "bud_charleroi_invest_borrow_2026,city_charleroi,2026,20000000,,,budgeted,src_charleroi_synthese_bi2026,strong,Intro: financement par emprunts part communale investissements limite a 20m EUR",
)

append_lines(DATA / "budgets.csv", [
    # L1 economic classes BI2026 strong
    "bud_charleroi_personnel_2026,city_charleroi,2026,189695747.83,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 dep personnel ord 189695747.83 (+0.85m vs BI2025; no natural attrition replace beyond 30 FTE)",
    "bud_charleroi_fonctionnement_2026,city_charleroi,2026,48217554.16,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 dep fonctionnement 48217554.16",
    "bud_charleroi_dette_ord_2026,city_charleroi,2026,99153068.00,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 dep dette ord 99153068 incl Oxygene interest path",
    "bud_charleroi_ord_total_gen_2026,city_charleroi,2026,582521211.12,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 ord total general dep=rec 582521211.12",
    "bud_charleroi_rec_transferts_2026,city_charleroi,2026,468482566.69,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 recettes transferts ord 468482566.69",
    "bud_charleroi_rec_prestation_2026,city_charleroi,2026,36575988.20,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 recettes prestation 36575988.20",
    "bud_charleroi_extra_invest_2026,city_charleroi,2026,15460876.23,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 extra investissements exercice propre 15460876.23 (security continuity only)",
    "bud_charleroi_extra_dep_propre_2026,city_charleroi,2026,20446042.59,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 extra total exercice propre dep 20446042.59",
    "bud_charleroi_extra_total_gen_2026,city_charleroi,2026,118062628.68,,,budgeted,src_charleroi_synthese_bi2026,strong,BI2026 extra total general dep 118062628.68 (incl antérieurs+prélèvements)",
    "bud_charleroi_oxygene_tranche_2026,city_charleroi,2026,48600000,,,budgeted,src_charleroi_synthese_bi2026,medium,Synthese text: derniere tranche aides Oxygene 48.6m (-22.8m vs 2025); cahier prelevement Oxygene-class 48662457",
    "bud_charleroi_fonds_communes_2026,city_charleroi,2026,200080384.62,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier: Fonds des Communes dotation principale BI2026 200080384.62",
    # Large institutional transfers BI2026
    "bud_charleroi_zpl_2026,city_charleroi,2026,82893812.02,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier art 33000/435.01/001 Intervention Zone de police locale BI2026 82893812.02 (MB2025 69.8m; BI2025 88.5m)",
    "bud_charleroi_cpas_dot_a_2026,city_charleroi,2026,71037637.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier 83101 CPAS charges fonctionnement path BI2026 71037637",
    "bud_charleroi_cpas_dot_b_2026,city_charleroi,2026,22144000.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier 83102 CPAS contributions path BI2026 22144000; sum A+B ~93.18m (+0.7m vs BI2025 class matches synthese)",
    "bud_charleroi_cpas_total_2026,city_charleroi,2026,93181637.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Sum CPAS A+B 93.181637m BI2026 (approx; exclude small PCS/archive lines)",
    "bud_charleroi_zohe_2026,city_charleroi,2026,8112990.01,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier Dotation zone de secours ZOHE BI2026 8112990.01 (-5.3m class vs BI2025 13.39m; province financing)",
    "bud_charleroi_rca_2026,city_charleroi,2026,3857880.72,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier Subside Regie communale autonome BI2026 3857880.72",
    "bud_charleroi_tibi_s1_2026,city_charleroi,2026,22481605.62,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier Tibi Secteur1 immondices parcs conteneurs BI2026 22481605.62",
    "bud_charleroi_tibi_s2_2026,city_charleroi,2026,8630102.94,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier Tibi Secteur2 mutualisation proprete BI2026 8630102.94",
    "bud_charleroi_tibi_s3_2026,city_charleroi,2026,375007.59,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier Tibi Secteur3 depots clandestins BI2026 375007.59",
    "bud_charleroi_tibi_sacs_2026,city_charleroi,2026,2115202.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cahier distribution gratuite sacs poubelles BI2026 2115202",
    "bud_charleroi_tibi_total_class_2026,city_charleroi,2026,33601918.15,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Sum Tibi S1+S2+S3+sacs ~33.60m BI2026",
    # Named ASBL L5 culture/sport/social (top)
    "bud_charleroi_asbl_pba_2026,city_charleroi,2026,1339834.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Palais des Beaux-Arts BI2026 1339834 (stable vs 2024-25)",
    "bud_charleroi_asbl_ccr_2026,city_charleroi,2026,864310.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Centre Culturel Regional de Charleroi BI2026 864310 (BI2025 809310)",
    "bud_charleroi_asbl_parc_sports_2026,city_charleroi,2026,553552.25,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Parc des Sports a Charleroi BI2026 553552.25 (down from BI2024 738k)",
    "bud_charleroi_sport_promo_2026,city_charleroi,2026,516905.75,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Subsides promotion du sport BI2026 516905.75 (pooled not single ASBL)",
    "bud_charleroi_asbl_maison_part_2026,city_charleroi,2026,415053.53,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Maison de la participation path BI2026 415053.53 (cahier 084x social)",
    "bud_charleroi_regie_logement_2026,city_charleroi,2026,393153.34,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Subside a une Regie (logement path) BI2026 393153.34",
    "bud_charleroi_asbl_maison_part_assoc_2026,city_charleroi,2026,312000.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Maison de la participation et des associations BI2026 312000",
    "bud_charleroi_asbl_centreville_2026,city_charleroi,2026,201250.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Charleroi Centre-Ville BI2026 201250 (was 245k)",
    "bud_charleroi_asbl_maison_du_2026,city_charleroi,2026,142394.28,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Maison du ... commerce path BI2026 142394.28 (was 189859)",
    "bud_charleroi_asbl_bois_cazier_2026,city_charleroi,2026,142131.38,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Le Bois du Cazier BI2026 142131.38",
    "bud_charleroi_asbl_oeuvre_2026,city_charleroi,2026,103982.55,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Oeuvre (social path) BI2026 103982.55",
    "bud_charleroi_telesambre_2026,city_charleroi,2026,71937.60,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Television locale Telesambre BI2026 71937.60",
    "bud_charleroi_asbl_museum_2026,city_charleroi,2026,70000.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Charleroi Museum BI2026 70000 (up from 40k)",
    "bud_charleroi_quai10_2026,city_charleroi,2026,62341.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,Cinema QUAI 10 BI2026 62341 (stable)",
    "bud_charleroi_asbl_danses_2026,city_charleroi,2026,56250.00,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Charleroi Danses BI2026 56250",
    "bud_charleroi_asbl_photo_2026,city_charleroi,2026,45869.25,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Musee de la Photographie BI2026 45869.25",
    "bud_charleroi_asbl_ancre_2026,city_charleroi,2026,36408.75,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Theatre de l Ancre BI2026 36408.75",
    "bud_charleroi_asbl_article27_2026,city_charleroi,2026,31282.50,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Article 27 BI2026 31282.50",
    "bud_charleroi_asbl_rockerill_2026,city_charleroi,2026,30973.50,,,budgeted,src_charleroi_cahier_ord_bi2026,strong,ASBL Rockerill BI2026 30973.50",
    "bud_charleroi_yernaux_semester_2026,city_charleroi,2026,600000,,,budgeted,src_charleroi_synthese_bi2026,medium,Synthese: intervention prix entrees complexe Yernaux un semestre 0.6m (RCA-linked; not full-year ASBL line)",
    # Functional chapter culture invest
    "bud_charleroi_invest_educ_arts_2026,city_charleroi,2026,2184300.00,,,budgeted,src_charleroi_synthese_bi2026,strong,Extra invest Education Populaire et Arts function 789 BI2026 2184300",
])

# --- commitments ---
append_lines(DATA / "commitments.csv", [
    'cmt_charleroi_bi2026_ord,Charleroi BI2026 ordinary budget official eComptes,city_charleroi,Ville de Charleroi,CDLD Art L1122-23 synthese + cahier ordinaire,2026-01-01,2026,2026,577887103.70,"{""dep_propre"":577887103.70,""dep_gen"":582521211.12,""personnel"":189695747.83,""fonctionnement"":48217554.16,""transferts"":240303135.19,""dette"":99153068.00,""rec_transferts"":468482566.69,""rec_prestation"":36575988.20,""fonds_communes"":200080384.62,""oxygene_tranche_class"":48600000,""zpl"":82893812.02,""cpas_sum"":93181637,""zohe"":8112990.01,""rca"":3857880.72,""tibi_class"":33601918.15,""invest_borrow_cap"":20000000,""extra_invest_propre"":15460876.23}",0,active,https://www.charleroi.be/assets/files/Rapport-de-synthese-du-budget-initial-2026.pdf,Municipal ops under Plan Oxygene end-2026,Publish open register top20 third parties; post-Oxygene cliff plan,src_charleroi_synthese_bi2026,strong,Charleroi>BI2026,tick152 official replaces press 567m',
    'cmt_charleroi_asbl_top_l5_2026,Charleroi named third-party ASBL subsidies BI2026 sample,city_charleroi,Named ASBL culture sport social,Cahier service ordinaire apres reformation BI2026,2026-01-01,2026,2026,1339834,"{""pba"":1339834,""ccr"":864310,""parc_sports"":553552.25,""sport_promo_pool"":516905.75,""maison_part"":415053.53,""maison_part_assoc"":312000,""centre_ville"":201250,""bois_cazier"":142131.38,""quai10"":62341,""museum"":70000,""danses"":56250,""photo"":45869.25,""ancre"":36408.75,""article27"":31282.50,""rockerill"":30973.50,""telesambre"":71937.60,""note"":""sample not exhaustive top20; residual FOI for full ranked list""}",0,active,https://www.charleroi.be/assets/files/Cahier-du-service-ordinaire-apres-reformation.pdf,Culture sport social third-party map,Complete ranked top20 CSV open data,src_charleroi_cahier_ord_bi2026,strong,Charleroi>L5>ASBL,tick152 closed main opacity vs FOI-only path',
])

# --- leaderboard updates ---
replace_row(
    DATA / "leaderboard.csv",
    "lb_charleroi_budget",
    "lb_charleroi_budget,Charleroi city ordinary budget total propre,local,ops,Charleroi>budget,577887104,3467322622,BI2026 official 577.89m propre / 582.52m gen; press 567m superseded,strong,src_charleroi_synthese_bi2026,City residents,Municipal operations,Oxygene constrained end-2026,3,7.5,6,5.3,Publish post-Oxygene path; keep open L5 register,seed,,tick152 official PDF",
)
replace_row(
    DATA / "leaderboard.csv",
    "lb_charleroi_4p",
    "lb_charleroi_4p,Charleroi transfer expenditure block (4P-heavy),local,ops,Charleroi>4P,240303135,1441818810,BI2026 official transfers 240.30m; ZPL 82.9m CPAS ~93.2m ZOHE 8.1m Tibi ~33.6m,strong,src_charleroi_synthese_bi2026,Residents safety social,Police fire pensions poverty waste,Mostly mandated not pure waste,4,7.5,6,5.7,Fonds des communes reform; provincialise rescue; open ASBL top20,seed,,tick152; 38pct of 578m propre",
)

append_lines(DATA / "leaderboard.csv", [
    "lb_charleroi_zpl,Charleroi police zone (ZPL) city transfer ~83m,local,ops,Charleroi>ZPL,82893812,497362872,BI2026 strong cahier 82.89m; down vs BI2025 88.5m with federal sectoral interventions,strong,src_charleroi_cahier_ord_bi2026,City residents,Local police financing,Mandated multi-level cost not discretionary waste,3,7.0,5,5.0,Federal/zone financing reform; transparent shared cost,seed,,tick152",
    "lb_charleroi_cpas,Charleroi CPAS city contributions ~93m,local,ops,Charleroi>CPAS,93181637,559089822,BI2026 cahier sum ~93.18m (+0.7m vs BI2025 class); social mandated,strong,src_charleroi_cahier_ord_bi2026,Vulnerable residents,Public social assistance,Core safety net not pure waste,2,7.5,5,4.8,Outcome KPIs; dual CPAS/city overhead audit,seed,,tick152",
    "lb_charleroi_pba,Charleroi ASBL Palais des Beaux-Arts 1.34m,local,subsidy,Charleroi>Culture>PBA,1339834,1339834,BI2026 strong named ASBL 1.339834m stable; separate 7.6m reno request regional,strong,src_charleroi_cahier_ord_bi2026,Culture audience,Culture venue ops,Named L5; dual regional reno request,4,4.5,4,4.3,KPI visitors; co-finance audit with regional reno,seed,,tick152",
    "lb_charleroi_ccr,Charleroi Centre Culturel Regional ASBL 0.86m,local,subsidy,Charleroi>Culture>CCR,864310,864310,BI2026 864310 up from 809310 BI2025,strong,src_charleroi_cahier_ord_bi2026,Culture audience,Regional cultural centre,Named L5,4,4.0,4,4.0,Publish outputs; dual CCR/PBA map,seed,,tick152",
])

# --- research_queue rq_144 done ---
text, enc = read_text(DATA / "research_queue.csv")
lines = text.splitlines()
out = []
for ln in lines:
    if ln.startswith("rq_144,"):
        out.append(
            'rq_144,Charleroi budget PDF L5 named ASBL,continuous,6,done,L5,city_charleroi,"Find BI2026 PDF named association table.",gap_charleroi_subsidies_top20,2026-07-27T14:00:00Z,'
            + UTC
            + ',"tick152: official synthese 577.89m + cahier named PBA 1.34m CCR 0.86m ParcSports 0.55m + ZPL/CPAS/Tibi; FOI residual full ranked top20"'
        )
    else:
        out.append(ln)
write_text(DATA / "research_queue.csv", "\n".join(out) + "\n", enc)

# --- FOI residual: keep ready but note partial public fill ---
text, enc = read_text(DATA / "foi_queue.csv")
lines = text.splitlines()
out = []
for ln in lines:
    if ln.startswith("gap_charleroi_subsidies_top20,"):
        # update notes / description residual
        # keep status ready; update last field notes if present
        parts = ln.split(",")
        # rebuild carefully - FOI CSV may have commas in fields without quotes for some rows
        # Safer: replace status notes at end via string ops
        out.append(
            "gap_charleroi_subsidies_top20,Charleroi>subsidies>top20,city_charleroi,"
            "Top 20 third-party subsidies and ASBL grants 2025-2026 with amounts ranked CSV,"
            "tick152: major named ASBL now public in cahier (PBA CCR ParcSports etc) + ZPL/CPAS/Tibi; residual full ranked top20+sport club list+export,"
            "6,Ville de Charleroi publicite administration,,,docs/doge/foi/drafts/gap_charleroi_subsidies_top20.md,ready,2026-07-20,,,,,2026-07-20T03:40:00Z,"
            + UTC
            + ",rq_144,partial public fill tick152"
        )
    else:
        out.append(ln)
write_text(DATA / "foi_queue.csv", "\n".join(out) + "\n", enc)

# --- FOI draft update note ---
draft = ROOT / "foi" / "drafts" / "gap_charleroi_subsidies_top20.md"
if draft.exists():
    dtext, denc = read_text(draft)
    note = (
        "\n\n## Update tick152 (2026-07-28)\n\n"
        "Public primary sources now cover BI2026 aggregates (synthese eComptes) and **many named ASBL lines** "
        "in the cahier du service ordinaire (PBA EUR 1.339834m; CCR 0.864m; Parc des Sports 0.554m; "
        "ZPL 82.9m; CPAS ~93.2m; Tibi class ~33.6m). Residual FOI still useful for a **single ranked top-20 CSV** "
        "of all third-party grants 2025-2026 and sport-club detail under the promotion-du-sport pool. "
        "**Do not send** until human confirms; status remains ready.\n"
    )
    if "Update tick152" not in dtext:
        write_text(draft, dtext.rstrip() + note, denc)

# --- loop_state ---
write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},rq_144,{TICK},no,"Scheduler 60s. Next prio6 Myria housing Brussels communes; FOI ready human send. rq_144 Charleroi BI2026 official+ASBL done."\n',
    "utf-8",
)

# --- loop_log ---
log = ROOT / "loop_log.md"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **rq_144** (Charleroi BI2026 PDF named ASBL)
- Found (strong official PDFs charleroi.be):
  - **Synthese BI2026:** ord propre **EUR 577.89m** / gen **582.52m** (press ~567m superseded); personnel **189.70m**; fct **48.22m**; transferts **240.30m**; dette **99.15m**.
  - **Oxygene** last tranche class **~48.6m** (−22.8m vs 2025); invest borrow cap **20m**; extra invest propre **15.46m**.
  - **Cahier ordinaire (271p):** named L5 — **ZPL 82.89m**; **CPAS ~93.18m**; **ZOHE 8.11m**; **RCA 3.86m**; **Tibi class ~33.60m**; **PBA ASBL 1.34m**; **CCR 0.86m**; **Parc des Sports 0.55m**; sport promo pool **0.52m**; Bois du Cazier **0.14m**; QUAI 10 **62k**; etc.
- Wrote: sources 3; budgets ~40 (replace press totals + L5); cmt 2; lb 4 new + 2 update; rq_144=done; FOI residual still ready (ranked top20 CSV).
- FOI: gap_charleroi_subsidies_top20 ready residual — **human send only**.
- Next: prio6/5 **rq_120 Myria** / **rq_149 housing** / **rq_145 Brussels communes**.
"""
ltext, lenc = read_text(log)
if not ltext.endswith("\n"):
    ltext += "\n"
write_text(log, ltext + entry, lenc)

print("tick152 write complete")
