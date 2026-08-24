# -*- coding: utf-8 -*-
import csv

csv.field_size_limit(10**7)
UTC = "2026-08-25T10:40:00Z"
ENTITY = "vzw_t_buurthuis_uccle"
GAP = "gap_buurthuis_nbb_pdf_assets_debt_ops_empty_neg_equity_matrix_l5"
COMM = "comm_buurthuis_jr2025_statutory_mrs_shell"
LB = "lb_buurthuis_ops_empty_neg_equity_16_71m_jr2025"
SRC_EN = "src_buurthuis_jr2025_cw_en"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


for s in [
    {
        "source_id": "src_buurthuis_jr2025_cw",
        "title": "Companyweb NL 't Buurthuis YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0435565236/-t-buurthuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2121; YE2025 omzet unpublished (YE2024 8462461) pnl -3557 equity NEG -16709239 bruto -3557 FTE empty; neerlegging 08.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2121/buurthuis_nl.html",
    },
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN 't Buurthuis YE2025 statutory",
        "url": "https://www.companyweb.be/en/0435565236/-t-buurthuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2121; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; Turnover unpublished; Equity NEG -16709239; raw docs/doge/data/raw/tick2121/buurthuis_en.html",
    },
    {
        "source_id": "src_buurthuis_jr2025_cw_fr",
        "title": "Companyweb FR 't Buurthuis YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0435565236/-t-buurthuis",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": "tick2121; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2121/buurthuis_fr.html",
    },
    {
        "source_id": "src_buurthuis_kbo_2121",
        "title": "KBO VZW 't Buurthuis 0435.565.236 Actief Uccle",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435565236",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": "tick2121; Actief VZW; Alsembergsesteenweg 1037 1180 Uccle; 0 VE; bestuurder/gedelegeerd emeis Belgium 0887.690.451 + Guichard/Van Houtte; same seat as RSW 0459.540.765",
    },
    {
        "source_id": "src_buurthuis_emeis_contact_2121",
        "title": "emeis Belgium / Senior Westland FOI contact path",
        "url": "https://emeis.be/fr/emplacements/maison-de-repos-et-de-soins/seniors-westland",
        "publisher": "emeis Belgium",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": "tick2121; senior.westland@emeis.com; Rue Adolphe Willemyns 224 Anderlecht ops brand; shell seat Uccle Alsemberg 1037",
    },
]:
    append_csv("docs/doge/data/sources.csv", s)

append_csv(
    "docs/doge/data/entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "'t Buurthuis (Ukkel / emeis-path MRS shell)",
        "name_fr": "ASBL 't Buurthuis (Uccle / coquille MRS emeis)",
        "name_en": "'t Buurthuis nursing-home ASBL shell (Uccle; emeis path)",
        "level": "other",
        "parent_id": "sec_brussels",
        "community_language": "nl",
        "website": "https://emeis.be/",
        "foi_email": "senior.westland@emeis.com",
        "foi_postal": "Chaussee d'Alsemberg 1037, 1180 Uccle",
        "notes": "tick2121 YE2025 Medium CW NL+EN+FR + Strong KBO 0435.565.236 Actief VZW 0 VE NACE 87.301 ROB; omzet YE2025 unpublished (YE2024 8.46m) bruto -3.6k pnl -3.6k equity NEG -16.71m FTE empty (was 102.3); assets/debt Unknown; filed 08.07.2026; FOI gap_buurthuis_nbb_pdf_assets_debt_ops_empty_neg_equity_matrix_l5; emeis Belgium bestuurder 0887.690.451; same seat as RSW SA; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT emeis holding / Le Bosquet / Strebo / Entraide",
    },
)

for bid, amt, basis in [
    ("bud_buurthuis_omzet_ye2024_last_ops", "8462461", "CW YE2024 omzet / last published operating envelope (YE2025 omzet unpublished)"),
    ("bud_buurthuis_equity_neg_jr2025_statutory", "-16709239", "CW YE2025 Eigen vermogen / Equity NEG"),
    ("bud_buurthuis_pnl_jr2025_statutory", "-3557", "CW YE2025 Profit/Loss near-zero"),
    ("bud_buurthuis_bruto_jr2025_statutory", "-3557", "CW YE2025 Brutomarge / Gross margin"),
    ("bud_buurthuis_fte_ye2024_last_ops", "102.3", "CW YE2024 FTE (YE2025 FTE empty)"),
]:
    append_csv(
        "docs/doge/data/budgets.csv",
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": "2025" if "jr2025" in bid else "2024",
            "amount_eur": amt,
            "amount_min_eur": amt,
            "amount_max_eur": amt,
            "basis": basis,
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2121; Medium CW; YE2025 ops emptied; assets/debt Unknown pending NBB PDF",
        },
    )

append_csv(
    "docs/doge/data/commitments.csv",
    {
        "commitment_id": COMM,
        "title": "'t Buurthuis YE2025 leftover dual (ops emptied / equity NEG 16.71m / last omzet 8.46m)",
        "entity_id": ENTITY,
        "beneficiary": "Former MRS residents / emeis path Brussels (ops emptied YE2025)",
        "legal_basis": "VZW maison de repos ROB (KBO 0435.565.236; NACE 87.301; 0 VE; emeis Belgium bestuurder)",
        "decision_date": "2026-07-08",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "8462461",
        "cash_by_year": '{"2024_omzet_last_ops":8462461,"2025_omzet":"unpublished","2025_pnl":-3557,"2025_equity":-16709239,"2025_bruto":-3557,"2024_fte":102.3}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0435565236/-t-buurthuis",
        "stated_goal": "Public-interest nursing-home care (emeis-path; Iriscare-adjacent) — ops emptied YE2025",
        "cut_option": "Publish NBB PDF assets/debt FOI; explain ops transfer destination + NEG equity -16.71m continuity; map Iriscare agrément vs emeis holding dual",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>Uccle>tBuurthuis>JR2025_statutory_L5",
        "notes": "tick2121; Medium CW; YE2024 omzet primary last-ops envelope; YE2025 omzet unpublished; assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT emeis holding / RSW SA deferred",
    },
)

append_csv(
    "docs/doge/data/leaderboard.csv",
    {
        "item_id": LB,
        "name": "'t Buurthuis ops emptied / equity NEG 16.71m / last omzet 8.46m (YE2025)",
        "level": "L5",
        "type": "mrs_statutory_asbl_emeis_shell",
        "hierarchy_path": "Bruxelles>Uccle>tBuurthuis>JR2025",
        "annual_cost_eur": "8462461",
        "total_cost_eur": "16709239",
        "tco_notes": "CW YE2025 omzet unpublished (YE2024 last ops 8462461 primary); bruto -3557; pnl -3557 near-zero vs YE2024 LOSS -4.03m; equity NEG -16709239; FTE empty (was 102.3); assets/debt Unknown pending NBB PDF; emeis Belgium bestuurder shell",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Former MRS care users (ops emptied YE2025; emeis path)",
        "stated_goal": "Public-interest nursing-home care (Iriscare-adjacent)",
        "measured_outcome": "YE2025 ops emptied (omzet/FTE blank); equity NEG -16.71m; pnl near-zero vs prior multi-m LOSS; last ops omzet 8.46m YE2024",
        "absurdity_score": "8.5",
        "cost_score": "5.5",
        "difficulty": "3.5",
        "priority_index": "7.1",
        "cut_proposal": "FOI NBB PDF + ops-transfer destination + explain chronic NEG equity -16.71m; dual emeis holding / RSW SA / Iriscare agrément",
        "status": "open",
        "struck_reason": "",
        "notes": "tick2121; Medium CW; FOI gap_buurthuis_nbb_pdf_assets_debt_ops_empty_neg_equity_matrix_l5; preferred FARO/AIESH/REW still YE2024; DISTINCT emeis holding; RSW deferred",
    },
)

append_csv(
    "docs/doge/data/foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Bruxelles>Uccle>tBuurthuis>NBB_PDF_assets_debt_ops_empty_neg_equity",
        "entity_id": ENTITY,
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); YE2025 omzet unpublished / ops-empty path; FTE empty vs 102.3; NEG equity -16.71m continuity; ops transfer destination vs emeis Belgium / RSW SA / Iriscare",
        "why_it_matters": "Medium CW shows emptied MRS ASBL shell (was 8.46m omzet / 102 FTE) with chronic NEG equity -16.71m under emeis Belgium bestuurder — material public-care continuity + insolvency transparency gap",
        "priority": "9",
        "recipient_body": "VZW 't Buurthuis / emeis Belgium",
        "recipient_email": "senior.westland@emeis.com",
        "recipient_postal": "Chaussee d'Alsemberg 1037, 1180 Uccle",
        "draft_letter_path": "docs/doge/foi/drafts/gap_buurthuis_nbb_pdf_assets_debt_ops_empty_neg_equity_matrix_l5.md",
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
        "notes": "tick2121; human-send only; Medium CW; next every-10 2130",
    },
)

rq_path = "docs/doge/data/research_queue.csv"
with open(rq_path, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row["task_id"] == "rq_2121":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed: leftover dual 't Buurthuis after Le Bosquet; preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
            "live YE2025 Medium CW NL+EN+FR + Strong KBO 0435.565.236; ops emptied omzet unpublished equity NEG 16.71m last omzet 8.46m; "
            "FOI ready NBB PDF; DISTINCT emeis holding / RSW deferred"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2121 't Buurthuis YE2025 Medium CW ops-empty NEG equity; FOI ready not sent; next rq_2122; next every-10 2130"
rows.append(
    {
        "task_id": "rq_2122",
        "title": "leftover dual hole-fill after 't Buurthuis — prefer AGB/FARO-YE2025/AIESH-REW/RSW/unused IGS-DSO-WZC-MRS",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 2122 after 't Buurthuis YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else Residence Senior's Westland SA 0459.540.765 if unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
            "Do NOT redo 't Buurthuis, Le Bosquet, Strebo Services, Entraide Fraternelle Jolimont, La Charmille, Les Charmilles Sambreville, "
            "Les Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, "
            "Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, AIEG, RESA, Enodia, "
            "Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, emeis."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick2121 't Buurthuis; FARO/AIESH/REW still YE2024; RSW deferred; next every-10 2130",
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
            "last_unit_id": "rq_2121",
            "ticks_completed": "2121",
            "paused": "no",
            "notes": (
                "tick2121 leftover 't Buurthuis 0435.565.236 Medium CW "
                "(ops emptied YE2025 omzet unpublished last ops 8.46m equity NEG -16.71m pnl -3.6k FTE empty was 102.3; "
                "assets/debt Unknown; emeis Belgium bestuurder shell Uccle); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Le Bosquet taken; RSW deferred; next rq_2122; next every-10 2130; continuous hole_fill"
            ),
        }
    )

print("OK tick2121 writes")
