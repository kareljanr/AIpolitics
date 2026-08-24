# tick 2272: leftover dual Fournipac Andenne YE2025 hole-fill
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2272"
TS = "2026-08-27T10:10:00Z"
ENTITY = "vzw_fournipac_andenne"
GAP = "gap_fournipac_nbb_pdf_assets_debt_equity_drop_45pct_pnl_loss_widen_eta_matrix_l5"
LB = "lb_fournipac_omzet_3_71m_equity_drop_45pct_pnl_loss_widen_jr2025"
COMM = "comm_fournipac_jr2025_statutory_eta_equity_drop_45pct_pnl_loss_widen"
SRC_EN = "src_fournipac_jr2025_cw_en"

OMZET = 3706571
BRUTO = 3063961
PNL = -228155
EQUITY = 335681
FTE = 95.0
OMZET24 = 3879595
BRUTO24 = 3302827
PNL24 = -185379
EQUITY24 = 614369
FTE24 = 96.1
RATIO = round(BRUTO / OMZET, 2)  # 0.83


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
        "title": "Fournipac YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0457234739/fournipac",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 25.04.2026; assets/debt Unknown",
    },
    {
        "source_id": "src_fournipac_jr2025_cw_nl",
        "title": "Fournipac YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0457234739/fournipac",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 25.04.2026; NACE beschutte werkplaatsen",
    },
    {
        "source_id": "src_fournipac_jr2025_cw_fr",
        "title": "Fournipac YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0457234739/fournipac",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Andenne; marge brute {BRUTO}",
    },
    {
        "source_id": "src_fournipac_kbo_0457234739",
        "title": "KBO Fournipac 0457.234.739",
        "url": "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0457234739",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW sinds 23.03.2026 (ex-SCRL); 2 VE; Rue Géron 14 5300 Andenne; NACE RSZ 88.993 + BTW 10.120 poultry; begindatum 14.12.1995",
    },
    {
        "source_id": "src_fournipac_site_contact_2272",
        "title": "Fournipac FOI channel info@fournipac.be",
        "url": "https://www.fournipac.be/politique-de-confidentialite/",
        "publisher": "Fournipac ASBL",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@fournipac.be; +32 85 61 60 70; Rue Géron 14 Andenne; Walloon ETA AViQ agroalimentaire (integrated activity path toward L'Atelier Namur)",
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
        "budget_id": "bud_fournipac_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet DROP -4.46% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_fournipac_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto DROP -7.23% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_fournipac_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl LOSS WIDEN",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl LOSS WIDEN -23.07% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_fournipac_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity DROP -45.36% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_fournipac_fte_jr2025_statutory",
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
        "budget_id": "bud_fournipac_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS WIDEN -23.07%)",
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
        "title": f"Fournipac YE2025 leftover dual (omzet 3.71m / bruto~{RATIO}x / equity DROP -45.36% / pnl LOSS WIDEN / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Andenne-Seilles / Walloon adapted-work AViQ agroalimentaire",
        "legal_basis": "ASBL/VZW ETA Fournipac (KBO 0457.234.739; Actief; 2 VE; NACE 88.993; Andenne)",
        "decision_date": "2026-04-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0457234739/fournipac",
        "stated_goal": "Walloon ETA agroalimentaire (conditionnement / volaille / froid) — activity path integrating toward L'Atelier Namur",
        "cut_option": "Publish NBB PDF assets/debt; reconcile equity DROP -45% + chronic LOSS vs AViQ ETA + L'Atelier integration matrix",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Namur>Andenne>Fournipac>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl LOSS WIDEN {PNL}; equity DROP {EQUITY}; FTE {FTE}; 2 VE; after Serre-Outil@2271; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024",
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
        "name": f"Fournipac omzet 3.71m / equity DROP -45.36% / pnl LOSS WIDEN -23% / FTE {FTE} (YE2025 Walloon ETA Andenne)",
        "level": "L5",
        "type": "eta_asbl_statutory",
        "hierarchy_path": "Wallonie>Namur>Andenne>Fournipac>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet {OMZET} (-4.46%) / bruto {BRUTO} (-7.23%; ~{RATIO}x) / pnl LOSS WIDEN {PNL} (-23.07%) / equity DROP {EQUITY} (-45.36%) / FTE {FTE} (vs {FTE24}) / 2 VE Walloon ETA agroalimentaire",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "ETA workers Andenne-Seilles / AViQ adapted-work agroalimentaire",
        "stated_goal": "Walloon ETA sheltered workshop (food packaging / poultry / cold chain)",
        "measured_outcome": f"omzet DROP -4.46%; bruto DROP -7.23%; pnl LOSS WIDEN -23.07%; equity DROP -45.36%; FTE {FTE}; filed 25.04.2026; VZW form since 23.03.2026",
        "absurdity_score": 7.8,
        "cost_score": 5.8,
        "difficulty": 3.0,
        "priority_index": 6.45,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose AViQ ETA + L'Atelier Namur integration matrix behind equity collapse -45% + chronic LOSS",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Serre-Outil@2271; distinct from mined L'Atelier Namur@2241",
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
        "name_nl": "Fournipac VZW (Andenne / Walloon ETA agroalimentaire)",
        "name_fr": "Fournipac ASBL (Andenne / entreprise de travail adapté agroalimentaire)",
        "name_en": "Fournipac adapted-work ASBL (Andenne Walloon ETA agroalimentaire)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.fournipac.be",
        "foi_email": "info@fournipac.be",
        "foi_postal": "Rue Géron 14, 5300 Andenne",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0457.234.739 Actief 2 VE NACE 88.993; omzet DROP {OMZET} (-4.46%) bruto DROP {BRUTO} (~{RATIO}x / -7.23%) pnl LOSS WIDEN {PNL} (-23.07%) equity DROP {EQUITY} (-45.36%) FTE {FTE}; neerlegging 25.04.2026; VZW sinds 23.03.2026; assets/debt Unknown; FOI {GAP}; after Serre-Outil@2271; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; distinct L'Atelier@2241; not TE-additive",
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
        "hierarchy_path": "Wallonie>Namur>Andenne>Fournipac>NBB_PDF_assets_debt_equity_drop_45pct_pnl_loss_widen",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); equity DROP EUR{EQUITY} vs EUR{EQUITY24} (-45.36%); pnl LOSS WIDEN EUR{PNL} vs EUR{PNL24}; AViQ ETA subsidy matrix; L'Atelier Namur integration / asset transfer disclosure; FTE {FTE}; activity split conditionnement/volaille/froid",
        "why_it_matters": f"Medium CW shows Walloon ETA agroalimentaire (omzet 3.71m / equity DROP -45% / pnl LOSS WIDEN / FTE {FTE}) under AViQ path with L'Atelier integration news; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Fournipac ASBL",
        "recipient_email": "info@fournipac.be",
        "recipient_postal": "Rue Géron 14, 5300 Andenne",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after Serre-Outil@2271",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- research_queue: mark 2272 done + spawn 2273 ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2272":
        r["title"] = (
            f"leftover dual — Fournipac YE2025 Medium (omzet DROP 3.71m / equity DROP -45.36% / pnl LOSS WIDEN / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Fournipac YE2025 FREE Walloon ETA Andenne after Serre-Outil; preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Fournipac ASBL/VZW Andenne 0457.234.739 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet DROP {OMZET} (-4.46%); bruto DROP {BRUTO} (~{RATIO}x / -7.23%); pnl LOSS WIDEN {PNL} (-23.07% vs {PNL24}); "
            f"equity DROP {EQUITY} (-45.36% vs {EQUITY24}); FTE {FTE} (-1.14% vs {FTE24}); 2 VE; NACE 88.993; "
            f"neerlegging 25.04.2026; VZW sinds 23.03.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Serre-Outil@2271; next EVERY-10 2280"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2272 not found or already claimed")

# avoid duplicate spawn if concurrent
if not any(r.get("task_id") == "rq_2273" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2273",
            "title": "leftover dual after Fournipac — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Fournipac YE2025 Medium (omzet DROP 3.71m / equity DROP -45.36% / pnl LOSS WIDEN / FTE {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else Heropbeuring if NBB/CW euros live, else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros. "
                "Do not redo Fournipac/Serre-Outil/Amis des Aveugles/Hautes Ardennes/Village n1/Trait/Ouvroir/APRE/"
                "Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/L'Atelier/ETA123/Axedis stack. "
                "Citeco/Groupe Foes YE2024 stalls as of tick2272. Next EVERY-10: 2280."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2272 Fournipac; FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
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
            "last_unit_id": "rq_2272",
            "ticks_completed": "2272",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Fournipac 0457.234.739 Medium "
                f"(omzet DROP {OMZET} -4.46%; bruto DROP {BRUTO} ~{RATIO}x; pnl LOSS WIDEN {PNL}; equity DROP {EQUITY} -45.36%; FTE {FTE}; 2 VE Andenne ETA AViQ agroalimentaire); "
                f"after Serre-Outil@2271; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2273; next EVERY-10 2280; continuous hole_fill"
            ),
        }
    )

# --- FOI draft ---
draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Fournipac (NBB PDF / equity DROP −45% / pnl LOSS WIDEN / AViQ ETA + L'Atelier matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Fournipac ASBL/VZW — KBO **0457.234.739** (Actief; Rue Géron 14, 5300 Andenne; **2 VE**; FTE {FTE} CW; NACE **88.993** + 10.120; Walloon ETA AViQ agroalimentaire)  
**recipient:** info@fournipac.be · Rue Géron 14, 5300 Andenne (+32 85 61 60 70)  
**sources:** [CW EN](https://www.companyweb.be/en/0457234739/fournipac) · [CW NL](https://www.companyweb.be/nl/0457234739/fournipac) · [CW FR](https://www.companyweb.be/fr/0457234739/fournipac) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=0457234739) · [site](https://www.fournipac.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW FOURNIPAC sinds **23.03.2026** (ex-SCRL; publication forme juridique 09.04.2026); **2 VE**; zetel Rue Géron 14, 5300 Andenne; RSZ NACE **88.993**; BTW also **10.120** poultry; begindatum 14.12.1995.
- CW YE2025: omzet **EUR{OMZET:,}** DROP −4.46% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP −7.23% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS WIDEN −23.07% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP −45.36% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (−1.14% vs {FTE24}); filed **25.04.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Serre-Outil@2271. Distinct from mined L'Atelier Namur@2241 (integration path reported Nov 2025).

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Fournipac ASBL
via info@fournipac.be
Rue Géron 14, 5300 Andenne
Objet: Publicité des comptes annuels 2025 Fournipac (BCE 0457.234.739)

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Explication de la chute des fonds propres EUR{EQUITY} (vs EUR{EQUITY24}, −45.36%) et
   de la perte EUR{PNL} (vs EUR{PNL24}, −23.07%) malgré CA EUR{OMZET}.
3. Matrice des subsides AViQ / aides à l'emploi derrière FTE {FTE} et activités agroalimentaires.
4. Transparence sur le rapprochement / intégration avec L'Atelier (Namur) : transferts d'actifs,
   dettes, travailleurs, et continuité juridique YE2025–YE2026.
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
raw = Path(f"docs/doge/raw/tick{TICK}")
raw.mkdir(parents=True, exist_ok=True)
(raw / "fournipac_summary.json").write_text(
    json.dumps(
        {
            "kbo": "0457.234.739",
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio_bruto_omzet": RATIO,
            "filed": "2026-04-25",
            "confidence": "medium",
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
data_raw = Path(f"docs/doge/data/raw/tick{TICK}")
data_raw.mkdir(parents=True, exist_ok=True)
(data_raw / "unit.txt").write_text(
    f"rq_{TICK} Fournipac Andenne YE2025 Medium omzet {OMZET} equity DROP -45.36%\n",
    encoding="utf-8",
)

print(f"OK tick{TICK} Fournipac omzet={OMZET} equity={EQUITY} pnl={PNL} ratio={RATIO}")
