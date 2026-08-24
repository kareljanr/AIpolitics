# tick 2273: leftover dual Pépinières La Gaume Tintigny YE2025 hole-fill
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2273"
TS = "2026-08-27T10:25:00Z"
ENTITY = "sc_pepinieres_la_gaume_tintigny"
GAP = "gap_la_gaume_nbb_pdf_assets_debt_equity_drop_14pct_pnl_loss_narrow_eta_matrix_l5"
LB = "lb_la_gaume_omzet_3_00m_equity_drop_14pct_pnl_loss_narrow_jr2025"
COMM = "comm_la_gaume_jr2025_statutory_eta_equity_drop_14pct_pnl_loss_narrow"
SRC_EN = "src_la_gaume_jr2025_cw_en"

OMZET = 3001950
BRUTO = 1607962
PNL = -280521
EQUITY = 1802275
FTE = 86.0
OMZET24 = 3151432
BRUTO24 = 1459243
PNL24 = -439942
EQUITY24 = 2086363
FTE24 = 83.5
RATIO = round(BRUTO / OMZET, 2)  # 0.54


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
        "title": "Pépinières La Gaume YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0417548673/pepinieres-la-gaume",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 12.05.2026; assets/debt Unknown",
    },
    {
        "source_id": "src_la_gaume_jr2025_cw_nl",
        "title": "Pépinières La Gaume YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0417548673/pepinieres-la-gaume",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 12.05.2026; NACE beschutte werkplaatsen; CV Pepinieres La Gaume",
    },
    {
        "source_id": "src_la_gaume_jr2025_cw_fr",
        "title": "Pépinières La Gaume YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0417548673/pepinieres-la-gaume",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; SC Actif Tintigny; CA {OMZET}; marge brute {BRUTO}; perte {PNL}",
    },
    {
        "source_id": "src_la_gaume_kbo_0417548673",
        "title": "KBO Pépinières La Gaume 0417.548.673",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0417548673",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief SC (coöperatieve vennootschap sinds 10.05.2021); 1 VE; Rue des Saucettes Breuvanne 90 6730 Tintigny; RSZ NACE 88.993; BTW 01.309/18.140/81.300; begindatum 27.06.1977; erkenning aannemer",
    },
    {
        "source_id": "src_la_gaume_site_contact_2273",
        "title": "Pépinières La Gaume FOI channel info@pepiniereslagaume.be",
        "url": "https://pepiniereslagaume.be/",
        "publisher": "Pépinières La Gaume SC",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@pepiniereslagaume.be; +32 63 44 00 70; Rue des Saucettes 90 Breuvanne Tintigny; Walloon ETA AViQ pépinière/espaces verts/éco-construction",
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
        "budget_id": "bud_la_gaume_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet DROP -4.74% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_la_gaume_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +10.19% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_la_gaume_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl LOSS NARROW",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl LOSS NARROW +36.24% vs YE2024 {PNL24} (loss less deep)",
    },
    {
        "budget_id": "bud_la_gaume_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity DROP -13.62% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_la_gaume_fte_jr2025_statutory",
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
        "budget_id": "bud_la_gaume_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS NARROW +36.24%)",
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
        "title": f"La Gaume YE2025 leftover dual (omzet 3.00m / bruto~{RATIO}x / equity DROP -13.62% / pnl LOSS NARROW / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Tintigny-Breuvanne / Walloon adapted-work AViQ pépinière-espaces verts",
        "legal_basis": "SC ETA Pépinières La Gaume (KBO 0417.548.673; Actief; 1 VE; NACE 88.993; Tintigny)",
        "decision_date": "2026-05-12",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0417548673/pepinieres-la-gaume",
        "stated_goal": "Walloon ETA pépinière / jardinerie / espaces verts / éco-construction — inclusive green employment",
        "cut_option": "Publish NBB PDF assets/debt; reconcile multi-year LOSS + equity DROP -14% vs AViQ ETA wage-intervention matrix despite bruto JUMP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Luxembourg>Tintigny>Pepinieres_La_Gaume>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE SC; after Fournipac@2272; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024",
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
        "name": f"La Gaume omzet 3.00m / equity DROP -13.62% / pnl LOSS NARROW / FTE {FTE} (YE2025 Walloon ETA Tintigny)",
        "level": "L5",
        "type": "eta_sc_statutory",
        "hierarchy_path": "Wallonie>Luxembourg>Tintigny>Pepinieres_La_Gaume>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet {OMZET} (-4.74%) / bruto {BRUTO} (+10.19%; ~{RATIO}x) / pnl LOSS NARROW {PNL} (+36.24% vs deeper loss) / equity DROP {EQUITY} (-13.62%) / FTE {FTE} (vs {FTE24}) / 1 VE Walloon ETA pépinière",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "ETA workers Tintigny-Breuvanne / AViQ adapted-work green sectors",
        "stated_goal": "Walloon ETA sheltered workshop (nursery / landscaping / eco-construction)",
        "measured_outcome": f"omzet DROP -4.74%; bruto JUMP +10.19%; pnl LOSS NARROW +36.24% (still loss); equity DROP -13.62%; FTE JUMP {FTE}; multi-year loss 2022-25; filed 12.05.2026",
        "absurdity_score": 7.4,
        "cost_score": 5.7,
        "difficulty": 3.0,
        "priority_index": 6.05,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA matrix behind multi-year LOSS + equity bleed -14% despite bruto JUMP + FTE JUMP",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Fournipac@2272; unused vs mined Lorraine/Saupont/Hautes Ardennes stack",
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
        "name_nl": "Pépinières La Gaume CV (Tintigny / Walloon ETA pépinière)",
        "name_fr": "Pépinières La Gaume SC (Tintigny / entreprise de travail adapté pépinière)",
        "name_en": "Pépinières La Gaume adapted-work SC (Tintigny Walloon ETA nursery)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://pepiniereslagaume.be/",
        "foi_email": "info@pepiniereslagaume.be",
        "foi_postal": "Rue des Saucettes Breuvanne 90, 6730 Tintigny",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0417.548.673 Actief 1 VE SC NACE 88.993; omzet DROP {OMZET} (-4.74%) bruto JUMP {BRUTO} (~{RATIO}x / +10.19%) pnl LOSS NARROW {PNL} (+36.24%) equity DROP {EQUITY} (-13.62%) FTE {FTE}; neerlegging 12.05.2026; assets/debt Unknown; FOI {GAP}; after Fournipac@2272; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive",
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
        "hierarchy_path": "Wallonie>Luxembourg>Tintigny>Pepinieres_La_Gaume>NBB_PDF_assets_debt_equity_drop_14pct_pnl_loss_narrow",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); equity DROP EUR{EQUITY} vs EUR{EQUITY24} (-13.62%); pnl LOSS NARROW EUR{PNL} vs EUR{PNL24}; multi-year loss 2022-25; AViQ ETA subsidy matrix; FTE {FTE}; activity split pépinière/espaces verts/éco-construction/Apibel",
        "why_it_matters": f"Medium CW shows Walloon ETA SC Tintigny (omzet 3.00m / equity DROP -14% / multi-year LOSS / FTE {FTE}) under AViQ green-sector path; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Pépinières La Gaume SC",
        "recipient_email": "info@pepiniereslagaume.be",
        "recipient_postal": "Rue des Saucettes Breuvanne 90, 6730 Tintigny",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after Fournipac@2272",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- research_queue: mark 2273 done + spawn 2274 ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2273":
        r["title"] = (
            f"leftover dual — Pépinières La Gaume YE2025 Medium (omzet DROP 3.00m / equity DROP -13.62% / pnl LOSS NARROW / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Pépinières La Gaume YE2025 FREE Walloon ETA Tintigny after Fournipac; preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Pépinières La Gaume SC Tintigny 0417.548.673 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet DROP {OMZET} (-4.74%); bruto JUMP {BRUTO} (~{RATIO}x / +10.19%); pnl LOSS NARROW {PNL} (+36.24% vs {PNL24}); "
            f"equity DROP {EQUITY} (-13.62% vs {EQUITY24}); FTE {FTE} (+3.0% vs {FTE24}); 1 VE SC; NACE 88.993; "
            f"neerlegging 12.05.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Fournipac@2272; next EVERY-10 2280"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2273 not found or already claimed")

if not any(r.get("task_id") == "rq_2274" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2274",
            "title": "leftover dual after La Gaume — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Pépinières La Gaume YE2025 Medium (omzet DROP 3.00m / equity DROP -13.62% / pnl LOSS NARROW / FTE {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Adapta/Atelier 85/Criquelion/Roseau Vert if YE2025). "
                "Do not redo La Gaume/Fournipac/Serre-Outil/Amis des Aveugles/Hautes Ardennes/Village n1/Trait/Ouvroir/APRE/"
                "Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/L'Atelier/Metalgroup stack. "
                "Citeco/Groupe Foes/Atelier 85 YE2024 stalls as of tick2273. Next EVERY-10: 2280."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2273 La Gaume; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; next every-10 2280"
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
            "last_unit_id": "rq_2273",
            "ticks_completed": "2273",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Pépinières La Gaume 0417.548.673 Medium "
                f"(omzet DROP {OMZET} -4.74%; bruto JUMP {BRUTO} ~{RATIO}x; pnl LOSS NARROW {PNL}; equity DROP {EQUITY} -13.62%; FTE {FTE}; 1 VE SC Tintigny ETA AViQ pépinière); "
                f"after Fournipac@2272; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2274; next EVERY-10 2280; continuous hole_fill"
            ),
        }
    )

# --- FOI draft ---
draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Pépinières La Gaume (NBB PDF / equity DROP −14% / pnl LOSS NARROW / AViQ ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Pépinières La Gaume SC — KBO **0417.548.673** (Actief; Rue des Saucettes Breuvanne 90, 6730 Tintigny; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA AViQ pépinière/espaces verts)  
**recipient:** info@pepiniereslagaume.be · Rue des Saucettes Breuvanne 90, 6730 Tintigny (+32 63 44 00 70)  
**sources:** [CW EN](https://www.companyweb.be/en/0417548673/pepinieres-la-gaume) · [CW NL](https://www.companyweb.be/nl/0417548673/pepinieres-la-gaume) · [CW FR](https://www.companyweb.be/fr/0417548673/pepinieres-la-gaume) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0417548673) · [site](https://pepiniereslagaume.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief SC PEPINIERES LA GAUME (coöperatieve vennootschap sinds **10.05.2021**); **1 VE**; zetel Rue des Saucettes Breuvanne 90, 6730 Tintigny; RSZ NACE **88.993**; BTW **01.309** / **18.140** / **81.300**; begindatum 27.06.1977; erkenning aannemer.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −4.74% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +10.19% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS NARROW +36.24% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −13.62% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (+3.0% vs {FTE24}); filed **12.05.2026**. Multi-year loss YE2022–YE2025.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Atelier 85 YE2024; Heropbeuring CW opaque. After Fournipac@2272. Do not redo Lorraine/Saupont/Hautes Ardennes/Village n1 stack.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Pépinières La Gaume SC
via info@pepiniereslagaume.be
Rue des Saucettes Breuvanne 90, 6730 Tintigny
Objet: Publicité des comptes annuels 2025 Pépinières La Gaume (BCE 0417.548.673)

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la chute des fonds propres EUR{EQUITY} (vs EUR{EQUITY24}, −13.62%) et
   de la perte multi-annuelle EUR{PNL} (vs EUR{PNL24}; pertes 2022–2025) malgré CA EUR{OMZET}
   et marge brute en hausse EUR{BRUTO}.
3. Matrice des subsides AViQ / aides à l'emploi derrière FTE {FTE} et activités
   pépinière / espaces verts / éco-construction / Apibel.
4. Dettes LT/CT et trésorerie YE2025 (non publiées sur Companyweb).
5. Ventilation des recettes commerciales vs aides publiques YE2024–YE2025.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# --- raw snapshots ---
raw = Path(f"docs/doge/raw/tick{TICK}")
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": TICK,
            "unit": "rq_2273",
            "entity": ENTITY,
            "kbo": "0417.548.673",
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio_bruto_omzet": RATIO,
            "confidence": "medium",
            "gap": GAP,
            "next": "rq_2274",
        },
        indent=2,
    ),
    encoding="utf-8",
)
data_raw = Path(f"docs/doge/data/raw/tick{TICK}")
data_raw.mkdir(parents=True, exist_ok=True)
(data_raw / "summary.json").write_text((raw / "summary.json").read_text(encoding="utf-8"), encoding="utf-8")

print(f"tick{TICK} write OK — {ENTITY} omzet={OMZET} equity={EQUITY} pnl={PNL} FTE={FTE}")
