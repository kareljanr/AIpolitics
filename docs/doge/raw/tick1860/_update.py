import csv
from pathlib import Path

csv.field_size_limit(10**7)
DATA = Path("docs/doge/data")
now = "2026-08-26T02:15:00Z"
tick = 1860
eid = "onroerend_erfgoed"
src = "src_diependaele_ioed_oeg_package"
url = (
    "https://www.matthiasdiependaele.be/nieuws/"
    "minister-diependaele-steunt-lokale-onroerenderfgoedwerking-met-in-totaal-32-miljoen-euro"
)
IOED = 2684667.73
OEG = 390000.0
HYDRA_BK = 178106.80  # subset of IOED, not additive
TOTAL = IOED + OEG  # 3074667.73


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
        "title": "Minister Diependaele — IOED+OEG subsidies named table (~3.075m)",
        "url": url,
        "publisher": "Kabinet / Matthias Diependaele (Onroerend Erfgoed)",
        "accessed_date": "2026-08-26",
        "source_class": "official_web",
        "notes": (
            "tick1860; 30 IOED 2684667.73 + 11 OEG 390000; Hydra+BK first-year 178106.80 "
            "subset of 30 (not additive); SWO 2021-2026 / 2024-2026"
        ),
    },
    {
        "source_id": "src_oe_ioed_erkend_portal",
        "title": "Agentschap Onroerend Erfgoed — erkende IOED instrument",
        "url": "https://www.onroerenderfgoed.be/een-erkende-ioed",
        "publisher": "Agentschap Onroerend Erfgoed",
        "accessed_date": "2026-08-26",
        "source_class": "official_register",
        "notes": "tick1860; linked from Diependaele announcement; instrument page",
    },
]
write_csv("sources.csv", sources, scols)

budgets, bcols = read_csv("budgets.csv")
for bid, amt, basis in [
    ("bud_ioed_package_2_685m_diependaele", int(round(IOED)), "Diependaele named 30-IOED annual subsidy table"),
    ("bud_oeg_package_0_390m_diependaele", int(round(OEG)), "Diependaele named 11-OEG first subsidy table"),
    ("bud_ioed_oeg_total_3_075m_diependaele", int(round(TOTAL)), "IOED+OEG headline package (Hydra/BK subset not added)"),
    ("bud_ioed_hydra_bk_first_0_178m_subset", int(round(HYDRA_BK)), "Hydra+Erfgoed Brabantse Kouters first-year SUBSET of 30"),
]:
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": eid,
            "year": "2024",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": f"tick{tick}; {basis}; may overlap IOED JR code73; not TE-additive; year from SWO/first-year note",
        }
    )
write_csv("budgets.csv", budgets, bcols)

# entity onroerend_erfgoed should already exist — append note only if missing
ents, ecols = read_csv("entities.csv")
have = any(e.get("entity_id") == eid for e in ents)
if not have:
    ents.append(
        {
            "entity_id": eid,
            "name_nl": "Agentschap Onroerend Erfgoed",
            "name_fr": "Agence du Patrimoine",
            "name_en": "Flanders Immovable Heritage Agency",
            "level": "agency",
            "parent_id": "vl_gov",
            "community_language": "nl",
            "website": "https://www.onroerenderfgoed.be/",
            "foi_email": "openbaarheid@vlaanderen.be",
            "foi_postal": "Havenlaan 88 1000 Brussel",
            "notes": "tick1860 Diependaele IOED+OEG named package booked",
        }
    )
else:
    for e in ents:
        if e.get("entity_id") == eid:
            prev = e.get("notes") or ""
            add = "tick1860 Diependaele IOED 2.685m + OEG 0.390m named L5"
            if "tick1860 Diependaele" not in prev:
                e["notes"] = (prev + "; " + add).strip("; ")
            break
write_csv("entities.csv", ents, ecols)

comms, ccols = read_csv("commitments.csv")
comms += [
    {
        "commitment_id": "comm_ioed_package_2_685m_diependaele",
        "title": "Flanders IOED annual operating subsidies 30 named (EUR 2.685m)",
        "entity_id": eid,
        "beneficiary": "30 erkende IOEDs / 214+ municipalities",
        "legal_basis": "Onroerenderfgoeddecreet; SWO IOED 2021-2026",
        "decision_date": "2024-01-01",
        "start_year": "2024",
        "end_year": "2026",
        "total_envelope_eur": str(int(round(IOED))),
        "cash_by_year": f"{{2024:{int(round(IOED))}}}",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": url,
        "stated_goal": "Local immovable-heritage capacity via intermunicipal IOEDs",
        "cut_option": "FOI besluit PDF + VAK/VEK map; publish remaining SWO years",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>IOED>named_package_L5",
        "notes": (
            "tick1860; Berg en Nete 85613.77 … WinAr 95775.25; Hydra+BK 178106.80 subset; "
            "may overlap mined IOED JR bruto; not TE-additive"
        ),
    },
    {
        "commitment_id": "comm_oeg_package_0_390m_diependaele",
        "title": "Flanders OEG first operating subsidies 11 named (EUR 0.390m)",
        "entity_id": eid,
        "beneficiary": "Beernem Bilzen Brugge Gent Koksijde Kontich Leuven Riemst Roeselare Voeren Zonnebeke",
        "legal_basis": "Onroerenderfgoeddecreet; erkende onroerenderfgoedgemeente",
        "decision_date": "2024-01-01",
        "start_year": "2024",
        "end_year": "2026",
        "total_envelope_eur": str(int(round(OEG))),
        "cash_by_year": f"{{2024:{int(round(OEG))}}}",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": url,
        "stated_goal": "First operating subsidy to 11 onroerenderfgoedgemeenten",
        "cut_option": "FOI besluit + multi-year path; Brugge/Gent/Leuven 90k each",
        "source_id": src,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>OEG>named_package_L5",
        "notes": "tick1860; Brugge/Gent/Leuven 90000; Roeselare 50000; eight at 10000; additive to IOED package",
    },
]
write_csv("commitments.csv", comms, ccols)

lbs, lcols = read_csv("leaderboard.csv")
lbs += [
    {
        "item_id": "lb_ioed_package_2_685m_diependaele",
        "name": "IOED named annual package EUR2.685m (30 IOED / Diependaele)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>IOED>named_package_L5",
        "annual_cost_eur": str(int(round(IOED))),
        "total_cost_eur": str(int(round(IOED))),
        "tco_notes": "30 named IOED; Hydra+BK 178k subset; SWO 2021-2026; may overlap entity JR",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "30 IOEDs covering 214+ VL municipalities",
        "stated_goal": "Local heritage policy capacity",
        "measured_outcome": "Named per-IOED table published; besluit PDF residual FOI",
        "absurdity_score": "3.5",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "3.55",
        "cut_proposal": "Publish besluit+VAK path; review formula vs protected-stock metrics",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1860; EVERY-10; subset of OE agency package; not TE-additive",
    },
    {
        "item_id": "lb_oeg_package_0_390m_diependaele",
        "name": "OEG first subsidies EUR0.390m (11 cities / Diependaele)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>OEG>named_package_L5",
        "annual_cost_eur": str(int(round(OEG))),
        "total_cost_eur": str(int(round(OEG))),
        "tco_notes": "Brugge/Gent/Leuven 90k; Roeselare 50k; eight 10k",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "11 onroerenderfgoedgemeenten",
        "stated_goal": "First OEG operating subsidy wave",
        "measured_outcome": "Named table published; besluit residual FOI",
        "absurdity_score": "3.0",
        "cost_score": "1.5",
        "difficulty": "3.0",
        "priority_index": "2.25",
        "cut_proposal": "FOI multi-year path; avoid double-count with city OE spend",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1860; additive to IOED 2.685m; not TE-additive",
    },
    {
        "item_id": "lb_ioed_oeg_total_3_075m_diependaele",
        "name": "IOED+OEG Diependaele named total EUR3.075m (~3.2m headline)",
        "level": "L5",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>IOED_OEG>named_package_L5",
        "annual_cost_eur": str(int(round(TOTAL))),
        "total_cost_eur": str(int(round(TOTAL))),
        "tco_notes": "2.68466773m + 0.390m; Hydra/BK not double-counted",
        "confidence": "strong",
        "source_id": src,
        "beneficiaries": "30 IOED + 11 OEG",
        "stated_goal": "Local OE capacity package",
        "measured_outcome": "Public named table; formal besluit FOI",
        "absurdity_score": "3.5",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "3.55",
        "cut_proposal": "Map into BO OE VEK; publish remaining SWO cash",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1860; headline ~3.2m; dual L5 fill; not TE-additive",
    },
]
write_csv("leaderboard.csv", lbs, lcols)

fois, fcols = read_csv("foi_queue.csv")
fois.append(
    {
        "gap_id": "gap_ioed_oeg_diependaele_besluit_year_vak_l5",
        "hierarchy_path": "Vlaanderen>Omgeving>OnroerendErfgoed>IOED_OEG>besluit_VAK_L5",
        "entity_id": eid,
        "what_is_missing": (
            "Formal ministerieel besluit PDF + exact award/cash year(s); VAK/VEK mapping "
            "inside BO OE package; confirm Hydra+BK 178106.80 is subset of 30-IOED total; "
            "remaining SWO years cash path per IOED/OEG"
        ),
        "why_it_matters": (
            "Named L5 table now public (~3.075m) but besluit/year/BO mapping still opaque; "
            "needed to avoid double-count vs agency OE package and mined IOED JR bruto"
        ),
        "priority": "7",
        "recipient_body": "Agentschap Onroerend Erfgoed / openbaarheid Vlaanderen",
        "recipient_email": "openbaarheid@vlaanderen.be",
        "recipient_postal": "Havenlaan 88 1000 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_ioed_oeg_diependaele_besluit_year_vak_l5.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_ioed_package_2_685m_diependaele|comm_oeg_package_0_390m_diependaele",
        "linked_leaderboard_id": "lb_ioed_oeg_total_3_075m_diependaele",
        "created_utc": now,
        "updated_utc": now,
        "notes": "tick1860 EVERY-10+leftover; human-send only; Dijk92 CDN403 still ready separately",
    }
)
write_csv("foi_queue.csv", fois, fcols)

rq, rcols = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_1860":
        row["status"] = "done"
        row["entity_id"] = eid
        row["blocked_gap_id"] = "gap_ioed_oeg_diependaele_besluit_year_vak_l5"
        row["updated_utc"] = now
        row["notes"] = (
            "tick1860 DONE EVERY-10 progress+waste refreshed; leftover Diependaele IOED "
            "2.685m + OEG 0.390m named Strong; Hydra+BK 0.178m subset; besluit/VAK FOI; "
            "AGB Bornem JR2024; Dijk92 403; FARO YE2024"
        )
rq.append(
    {
        "task_id": "rq_1861",
        "title": "Leftover dual residual hole-fill after Diependaele IOED+OEG (AGB/Dijk92/FARO/other HVZ-if-live / other IGS)",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>leftover_dual",
        "entity_id": "",
        "instructions": (
            "Tick 1861 after 1860 EVERY-10 + Diependaele IOED/OEG. Prefer leftover AGB/APB if PDF live, "
            "else Dijk92/Enebra if CDN 200, else FARO if TRUE NBB YE2025, else other HVZ/IGS with live "
            "official JR2025 euros (prefer full rekening not besluit-only). DiependaeleIOED+Audio+"
            "TerNetheFOI+Beschut+DeWijngaard+WVBlankenberge+WZGVoorkempen+KINA taken. Skip done. "
            "Prefer NON-Eneco. Next every-10 1870."
        ),
        "blocked_gap_id": "",
        "created_utc": now,
        "updated_utc": now,
        "notes": "spawned after tick1860; next every-10 1870",
    }
)
write_csv("research_queue.csv", rq, rcols)

ls, lsc = read_csv("loop_state.csv")
for row in ls:
    if row.get("state_id") == "main":
        row["last_tick_utc"] = now
        row["last_unit_id"] = "rq_1860"
        row["ticks_completed"] = "1860"
        row["paused"] = "no"
        row["notes"] = (
            "tick1860 EVERY-10 progress+waste + leftover Diependaele IOED 2.685m + OEG 0.390m "
            "(Hydra+BK 0.178m subset); besluit/VAK FOI; AGB Bornem JR2024; Dijk92 403; FARO YE2024; "
            "next rq_1861; next every-10 1870; continuous hole_fill"
        )
write_csv("loop_state.csv", ls, lsc)

print(
    "OK",
    tick,
    "budgets",
    len(budgets),
    "comms",
    len(comms),
    "lbs",
    len(lbs),
    "foi",
    len(fois),
    "rq",
    len(rq),
)
