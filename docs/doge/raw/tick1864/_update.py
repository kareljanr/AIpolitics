import csv
from pathlib import Path

csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
now = "2026-08-26T03:50:00Z"
tick = 1864
eid = "nv_bcva"
pdf_url = "http://cdn.staatsbladmonitor.be/2025pdf/2025-00574885.pdf"
src = "src_bcva_jr2025_nbb"
gap = "gap_bcva_omzet_empty_bruto_0_28m_pers_0_12m_l5"

ASSETS = 1650183
EQUITY = 1075358
BRUTO = 284037
PERS = 118696
PNL = 2361
DEBT = 574825
CASH = 61470
BUILDINGS = 1323575
CAPITAL = 1145000
FIN_DEBT_LT = 361213


def read_csv(name):
    with (DATA / name).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(name, rows, fieldnames):
    with (DATA / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})


sources, scols = read_csv("sources.csv")
sources += [
    {
        "source_id": src,
        "title": "Bedrijvencentrum Vlaamse Ardennen NBB MIC-kap FY2024/25 deposit 2025-00574885",
        "url": pdf_url,
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": "2026-08-26",
        "source_class": "primary_pdf",
        "notes": (
            "tick1864; 67138 bytes / 22p; AV 21.11.2025; YE 30.06.2025; assets 1650183 bruto 284037 "
            "pers 118696 pnl 2361 equity 1075358 debt 574825 cash 61470; omzet 70 empty"
        ),
    },
    {
        "source_id": "src_kbo_bcva_0430712662",
        "title": "KBO Bedrijvencentrum Vlaamse Ardennen NV 0430.712.662",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430712662",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick1864; zetel Meersbloem-Melden 46 9700 Oudenaarde; board Fluvius/Artevelde/Aarova",
    },
]
write_csv("sources.csv", sources, scols)

budgets, bcols = read_csv("budgets.csv")
for bid, amt, basis in [
    ("bud_bcva_assets_1_65m_jr2025", ASSETS, "NBB 20/58 balanstotaal YE30062025"),
    ("bud_bcva_bruto_0_28m_jr2025", BRUTO, "NBB 9900 brutomarge"),
    ("bud_bcva_pers_0_12m_jr2025", PERS, "NBB 62 / sociale balans 102"),
    ("bud_bcva_pnl_2_4k_jr2025", PNL, "NBB 9904 winst boekjaar"),
    ("bud_bcva_equity_1_08m_jr2025", EQUITY, "NBB 10/15 eigen vermogen"),
    ("bud_bcva_debt_0_57m_jr2025", DEBT, "NBB 17/49 schulden"),
    ("bud_bcva_cash_61k_jr2025", CASH, "NBB 54/58 liquide middelen"),
]:
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": eid,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": f"tick{tick}; FY 01.07.2024-30.06.2025; not TE-additive",
        }
    )
write_csv("budgets.csv", budgets, bcols)

ents, ecols = read_csv("entities.csv")
if not any(e.get("entity_id") == eid for e in ents):
    ents.append(
        {
            "entity_id": eid,
            "name_nl": "Bedrijvencentrum Vlaamse Ardennen NV (leftover IGS/NV bedrijfencentrum Oudenaarde belt)",
            "name_fr": "Centre d'entreprises Ardennes flamandes SA",
            "name_en": "Flemish Ardennes Business Centre NV (leftover public-perimeter)",
            "level": "other",
            "parent_id": "city_oudenaarde",
            "community_language": "nl",
            "website": "https://www.bedrijvencentrum-vlaamseardennen.be/",
            "foi_email": "info@bedrijvencentrumva.be",
            "foi_postal": "Meersbloem-Melden 46 9700 Oudenaarde",
            "notes": (
                "tick1864 leftover after Bosgroep/Dijk92/FARO hunt; KBO 0430.712.662; NBB YE30062025 "
                "live; assets 1.65m bruto 0.28m pers 0.12m pnl +2.4k; board Fluvius/Artevelde/Aarova; "
                "omzet empty FOI"
            ),
        }
    )
write_csv("entities.csv", ents, ecols)

comms, ccols = read_csv("commitments.csv")
comms += [
    {
        "commitment_id": "comm_bcva_jr2025_bruto",
        "title": "BCVA FY2024/25 leftover bedrijfencentrum dual (bruto 0.28m / pers 0.12m / PnL +2.4k)",
        "entity_id": eid,
        "beneficiary": "SME tenants / Oudenaarde-Vlaamse Ardennen dual perimeter",
        "legal_basis": "WVV NV; NBB neerlegging; Bestuursdecreet openbaarheid",
        "decision_date": "2025-11-21",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": str(BRUTO),
        "cash_by_year": f"{{fy2024_25:{BRUTO}}}",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": pdf_url,
        "stated_goal": "Local business centre / incubator buildings",
        "cut_option": "FOI omzet70 empty + shareholder % + public subsidy path",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>BCVA>JR2025_L5",
        "notes": (
            f"tick{tick}; assets {ASSETS} equity {EQUITY} buildings {BUILDINGS} debt {DEBT} "
            f"finLT {FIN_DEBT_LT} cash {CASH} pers {PERS} VTE~2; overgedragen -75740; dividend 0"
        ),
    },
    {
        "commitment_id": "comm_bcva_buildings_1_32m_jr2025",
        "title": "BCVA terreinen/gebouwen 1.324m YE30062025",
        "entity_id": eid,
        "beneficiary": "Business centre tenants",
        "legal_basis": "NBB MIC-kap code 22",
        "decision_date": "2025-11-21",
        "start_year": "2024",
        "end_year": "2025",
        "total_envelope_eur": str(BUILDINGS),
        "cash_by_year": "",
        "remaining_eur": str(BUILDINGS),
        "status": "active",
        "evaluation_url": pdf_url,
        "stated_goal": "Real-estate shell for regional SME centre",
        "cut_option": "FOI tenant matrix public vs private",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>BCVA>JR2025_L5",
        "notes": f"tick{tick}; MVA buildings core of 1.42m vaste activa",
    },
]
write_csv("commitments.csv", comms, ccols)

lbs, lcols = read_csv("leaderboard.csv")
lbs += [
    {
        "item_id": "lb_bcva_bruto_0_28m_omzet_empty_jr2025",
        "name": "BCVA bruto 0.28m / omzet empty / pers 0.12m (Fluvius board dual)",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>BCVA>JR2025_L5",
        "annual_cost_eur": str(BRUTO),
        "total_cost_eur": str(ASSETS),
        "tco_notes": "bruto 284037 omzet70 empty pers 118696 VTE2 pnl +2361 equity 1.08m debt 0.57m",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "SME tenants / public-perimeter shareholders",
        "stated_goal": "Regional business centre",
        "measured_outcome": "PnL swing from -38.8k to +2.4k; cum loss still -75.7k",
        "absurdity_score": "5.5",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "4.35",
        "cut_proposal": "Publish omzet/huur/subsidy split + shareholder %",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1864; primary NBB; leftover IGS/NV dual; not TE-additive",
    },
    {
        "item_id": "lb_bcva_buildings_1_32m_debt_0_57m_jr2025",
        "name": "BCVA buildings 1.32m / debt 0.57m / cash 61k",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>BCVA>JR2025_L5",
        "annual_cost_eur": str(DEBT),
        "total_cost_eur": str(BUILDINGS),
        "tco_notes": "buildings 1323575 finLT 361213 total debt 574825 cash 61470 capital 1145000",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "BCVA treasury / bank creditors",
        "stated_goal": "Property-backed business centre",
        "measured_outcome": "Debt declining vs prior 669k",
        "absurdity_score": "4.5",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "4.0",
        "cut_proposal": "FOI tenant rents vs debt service",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1864; primary NBB; not TE-additive",
    },
]
write_csv("leaderboard.csv", lbs, lcols)

fois, fcols = read_csv("foi_queue.csv")
fois.append(
    {
        "gap_id": gap,
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Oudenaarde>BCVA>omzet_share_L5",
        "entity_id": eid,
        "what_is_missing": (
            "Omzet 70 empty vs bruto 284037 path (huur/subsidies); aandeelhouders % "
            "(gemeenten/Fluvius/Artevelde/Aarova/private); public subsidies 2024-25; "
            "tenant matrix buildings 1.32m; AV 21.11.2025 notulen"
        ),
        "why_it_matters": (
            "Public-perimeter bedrijfencentrum with Fluvius/Artevelde/Aarova on board — "
            "empty omzet hides rent/subsidy dual of mined Oudenaarde belt"
        ),
        "priority": "7",
        "recipient_body": "Bedrijvencentrum Vlaamse Ardennen NV / raad van bestuur",
        "recipient_email": "info@bedrijvencentrumva.be",
        "recipient_postal": "Meersbloem-Melden 46 9700 Oudenaarde",
        "draft_letter_path": f"docs/doge/foi/drafts/{gap}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_bcva_jr2025_bruto",
        "linked_leaderboard_id": "lb_bcva_bruto_0_28m_omzet_empty_jr2025",
        "created_utc": now,
        "updated_utc": now,
        "notes": "tick1864 residual; human-send only; Dijk92 403; FARO YE2024; Bosgroep IJzer still unpublished",
    }
)
write_csv("foi_queue.csv", fois, fcols)

rq, rcols = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_1864":
        row["status"] = "done"
        row["entity_id"] = eid
        row["blocked_gap_id"] = gap
        row["updated_utc"] = now
        row["notes"] = (
            "tick1864 DONE Bedrijvencentrum Vlaamse Ardennen NV KBO 0430.712.662 NBB "
            "2025-00574885 FY YE30062025; assets 1.65m bruto 0.28m pers 0.12m pnl +2.4k; "
            "omzet empty FOI; AGB Bornem JR2024; Dijk92 403; FARO YE2024; Bosgroep IJzer no deposit"
        )
rq.append(
    {
        "task_id": "rq_1865",
        "title": "Leftover dual residual hole-fill after BCVA (AGB/Dijk92/FARO/Bosgroep IJzer-if-CDN / other HVZ-IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1865 after 1864 BCVA NBB. Prefer leftover AGB/APB if PDF live, else Dijk92/Enebra "
            "if CDN 200, else FARO if TRUE NBB YE2025, else Bosgroep IJzer en Leie if CDN 200, else "
            "other HVZ/IGS live JR2025 euros. BCVA+BosgroepHoutlandFOI+Digipolis+BosgroepLimburgFOI "
            "taken. Skip done. Prefer NON-Eneco. Next every-10 1870."
        ),
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": now,
        "notes": "spawned after tick1864; next every-10 1870",
    }
)
write_csv("research_queue.csv", rq, rcols)

ls, lsc = read_csv("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = now
        row["last_unit_id"] = "rq_1864"
        row["ticks_completed"] = "1864"
        row["paused"] = "no"
        row["notes"] = (
            "tick1864 leftover BCVA NV 0430.712.662 NBB YE30062025 (assets 1.65m bruto 0.28m "
            "pers 0.12m pnl +2.4k); omzet empty FOI; AGB Bornem JR2024; Dijk92 403; FARO YE2024; "
            "next rq_1865; next every-10 1870; continuous hole_fill"
        )
write_csv("loop_state.csv", ls, lsc)

print("OK", tick, "budgets", len(budgets), "foi", len(fois))
