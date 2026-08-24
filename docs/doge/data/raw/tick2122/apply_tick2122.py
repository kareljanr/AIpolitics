# -*- coding: utf-8 -*-
import csv
import re

csv.field_size_limit(10**7)
UTC = "2026-08-25T10:55:00Z"
ENTITY = "asbl_unite_jolimont"
GAP = "gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5"
COMM = "comm_unite_jolimont_jr2025_statutory_hospital_mrs"
LB = "lb_unite_jolimont_bruto_drop_26k_pnl_flip_fte0_jr2025"
SRC_EN = "src_unite_jolimont_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_unite_jolimont_jr2025_cw",
        "title": "Companyweb NL Unité Jolimont YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0748968276/unite-jolimont",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2122; YE2025 bruto DROP 26298 pnl FLIP 11109 equity JUMP 78367 omzet unpublished FTE Micro 0; neerlegging 26.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2122/unite_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Unité Jolimont YE2025 statutory",
        "url": "https://www.companyweb.be/en/0748968276/unite-jolimont",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2122; EN mirror YE2025 Medium; filed 26-06-2026; Last balance sheet year 2025; Micro 0 FTE; bruto 26298.19; raw docs/doge/data/raw/tick2122/unite_en.html",
    },
    {
        "source_id": "src_unite_jolimont_jr2025_cw_fr",
        "title": "Companyweb FR Unité Jolimont YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0748968276/unite-jolimont",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2122; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2122/unite_fr.html",
    },
    {
        "source_id": "src_unite_jolimont_kbo_2122",
        "title": "KBO ASBL Unité Jolimont 0748.968.276 Actief La Louviere",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0748968276",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2122; Actief ASBL/VZW; Rue Ferrer(PAU) 159 7100 La Louviere; 0 VE; NACE 87.101/86.109/88.911/68.201; aanbestedende overheid; email secretariat.general@jolimont.be",
    },
    {
        "source_id": "src_unite_jolimont_nbb_2122",
        "title": "NBB consult Unité Jolimont 0748968276",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0748968276",
        "publisher": "NBB Balanscentrale",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2122; FOI target for full PDF assets/debt; CW YE2025 Medium until PDF",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Unité Jolimont (ASBL / hospital-MRS wind-down)",
        "name_fr": "ASBL Unité Jolimont (activités hospitalières / MRS)",
        "name_en": "Unité Jolimont ASBL (Jolimont hospital/MRS unit)",
        "level": "other",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://jolimont.be",
        "foi_email": "secretariat.general@jolimont.be",
        "foi_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "notes": "tick2122 YE2025 Medium CW NL+EN+FR + Strong KBO 0748.968.276 Actief ASBL 0 VE NACE 87.101/86.109/88.911/68.201 aanbestedende overheid; bruto DROP 26.3k (-98.14% vs YE2024 1.42m) pnl FLIP 11.1k from LOSS -327.6k equity JUMP 78.4k (+16.52%) omzet YE2025 unpublished (YE2024 1.51m) FTE Micro 0 (was 13.7); assets/debt Unknown; filed 26.06.2026; FOI gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Le Bosquet/Entraide/Strebo/La Charmille/'t Buurthuis",
    },
)

for bid, amt, basis, year in [
    ("bud_unite_jolimont_bruto_jr2025_statutory", "26298", "CW YE2025 Brutomarge / Gross margin (primary YE2025 envelope; omzet unpublished)", "2025"),
    ("bud_unite_jolimont_pnl_jr2025_statutory", "11109", "CW YE2025 Profit/Loss FLIP from YE2024 LOSS -327626", "2025"),
    ("bud_unite_jolimont_equity_jr2025_statutory", "78367", "CW YE2025 Eigen vermogen / Equity", "2025"),
    ("bud_unite_jolimont_omzet_jr2024_prior", "1510548", "CW YE2024 Turnover prior-year residual (YE2025 omzet unpublished)", "2024"),
    ("bud_unite_jolimont_fte_jr2025_statutory", "0", "CW Micro 0 FTE / no employees YE2025 (was 13.7 YE2024)", "2025"),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2122; Medium CW; assets/debt Unknown pending NBB PDF; wind-down residual",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Unité Jolimont YE2025 leftover dual (bruto DROP 26k / pnl FLIP / FTE 0)",
        "entity_id": ENTITY,
        "beneficiary": "Hospital/MRS/creche continuum users (Jolimont; 0 VE YE2025)",
        "legal_basis": "ASBL hospital/MRS (KBO 0748.968.276; NACE 87.101/86.109/88.911; 0 VE; aanbestedende overheid)",
        "decision_date": "2026-06-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "26298",
        "cash_by_year": '{"2025_bruto":26298,"2025_pnl":11109,"2025_equity":78367,"2025_fte":0,"2024_omzet":1510548,"2024_bruto":1415916}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0748968276/unite-jolimont",
        "stated_goal": "Public-interest hospital/MRS/creche unit (Jolimont continuum; wind-down YE2025)",
        "cut_option": "Publish NBB PDF assets/debt FOI; explain bruto DROP -98% + omzet unpublished + FTE to 0 while Actief; map dual vs Le Bosquet/Entraide/Strebo",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>UniteJolimont>JR2025_statutory_L5",
        "notes": "tick2122; Medium CW; bruto primary YE2025 (omzet Unknown); YE2024 omzet 1.51m residual context; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Le Bosquet/Entraide/Strebo/'t Buurthuis",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "Unité Jolimont bruto DROP 26k / pnl FLIP / FTE→0 (YE2025 wind-down)",
        "level": "L5",
        "type": "hospital_mrs_statutory_asbl_jolimont_winddown",
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>UniteJolimont>JR2025",
        "annual_cost_eur": "26298",
        "total_cost_eur": "1510548",
        "tco_notes": "CW YE2025 bruto 26298 DROP -98.14% (primary); pnl 11109 FLIP from LOSS -327626; equity 78367 JUMP +16.52%; omzet YE2025 unpublished (YE2024 1510548 residual TCO context); FTE Micro 0 (was 13.7); assets/debt Unknown pending NBB PDF; 0 VE aanbestedende overheid Jolimont",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Hospital/MRS/creche continuum (Jolimont; 0 VE)",
        "stated_goal": "Public-interest hospital/MRS unit (AViQ-path Jolimont)",
        "measured_outcome": "bruto DROP -98.14%; pnl FLIP from LOSS; equity JUMP +16.52%; FTE to 0; omzet unpublished",
        "absurdity_score": "7.2",
        "cost_score": "2.8",
        "difficulty": "3.2",
        "priority_index": "5.8",
        "cut_proposal": "FOI NBB PDF + explain wind-down bruto DROP/omzet gap/FTE→0 while Actief aanbestedende overheid; dual vs Le Bosquet/Entraide/Strebo",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2122; Medium CW; FOI gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT Le Bosquet/Entraide/Strebo/La Charmille/'t Buurthuis",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>LaLouviere>UniteJolimont>NBB_PDF_assets_debt_winddown",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet unpublished path; bruto DROP -98% explanation; FTE to 0 vs Actief; dual Jolimont Le Bosquet/Entraide/Strebo matrix",
        "why_it_matters": "Medium CW shows Jolimont aanbestedende-overheid ASBL wind-down: bruto 26k from 1.42m, pnl FLIP from -328k LOSS, FTE Micro 0, omzet unpublished — opacity on residual public hospital/MRS path",
        "priority": "8",
        "recipient_body": "ASBL Unité Jolimont / Groupe Jolimont",
        "recipient_email": "secretariat.general@jolimont.be",
        "recipient_postal": "Rue Ferrer(PAU) 159, 7100 La Louviere",
        "draft_letter_path": "docs/doge/foi/drafts/gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick2122; human-send only; Medium CW; next every-10 2130",
    },
)

# Patch FOI draft tick number if needed
draft = "docs/doge/foi/drafts/gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5.md"
with open(draft, encoding="utf-8") as f:
    txt = f.read()
txt = txt.replace("**tick:** 2121", "**tick:** 2122")
with open(draft, "w", encoding="utf-8") as f:
    f.write(txt)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

# dedupe rq_2122/2123 if any
seen = set()
deduped = []
for row in rows:
    tid = row.get("task_id")
    if tid in ("rq_2122", "rq_2123") and tid in seen:
        continue
    if tid:
        seen.add(tid)
    deduped.append(row)
rows = deduped

has_2123 = any(row.get("task_id") == "rq_2123" for row in rows)
for row in rows:
    if row["task_id"] == "rq_2122":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["title"] = "leftover dual — Unité Jolimont YE2025 Medium"
        row["instructions"] = (
            "Completed leftover dual Unité Jolimont after 't Buurthuis; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO 0748.968.276; "
            "bruto DROP 26.3k pnl FLIP 11.1k equity JUMP 78.4k omzet unpublished FTE Micro 0; FOI ready NBB PDF; "
            "DISTINCT Le Bosquet/Entraide/Strebo/'t Buurthuis (rq_2121 race recovery)"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2122 Unité Jolimont YE2025 Medium CW; FOI ready not sent; next rq_2123; next every-10 2130"
if not has_2123:
    rows.append(
        {
            "task_id": "rq_2123",
            "title": "leftover dual hole-fill after Unité Jolimont — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2123 after Unité Jolimont YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche. Do NOT redo Unité Jolimont, "
                "'t Buurthuis Uccle, Le Bosquet, Strebo Services, Entraide Fraternelle Jolimont, La Charmille Pont-a-Celles, Residence Les Charmilles Sambreville, "
                "Les Sittelles Chastre, Les Buissons / Chateau Sous Bois Spa, Residence 3 / Saphir, Elisabeth Aan Zee Oostende, "
                "Maison de Repos du XXe Aout / PLIMCO, Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, "
                "IDELUX*, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, "
                "AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, "
                "AGB Bornem, Armonea, emeis, RSW."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2122 Unité Jolimont; FARO/AIESH/REW still YE2024; next every-10 2130",
        }
    )
with open(rq_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_2122",
            "ticks_completed": "2122",
            "paused": "no",
            "notes": (
                "tick2122 leftover Unité Jolimont 0748.968.276 Medium CW "
                "(bruto DROP 26.3k pnl FLIP 11.1k equity JUMP 78.4k omzet unpublished FTE Micro 0; "
                "assets/debt Unknown; 0 VE NACE 87.101/86.109/88.911 Jolimont hospital-MRS wind-down); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; 't Buurthuis/Le Bosquet taken; next rq_2123; next every-10 2130; continuous hole_fill"
            ),
        }
    )

# Fix mistaken Unité-as-2121 log block → note race + add 2122 entry
log_path = "docs/doge/loop_log.md"
with open(log_path, encoding="utf-8") as f:
    log = f.read()
# neutralize false 2121 Unité header if present
log = log.replace(
    "## Tick 2121 - 2026-08-25T10:40:00Z - rq_2121 Unite Jolimont (bruto DROP 26.3k / pnl FLIP 11.1k / FTE Micro 0 / Medium)",
    "## Tick 2121 RACE-NOTE - Unité Jolimont draft collided with concurrent 't Buurthuis; recovered as tick 2122",
)
entry = """

## Tick 2122 - 2026-08-25T10:55:00Z - rq_2122 Unité Jolimont (bruto DROP 26.3k / pnl FLIP 11.1k / FTE Micro 0 / Medium)

- Unit: **rq_2122** leftover dual after **rq_2121 't Buurthuis** (race: concurrent agent took rq_2121; this tick recovers Unité Jolimont research). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Unité Jolimont** YE2025 (KBO **0748.968.276**; Rue Ferrer(PAU) 159 La Louvière; **ASBL** NACE **87.101/86.109/88.911** / **0 VE**; aanbestedende overheid; Jolimont hospital-MRS wind-down). Do not redo 't Buurthuis/Le Bosquet/Strebo/Entraide/La Charmille/Charmilles/Sittelles/Buissons/Residence 3/Elisabeth Aan Zee/XXe Août/Ninove.
- Found: Companyweb NL+EN+FR YE2025 - bruto **EUR26298** DROP -98.14% vs YE2024 EUR1415916; pnl **EUR11109** FLIP from YE2024 LOSS EUR-327626; equity **EUR78367** JUMP +16.52%; omzet YE2025 **unpublished** (YE2024 EUR1510548); FTE **Micro 0** (was 13.7); neerlegging **26.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via secretariat.general@jolimont.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 asbl_unite_jolimont); foi + draft gap_unite_jolimont_nbb_pdf_assets_debt_winddown_bruto_drop_pnl_flip_matrix_l5; rq_2122=done + rq_2123 open; loop_state ticks=2122; raw docs/doge/data/raw/tick2122/; deduped duplicate rq_2122 open row.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: rq_2123 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
if "## Tick 2122 - 2026-08-25T10:55:00Z" not in log:
    log = log.rstrip() + entry
with open(log_path, "w", encoding="utf-8") as f:
    f.write(log)

print("OK tick2122 writes")
