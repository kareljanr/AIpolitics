# tick 2279: leftover dual Les Ateliers de l'Avenir Grâce-Hollogne YE2025 hole-fill
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2279"
TS = "2026-08-27T12:00:00Z"
ENTITY = "vzw_ateliers_de_lavenir_grace_hollogne"
GAP = "gap_ateliers_avenir_nbb_pdf_assets_debt_omzet_jump_6_73m_pnl_loss_widen_equity_drop_eta_matrix_l5"
LB = "lb_ateliers_avenir_omzet_6_73m_pnl_loss_widen_equity_drop_jr2025"
COMM = "comm_ateliers_avenir_jr2025_statutory_eta_omzet_jump_pnl_loss_widen_equity_drop"
SRC_EN = "src_ateliers_avenir_jr2025_cw_en"

OMZET = 6727179
BRUTO = 7139239
PNL = -397392
EQUITY = 11347959
FTE = 144.8
OMZET24 = 5789017
BRUTO24 = 6774187
PNL24 = -149951
EQUITY24 = 11882478
FTE24 = 142.9
RATIO = round(BRUTO / OMZET, 2)  # 1.06


def append_csv(path, fieldnames, rows):
    path = Path(path)
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
        "title": "Les Ateliers de l'Avenir YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0427352306/les-ateliers-de-lavenir",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 06.07.2026; assets/debt Unknown",
    },
    {
        "source_id": "src_ateliers_avenir_jr2025_cw_nl",
        "title": "Les Ateliers de l'Avenir YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0427352306/les-ateliers-de-lavenir",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 06.07.2026; NACE beschutte werkplaatsen; VZW Les Ateliers De L'avenir",
    },
    {
        "source_id": "src_ateliers_avenir_jr2025_cw_fr",
        "title": "Les Ateliers de l'Avenir YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0427352306/les-ateliers-de-lavenir",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Grâce-Hollogne; CA {OMZET}; marge brute {BRUTO}; perte {PNL}",
    },
    {
        "source_id": "src_ateliers_avenir_kbo_0427352306",
        "title": "KBO Les Ateliers de l'Avenir 0427.352.306",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=fr&ondernemingsnummer=0427352306",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief ASBL depuis 10.06.1985; 1 VE; Rue de l'Avenir 75 4460 Grâce-Hollogne; RSZ/BTW NACE 88.993; dénomination LES ATELIERS DE L'AVENIR depuis 19.03.2024; absorption 0460.282.816 Atelier de l'Avenir 19.03.2024; agrégation entrepreneur; DG Vincent de Hey",
    },
    {
        "source_id": "src_ateliers_avenir_site_contact_2279",
        "title": "Les Ateliers de l'Avenir FOI channel commercial@ateliersdelavenir.be",
        "url": "https://www.lesateliersdelavenir.be/",
        "publisher": "Les Ateliers de l'Avenir ASBL",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; commercial@ateliersdelavenir.be; gilles.nerrinck@ateliersdelavenir.be; +32 4 239 70 10; Rue de l'Avenir 75 Grâce-Hollogne; Walloon ETA AViQ wood/ossature/paletterie deaf-inclusion",
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
        "budget_id": "bud_ateliers_avenir_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +16.21% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ateliers_avenir_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +5.39% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_ateliers_avenir_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl LOSS WIDEN",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl LOSS WIDEN -165.02% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ateliers_avenir_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity DROP -4.5% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ateliers_avenir_fte_jr2025_statutory",
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
        "budget_id": "bud_ateliers_avenir_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS WIDEN -165%)",
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
        "title": f"Ateliers de l'Avenir YE2025 leftover dual (omzet JUMP 6.73m / bruto~{RATIO}x / pnl LOSS WIDEN / equity DROP -4.5% / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Grâce-Hollogne / AViQ adapted-work deaf-inclusion wood construction path",
        "legal_basis": "ASBL ETA Les Ateliers de l'Avenir (KBO 0427.352.306; Actief; 1 VE; NACE 88.993; Grâce-Hollogne; absorbed 0460.282.816 19.03.2024)",
        "decision_date": "2026-07-06",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0427352306/les-ateliers-de-lavenir",
        "stated_goal": "Walloon ETA wood joinery / ossature bois / paletterie — inclusive employment for deaf/hard-of-hearing",
        "cut_option": "Publish NBB PDF assets/debt; reconcile LOSS WIDEN despite omzet JUMP +16% + post-merger path vs AViQ ETA wage-intervention matrix",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Grace_Hollogne>Ateliers_de_lAvenir>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl LOSS WIDEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE ASBL; after IN-Z/m-accent@2278; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024",
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
        "name": f"Ateliers de l'Avenir omzet JUMP 6.73m / pnl LOSS WIDEN -0.40m / equity DROP -4.5% / FTE {FTE} (YE2025 Walloon ETA Grâce-Hollogne)",
        "level": "L5",
        "type": "eta_asbl_statutory",
        "hierarchy_path": "Wallonie>Liege>Grace_Hollogne>Ateliers_de_lAvenir>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet JUMP {OMZET} (+16.21%) / bruto JUMP {BRUTO} (+5.39%; ~{RATIO}x) / pnl LOSS WIDEN {PNL} (-165% vs {PNL24}) / equity DROP {EQUITY} (-4.5%) / FTE {FTE} (vs {FTE24}) / 1 VE post-merger Walloon ETA wood",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "ETA workers Grâce-Hollogne / AViQ adapted-work deaf-inclusion wood sectors",
        "stated_goal": "Walloon ETA sheltered workshop (joinery / timber frame / pallet circular)",
        "measured_outcome": f"omzet JUMP +16.21%; bruto JUMP +5.39%; pnl LOSS WIDEN -165%; equity DROP -4.5%; FTE {FTE}; second consecutive loss year post 2024 merger; filed 06.07.2026",
        "absurdity_score": 7.0,
        "cost_score": 5.8,
        "difficulty": 3.0,
        "priority_index": 6.10,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA matrix behind LOSS WIDEN despite omzet JUMP +16% + equity bleed post-merger",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after IN-Z/m-accent@2278; unused FREE vs mined Metalgroup/CARP/APAC/Atelier85 stack",
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
        "name_nl": "Les Ateliers de l'Avenir VZW (Grâce-Hollogne / Walloon ETA houtbouw)",
        "name_fr": "Les Ateliers de l'Avenir ASBL (Grâce-Hollogne / entreprise de travail adapté bois)",
        "name_en": "Les Ateliers de l'Avenir adapted-work ASBL (Grâce-Hollogne Walloon ETA timber)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.lesateliersdelavenir.be/",
        "foi_email": "commercial@ateliersdelavenir.be",
        "foi_postal": "Rue de l'Avenir 75, 4460 Grâce-Hollogne",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0427.352.306 Actief 1 VE ASBL NACE 88.993; omzet JUMP {OMZET} (+16.21%) bruto JUMP {BRUTO} (~{RATIO}x / +5.39%) pnl LOSS WIDEN {PNL} (-165%) equity DROP {EQUITY} (-4.5%) FTE {FTE}; neerlegging 06.07.2026; assets/debt Unknown; absorbed 0460.282.816 19.03.2024; FOI {GAP}; after IN-Z/m-accent@2278; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive",
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
        "hierarchy_path": "Wallonie>Liege>Grace_Hollogne>Ateliers_de_lAvenir>NBB_PDF_assets_debt_omzet_jump_pnl_loss_widen_equity_drop",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet JUMP EUR{OMZET} (+16.21%); pnl LOSS WIDEN EUR{PNL} vs EUR{PNL24}; equity DROP EUR{EQUITY} (-4.5%); post-merger absorption 0460.282.816; AViQ ETA subsidy matrix; FTE {FTE}; activity split menuiserie/ossature/paletterie",
        "why_it_matters": f"Medium CW shows Walloon ETA ASBL Grâce-Hollogne (omzet JUMP 6.73m / pnl LOSS WIDEN / equity DROP -4.5% / FTE {FTE}) under AViQ wood-inclusion path; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Les Ateliers de l'Avenir ASBL",
        "recipient_email": "commercial@ateliersdelavenir.be",
        "recipient_postal": "Rue de l'Avenir 75, 4460 Grâce-Hollogne",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after IN-Z/m-accent@2278",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- research_queue: mark 2279 done + spawn 2280 ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2279":
        if r.get("status") != "open":
            raise SystemExit(f"rq_2279 already claimed status={r.get('status')}")
        r["title"] = (
            f"leftover dual — Ateliers de l'Avenir YE2025 Medium (omzet JUMP 6.73m / pnl LOSS WIDEN / equity DROP -4.5% / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Les Ateliers de l'Avenir YE2025 FREE Walloon ETA Grâce-Hollogne after IN-Z/m-accent; preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Les Ateliers de l'Avenir ASBL Grâce-Hollogne 0427.352.306 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+16.21%); bruto JUMP {BRUTO} (~{RATIO}x / +5.39%); pnl LOSS WIDEN {PNL} (-165% vs {PNL24}); "
            f"equity DROP {EQUITY} (-4.5% vs {EQUITY24}); FTE {FTE} (vs {FTE24}); 1 VE ASBL; NACE 88.993; "
            f"neerlegging 06.07.2026; absorbed 0460.282.816 19.03.2024; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after IN-Z/m-accent@2278; next EVERY-10 2280"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2279 not found")

if not any(r.get("task_id") == "rq_2280" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2280",
            "title": "EVERY-10 progress + leftover dual after Ateliers de l'Avenir — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"EVERY-10 mandatory: refresh progress_every_10_ticks.md (layers A–E) + doge_waste_top10_current.md then hole-fill ONE unit. "
                f"leftover dual after Les Ateliers de l'Avenir YE2025 Medium (omzet JUMP 6.73m / pnl LOSS WIDEN / equity DROP -4.5% / FTE {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros. "
                "Do NOT redo Ateliers de l'Avenir/IN-Z/m-accent/AMAB/C.A.R.P./Atelier Saint-Vincent/A.P.A.C./Adapta/Atelier 85/"
                "La Gaume/De Enter/Fournipac/Le Rucher/Metalgroup/APAM/Jeunes Jardiniers/Pilifs/TRAVCO stack. "
                "Citeco/Groupe Foes still YE2024 as of tick2279. EVERY-10 tick."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2279 Ateliers de l'Avenir; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "Heropbeuring CW opaque; Relais Haute Sambre YE2024; EVERY-10 2280 mandatory progress refresh"
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
            "last_unit_id": "rq_2279",
            "ticks_completed": "2279",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Ateliers de l'Avenir 0427.352.306 Medium "
                f"(omzet JUMP {OMZET} +16.21%; bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS WIDEN {PNL}; equity DROP {EQUITY} -4.5%; FTE {FTE}; 1 VE Grâce-Hollogne ETA AViQ wood); "
                f"after IN-Z/m-accent@2278; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2280 EVERY-10; continuous hole_fill"
            ),
        }
    )

# --- FOI draft ---
draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Les Ateliers de l'Avenir (NBB PDF / omzet JUMP 6.73m / pnl LOSS WIDEN / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Ateliers de l'Avenir ASBL — KBO **0427.352.306** (Actief; Rue de l'Avenir 75, 4460 Grâce-Hollogne; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA AViQ)  
**recipient:** commercial@ateliersdelavenir.be · Rue de l'Avenir 75, 4460 Grâce-Hollogne (+32 4 239 70 10)  
**sources:** [CW EN](https://www.companyweb.be/en/0427352306/les-ateliers-de-lavenir) · [CW NL](https://www.companyweb.be/nl/0427352306/les-ateliers-de-lavenir) · [CW FR](https://www.companyweb.be/fr/0427352306/les-ateliers-de-lavenir) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=fr&ondernemingsnummer=0427352306) · [site](https://www.lesateliersdelavenir.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL LES ATELIERS DE L'AVENIR (dénomination depuis **19.03.2024**); **1 VE**; zetel Rue de l'Avenir 75, 4460 Grâce-Hollogne; RSZ/BTW NACE **88.993**; begindatum 10.06.1985; absorption **0460.282.816** Atelier de l'Avenir **19.03.2024**; agrégation entrepreneur; DG Vincent de Hey.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +16.21% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +5.39% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS WIDEN −165.02% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −4.5% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (vs {FTE24}); filed **06.07.2026**. Second consecutive loss year.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Heropbeuring CW opaque; Relais Haute Sambre YE2024. After IN-Z/m-accent@2278. Do not redo Metalgroup/CARP/APAC/Atelier85/La Gaume stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Les Ateliers de l'Avenir ASBL
via commercial@ateliersdelavenir.be
Rue de l'Avenir 75, 4460 Grâce-Hollogne
Betreft: Openbaarmaking jaarrekening 2025 Les Ateliers de l'Avenir (KBO 0427.352.306)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Wallonië / Code de la démocratie locale et de la décentralisation / openbaarheid
bestuursdocumenten), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+16.21%) naast verlies EUR{PNL}
   (vs YE2024 EUR{PNL24}; −165%) en equity DROP EUR{EQUITY} (−4.5%).
3. Overzicht van AViQ/Waalse toelagen achter personeelskosten (FTE {FTE}) en
   de ETA-loonkostentussenkomstmatrix YE2025.
4. Verdeling omzet/activiteiten (menuiserie / ossature bois / paletterie) +
   effect van de fusie/absorptie 0460.282.816 (19.03.2024) op YE2025.
5. Schulden LT/KT en liquide middelen YE2025 (niet gepubliceerd op Companyweb).

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# --- raw snapshots ---
raw = Path(f"docs/doge/data/raw/tick{TICK}")
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": TICK,
            "unit": "rq_2279",
            "entity": ENTITY,
            "kbo": "0427.352.306",
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
    f"Les Ateliers De L'avenir YE2025 CW EN\nomzet {OMZET} (+16.21%) bruto {BRUTO} (+5.39%) pnl {PNL} (-165.02%) equity {EQUITY} (-4.5%) FTE {FTE}\nfiled 06.07.2026\nurl https://www.companyweb.be/en/0427352306/les-ateliers-de-lavenir\n",
    encoding="utf-8",
)

print(f"tick{TICK} write OK: {ENTITY} omzet={OMZET} pnl={PNL} pi=6.10 next=rq_2280 EVERY-10")
