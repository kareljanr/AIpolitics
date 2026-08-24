# tick 2283: leftover dual Ateljee Gent YE2025 hole-fill — claim queue FIRST
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2283"
TS = "2026-08-27T13:30:00Z"
ENTITY = "vzw_ateljee_gent"
GAP = "gap_ateljee_nbb_pdf_assets_debt_omzet_jump_10_66m_pnl_loss_flip_fte_jump_matrix_l5"
LB = "lb_ateljee_omzet_10_66m_bruto_1_83x_pnl_loss_flip_fte_jump_jr2025"
COMM = "comm_ateljee_jr2025_statutory_maatwerk_omzet_jump_pnl_loss_flip_fte_jump"
SRC_EN = "src_ateljee_jr2025_cw_en"

OMZET = 10664761
BRUTO = 19503939
PNL = -860427
EQUITY = 8129150
FTE = 478.6
OMZET24 = 8765694
BRUTO24 = 14963833
PNL24 = 37727
EQUITY24 = 8401418
FTE24 = 355.2
RATIO = round(BRUTO / OMZET, 2)  # 1.83


def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


# --- CLAIM rq_2283 FIRST ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

claimed = False
for r in rq_rows:
    if r.get("task_id") == "rq_2283":
        if r.get("status") != "open":
            raise SystemExit(f"rq_2283 already claimed status={r.get('status')} title={r.get('title')}")
        r["status"] = "in_progress"
        r["entity_id"] = ENTITY
        r["updated_utc"] = TS
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Ateljee Gent in_progress"
        claimed = True
        break
if not claimed:
    raise SystemExit("rq_2283 not found")

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)
print(f"CLAIMED rq_2283 -> in_progress {ENTITY}")

# --- sources ---
src_fields = [
    "source_id",
    "title",
    "url",
    "publisher",
    "accessed_date",
    "source_class",
    "notes",
]
sources = [
    {
        "source_id": SRC_EN,
        "title": "Ateljee YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0430839554/ateljee",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 30.06.2026; assets/debt Unknown; restructuring pub 11.04.2025",
    },
    {
        "source_id": "src_ateljee_jr2025_cw_nl",
        "title": "Ateljee YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0430839554/ateljee",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 30.06.2026; NACE beschutte werkplaatsen; VZW Ateljee Gent",
    },
    {
        "source_id": "src_ateljee_jr2025_cw_fr",
        "title": "Ateljee YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0430839554/ateljee",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Gent; CA {OMZET}; marge brute {BRUTO}; perte {PNL}",
    },
    {
        "source_id": "src_ateljee_kbo_0430839554",
        "title": "KBO Ateljee 0430.839.554",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0430839554",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW ATELJEE sinds 04.03.1985; 19 VE; Getouwstraat 11 9000 Gent sinds 29.01.2020; RSZ/BTW NACE 88.993 (+81.300/47.793/56.111)",
    },
    {
        "source_id": "src_ateljee_site_contact_2283",
        "title": "Ateljee FOI channel info@ateljeevzw.be",
        "url": "https://ateljeevzw.be/neem-contact-op",
        "publisher": "Ateljee VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@ateljeevzw.be; +32 9 224 07 15; Getouwstraat 11 Gent; Flemish maatwerk / Kringwinkel Ateljee",
    },
]
append_csv(ROOT / "sources.csv", src_fields, sources)

bud_fields = [
    "budget_id",
    "entity_id",
    "year",
    "amount_eur",
    "amount_min_eur",
    "amount_max_eur",
    "basis",
    "source_id",
    "confidence",
    "notes",
]
budgets = [
    {
        "budget_id": "bud_ateljee_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +21.66% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ateljee_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +30.34% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_ateljee_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl LOSS FLIP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP < -1000% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ateljee_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity DROP -3.24% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ateljee_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": f"CW social-balance FTE {FTE}",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE24} (+34.7%); assets/debt Unknown; restructuring 11.04.2025",
    },
    {
        "budget_id": "bud_ateljee_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS FLIP)",
    },
]
append_csv(ROOT / "budgets.csv", bud_fields, budgets)

cash = {
    "2025_omzet": OMZET,
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
    "2024_omzet": OMZET24,
    "2024_bruto": BRUTO24,
    "2024_pnl": PNL24,
    "2024_equity": EQUITY24,
    "2024_fte": FTE24,
}
comm_fields = [
    "commitment_id",
    "title",
    "entity_id",
    "beneficiary",
    "legal_basis",
    "decision_date",
    "start_year",
    "end_year",
    "total_envelope_eur",
    "cash_by_year",
    "remaining_eur",
    "status",
    "evaluation_url",
    "stated_goal",
    "cut_option",
    "source_id",
    "confidence",
    "hierarchy_path",
    "notes",
]
commitments = [
    {
        "commitment_id": COMM,
        "title": f"Ateljee YE2025 leftover dual (omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP / FTE JUMP {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "Maatwerkers / Kringwinkel Ateljee Gent path",
        "legal_basis": "VZW Ateljee (KBO 0430.839.554; Actief; 19 VE; NACE 88.993; Gent; restructuring pub 11.04.2025)",
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0430839554/ateljee",
        "stated_goal": "Flemish maatwerk / Kringwinkel reuse + inclusive employment Gent",
        "cut_option": "Publish NBB PDF assets/debt; reconcile LOSS FLIP + FTE JUMP +34.7% post-restructuring vs Vlaamse maatwerk wage-intervention matrix",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ateljee>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; FTE JUMP {FTE}; 19 VE VZW; after Die Zukunft@2282; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024",
    }
]
append_csv(ROOT / "commitments.csv", comm_fields, commitments)

lb_fields = [
    "item_id",
    "name",
    "level",
    "type",
    "hierarchy_path",
    "annual_cost_eur",
    "total_cost_eur",
    "tco_notes",
    "confidence",
    "source_id",
    "beneficiaries",
    "stated_goal",
    "measured_outcome",
    "absurdity_score",
    "cost_score",
    "difficulty",
    "priority_index",
    "cut_proposal",
    "status",
    "struck_reason",
    "notes",
]
leaderboard = [
    {
        "item_id": LB,
        "name": f"Ateljee omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP -0.86m / FTE JUMP {FTE} (YE2025 Flemish maatwerk Gent)",
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ateljee>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet JUMP {OMZET} (+21.66%) / bruto JUMP {BRUTO} (+30.34%; ~{RATIO}x) / pnl LOSS FLIP {PNL} (< -1000% vs {PNL24}) / equity DROP {EQUITY} (-3.24%) / FTE JUMP {FTE} (vs {FTE24} +34.7%) / 19 VE post-restructuring Flemish maatwerk Kringwinkel",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Maatwerkers / Kringwinkel clients Gent region",
        "stated_goal": "Flemish maatwerkbedrijf / Kringwinkel reuse + inclusive employment",
        "measured_outcome": f"omzet JUMP +21.66%; bruto JUMP +30.34%; pnl LOSS FLIP; equity DROP -3.24%; FTE JUMP +34.7% to {FTE}; restructuring pub 11.04.2025; filed 30.06.2026",
        "absurdity_score": 7.5,
        "cost_score": 6.2,
        "difficulty": 3.0,
        "priority_index": 6.70,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose Vlaamse maatwerk matrix + merger/restructuring behind LOSS FLIP despite omzet JUMP +22% and FTE JUMP +35%",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after Die Zukunft@2282; unused FREE vs mined Den Azalee/Alternatief/IN-Z/m-accent/AMAB stack",
    }
]
append_csv(ROOT / "leaderboard.csv", lb_fields, leaderboard)

ent_fields = [
    "entity_id",
    "name_nl",
    "name_fr",
    "name_en",
    "level",
    "parent_id",
    "community_language",
    "website",
    "foi_email",
    "foi_postal",
    "notes",
]
entities = [
    {
        "entity_id": ENTITY,
        "name_nl": "Ateljee VZW (Gent / Vlaams maatwerk Kringwinkel)",
        "name_fr": "Ateljee ASBL (Gand / entreprise de travail adapté flamande)",
        "name_en": "Ateljee adapted-work ASBL (Ghent Flemish maatwerk / Kringwinkel)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://ateljeevzw.be/",
        "foi_email": "info@ateljeevzw.be",
        "foi_postal": "Getouwstraat 11, 9000 Gent",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0430.839.554 Actief 19 VE VZW NACE 88.993; omzet JUMP {OMZET} (+21.66%) bruto JUMP {BRUTO} (~{RATIO}x / +30.34%) pnl LOSS FLIP {PNL} equity DROP {EQUITY} (-3.24%) FTE JUMP {FTE} (+34.7%); neerlegging 30.06.2026; restructuring 11.04.2025; assets/debt Unknown; FOI {GAP}; after Die Zukunft@2282; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; not TE-additive",
    }
]
append_csv(ROOT / "entities.csv", ent_fields, entities)

foi_fields = [
    "gap_id",
    "hierarchy_path",
    "entity_id",
    "what_is_missing",
    "why_it_matters",
    "priority",
    "recipient_body",
    "recipient_email",
    "recipient_postal",
    "draft_letter_path",
    "status",
    "date_ready",
    "date_sent",
    "date_due",
    "date_answered",
    "response_summary",
    "linked_commitment_id",
    "linked_leaderboard_id",
    "created_utc",
    "updated_utc",
    "notes",
]
foi = [
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Oost_Vlaanderen>Gent>Ateljee>NBB_PDF_assets_debt_omzet_jump_pnl_loss_flip_fte_jump",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet JUMP EUR{OMZET} (+21.66%); bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs EUR{PNL24}; FTE JUMP {FTE} vs {FTE24} (+34.7%); restructuring/fusie details pub 11.04.2025; Vlaamse maatwerk subsidy matrix",
        "why_it_matters": f"Medium CW shows Flemish maatwerk VZW Gent (omzet JUMP 10.66m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / FTE JUMP +35% to {FTE}) under Vlaamse maatwerk path post-restructuring; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Ateljee VZW",
        "recipient_email": "info@ateljeevzw.be",
        "recipient_postal": "Getouwstraat 11, 9000 Gent",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-27",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": TS,
        "updated_utc": TS,
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after Die Zukunft@2282",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- close rq_2283 done + spawn rq_2284 ---
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2283":
        if r.get("status") not in ("open", "in_progress"):
            raise SystemExit(f"rq_2282 unexpected status={r.get('status')}")
        r["title"] = (
            f"leftover dual — Ateljee YE2025 Medium (omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP / FTE JUMP {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Ateljee YE2025 FREE Flemish maatwerk/Kringwinkel Gent after De Dageraad/Ateliers du 94; preferred AGB/FARO/AIESH/REW/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Ateljee VZW Gent 0430.839.554 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+21.66%); bruto JUMP {BRUTO} (~{RATIO}x / +30.34%); pnl LOSS FLIP {PNL} (< -1000% vs {PNL24}); "
            f"equity DROP {EQUITY} (-3.24% vs {EQUITY24}); FTE JUMP {FTE} (vs {FTE24} +34.7%); 19 VE VZW; NACE 88.993; "
            f"neerlegging 30.06.2026; restructuring 11.04.2025; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after Die Zukunft@2282; next EVERY-10 2290"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2283 not found on close")

if not any(r.get("task_id") == "rq_2284" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2284",
            "title": "leftover dual after Ateljee — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Ateljee YE2025 Medium (omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP / FTE JUMP {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Sterpunt/Labeur/Orbit/Die Zukunft/Roseau Vert/Ateliers Mons if YE2025). "
                "Do NOT redo Ateljee/Die Zukunft/De Dageraad/Ateliers du 94/Den Azalee/eurakor/Ateliers de l'Avenir/IN-Z/m-accent/AMAB/"
                "Atelier Alternatief/C.A.R.P./A.P.A.C. stack. "
                "Citeco/Groupe Foes/FARO/AIESH/REW still YE2024 as of tick2283."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2283 Ateljee; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "Heropbeuring CW opaque; Manupal/Aralea/Posthoorn/Vlotter/Buseloc YE2024; next every-10 2290"
            ),
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)

state_path = ROOT / "loop_state.csv"
with state_path.open("w", newline="", encoding="utf-8") as f:
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
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_2283",
            "ticks_completed": "2283",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Ateljee 0430.839.554 Medium "
                f"(omzet JUMP {OMZET} +21.66%; bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS FLIP {PNL}; equity DROP {EQUITY} -3.24%; FTE JUMP {FTE} +34.7%; 19 VE Gent maatwerk Kringwinkel); "
                f"after Die Zukunft@2282; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; next rq_2284; next EVERY-10 2290; continuous hole_fill"
            ),
        }
    )

draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Ateljee (NBB PDF / omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ateljee VZW — KBO **0430.839.554** (Actief; Getouwstraat 11, 9000 Gent; **19 VE**; FTE {FTE} CW; NACE **88.993**; Flemish maatwerk / Kringwinkel)  
**recipient:** info@ateljeevzw.be · Getouwstraat 11, 9000 Gent (+32 9 224 07 15)  
**sources:** [CW EN](https://www.companyweb.be/en/0430839554/ateljee) · [CW NL](https://www.companyweb.be/nl/0430839554/ateljee) · [CW FR](https://www.companyweb.be/fr/0430839554/ateljee) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0430839554) · [site](https://ateljeevzw.be/neem-contact-op)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **ATELJEE** sinds **04.03.1985**; **19 VE**; zetel Getouwstraat 11, 9000 Gent (sinds 29.01.2020); RSZ/BTW NACE **88.993** (+81.300 landschap / 47.793 tweedehands / 56.111 horeca).
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +21.66% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +30.34% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP (< −1000%) vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −3.24% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** JUMP vs {FTE24} (+34.7%); filed **30.06.2026**. Restructuring publication **11.04.2025**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; REW YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal/Aralea/Posthoorn/Vlotter/Buseloc YE2024; Heropbeuring CW opaque. After De Dageraad/Ateliers du 94@2281. Do NOT redo Den Azalee / Alternatief / IN-Z / m-accent / AMAB / eurakor / Ateliers de l'Avenir stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ateljee VZW
via info@ateljeevzw.be
Getouwstraat 11, 9000 Gent
Betreft: Openbaarmaking jaarrekening 2025 Ateljee (KBO 0430.839.554)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+21.66%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet), pnl LOSS FLIP EUR{PNL} (vs YE2024 EUR{PNL24}) en FTE JUMP {FTE}
   (vs {FTE24}; +34.7%).
3. Overzicht van Vlaamse maatwerktoelagen achter personeelskosten (FTE {FTE}) en
   de loonkostentussenkomstmatrix YE2025.
4. Details van de herstructurering/fusie (publicatie 11.04.2025) en impact op YE2025
   omzet/FTE/resultaat; verdeling Kringwinkel / hergebruik / maatwerkproductie.
5. Schulden LT/KT en liquide middelen YE2025 (niet gepubliceerd op Companyweb).

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

raw = Path(f"docs/doge/data/raw/tick{TICK}")
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": TICK,
            "unit": "rq_2283",
            "entity": ENTITY,
            "kbo": "0430.839.554",
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio_bruto_omzet": RATIO,
            "confidence": "medium",
            "gap": GAP,
            "sources": [s["source_id"] for s in sources],
        },
        indent=2,
    ),
    encoding="utf-8",
)
(raw / "cw_en_excerpt.txt").write_text(
    f"Ateljee YE2025 CW EN\nomzet {OMZET} (+21.66%) bruto {BRUTO} (+30.34%) pnl {PNL} LOSS FLIP equity {EQUITY} (-3.24%) FTE {FTE} JUMP\nfiled 30.06.2026 restructuring 11.04.2025\nurl https://www.companyweb.be/en/0430839554/ateljee\n",
    encoding="utf-8",
)

log_path = Path("docs/doge/loop_log.md")
log_entry = f"""

### 2026-08-27T13:15:00Z - tick 2283 - rq_2283 Ateljee Gent (omzet JUMP 10.66m / bruto~{RATIO}x / pnl LOSS FLIP / FTE JUMP {FTE} / Medium)

- Unit: **rq_2283** leftover dual after **rq_2282 Die Zukunft**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Citeco still **YE2024**; Groupe Foes still **YE2024**; Manupal/Aralea/Posthoorn/Vlotter/Buseloc still **YE2024**; Heropbeuring still **CW opaque**. Took unused FREE Flemish maatwerk / Kringwinkel **Ateljee VZW** YE2025 (KBO **0430.839.554**; Getouwstraat 11 Gent; **Actief** **19 VE**; NACE **88.993**; restructuring pub 11.04.2025). Do not redo Die Zukunft/De Dageraad/Ateliers du 94/Den Azalee/eurakor/Ateliers de l'Avenir/IN-Z/m-accent/AMAB/Atelier Alternatief stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +21.66% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +30.34% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP (< -1000% vs YE2024 EUR{PNL24}); equity **EUR{EQUITY}** DROP -3.24%; FTE **{FTE}** JUMP (vs {FTE24} +34.7%); neerlegging **30.06.2026**. Strong KBO Actief 19 VE VZW. Assets/debt Unknown. Medium. FOI via info@ateljeevzw.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.70); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2283=done + rq_2284 open; loop_state ticks=2282; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: rq_2283 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"tick{TICK} write OK: {ENTITY} omzet={OMZET} pnl={PNL} pi=6.70 next=rq_2284")
