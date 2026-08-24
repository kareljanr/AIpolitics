# tick 2289: leftover dual REW Wavre YE2025 hole-fill — claim queue FIRST
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path("docs/doge/data")
TICK = "2289"
TS = "2026-08-27T14:45:00Z"
ENTITY = "igs_rew_wavre"
GAP = "gap_rew_nbb_pdf_assets_debt_omzet_14_72m_pnl_profit_flip_fte_jump_dso_matrix_l5"
LB = "lb_rew_omzet_14_72m_pnl_profit_flip_fte_jump_jr2025"
COMM = "comm_rew_jr2025_statutory_dso_wavre_omzet_pnl_profit_flip"
SRC_EN = "src_rew_jr2025_cw_en"

OMZET = 14717850
BRUTO = 8850569
PNL = 196086
EQUITY = 61985489
FTE = 35.0
OMZET24 = 13221985
BRUTO24 = 7512719
PNL24 = -255744
EQUITY24 = 61789403
FTE24 = 32.0
RATIO = round(BRUTO / OMZET, 2)  # 0.60
PI = 5.85


def append_csv(path, fieldnames, rows):
    path = Path(path)
    data = path.read_bytes()
    if data and not data.endswith(b"\n"):
        path.write_bytes(data + b"\n")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        for r in rows:
            w.writerow(r)


# --- CLAIM / TAKEOVER rq_2289 FIRST ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

claimed = False
for r in rq_rows:
    if r.get("task_id") == "rq_2289":
        st = r.get("status")
        eid = (r.get("entity_id") or "").strip()
        if st == "done":
            raise SystemExit("rq_2289 already done")
        if st == "open":
            r["status"] = "in_progress"
            r["entity_id"] = ENTITY
            r["updated_utc"] = TS
            r["notes"] = (r.get("notes") or "") + f"; tick{TICK} CLAIM REW Wavre in_progress"
        elif st == "in_progress" and (not eid or eid == ENTITY):
            r["entity_id"] = ENTITY
            r["updated_utc"] = TS
            if "REW" not in (r.get("notes") or ""):
                r["notes"] = (r.get("notes") or "") + f"; tick{TICK} TAKEOVER empty race-lock -> REW Wavre"
        else:
            raise SystemExit(f"rq_2289 blocked status={st} entity={eid}")
        claimed = True
        break
if not claimed:
    raise SystemExit("rq_2289 not found")

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields)
    w.writeheader()
    w.writerows(rq_rows)
print(f"CLAIMED/TOOK rq_2289 -> in_progress {ENTITY}")

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
        "title": "REW YE2025 Companyweb EN",
        "url": "https://www.companyweb.be/en/0644638937/reseau-denergies-de-wavre",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW EN YE2025; last balance sheet year 2025; omzet {OMZET} bruto {BRUTO} pnl {PNL} equity {EQUITY} FTE {FTE}; FAQ filing text lags 11-12-2025 / omzet 13.22m YE2024; assets/debt Unknown; Walloon municipal DSO Wavre",
    },
    {
        "source_id": "src_rew_jr2025_cw_nl",
        "title": "REW YE2025 Companyweb NL",
        "url": "https://www.companyweb.be/nl/0644638937/rew",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW NL corroboration YE2025; laatste balansjaar 2025; omzet JUMP {OMZET}; pnl PROFIT FLIP {PNL}; NACE distributie elektriciteit",
    },
    {
        "source_id": "src_rew_jr2025_cw_fr",
        "title": "REW YE2025 Companyweb FR",
        "url": "https://www.companyweb.be/fr/0644638937/rew",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-27",
        "source_class": "company_register_aggregator",
        "notes": f"tick{TICK}; Medium CW FR corroboration YE2025; dernier bilan 2025; CA {OMZET}; bénéfice {PNL}; marge brute {BRUTO}; SC Actif Wavre",
    },
    {
        "source_id": "src_rew_kbo_0644638937",
        "title": "KBO REW 0644.638.937",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0644638937",
        "publisher": "FOD Economie KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": f"tick{TICK}; Strong KBO Actief SC RESEAU D'ENERGIES DE WAVRE / REW sinds 18.12.2015; 1 VE; Aanbestedende overheid; RSZ NACE 35.140; BTW NACE 84.114; officiel.ic-rew@grdwavre.be; Rue Provinciale 265 1301 Wavre; jaarvergadering juni",
    },
    {
        "source_id": "src_rew_site_foi_2289",
        "title": "REW FOI channel officiel.ic-rew@grdwavre.be",
        "url": "https://www.rew.be/",
        "publisher": "REW / Reseau d'energies de Wavre",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": f"tick{TICK}; officiel.ic-rew@grdwavre.be + info@grdwavre.be; Walloon municipal electricity DSO Wavre/Bierges/Limal; Synergrid member dual AIEG/AIESH",
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
        "budget_id": "bud_rew_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": OMZET,
        "amount_max_eur": OMZET,
        "basis": "CW statutory omzet/turnover YE2025",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; omzet JUMP +11.31% vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_rew_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": BRUTO,
        "amount_max_eur": BRUTO,
        "basis": f"CW statutory bruto_marge YE2025 (~{RATIO}x omzet)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; bruto JUMP +17.81% vs YE2024 {BRUTO24}; bruto÷omzet ~{RATIO}x",
    },
    {
        "budget_id": "bud_rew_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": PNL,
        "amount_max_eur": PNL,
        "basis": "CW statutory winst/verlies YE2025 pnl PROFIT FLIP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; pnl PROFIT FLIP {PNL} vs YE2024 LOSS {PNL24} (+176.67% CW)",
    },
    {
        "budget_id": "bud_rew_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": EQUITY,
        "amount_max_eur": EQUITY,
        "basis": "CW statutory eigen_vermogen YE2025 equity JUMP",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; equity JUMP +0.32% vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_rew_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": f"CW social-balance FTE {FTE}",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown; Walloon municipal DSO",
    },
    {
        "budget_id": "bud_rew_pnl_jr2024_statutory_cmp",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": PNL24,
        "amount_min_eur": PNL24,
        "amount_max_eur": PNL24,
        "basis": "CW statutory pnl YE2024 comparative LOSS",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; YE2024 pnl LOSS {PNL24} comparative (pre PROFIT FLIP)",
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
        "title": f"REW YE2025 leftover dual (omzet JUMP 14.72m / pnl PROFIT FLIP / FTE {FTE} / Medium)",
        "entity_id": ENTITY,
        "beneficiary": "Wavre/Bierges/Limal electricity DSO customers + public lighting",
        "legal_basis": "SC REW (KBO 0644.638.937; Actief; 1 VE; NACE RSZ 35.140; Aanbestedende overheid; Walloon municipal DSO)",
        "decision_date": "2025-12-11",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": OMZET,
        "cash_by_year": json.dumps(cash, separators=(",", ":")),
        "remaining_eur": 0,
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0644638937/reseau-denergies-de-wavre",
        "stated_goal": "Municipal electricity distribution + public lighting for Wavre agglomeration",
        "cut_option": "Publish NBB PDF assets/debt/cash; disclose CWaPE regulated vs non-regulated split and Synergrid/AREWAL dual costs",
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Brabant_Wallon>Wavre>REW>JR2025_statutory_L5",
        "notes": f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} (~{RATIO}x); pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 1 VE SC; after Village Liegeois@2288 / De Sprong@2287; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; REW preferred dual NOW YE2025",
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
        "name": f"REW omzet JUMP 14.72m / pnl PROFIT FLIP / FTE {FTE} (YE2025 Walloon municipal DSO Wavre)",
        "level": "L5",
        "type": "walloon_municipal_dso_statutory",
        "hierarchy_path": "Wallonie>Brabant_Wallon>Wavre>REW>JR2025",
        "annual_cost_eur": OMZET,
        "total_cost_eur": OMZET,
        "tco_notes": f"CW omzet JUMP {OMZET} (+11.31%) / bruto JUMP {BRUTO} (+17.81%; ~{RATIO}x) / pnl PROFIT FLIP {PNL} (vs LOSS {PNL24}) / equity JUMP {EQUITY} (+0.32%) / FTE JUMP {FTE} (vs {FTE24}) / 1 VE municipal electricity DSO dual Synergrid/AIEG/AIESH",
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Wavre/Bierges/Limal electricity + public-lighting users",
        "stated_goal": "Walloon municipal electricity distribution GRD REW",
        "measured_outcome": f"omzet JUMP +11.31%; bruto JUMP +17.81%; pnl PROFIT FLIP after 2 LOSS years; equity JUMP +0.32%; FTE {FTE}; CW last year 2025",
        "absurdity_score": 5.8,
        "cost_score": 6.5,
        "difficulty": 2.5,
        "priority_index": PI,
        "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose CWaPE regulated activity matrix and AREWAL/Synergrid dual costs behind 14.7m municipal DSO turnover",
        "status": "open",
        "struck_reason": "",
        "notes": f"tick{TICK}; Medium CW; FOI {GAP}; preferred dual REW now YE2025 (prior ticks YE2024); stalls AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; after Village Liegeois@2288 / De Sprong@2287",
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
        "name_nl": "REW / Reseau d'energies de Wavre (Waals gemeentelijk elektriciteits-DSO)",
        "name_fr": "REW / Reseau d'energies de Wavre (GRD electricite communal wallon)",
        "name_en": "REW / Reseau d'energies de Wavre (Walloon municipal electricity DSO)",
        "level": "intercommunale",
        "parent_id": "wallonie_gov",
        "community_language": "fr",
        "website": "https://www.rew.be/",
        "foi_email": "officiel.ic-rew@grdwavre.be",
        "foi_postal": "Rue Provinciale 265, 1301 Wavre",
        "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0644.638.937 Actief 1 VE SC Aanbestedende overheid RSZ 35.140 BTW 84.114; omzet JUMP {OMZET} (+11.31%) bruto JUMP {BRUTO} (~{RATIO}x / +17.81%) pnl PROFIT FLIP {PNL} (vs LOSS {PNL24}) equity JUMP {EQUITY} (+0.32%) FTE JUMP {FTE}; FAQ filing lag 11-12-2025 YE2024-text; assets/debt Unknown; FOI {GAP}; after Village Liegeois@2288 / De Sprong@2287; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; dual Synergrid/AIEG/AIESH; not TE-additive",
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
        "hierarchy_path": "Wallonie>Brabant_Wallon>Wavre>REW>NBB_PDF_assets_debt_omzet_pnl_profit_flip_dso",
        "entity_id": ENTITY,
        "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet JUMP EUR{OMZET} (+11.31%); bruto EUR{BRUTO} (~{RATIO}x); pnl PROFIT FLIP EUR{PNL} vs LOSS EUR{PNL24}; FTE {FTE}; CWaPE regulated vs non-regulated / AREWAL-Synergrid dual cost matrix",
        "why_it_matters": f"Medium CW shows Walloon municipal electricity DSO Wavre (omzet JUMP 14.72m / pnl PROFIT FLIP after 2 LOSS years / equity 62.0m / FTE {FTE}); assets/debt unpublished; preferred dual long stalled YE2024 now YE2025",
        "priority": 8,
        "recipient_body": "REW / Reseau d'energies de Wavre",
        "recipient_email": "officiel.ic-rew@grdwavre.be",
        "recipient_postal": "Rue Provinciale 265, 1301 Wavre",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred dual REW YE2025 now live; stalls FARO/AIESH/Citeco/Groupe Foes YE2024; AGB Bornem JR2024; after Village Liegeois@2288",
    }
]
append_csv(ROOT / "foi_queue.csv", foi_fields, foi)

# --- close rq_2289 done + spawn rq_2290 ---
with rq_path.open(newline="", encoding="utf-8") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []

updated = False
for r in rq_rows:
    if r.get("task_id") == "rq_2289":
        if r.get("status") not in ("open", "in_progress"):
            raise SystemExit(f"rq_2289 unexpected status={r.get('status')}")
        r["title"] = (
            f"leftover dual — REW YE2025 Medium (omzet JUMP 14.72m / bruto~{RATIO}x / pnl PROFIT FLIP / FTE {FTE})"
        )
        r["status"] = "done"
        r["entity_id"] = ENTITY
        r["instructions"] = (
            "leftover dual REW YE2025 FREE Walloon municipal DSO Wavre after Village Liegeois; preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
        )
        r["blocked_gap_id"] = GAP
        r["updated_utc"] = TS
        r["notes"] = (
            f"tick{TICK}; REW SC Wavre 0644.638.937 YE2025 Medium CW NL+EN+FR + Strong KBO; "
            f"omzet JUMP {OMZET} (+11.31%); bruto JUMP {BRUTO} (~{RATIO}x / +17.81%); pnl PROFIT FLIP {PNL} (vs LOSS {PNL24}); "
            f"equity JUMP {EQUITY} (+0.32% vs {EQUITY24}); FTE JUMP {FTE} (vs {FTE24}); 1 VE SC Aanbestedende overheid; "
            f"RSZ 35.140 + BTW 84.114; FAQ filing lag 11-12-2025 YE2024-text; assets/debt Unknown; FOI {GAP} ready NOT sent; "
            f"stalls AGB Bornem JR2024 / FARO/AIESH/Citeco/Groupe Foes YE2024; after Village Liegeois@2288 / De Sprong@2287; next EVERY-10 2290"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2289 not found on close")

if not any(r.get("task_id") == "rq_2290" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_2290",
            "title": "EVERY-10 + leftover dual after REW — prefer AGB/FARO-YE2025/AIESH/Citeco-Groupe Foes-or-unused DSO-IGS-HVZ-ETA-maatwerk",
            "sprint": "hole_fill",
            "priority": "10",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "EVERY-10 mandatory: refresh progress_every_10_ticks.md (layers A–E) + doge_waste_top10_current.md "
                f"then hole-fill ONE unit. leftover dual after REW YE2025 Medium (omzet JUMP 14.72m / pnl PROFIT FLIP / FTE {FTE}). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH if YE2025, "
                "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                "else unused DSO/water/nuclear/IGS/HVZ if live YE2025, "
                "else unused ETA-VAPH-WZC-maatwerk with live sourced euros (Roseau Vert/Ateliers Mons/Monceau/Aralea if YE2025). "
                "Do NOT redo REW/Village Liegeois/De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/Die Zukunft/"
                "De Dageraad/Ateliers du 94/Village n1/Amis des Aveugles/AIEG stack. "
                "Citeco/Groupe Foes/FARO/AIESH still YE2024 as of tick2289; AGB Bornem JR2024."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": (
                "spawned after tick2289 REW; EVERY-10 mandatory at 2290; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                "AGB Bornem JR2024; Aralea/Manupal/Vlotter/Buseloc YE2024; next every-10 2290"
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
            "last_unit_id": "rq_2289",
            "ticks_completed": "2289",
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual REW 0644.638.937 Medium "
                f"(omzet JUMP {OMZET} +11.31%; bruto JUMP {BRUTO} ~{RATIO}x; pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY} +0.32%; FTE JUMP {FTE}; 1 VE Wavre municipal DSO); "
                f"after Village Liegeois@2288 / De Sprong@2287; AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next rq_2290 EVERY-10; continuous hole_fill"
            ),
        }
    )

draft = Path(f"docs/doge/foi/drafts/{GAP}.md")
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — REW (NBB PDF / omzet JUMP 14.72m / pnl PROFIT FLIP / FTE {FTE})

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** REW / Reseau d'energies de Wavre — KBO **0644.638.937** (Actief; Rue Provinciale 265, 1301 Wavre; **1 VE**; FTE {FTE} CW; RSZ **35.140**; Aanbestedende overheid; Walloon municipal electricity DSO)  
**recipient:** officiel.ic-rew@grdwavre.be · Rue Provinciale 265, 1301 Wavre  
**sources:** [CW EN](https://www.companyweb.be/en/0644638937/reseau-denergies-de-wavre) · [CW NL](https://www.companyweb.be/nl/0644638937/rew) · [CW FR](https://www.companyweb.be/fr/0644638937/rew) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0644638937) · [REW site](https://www.rew.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; FAQ filing text lags YE2024)

## Context
- KBO Strong: Actief SC **RESEAU D'ENERGIES DE WAVRE** / **REW** sinds **18.12.2015**; **1 VE**; zetel Rue Provinciale 265, 1301 Wavre (sinds 13.05.2019); Aanbestedende overheid; RSZ NACE **35.140**; BTW NACE **84.114**; FOI **officiel.ic-rew@grdwavre.be**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +11.31% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +17.81% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL:,}** PROFIT FLIP vs YE2024 LOSS EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +0.32% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (vs {FTE24}); CW last balance sheet year **2025** (FAQ text still cites filing 11-12-2025 / omzet 13.22m YE2024-lag — Medium).
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024. **REW preferred dual NOW YE2025** (long YE2024 stall broken). After Village Liegeois@2288 / De Sprong@2287. Do NOT redo Village Liegeois / De Sprong / Borgerstein / WEBO / Mobiel / Posthoorn / Ateljee / Die Zukunft / De Dageraad / Ateliers du 94 / Village n1 / Amis des Aveugles / AIEG stack.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: REW / Reseau d'energies de Wavre
via officiel.ic-rew@grdwavre.be
Rue Provinciale 265, 1301 Wavre
Betreft: Openbaarheid jaarrekening 2025 REW (KBO 0644.638.937)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Waals Decreet openbaarheid van bestuur e.a.), vraag ik openbaarmaking van:

1. NBB/CBSO PDF van de jaarrekening YE2025 (balans + resultaten + bijlage; activa/schulden/cash).
2. Toelichting bij omzet JUMP EUR{OMZET} (+11.31%) naast bruto EUR{BRUTO}
   (~{RATIO}x omzet) en pnl PROFIT FLIP EUR{PNL} (vs YE2024 LOSS EUR{PNL24}).
3. Splitsing CWaPE-gereguleerde vs niet-gereguleerde activiteiten / openbare verlichting
   (FTE {FTE}) en AREWAL/Synergrid dual-kosten YE2025.
4. Schulden LT/KT en liquide middelen YE2025 (niet gepubliceerd op Companyweb).
5. Overzicht van gemeentelijke / regionale transfers YE2024–YE2025.

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
            "unit": "rq_2289",
            "entity": ENTITY,
            "kbo": "0644.638.937",
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
    f"REW YE2025 CW EN\nomzet {OMZET} (+11.31%) bruto {BRUTO} (+17.81% ~{RATIO}x) pnl {PNL} PROFIT FLIP vs {PNL24} equity {EQUITY} (+0.32%) FTE {FTE}\nlast balance sheet year 2025; FAQ filing lag 11-12-2025 YE2024-text\nurl https://www.companyweb.be/en/0644638937/reseau-denergies-de-wavre\n",
    encoding="utf-8",
)

log_path = Path("docs/doge/loop_log.md")
log_entry = f"""

### 2026-08-27T14:45:00Z - tick 2289 - rq_2289 REW Wavre (omzet JUMP 14.72m / bruto~{RATIO}x / pnl PROFIT FLIP / FTE {FTE} / Medium)

- Unit: **rq_2289** leftover dual after **rq_2288 Village Liegeois** / **rq_2287 De Sprong**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco still **YE2024**; Groupe Foes still **YE2024**. **REW preferred dual NOW YE2025** (CW last balance sheet year **2025**; prior ticks incorrectly still YE2024). Took unused FREE Walloon municipal electricity DSO **REW / Reseau d'energies de Wavre** YE2025 (KBO **0644.638.937**; Rue Provinciale 265 Wavre; **Actief** **1 VE**; RSZ **35.140**; Aanbestedende overheid; Synergrid member dual AIEG/AIESH). Do not redo Village Liegeois/De Sprong/Borgerstein/WEBO/Mobiel/Posthoorn/Ateljee/Die Zukunft/De Dageraad/Ateliers du 94/Village n1/Amis des Aveugles/AIEG stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +11.31% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +17.81% (bruto÷omzet ~{RATIO}x); pnl **EUR{PNL}** PROFIT FLIP vs YE2024 LOSS EUR{PNL24}; equity **EUR{EQUITY}** JUMP +0.32%; FTE **{FTE}** (vs {FTE24}); FAQ filing text lags **11-12-2025** / omzet 13.22m YE2024 — Medium. Strong KBO Actief 1 VE SC. Assets/debt Unknown. FOI via officiel.ic-rew@grdwavre.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2289=done + rq_2290 open (EVERY-10); loop_state ticks=2289; raw docs/doge/data/raw/tick{TICK}/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2280**; next **2290 MUST** refresh progress + waste top10 then hole-fill one unit). Next: rq_2290 EVERY-10 + AGB/FARO-if-YE2025 / AIESH / Citeco-Groupe Foes / unused DSO-IGS-HVZ-ETA-maatwerk.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"tick{TICK} write OK: {ENTITY} omzet={OMZET} pnl={PNL} pi={PI} next=rq_2290 EVERY-10")
