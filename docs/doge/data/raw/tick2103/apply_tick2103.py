# tick 2103 — Korian Belgium NV YE2025 Medium (holding dual vs SLG ops)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFTS = ROOT / "foi" / "drafts"

csv.field_size_limit(10**7)
UTC = "2026-08-25T06:30:00Z"
TICK = 2103
RQ = "rq_2103"
NEXT_RQ = "rq_2104"
ENTITY = "nv_korian_belgium"
GAP = "gap_korian_belgium_nbb_pdf_assets_debt_pnl_drop_holding_dual_matrix_l5"
LB = "lb_korian_belgium_omzet_jump_36_66m_pnl_drop_holding_dual_jr2025"
COMM = "comm_korian_belgium_jr2025_statutory_holding_wzc"

OMZET = 36661929
PNL = 3410765
EQUITY = 194558071
BRUTO = 23130494
FTE = 47.4
OMZET24 = 35127187
PNL24 = 6790713
EQUITY24 = 191147306
BRUTO24 = 30615545
FTE24 = "Unknown"
OMZET_YOY = "JUMP +4.37%"
PNL_YOY = "DROP -49.77%"
EQUITY_YOY = "JUMP +1.78%"
BRUTO_YOY = "DROP -24.45%"
FTE_YOY = "Unknown YoY"
FILED = "15.08.2026"
KBO = "0869.769.702"
KBO_DIGITS = "0869769702"
EMAIL = "info@korian.be"
ADDR = "Satenrozen 1B, 2550 Kontich"
SITE = "https://www.korian.be/"
CW_NL = f"https://www.companyweb.be/nl/{KBO_DIGITS}/korian-belgium"
CW_EN = f"https://www.companyweb.be/en/{KBO_DIGITS}/korian-belgium"
CW_FR = f"https://www.companyweb.be/fr/{KBO_DIGITS}/korian-belgium"
KBO_URL = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO_DIGITS}"
)
NBB = f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}"
PI = "5.9"
ABSURD = "6.5"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Korian Belgium, ORES SC, SLG Vlaanderen, Always Home, "
    "SLG Operaties Vlaanderen, AREWAL, Familiezorg Gent, emeis Belgium, Begralim, "
    "Sint-Lucia, Lidwina, SED, Zilvervogel, Familiezorg WV, De Lovie, Ocura, "
    "Armonea, Colisée Belgium, AGB Bornem, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, "
    "BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
    "CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, "
    "EURIDICE, IRE*, BRUGEL, ORES Assets."
)


def append_csv(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        existing = list(reader)
    ids = set()
    id_key = None
    for cand in (
        "source_id",
        "budget_id",
        "commitment_id",
        "item_id",
        "entity_id",
        "gap_id",
        "task_id",
    ):
        if cand in (fieldnames or []):
            id_key = cand
            break
    if id_key:
        ids = {r.get(id_key) for r in existing}
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
        for r in rows:
            if id_key and r.get(id_key) in ids:
                continue
            out = {k: r.get(k, "") for k in fieldnames}
            w.writerow(out)


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: {RQ} status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Korian Belgium YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Korian Belgium YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto DROP {BRUTO} pnl DROP {PNL} "
                f"equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.301 ROB + RSZ 64.210 "
                "holding; 1 VE NV; dual SLG Vlaanderen / SLG Operaties; "
                "DISTINCT Armonea/Always Home/emeis/ORES SC"
            )
            r["notes"] = (
                f"tick{TICK} Korian Belgium Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto DROP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                f"equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next "
                f"{NEXT_RQ}; next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Korian Belgium — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Comnexio/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Korian Belgium YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                    "AIESH/REW if YE2025, else Comnexio 0727.639.263 YE2025 live unused "
                    "deferred, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Korian Belgium; next every-10 2110; "
                    "Comnexio YE2025 deferred"
                ),
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
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
            lineterminator="\n",
        )
        w.writeheader()
        w.writerow(
            {
                "state_id": "main",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "last_tick_utc": UTC,
                "last_unit_id": RQ,
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Korian Belgium {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE {FTE}; assets/debt Unknown; NACE 87.301+64.210 1 VE holding dual "
                    "SLG); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next "
                    f"{NEXT_RQ}; next every-10 2110; continuous hole_fill"
                ),
            }
        )


def write_foi_draft():
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP}.md"
    path.write_text(
        f"""# FOI draft — Korian Belgium (NBB PDF / assets-debt / pnl-drop / holding dual)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Korian Belgium NV — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR} · +32 (0)3 443 76 50  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [NBB consult]({NBB}) · [Korian contact]({SITE}contact/)  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; FTE YoY Unknown; KBO Strong identity)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **PROFIT EUR{PNL}** {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** ({FTE_YOY}); assets/debt **Unknown**.
- KBO: Actief NV; **1 VE**; BTW NACE **87.301** ROB + RSZ NACE **64.210** holdings; zetel {ADDR}; HQ of SLG path.
- Dual of **SLG Vlaanderen** VZW (omzet JUMP 115.87m / pnl FLIP LOSS / equity thin) and **SLG Operaties Vlaanderen** NV (omzet JUMP 58.28m / FTE JUMP 1095.3). Preferred stall still blocked: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Comnexio CW thin.
- DISTINCT from Armonea / Always Home / emeis / Colisée / ORES SC.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Korian Belgium NV
{ADDR}
via {EMAIL}
Betreft: Openbaarmaking NBB-jaarrekening 2025 Korian Belgium + balans/holding-dual matrix (KBO {KBO})
Geachte, op grond van toepasselijke openbaarheidsregels (waar van toepassing Bestuursdecreet / wet openbaarheid; desgevallend als houder/bestuurder van publiek gesubsidieerde ROB/RVT-groepsentiteiten) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}) + depositreferentie.
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Toelichting pnl DROP naar EUR{PNL} (-49.77% vs YE2024 EUR{PNL24}) en bruto DROP naar EUR{BRUTO} bij equity EUR{EQUITY}.
4. Split omzet/bruto naar holding (NACE 64.210) vs ROB (87.301) vs management fees / andere; FTE {FTE} sociale balans + YoY.
5. Relatie tot SLG Vlaanderen 0410.958.712 / SLG Operaties Vlaanderen 0845.064.196 (aandeelhouderschap, management fees, garanties, intra-groep schulden/vorderingen 2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )


def append_log():
    entry = f"""


## Tick {TICK} - {UTC} - rq_2103 Korian Belgium (omzet JUMP 36.66m / pnl DROP 3.41m / Medium)

- Unit: **rq_2103** leftover dual after **rq_2102 ORES SC** (concurrent race closed ORES on 2102; this tick takes preferred deferred **Korian Belgium**). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Comnexio CW thin/no YE euros. Took unused leftover **Korian Belgium** YE2025 (KBO **{KBO}**; {ADDR}; Antwerpen **NV** holding/ROB NACE **87.301 + RSZ 64.210** / **1 VE**; HQ of SLG path). Do not redo ORES SC/SLG Vlaanderen/SLG Operaties/Always Home/AREWAL/Familiezorg Gent/emeis/Begralim/Armonea/Colisée/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.37%; bruto **EUR{BRUTO}** DROP -24.45%; pnl **PROFIT EUR{PNL}** DROP -49.77% vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP +1.78%; FTE **{FTE}** (YoY Unknown); neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 1 VE; email {EMAIL}. Omzet used as primary envelope (holding dual vs SLG ops daughters).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2103/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**last every-10 was 2100**; next **2110**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Comnexio deferred / unused WZC).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_korian_belgium_jr2025_cw_nl",
                "title": "Companyweb NL — Korian Belgium YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} FTE {FTE}",
            },
            {
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "title": "Companyweb EN — Korian Belgium YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; equity {EQUITY}; FTE {FTE}; last BS year 2025",
            },
            {
                "source_id": "src_korian_belgium_jr2025_cw_fr",
                "title": "Companyweb FR — Korian Belgium YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_korian_belgium_kbo_{TICK}",
                "title": f"KBO — Korian Belgium {KBO}",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 1 VE; NACE 87.301 ROB + RSZ 64.210 holdings; "
                    f"zetel {ADDR}; Strong identity"
                ),
            },
            {
                "source_id": f"src_korian_belgium_contact_{TICK}",
                "title": "Korian Belgium contact",
                "url": f"{SITE}contact/",
                "publisher": "Korian Belgium",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; info@korian.be; +32 (0)3 443 76 50; {ADDR}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_korian_belgium_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope holding/ROB NV)",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {OMZET_YOY} vs YE2024 {OMZET24}; dual SLG ops daughters",
            },
            {
                "budget_id": "bud_korian_belgium_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_korian_belgium_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_korian_belgium_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_korian_belgium_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE}; YoY Unknown on CW; thin vs SLG ops FTE",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Korian Belgium YE2025 leftover dual "
                    "(omzet JUMP 36.66m / pnl DROP / holding dual)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "WZC/ROB/RVT residents via Korian Belgium holding / SLG path"
                ),
                "legal_basis": (
                    f"NV holding + ROB (KBO {KBO}; NACE 87.301 + RSZ 64.210; 1 VE)"
                ),
                "decision_date": "2026-08-15",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": (
                    "Private care holding / ROB HQ (Korian Belgium / SLG dual)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl/bruto DROP; map "
                    "holding dual vs SLG Vlaanderen / SLG Operaties related-party flows"
                ),
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>Korian_Belgium>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "dual SLG Vlaanderen / SLG Operaties; DISTINCT Armonea/Always Home/"
                    "emeis/Colisée/ORES SC"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    "Korian Belgium omzet JUMP 36.66m / pnl DROP / holding dual (YE2025)"
                ),
                "level": "L5",
                "type": "wzc_holding_statutory_private_care",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>Korian_Belgium>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} {OMZET_YOY} (primary); bruto {BRUTO} "
                    f"{BRUTO_YOY}; pnl PROFIT {PNL} {PNL_YOY}; equity {EQUITY} "
                    f"{EQUITY_YOY}; FTE {FTE} {FTE_YOY}; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_korian_belgium_jr2025_cw_en",
                "beneficiaries": (
                    "WZC/ROB path via holding HQ (1 VE); public Zorgkas day-price path "
                    "via SLG daughters"
                ),
                "stated_goal": "Private care holding / ROB HQ (Korian/SLG)",
                "measured_outcome": (
                    f"omzet {OMZET_YOY}; bruto {BRUTO_YOY}; pnl {PNL_YOY}; "
                    f"equity {EQUITY_YOY}; FTE {FTE} thin vs SLG ops daughters"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "FOI NBB PDF + holding vs ROB split + related-party map to "
                    "SLG Vlaanderen / SLG Operaties; Zorgkas continuity risk"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
                    "dual SLG Vlaanderen/Operaties; DISTINCT Armonea/Always Home/emeis/ORES SC"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Korian Belgium NV (Kontich / SLG HQ)",
                "name_fr": "Korian Belgium SA (Kontich / SLG HQ)",
                "name_en": "Korian Belgium NV (Kontich / SLG HQ)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV "
                    f"1 VE; NACE 87.301 ROB + RSZ 64.210 holdings; omzet JUMP "
                    f"{OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m pnl DROP "
                    f"{PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; "
                    f"assets/debt Unknown; neerlegging {FILED}; FOI {GAP}; preferred "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; {ADDR}; {EMAIL}; "
                    "dual vzw_slg_vlaanderen / nv_slg_operaties_vlaanderen; "
                    "DISTINCT Armonea/Always Home/emeis/Colisée/ORES SC"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>Korian_Belgium>NBB_PDF_assets_debt_pnl_drop_holding_dual"
                ),
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); "
                    "pnl/bruto DROP path; holding (64.210) vs ROB (87.301) omzet split; "
                    "FTE YoY; SLG Vlaanderen / SLG Operaties related-party map"
                ),
                "why_it_matters": (
                    "Medium CW shows 36.66m omzet Korian holding/ROB NV with pnl DROP "
                    "-49.77% and only 47.4 FTE while SLG daughters run 115m+58m omzet — "
                    "public-care day-price continuity risk without holding dual transparency"
                ),
                "priority": "8",
                "recipient_body": "Korian Belgium NV",
                "recipient_email": EMAIL,
                "recipient_postal": f"{ADDR} (tel +32 (0)3 443 76 50)",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-25",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK}; human-send only; Medium CW; next every-10 2110"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print(f"OK tick{TICK} {ENTITY} omzet={OMZET} pi={PI} gap={GAP}")


if __name__ == "__main__":
    main()
