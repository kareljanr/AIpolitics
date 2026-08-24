# tick 2270: EVERY-10 refresh + Les Hautes Ardennes YE2025 hole-fill
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2270"
TS = "2026-08-27T09:40:00Z"
ENTITY = "vzw_hautes_ardennes_vielsalm"
GAP = "gap_hautes_ardennes_nbb_pdf_assets_debt_bruto_gt_omzet_4_11x_pnl_drop_84pct_eta_matrix_l5"
LB = "lb_hautes_ardennes_bruto_12_66m_omzet_3_08m_bruto_gt_omzet_4_11x_pnl_drop_84pct_jr2025"
COMM = "comm_hautes_ardennes_jr2025_statutory_eta_bruto_gt_omzet_4_11x_pnl_drop_84pct"
SRC_EN = "src_hautes_ardennes_jr2025_cw_en"

OMZET = 3083922
BRUTO = 12661084
PNL = 62241
EQUITY = 8488313
FTE = 220.6
OMZET24 = 2851699
BRUTO24 = 12181618
PNL24 = 396823
EQUITY24 = 7987112
FTE24 = 218.8
RATIO = round(BRUTO / OMZET, 2)  # 4.11


def append_csv(path, fieldnames, rows):
    path = Path(path)
    # ensure trailing newline
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


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
        "title": "Les Hautes Ardennes Aide aux Personnes handicapées YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0407574994",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 25.07.2026; assets/debt Unknown",
    },
    {
        "source_id": "src_hautes_ardennes_jr2025_cw_nl",
        "title": "Les Hautes Ardennes YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0407574994/les-hautes-ardennes-aide-aux-personnes-handicapees",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 25.07.2026",
    },
    {
        "source_id": "src_hautes_ardennes_jr2025_cw_fr",
        "title": "Les Hautes Ardennes YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0407574994/les-hautes-ardennes-aide-aux-personnes-handicapees",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Vielsalm",
    },
    {
        "source_id": "src_hautes_ardennes_kbo_0407574994",
        "title": "KBO Les Hautes Ardennes 0407.574.994",
        "url": "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0407574994",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW; 5 VE; Place des Chasseurs Ardennais 32 6690 Vielsalm; NACE RSZ 88.993; aanbestedende overheid; begindatum 04.08.1961",
    },
    {
        "source_id": "src_hautes_ardennes_site_contact_2270",
        "title": "Les Hautes Ardennes FOI channel eta@leshautesardennes.be",
        "url": "http://www.leshautesardennes.be",
        "publisher": "Les Hautes Ardennes ASBL",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; eta@leshautesardennes.be; +32 80 29 25 55; Place des Chasseurs Ardennais 30/32 Vielsalm; Walloon ETA AViQ (bois/conditionnement/recyclage/parcs)",
    },
]
append_csv(ROOT / "sources.csv", src_fields, sources)

# --- budgets ---
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
        "budget_id": "bud_hautes_ardennes_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +8.14% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_hautes_ardennes_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +3.94% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_hautes_ardennes_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl DROP -84.32% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_hautes_ardennes_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity JUMP +6.28% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_hautes_ardennes_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": f"CW social-balance FTE {FTE}",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown",
    },
    {
        "budget_id": "bud_hautes_ardennes_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP -84.32%)",
    },
]
append_csv(ROOT / "budgets.csv", bud_fields, budgets)

# --- commitments ---
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
        "title": f"Les Hautes Ardennes YE2025 leftover dual (bruto 12.66m / omzet 3.08m / bruto~{RATIO}x / pnl DROP -84.32% / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "ETA + SAJ/hébergement workers Vielsalm / Walloon adapted-work + disability care AViQ",
        "legal_basis": "ASBL ETA Les Hautes Ardennes (KBO 0407.574.994; Actief; 5 VE; NACE 88.993; Vielsalm)",
        "decision_date": "2026-07-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": BRUTO,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0407574994",
        "stated_goal": "Walloon ETA + disability care ASBL (bois/conditionnement/recyclage/parcs + SAJ)",
        "cut_option": f"Publish NBB PDF assets/debt; reconcile bruto÷omzet ~{RATIO}x + pnl DROP -84% vs AViQ ETA/care matrix",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Luxembourg>Vielsalm>HautesArdennes>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (~{RATIO}x omzet {OMZET}); pnl DROP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 5 VE; EVERY-10 after Village n1@2269; AGB Bornem JR2024; FARO/AIESH YE2024; deferred Amis Aveugles YE2025",
    }
]
append_csv(ROOT / "commitments.csv", comm_fields, commitments)

# --- leaderboard ---
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
        "name": f"Les Hautes Ardennes bruto 12.66m / omzet 3.08m / bruto÷omzet ~{RATIO}x / pnl DROP -84.32% / FTE {FTE} (YE2025 Walloon ETA)",
        "level": "L5",
        "type": "eta_asbl_statutory",
        "hierarchy_path": "Wallonie>Luxembourg>Vielsalm>HautesArdennes>JR2025",
        "annual_cost_eur": BRUTO,
        "total_cost_eur": BRUTO,
        "tco_notes": f"CW omzet {OMZET} (+8.14%) / bruto {BRUTO} (+3.94%) / bruto÷omzet ~{RATIO}x / pnl DROP {PNL} (-84.32%) / equity JUMP {EQUITY} (+6.28%) / FTE {FTE} (vs {FTE24}) / 5 VE Walloon ETA+care",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "ETA + SAJ/hébergement workers Vielsalm / AViQ adapted-work + disability care",
        "stated_goal": "Walloon ETA sheltered workshop + disability care (bois/conditionnement/recyclage)",
        "measured_outcome": f"omzet JUMP +8.14%; bruto JUMP +3.94%; pnl DROP -84.32%; equity JUMP +6.28%; FTE {FTE}; filed 25.07.2026",
        "absurdity_score": 8.2,
        "cost_score": 6.8,
        "difficulty": 3.0,
        "priority_index": 6.80,
        "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA/care matrix behind bruto÷omzet ~{RATIO}x + pnl DROP 84%",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH YE2024; after Village n1@2269; deferred Amis Aveugles YE2025",
    }
]
append_csv(ROOT / "leaderboard.csv", lb_fields, leaderboard)

# --- entities ---
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
        "name_nl": "Les Hautes Ardennes VZW (Vielsalm / Walloon ETA + zorg)",
        "name_fr": "Les Hautes Ardennes ASBL (Vielsalm / entreprise de travail adapté + accueil)",
        "name_en": "Les Hautes Ardennes adapted-work + disability-care ASBL (Vielsalm Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "http://www.leshautesardennes.be",
        "foi_email": "eta@leshautesardennes.be",
        "foi_postal": "Place des Chasseurs Ardennais 32, 6690 Vielsalm",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.574.994 Actief 5 VE NACE 88.993; omzet JUMP {OMZET} (+8.14%) bruto JUMP {BRUTO} (~{RATIO}x / +3.94%) pnl DROP {PNL} (-84.32%) equity JUMP {EQUITY} (+6.28%) FTE {FTE}; neerlegging 25.07.2026; assets/debt Unknown; FOI {GAP}; EVERY-10 after Village n1@2269; AGB Bornem JR2024; FARO/AIESH YE2024; do not redo Village n1/Trait/Ouvroir/APRE/Renaitre/Stallbois/Sipres/La Lorraine",
    }
]
append_csv(ROOT / "entities.csv", ent_fields, entities)

# --- foi_queue ---
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
        "hierarchy_path": f"Wallonie>Luxembourg>Vielsalm>HautesArdennes>NBB_PDF_assets_debt_bruto_gt_omzet_{RATIO}x_pnl_drop_84pct",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO} (~{RATIO}x omzet EUR{OMZET}); pnl DROP EUR{PNL} vs EUR{PNL24} (-84.32%); AViQ ETA+SAJ subsidy matrix; FTE {FTE}; activity split bois/conditionnement/recyclage/parcs vs hébergement",
        "why_it_matters": f"Medium CW shows Walloon ETA+care ASBL (bruto 12.66m / omzet 3.08m / bruto~{RATIO}x / pnl DROP -84% / FTE {FTE}) under AViQ path; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Les Hautes Ardennes ASBL",
        "recipient_email": "eta@leshautesardennes.be",
        "recipient_postal": "Place des Chasseurs Ardennais 32, 6690 Vielsalm",
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
        "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH YE2024; AGB Bornem JR2024; after Village n1@2269; deferred Amis Aveugles YE2025",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- research_queue: mark 2270 done + spawn 2271 ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2270":
        r["title"] = f"EVERY-10 + leftover dual — Les Hautes Ardennes YE2025 Medium (omzet JUMP 3.08m / bruto~{RATIO}x / pnl DROP -84.32% / FTE {FTE})"
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = "EVERY-10 progress+top10 then leftover dual Les Hautes Ardennes YE2025 FREE Walloon ETA+care after Village n1"
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; EVERY-10 refreshed; Les Hautes Ardennes ASBL Vielsalm 0407.574.994 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+8.14%); bruto JUMP {BRUTO} (~{RATIO}x / +3.94%); pnl DROP {PNL} (-84.32% vs {PNL24}); "
            f"equity JUMP {EQUITY} (+6.28%); FTE {FTE} (+0.82% vs {FTE24}); 5 VE; NACE 88.993; neerlegging 25.07.2026; "
            f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH YE2024; "
            f"deferred Amis Aveugles YE2025; after Village n1@2269"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2270 not found")

rq_rows.append(
    {
        "task_id": "rq_2271",
        "title": "leftover dual after Hautes Ardennes — prefer AGB/FARO-YE2025/AIESH-REW/Amis Aveugles-or-unused ETA-VAPH-WZC-maatwerk",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after Les Hautes Ardennes YE2025 Medium (omzet JUMP 3.08m / bruto~{RATIO}x / pnl DROP -84.32% / FTE {FTE}). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
            "else unused Les Amis des Aveugles YE2025 (0406.579.854) or other unused ETA-VAPH-WZC-maatwerk with live sourced €. "
            "Do not redo Hautes Ardennes/Village n1/Trait/Ouvroir/APRE/Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": (
            "spawned after tick2270 EVERY-10 Hautes Ardennes; FARO/AIESH YE2024; AGB Bornem JR2024; REW stall opaque; "
            "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; Amis Aveugles YE2025 FREE deferred"
        ),
    }
)

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)

# --- loop_state ---
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
            "last_unit_id": "rq_2270",
            "ticks_completed": "2270",
            "paused": "no",
            "notes": (
                f"tick{TICK} EVERY-10 + leftover dual Les Hautes Ardennes 0407.574.994 Medium "
                f"(omzet JUMP {OMZET} +8.14%; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} -84.32%; equity JUMP {EQUITY}; FTE {FTE}; 5 VE Vielsalm ETA+care AViQ); "
                f"after Village n1@2269; AGB Bornem JR2024; FARO/AIESH YE2024; deferred Amis Aveugles YE2025; next rq_2271; next EVERY-10 2280; continuous hole_fill"
            ),
        }
    )

# --- FOI draft ---
draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.write_text(
    f"""# FOI draft — Les Hautes Ardennes (NBB PDF / bruto÷omzet ~{RATIO}x / pnl DROP -84% / AViQ ETA+care matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Hautes Ardennes ASBL — KBO **0407.574.994** (Actief; Place des Chasseurs Ardennais 32, 6690 Vielsalm; **5 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA AViQ + SAJ/hébergement)  
**recipient:** eta@leshautesardennes.be · Place des Chasseurs Ardennais 32, 6690 Vielsalm (+32 80 29 25 55)  
**sources:** [CW EN](https://www.companyweb.be/en/0407574994) · [CW NL](https://www.companyweb.be/nl/0407574994/les-hautes-ardennes-aide-aux-personnes-handicapees) · [CW FR](https://www.companyweb.be/fr/0407574994/les-hautes-ardennes-aide-aux-personnes-handicapees) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0407574994) · [site](http://www.leshautesardennes.be)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW Les Hautes Ardennes, Aide aux Personnes handicapées; **5 VE**; zetel Place des Chasseurs Ardennais 32, 6690 Vielsalm; RSZ NACE **88.993**; aanbestedende overheid; begindatum 04.08.1961.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +8.14% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +3.94% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP -84.32% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +6.28%; FTE **{FTE}** (+0.82% vs {FTE24}); filed **25.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024 (CW last balansjaar 2024); AIESH YE2024 (0201.712.587); REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Village n1@2269. Deferred Amis Aveugles YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Les Hautes Ardennes ASBL
via eta@leshautesardennes.be
Place des Chasseurs Ardennais 32, 6690 Vielsalm
Objet: Publicité des comptes annuels 2025 Les Hautes Ardennes (BCE 0407.574.994)

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la chute du résultat EUR{PNL} vs EUR{PNL24} (-84.32%) et du ratio marge brute/CA ~{RATIO}x.
3. Matrice des subsides AViQ / ETA / SAJ / hébergement derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (bois / conditionnement / recyclage DEEE-pneus / parcs / restaurant social vs accueil).
5. Dettes LT/CT et trésorerie YE2025 (non publiées sur Companyweb).

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# --- raw snapshots ---
raw_txt = f"""tick{TICK} Les Hautes Ardennes YE2025
KBO 0407.574.994 Actief 5 VE Place des Chasseurs Ardennais 32 6690 Vielsalm NACE 88.993
CW EN/NL/FR YE2025 filed 25.07.2026
omzet {OMZET} (+8.14% vs {OMZET24})
bruto {BRUTO} (+3.94% vs {BRUTO24}) bruto/omzet ~{RATIO}x
pnl {PNL} (-84.32% vs {PNL24})
equity {EQUITY} (+6.28% vs {EQUITY24})
FTE {FTE} (vs {FTE24})
assets/debt Unknown Medium CW + Strong KBO
FOI eta@leshautesardennes.be ready NOT sent
EVERY-10 after Village n1@2269; stalls FARO/AIESH YE2024; AGB Bornem JR2024
deferred Amis Aveugles 0406.579.854 YE2025
"""
Path("docs/doge/raw/tick2270/hautes_ardennes_summary.txt").write_text(raw_txt, encoding="utf-8")
Path("docs/doge/data/raw/tick2270/hautes_ardennes_summary.txt").write_text(raw_txt, encoding="utf-8")

print("OK tick2270 CSVs+FOI+raw written")
print("RATIO", RATIO, "PI", 6.80, "BRUTO", BRUTO)
