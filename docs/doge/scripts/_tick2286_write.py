# tick 2286: leftover dual Borgerstein/WEBO YE2025 hole-fill — claim queue FIRST
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2286"
TS = "2026-08-27T14:00:00Z"
ENTITY = "vzw_borgerstein_webo_sint_katelijne_waver"
GAP = "gap_borgerstein_nbb_pdf_assets_debt_bruto_2_62x_omzet_14_70m_pnl_drop_vaph_maatwerk_matrix_l5"
LB = "lb_borgerstein_omzet_14_70m_bruto_2_62x_pnl_drop_fte_548_jr2025"
COMM = "comm_borgerstein_jr2025_statutory_vaph_maatwerk_webo_omzet_bruto_pnl"
SRC_EN = "src_borgerstein_jr2025_cw_en"

OMZET = 14704588
BRUTO = 38569987
PNL = 539219
EQUITY = 38483521
FTE = 548.1
OMZET24 = 14520891
BRUTO24 = 37280802
PNL24 = 686170
EQUITY24 = 38182019
FTE24 = 542.2
RATIO = round(BRUTO / OMZET, 2)  # 2.62
PI = 6.20


def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


# --- CLAIM rq_2286 FIRST ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

claimed = False
for r in rq_rows:
    if r.get("task_id") == "rq_2286":
        if r.get("status") != "open":
            raise SystemExit(f"rq_2286 already claimed status={r.get('status')} title={r.get('title')}")
        r["status"] = "in_progress"
        r["entity_id"] = ENTITY
        r["updated_utc"] = TS
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Borgerstein/WEBO in_progress"
        claimed = True
        break
if not claimed:
    raise SystemExit("rq_2286 not found")

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)
print(f"CLAIMED rq_2286 -> in_progress {ENTITY}")

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
        "title": "Borgerstein YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0413895535/borgerstein",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 23.05.2026; assets/debt Unknown; brand maatwerk WEBO",
    },
    {
        "source_id": "src_borgerstein_jr2025_cw_nl",
        "title": "Borgerstein YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0413895535/borgerstein",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 23.05.2026; NACE residential mental disability + maatwerk WEBO",
    },
    {
        "source_id": "src_borgerstein_jr2025_cw_fr",
        "title": "Borgerstein YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0413895535/borgerstein",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Sint-Katelijne-Waver; CA {OMZET}; marge brute {BRUTO}; bénéfice {PNL}",
    },
    {
        "source_id": "src_borgerstein_kbo_0413895535",
        "title": "KBO Borgerstein 0413.895.535",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0413895535",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW Borgerstein sinds 28.12.1973; 3 VE; Kapelweg 7 2860 Sint-Katelijne-Waver sinds 20.10.2021; Aanbestedende overheid; RSZ NACE 87.202; BTW NACE 88.993/81.300/46.170",
    },
    {
        "source_id": "src_borgerstein_webo_site_contact_2284",
        "title": "WEBO/Borgerstein FOI channel info.webo@borgerstein.be",
        "url": "https://maatwerkbedrijfwebo.be/",
        "publisher": "Maatwerkbedrijf WEBO / Borgerstein VZW",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info.webo@borgerstein.be; Kempenarestraat / Kapelweg Sint-Katelijne-Waver; VAPH zorg + maatwerk WEBO dual",
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
        "budget_id": "bud_borgerstein_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +1.27% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_borgerstein_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +3.46% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_borgerstein_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl DROP -21.42% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_borgerstein_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity JUMP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity JUMP +0.79% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_borgerstein_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": f"CW social-balance FTE {FTE}",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown; VAPH+maatwerk dual",
    },
    {
        "budget_id": "bud_borgerstein_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP)",
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
        "title": f"Borgerstein/WEBO YE2025 leftover dual (omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "VAPH residents + maatwerkers WEBO Sint-Katelijne-Waver path",
        "legal_basis": "VZW Borgerstein (KBO 0413.895.535; Actief; 3 VE; NACE RSZ 87.202 + BTW 88.993; Aanbestedende overheid; brand maatwerk WEBO)",
        "decision_date": "2026-05-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0413895535/borgerstein",
        "stated_goal": "VAPH residential care + Flemish maatwerk WEBO inclusive employment",
        "cut_option": "Publish NBB PDF assets/debt; split VAPH zorg vs maatwerk WEBO wage-intervention matrix behind bruto≫omzet ~2.62x",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Antwerpen>Sint_Katelijne_Waver>Borgerstein_WEBO>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 3 VE VZW; after Mobiel@2285 / Posthoorn@2284; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024",
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
        "name": f"Borgerstein/WEBO omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE} (YE2025 VAPH+maatwerk SKW)",
        "level": "L5",
        "type": "vaph_maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Antwerpen>Sint_Katelijne_Waver>Borgerstein_WEBO>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet JUMP {OMZET} (+1.27%) / bruto JUMP {BRUTO} (+3.46%; ~{RATIO}x) / pnl DROP {PNL} (-21.42% vs {PNL24}) / equity JUMP {EQUITY} (+0.79%) / FTE {FTE} (vs {FTE24}) / 3 VE VAPH residential + maatwerk WEBO dual",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "VAPH residents / maatwerkers WEBO Sint-Katelijne-Waver",
        "stated_goal": "VAPH residential care for adults with mental disability + Flemish maatwerk WEBO",
        "measured_outcome": f"omzet JUMP +1.27%; bruto JUMP +3.46% (~{RATIO}x omzet); pnl DROP -21.42%; equity JUMP +0.79%; FTE {FTE}; filed 23.05.2026",
        "absurdity_score": 7.0,
        "cost_score": 6.4,
        "difficulty": 3.0,
        "priority_index": PI,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose VAPH vs Vlaamse maatwerk wage-intervention split behind bruto≫omzet ~2.62x on 14.7m turnover dual entity",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after Mobiel@2285 / Posthoorn@2284; unused FREE vs mined Ateljee/Die Zukunft/Dageraad/A94/eurakor/Alternatief stack",
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
        "name_nl": "Borgerstein VZW / maatwerkbedrijf WEBO (Sint-Katelijne-Waver / VAPH+maatwerk)",
        "name_fr": "Borgerstein ASBL / entreprise de travail adapté WEBO (Sint-Katelijne-Waver)",
        "name_en": "Borgerstein ASBL / WEBO adapted-work (Sint-Katelijne-Waver VAPH+maatwerk dual)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://maatwerkbedrijfwebo.be/",
        "foi_email": "info.webo@borgerstein.be",
        "foi_postal": "Kapelweg 7, 2860 Sint-Katelijne-Waver",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0413.895.535 Actief 3 VE VZW Aanbestedende overheid RSZ 87.202 BTW 88.993; omzet JUMP {OMZET} (+1.27%) bruto JUMP {BRUTO} (~{RATIO}x / +3.46%) pnl DROP {PNL} (-21.42%) equity JUMP {EQUITY} (+0.79%) FTE {FTE}; neerlegging 23.05.2026; assets/debt Unknown; FOI {GAP}; after Mobiel@2285 / Posthoorn@2284; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; not TE-additive",
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
        "hierarchy_path": "Vlaanderen>Antwerpen>Sint_Katelijne_Waver>Borgerstein_WEBO>NBB_PDF_assets_debt_bruto_gt_omzet_vaph_maatwerk",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet JUMP EUR{OMZET} (+1.27%); bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} vs EUR{PNL24}; FTE {FTE}; VAPH zorg vs maatwerk WEBO subsidy split / wage-intervention matrix",
        "why_it_matters": f"Medium CW shows VAPH+maatwerk dual VZW SKW (omzet JUMP 14.70m / bruto≫omzet ~{RATIO}x / pnl DROP -21% / FTE {FTE}) under Vlaamse VAPH+maatwerk path; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Borgerstein VZW / maatwerkbedrijf WEBO",
        "recipient_email": "info.webo@borgerstein.be",
        "recipient_postal": "Kapelweg 7, 2860 Sint-Katelijne-Waver",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after Mobiel@2285 / Posthoorn@2284",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- close rq_2286 done + spawn rq_2287 ---
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2286":
        if r.get("status") not in ("open", "in_progress"):
            raise SystemExit(f"rq_2286 unexpected status={r.get('status')}")
        r["title"] = (
            f"leftover dual — Borgerstein/WEBO YE2025 Medium (omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Borgerstein/WEBO YE2025 FREE VAPH+maatwerk Sint-Katelijne-Waver after Mobiel/Posthoorn; preferred AGB/FARO/AIESH/REW/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Borgerstein VZW / WEBO SKW 0413.895.535 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+1.27%); bruto JUMP {BRUTO} (~{RATIO}x / +3.46%); pnl DROP {PNL} (-21.42% vs {PNL24}); "
            f"equity JUMP {EQUITY} (+0.79% vs {EQUITY24}); FTE {FTE} (vs {FTE24}); 3 VE VZW Aanbestedende overheid; "
            f"RSZ 87.202 + BTW 88.993; neerlegging 23.05.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after Mobiel@2285 / Posthoorn@2284; next EVERY-10 2290"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2286 not found on close")

if not any(r.get("task_id") == "rq_2287" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2287",
            "title": "leftover dual after Borgerstein/WEBO — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Borgerstein/WEBO YE2025 Medium (omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Sterpunt/Labeur/Orbit/Ateliers Mons/De Sprong if YE2025). "
                "Do NOT redo Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/Die Zukunft/De Dageraad/Ateliers du 94/Den Azalee/eurakor/"
                "Ateliers de l'Avenir/IN-Z/m-accent/AMAB/Atelier Alternatief/TWI stack. "
                "Citeco/Groupe Foes/FARO/AIESH/REW still YE2024 as of tick2286; De Sprong still YE2024; Manupal/Aralea YE2024."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2286 Borgerstein/WEBO; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "Heropbeuring CW opaque; Manupal/Aralea/Vlotter/Buseloc/De Sprong YE2024; next every-10 2290"
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
            "last_unit_id": "rq_2286",
            "ticks_completed": "2286",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Borgerstein/WEBO 0413.895.535 Medium "
                f"(omzet JUMP {OMZET} +1.27%; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -21.42%; equity JUMP {EQUITY} +0.79%; FTE {FTE}; 3 VE SKW VAPH+maatwerk); "
                f"after Mobiel@2285 / Posthoorn@2284; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; next rq_2287; next EVERY-10 2290; continuous hole_fill"
            ),
        }
    )

draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Borgerstein/WEBO (NBB PDF / omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE})

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Borgerstein VZW / maatwerkbedrijf WEBO — KBO **0413.895.535** (Actief; Kapelweg 7, 2860 Sint-Katelijne-Waver; **3 VE**; FTE {FTE} CW; RSZ **87.202** + BTW **88.993**; VAPH+maatwerk dual; Aanbestedende overheid)  
**recipient:** info.webo@borgerstein.be · Kapelweg 7, 2860 Sint-Katelijne-Waver  
**sources:** [CW EN](https://www.companyweb.be/en/0413895535/borgerstein) · [CW NL](https://www.companyweb.be/nl/0413895535/borgerstein) · [CW FR](https://www.companyweb.be/fr/0413895535/borgerstein) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0413895535) · [WEBO site](https://maatwerkbedrijfwebo.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW **Borgerstein** sinds **28.12.1973**; **3 VE**; zetel Kapelweg 7, 2860 Sint-Katelijne-Waver (sinds 20.10.2021); Aanbestedende overheid; RSZ NACE **87.202**; BTW NACE **88.993** (+81.300 landschap / 46.170 handelsbemiddeling). Brand **maatwerkbedrijf WEBO**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +1.27% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +3.46% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP −21.42% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +0.79% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (vs {FTE24}); filed **23.05.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; REW YE2024; Citeco YE2024; Groupe Foes YE2024; Manupal/Aralea/Vlotter/Buseloc/De Sprong YE2024; Heropbeuring CW opaque. After Mobiel@2285 / Posthoorn@2284. Do NOT redo Mobiel / Posthoorn / Ateljee / Die Zukunft / De Dageraad / Ateliers du 94 / eurakor / Alternatief / TWI stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Borgerstein VZW / maatwerkbedrijf WEBO
via info.webo@borgerstein.be
Kapelweg 7, 2860 Sint-Katelijne-Waver
Betreft: Openbaarmaking jaarrekening 2025 Borgerstein (KBO 0413.895.535)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Vlaams Bestuursdecreet e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+1.27%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet) en pnl DROP EUR{PNL} (vs YE2024 EUR{PNL24}; −21.42%).
3. Splitsing VAPH-zorginkomsten vs maatwerk WEBO-omzet/toelagen achter personeelskosten
   (FTE {FTE}) en de Vlaamse maatwerk loonkostentussenkomstmatrix YE2025.
4. Schulden LT/KT en liquide middelen YE2025 (niet gepubliceerd op Companyweb).
5. Overzicht van publieke toelagen (VAPH / maatwerk / gemeentelijk) YE2024–YE2025.

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
            "unit": "rq_2286",
            "entity": ENTITY,
            "kbo": "0413.895.535",
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
    f"Borgerstein/WEBO YE2025 CW EN\nomzet {OMZET} (+1.27%) bruto {BRUTO} (+3.46% ~{RATIO}x) pnl {PNL} DROP -21.42% equity {EQUITY} (+0.79%) FTE {FTE}\nfiled 23.05.2026 VAPH+maatwerk dual SKW\nurl https://www.companyweb.be/en/0413895535/borgerstein\n",
    encoding="utf-8",
)

log_path = Path("docs/doge/loop_log.md")
log_entry = f"""

### 2026-08-27T14:00:00Z - tick 2286 - rq_2286 Borgerstein/WEBO Sint-Katelijne-Waver (omzet JUMP 14.70m / bruto~{RATIO}x / pnl DROP / FTE {FTE} / Medium)

- Unit: **rq_2286** leftover dual after **rq_2285 Mobiel** / **rq_2284 De Posthoorn**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Citeco still **YE2024**; Groupe Foes still **YE2024**; Manupal/Aralea/Posthoorn/Vlotter/Buseloc/De Sprong still **YE2024**; Heropbeuring still **CW opaque**. Took unused FREE Flemish VAPH+maatwerk **Borgerstein VZW / maatwerkbedrijf WEBO** YE2025 (KBO **0413.895.535**; Kapelweg 7 Sint-Katelijne-Waver; **Actief** **3 VE**; RSZ **87.202** + BTW **88.993**; Aanbestedende overheid). Do not redo Mobiel/Posthoorn/Ateljee/Die Zukunft/De Dageraad/Ateliers du 94/Den Azalee/eurakor/Ateliers de l'Avenir/IN-Z/m-accent/AMAB/Atelier Alternatief/TWI stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +1.27% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +3.46% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** DROP -21.42% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +0.79%; FTE **{FTE}** (vs {FTE24}); neerlegging **23.05.2026**. Strong KBO Actief 3 VE VZW. Assets/debt Unknown. Medium. FOI via info.webo@borgerstein.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2286=done + rq_2287 open; loop_state ticks=2286; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: rq_2287 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused ETA-VAPH-WZC-maatwerk Sterpunt-Labeur-Orbit-Ateliers Mons).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"tick{TICK} write OK: {ENTITY} omzet={OMZET} pnl={PNL} pi={PI} next=rq_2287")
