# tick 2288: leftover dual Village Liegeois Marie-Reine Prignon YE2025 hole-fill
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2288"
TS = "2026-08-27T14:30:00Z"
ENTITY = "vzw_village_liegeois_seraing"
GAP = "gap_village_liegeois_nbb_pdf_assets_debt_empty_omzet_bruto_2_25m_pnl_drop_fte_jump_eta_matrix_l5"
LB = "lb_village_liegeois_bruto_2_25m_empty_omzet_pnl_drop_fte_jump_jr2025"
COMM = "comm_village_liegeois_jr2025_statutory_eta_empty_omzet_bruto_2_25m_pnl_drop_fte_jump"
SRC_EN = "src_village_liegeois_jr2025_cw_en"

BRUTO = 2254026
PNL = 177921
EQUITY = 2552242
FTE = 58.0
BRUTO24 = 2091194
PNL24 = 191047
EQUITY24 = 2393627
FTE24 = 54.5
ENVELOPE = BRUTO
PI = 5.05


def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

claimed = False
for r in rq_rows:
    if r.get("task_id") == "rq_2288":
        if r.get("status") not in ("open", "in_progress"):
            raise SystemExit(f"rq_2288 already claimed status={r.get('status')} title={r.get('title')}")
        r["status"] = "in_progress"
        r["entity_id"] = ENTITY
        r["updated_utc"] = TS
        r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM Village Liegeois Seraing in_progress"
        claimed = True
        break
if not claimed:
    raise SystemExit("rq_2288 not found")

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)
print(f"CLAIMED rq_2288 -> in_progress {ENTITY}")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
sources = [
    {
        "source_id": SRC_EN,
        "title": "Village Liegeois YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0430721768",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; empty omzet; bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; filed 23.06.2026; assets/debt Unknown; Full name Village Liegeois Marie-Reine Prignon; abbrev C.A.P.V.A.L. Village n05 Reine Fabiola",
    },
    {
        "source_id": "src_village_liegeois_jr2025_cw_nl",
        "title": "Village Liegeois YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0430721768/village-liegeois",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; neerlegging 23.06.2026; geen omzet; bruto {BRUTO}; NACE beschutte werkplaatsen; VZW Seraing",
    },
    {
        "source_id": "src_village_liegeois_jr2025_cw_fr",
        "title": "Village Liegeois YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0430721768",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; ASBL Actif Seraing; CA non publié; marge brute {BRUTO}; bénéfice {PNL}",
    },
    {
        "source_id": "src_village_liegeois_kbo_0430721768",
        "title": "KBO Village Liegeois Marie-Reine Prignon 0430.721.768",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0430721768",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief VZW VILLAGE LIEGEOIS MARIE - REINE PRIGNON sinds 18.10.1986; afkorting C.A.P.V.A.L. Village n05 Reine Fabiola; 1 VE; Rue du Teris 25 4100 Seraing; RSZ/BTW NACE 88.993 (+16.240/81.300/43.350/01.191); Florence Prignon dagelijks bestuur",
    },
    {
        "source_id": "src_village_liegeois_site_contact_2288",
        "title": "Village Liegeois FOI channel info@villageliegeois.be",
        "url": "https://www.villageliegeois.be/",
        "publisher": "Village Liegeois ASBL",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; info@villageliegeois.be; Rue du Teris 25 4100 Seraing; tel 04/337 56 76 (AVIQ ETA listing); Walloon ETA parks/jardins/conditionnement/menuiserie",
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
        "budget_id": "bud_village_liegeois_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": "CW statutory bruto_marge YE2025 (empty omzet primary envelope)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +7.79% vs YE2024 {BRUTO24}; empty omzet",
    },
    {
        "budget_id": "bud_village_liegeois_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl DROP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl DROP -6.87% vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_village_liegeois_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity JUMP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity JUMP +6.63% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_village_liegeois_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": f"CW social-balance FTE {FTE}",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; FTE JUMP {FTE} vs YE2024 {FTE24}; assets/debt Unknown; empty omzet",
    },
    {
        "budget_id": "bud_village_liegeois_pnl_jr2024_statutory_cmp",
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
    "2025_omzet": None,
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
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
        "title": f"Village Liegeois YE2025 leftover dual (empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Seraing / AVIQ adapted-work path",
        "legal_basis": "ASBL Village Liegeois Marie-Reine Prignon (KBO 0430.721.768; Actief; 1 VE; NACE 88.993; Seraing; EWETA/AVIQ ETA)",
        "decision_date": "2026-06-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": ENVELOPE,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0430721768",
        "stated_goal": "Walloon ETA parks/gardens/packaging/carpentry inclusive employment Seraing",
        "cut_option": "Publish NBB PDF assets/debt; disclose AVIQ wage-intervention matrix behind empty omzet + bruto 2.25m + FTE JUMP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Seraing>VillageLiegeois>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (empty omzet); pnl DROP {PNL}; equity JUMP {EQUITY}; FTE JUMP {FTE}; 1 VE ASBL; after De Sprong@2287 / Borgerstein@2286; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; NOT Village n1 Braine@2269",
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
        "name": f"Village Liegeois empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP {FTE} (YE2025 Walloon ETA Seraing)",
        "level": "L5",
        "type": "eta_asbl_statutory",
        "hierarchy_path": "Wallonie>Liege>Seraing>VillageLiegeois>JR2025",
        "annual_cost_eur": ENVELOPE,
        "total_cost_eur": ENVELOPE,
        "tco_notes": f"CW empty omzet; bruto JUMP {BRUTO} (+7.79%) / pnl DROP {PNL} (-6.87% vs {PNL24}) / equity JUMP {EQUITY} (+6.63%) / FTE JUMP {FTE} (vs {FTE24}); Walloon AVIQ ETA path; assets/debt Unknown",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "ETA workers / AVIQ clients Seraing-Liege",
        "stated_goal": "Entreprise de travail adapté (parks/packaging/carpentry) Marie-Reine Prignon",
        "measured_outcome": f"empty omzet; bruto JUMP +7.79%; pnl DROP -6.87%; equity JUMP +6.63%; FTE JUMP to {FTE}; filed 23.06.2026",
        "absurdity_score": 5.2,
        "cost_score": 4.8,
        "difficulty": 3.0,
        "priority_index": PI,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ wage-cost subsidy matrix behind empty omzet + bruto 2.25m envelope",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after De Sprong@2287 / Borgerstein@2286; NOT Village n1@2269 / Amis des Aveugles@2270",
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
        "name_nl": "Village Liegeois Marie-Reine Prignon VZW (Seraing / Waals ETA)",
        "name_fr": "Village Liegeois Marie-Reine Prignon ASBL (Seraing / entreprise de travail adapté wallonne)",
        "name_en": "Village Liegeois Marie-Reine Prignon adapted-work ASBL (Seraing Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.villageliegeois.be/",
        "foi_email": "info@villageliegeois.be",
        "foi_postal": "Rue du Teris 25, 4100 Seraing",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0430.721.768 Actief 1 VE VZW/ASBL NACE 88.993; empty omzet; bruto JUMP {BRUTO} (+7.79%) pnl DROP {PNL} (-6.87%) equity JUMP {EQUITY} (+6.63%) FTE JUMP {FTE}; neerlegging 23.06.2026; abbrev C.A.P.V.A.L. Village n05 Reine Fabiola; assets/debt Unknown; FOI {GAP}; after De Sprong@2287 / Borgerstein@2286; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NOT Village n1 Braine 0411.648.501@2269; not TE-additive",
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
        "hierarchy_path": "Wallonie>Liege>Seraing>VillageLiegeois>NBB_PDF_assets_debt_empty_omzet_bruto_pnl_drop_fte_jump",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet explanation; bruto EUR{BRUTO} (+7.79%); pnl DROP EUR{PNL} vs EUR{PNL24}; FTE JUMP {FTE} vs {FTE24}; AVIQ wage-intervention / EWETA subsidy matrix",
        "why_it_matters": f"Medium CW shows Walloon ETA ASBL Seraing (empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP to {FTE}) under AVIQ adapted-work path; assets/debt unpublished",
        "priority": 8,
        "recipient_body": "Village Liegeois Marie-Reine Prignon ASBL",
        "recipient_email": "info@villageliegeois.be",
        "recipient_postal": "Rue du Teris 25, 4100 Seraing",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after De Sprong@2287 / Borgerstein@2286; NOT Village n1@2269",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2288":
        if r.get("status") not in ("open", "in_progress"):
            raise SystemExit(f"rq_2288 unexpected status={r.get('status')}")
        r["title"] = (
            f"leftover dual — Village Liegeois YE2025 Medium (empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual Village Liegeois YE2025 FREE Walloon ETA Seraing after De Sprong / Borgerstein/WEBO; preferred AGB/FARO/AIESH/REW/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; Village Liegeois Marie-Reine Prignon 0430.721.768 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"empty omzet; bruto JUMP {BRUTO} (+7.79%); pnl DROP {PNL} (-6.87% vs {PNL24}); "
            f"equity JUMP {EQUITY} (+6.63% vs {EQUITY24}); FTE JUMP {FTE} (vs {FTE24}); 1 VE ASBL; NACE 88.993; "
            f"neerlegging 23.06.2026; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/REW/Citeco/Groupe Foes YE2024; after De Sprong@2287 / Borgerstein@2286; NOT Village n1@2269; next EVERY-10 2290"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2288 not found on close")

if not any(r.get("task_id") == "rq_2289" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2289",
            "title": "leftover dual after Village Liegeois — prefer AGB/FARO-YE2025/AIESH-REW/Citeco-Groupe Foes-or-unused DSO-IGS-HVZ-ETA-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                f"leftover dual after Village Liegeois YE2025 Medium (empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ if live YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Roseau Vert/Ateliers Mons/Monceau/De Sprong/Aralea if YE2025). "
                "Do NOT redo Village Liegeois/De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/Die Zukunft/De Dageraad/"
                "Ateliers du 94/Village n1/Amis des Aveugles stack. "
                "Citeco/Groupe Foes/FARO/AIESH/REW still YE2024 as of tick2288."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2288 Village Liegeois; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; "
                "Aralea/Manupal/Vlotter/Buseloc/De Sprong YE2024; next every-10 2290"
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
            "last_unit_id": "rq_2288",
            "ticks_completed": "2288",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual Village Liegeois 0430.721.768 Medium "
                f"(empty omzet; bruto JUMP {BRUTO} +7.79%; pnl DROP {PNL} -6.87%; equity JUMP {EQUITY} +6.63%; FTE JUMP {FTE}; 1 VE Seraing Walloon ETA); "
                f"after De Sprong@2287 / Borgerstein@2286; AGB Bornem JR2024; FARO/AIESH/REW/Citeco/Groupe Foes YE2024; next rq_2289; next EVERY-10 2290; continuous hole_fill"
            ),
        }
    )

draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — Village Liegeois (NBB PDF / empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Village Liegeois Marie-Reine Prignon ASBL — KBO **0430.721.768** (Actief; Rue du Teris 25, 4100 Seraing; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA / AVIQ; abbrev C.A.P.V.A.L. Village n05 Reine Fabiola)  
**recipient:** info@villageliegeois.be · Rue du Teris 25, 4100 Seraing (tél. 04/337 56 76)  
**sources:** [CW EN](https://www.companyweb.be/en/0430721768) · [CW NL](https://www.companyweb.be/nl/0430721768/village-liegeois) · [CW FR](https://www.companyweb.be/fr/0430721768) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0430721768) · [site](https://www.villageliegeois.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL **VILLAGE LIEGEOIS MARIE - REINE PRIGNON** sinds **18.10.1986**; **1 VE**; zetel Rue du Teris 25, 4100 Seraing; RSZ/BTW NACE **88.993** (+16.240 emballage / 81.300 landschap / 43.350 afwerking / 01.191 bloementeelt); Florence Prignon dagelijks bestuur.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +7.79% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP −6.87% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +6.63% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** JUMP vs {FTE24}; filed **23.06.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; REW YE2024; Citeco YE2024; Groupe Foes YE2024; Aralea/Manupal YE2024. After Borgerstein/WEBO@2286. Do NOT redo Village n°1 Braine@2269 / Amis des Aveugles@2270 / Mobiel / Posthoorn / Ateljee / Die Zukunft stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Village Liegeois Marie-Reine Prignon ASBL
via info@villageliegeois.be
Rue du Teris 25, 4100 Seraing
Betreft: Openbaarmaking jaarrekening 2025 Village Liegeois (KBO 0430.721.768)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Code de la démocratie locale / wallon openbaarheid e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij unpublished omzet naast bruto EUR{BRUTO} (+7.79%),
   pnl DROP EUR{PNL} (vs YE2024 EUR{PNL24}) en FTE JUMP {FTE} (vs {FTE24}).
3. Overzicht van AVIQ / EWETA loonkostentussenkomsten achter personeelskosten (FTE {FTE})
   en de subsidiematrix YE2025.
4. Verdeling omzet/activiteiten parks-jardins / conditionnement / menuiserie / mailing.
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
            "unit": "rq_2288",
            "entity": ENTITY,
            "kbo": "0430.721.768",
            "omzet": None,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "confidence": "medium",
            "gap": GAP,
            "sources": [s["source_id"] for s in sources],
        },
        indent=2,
    ),
    encoding="utf-8",
)
(raw / "cw_en_excerpt.txt").write_text(
    f"Village Liegeois YE2025 CW EN\nempty omzet bruto {BRUTO} (+7.79%) pnl {PNL} DROP equity {EQUITY} (+6.63%) FTE {FTE} JUMP\nfiled 23.06.2026\nurl https://www.companyweb.be/en/0430721768\n",
    encoding="utf-8",
)

log_path = Path("docs/doge/loop_log.md")
log_entry = f"""

### 2026-08-27T14:30:00Z - tick 2288 - rq_2288 Village Liegeois Seraing (empty omzet / bruto JUMP 2.25m / pnl DROP / FTE JUMP {FTE} / Medium)

- Unit: **rq_2288** leftover dual after **rq_2287 De Sprong** / **rq_2286 Borgerstein/WEBO**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Citeco still **YE2024**; Groupe Foes still **YE2024**; Aralea/Manupal/Vlotter/Buseloc/De Sprong still **YE2024**. Took unused FREE Walloon ETA **Village Liegeois Marie-Reine Prignon ASBL** YE2025 (KBO **0430.721.768**; Rue du Teris 25 Seraing; **Actief** **1 VE**; NACE **88.993**; abbrev C.A.P.V.A.L. Village n05 Reine Fabiola). Do not redo De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/Die Zukunft/Village n1 Braine@2269/Amis des Aveugles@2270 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +7.79% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP -6.87% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +6.63%; FTE **{FTE}** JUMP (vs {FTE24}); neerlegging **23.06.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via info@villageliegeois.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2288=done + rq_2289 open; loop_state ticks=2288; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290**). Next: rq_2289 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Groupe Foes / unused DSO-water-IGS-HVZ / unused ETA Roseau Vert-Ateliers Mons-Monceau / unused maatwerk De Sprong-Aralea).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"tick{TICK} write OK: {ENTITY} bruto={BRUTO} pnl={PNL} pi={PI} next=rq_2289")
