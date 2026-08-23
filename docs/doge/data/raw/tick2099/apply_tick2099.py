# tick 2099 — rq_2099 SLG Operaties Vlaanderen YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFTS = ROOT / "foi" / "drafts"

csv.field_size_limit(10**7)
UTC = "2026-08-25T05:40:00Z"
TICK = 2099
ENTITY = "nv_slg_operaties_vlaanderen"
GAP = "gap_slg_operaties_nbb_pdf_assets_debt_omzet_fte_jump_matrix_l5"
LB = "lb_slg_operaties_omzet_jump_58_28m_fte_jump_jr2025"
COMM = "comm_slg_operaties_jr2025_statutory_wzc"

OMZET = 58284887
PNL = 347702
EQUITY = 19875741
BRUTO = 36784094
FTE = 1095.3
OMZET24 = 11121236
PNL24 = 262190
EQUITY24 = 6603371
BRUTO24 = 6807365
FTE24 = 101.7
OMZET_YOY = "JUMP +424.09%"
PNL_YOY = "JUMP +32.61%"
EQUITY_YOY = "JUMP +200.99%"
BRUTO_YOY = "JUMP +440.36%"
FTE_YOY = "JUMP +976.01%"
FILED = "28.07.2026"
KBO = "0845.064.196"
KBO_DIGITS = "0845064196"
EMAIL = "info@korian.be"
ADDR = "Satenrozen 1B, 2550 Kontich"
SITE = "https://www.korian.be/"
CW_NL = f"https://www.companyweb.be/nl/{KBO_DIGITS}/slg-operaties-vlaanderen"
CW_EN = f"https://www.companyweb.be/en/{KBO_DIGITS}/slg-operaties-vlaanderen"
CW_FR = f"https://www.companyweb.be/fr/{KBO_DIGITS}/slg-operaties-vlaanderen"
KBO_URL = (
    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
    f"ondernemingsnummer={KBO_DIGITS}"
)
NBB = f"https://consult.cbso.nbb.be/consult-enterprise/{KBO_DIGITS}"
PI = "6.0"
ABSURD = "6.5"
COST = "6.2"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo SLG Operaties Vlaanderen, AREWAL, Familiezorg Gent, emeis Belgium, "
    "Begralim / Grauwzusters Limburg, Sint-Lucia Turnhout, Lidwina Mol, "
    "Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, "
    "Familiezorg West-Vlaanderen, De Lovie Poperinge, Ocura Beringen, "
    "WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, "
    "Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, "
    "WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, "
    "Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, "
    "Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, "
    "Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, "
    "Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Armonea, Always Home, "
    "Colisée Belgium, Psychogeriatrisch Centrum, AIEG, RESA, Enodia, Fluxys*, ETB, "
    "Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, "
    "Hydria, CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, "
    "SCK CEN, EURIDICE, IRE*, BRUGEL."
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
        if r["task_id"] == "rq_2099":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2099 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — SLG Operaties Vlaanderen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover SLG Operaties Vlaanderen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} "
                f"equity JUMP {EQUITY} FTE JUMP {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.301+87.101 NV 9 VE; "
                "Korian Belgium bestuurder; DISTINCT Armonea/Always Home/emeis"
            )
            r["notes"] = (
                f"tick{TICK} SLG Operaties Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m "
                f"equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2100 EVERY-10; "
                "next every-10 2100"
            )
            found = True
    if not found:
        raise SystemExit("rq_2099 missing")
    if not any(r["task_id"] == "rq_2100" for r in rows):
        rows.append(
            {
                "task_id": "rq_2100",
                "title": (
                    "EVERY-10 + leftover dual after SLG — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC-zorg"
                ),
                "sprint": "hole_fill",
                "priority": "9",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2100 EVERY-10 mandatory: refresh progress_every_10_ticks.md + "
                    "doge_waste_top10_current.md THEN hole-fill one unit. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                    "AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/"
                    "WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2099 SLG Operaties; EVERY-10 mandatory at 2100; "
                    "prefer FARO/AIESH/REW if YE2025 else unused WZC-zorg"
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
                "last_unit_id": "rq_2099",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover SLG Operaties Vlaanderen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE JUMP {FTE}; assets/debt Unknown; NACE 87.301+87.101 9 VE "
                    "Korian); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2100 EVERY-10; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def write_foi_draft():
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / f"{GAP}.md"
    path.write_text(
        f"""# FOI draft — SLG Operaties Vlaanderen (NBB PDF / assets-debt / omzet-FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** SLG Operaties Vlaanderen NV — KBO **{KBO}**  
**recipient:** {EMAIL} (Korian Belgium HQ, same zetel) · {ADDR} · +32 (0)3 443 76 50  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [NBB consult]({NBB}) · [Korian contact]({SITE}contact/)  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; KBO Strong identity)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** {OMZET_YOY}; bruto **EUR{BRUTO}** {BRUTO_YOY}; pnl **EUR{PNL}** {PNL_YOY}; equity **EUR{EQUITY}** {EQUITY_YOY}; FTE **{FTE}** {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief NV; **9 VE**; NACE **87.301** ROB + **87.101** RVT; zetel {ADDR} sinds 30.06.2025; bestuurder **Korian Belgium** 0869.769.702.
- Preferred stall still blocked: AGB Bornem JR2024-only; FARO NBB YE2024; AIESH YE2024; REW YE2024 (0644.638.937).
- DISTINCT from Armonea / Always Home / emeis / Colisée already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: SLG Operaties Vlaanderen NV / Korian Belgium
{ADDR}
via {EMAIL}
Betreft: Openbaarmaking NBB-jaarrekening 2025 SLG Operaties Vlaanderen + balans/resultaatmatrix (KBO {KBO})
Geachte, op grond van toepasselijke openbaarheidsregels (waar van toepassing Bestuursdecreet / wet openbaarheid; desgevallend als houder van publiek gesubsidieerde ROB/RVT-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}) + depositreferentie.
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Toelichting omzet JUMP EUR{OMZET} (+424.09% vs YE2024 EUR{OMZET24}) en FTE JUMP {FTE} (vs {FTE24}): consolidatie / overdracht / overnames matrix 2025.
4. Split omzet/bruto naar ROB vs RVT vs andere; Zorgkas/IFIC/publieke dagprijs vs private path.
5. Relatie tot Korian Belgium 0869.769.702 / Senior Living Group Vlaanderen / eventuele Always Home of andere groepsentiteiten (aandeelhouderschap, management fees, intra-groep schulden).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - rq_2099 SLG Operaties Vlaanderen (omzet JUMP 58.28m / FTE JUMP 1095.3 / Medium)

- Unit: **rq_2099** leftover dual after **rq_2098 AREWAL**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024** (KBO 0644.638.937). Took preferred deferred leftover **SLG Operaties Vlaanderen** YE2025 (KBO **{KBO}**; {ADDR}; Antwerpen **NV** ROB/RVT NACE **87.301+87.101** / **9 VE**; bestuurder Korian Belgium). Do not redo AREWAL/Familiezorg Gent/emeis/Begralim/Sint-Lucia/Lidwina/SED/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Armonea/Always Home/Colisée/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +424.09%; bruto **EUR{BRUTO}** JUMP +440.36%; pnl **PROFIT EUR{PNL}** JUMP +32.61% vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP +200.99%; FTE **{FTE}** JUMP vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 9 VE; email {EMAIL} (Korian HQ same zetel). Omzet used as primary envelope (NV ROB/RVT).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2099=done + rq_2100 open (EVERY-10); loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2099/ (+ tick2098 probes).
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100** — MUST refresh progress + waste top10 then hole-fill). Next: rq_2100.
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_slg_operaties_jr2025_cw",
                "title": "Companyweb NL — SLG Operaties Vlaanderen YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} FTE {FTE}",
            },
            {
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "title": "Companyweb EN — SLG Operaties Vlaanderen YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; equity {EQUITY}; FTE {FTE}",
            },
            {
                "source_id": "src_slg_operaties_jr2025_cw_fr",
                "title": "Companyweb FR — SLG Operaties Vlaanderen YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_slg_operaties_kbo_{TICK}",
                "title": f"KBO — SLG Operaties Vlaanderen {KBO}",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 9 VE; NACE 87.301+87.101; zetel {ADDR}; "
                    f"bestuurder Korian Belgium 0869.769.702; Strong identity"
                ),
            },
            {
                "source_id": f"src_slg_operaties_korian_contact_{TICK}",
                "title": "Korian Belgium contact (HQ same zetel as SLG Operaties)",
                "url": f"{SITE}contact/",
                "publisher": "Korian Belgium",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; info@korian.be; +32 (0)3 443 76 50; {ADDR}"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_slg_operaties_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope NV ROB/RVT)",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {OMZET_YOY} vs YE2024 {OMZET24}; FTE JUMP accompanies scale-up",
            },
            {
                "budget_id": "bud_slg_operaties_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_slg_operaties_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_slg_operaties_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_slg_operaties_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} {FTE_YOY} vs YE2024 {FTE24}; consolidation signal",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "SLG Operaties Vlaanderen YE2025 leftover dual "
                    "(omzet JUMP 58.28m / FTE JUMP 1095.3)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "WZC/ROB/RVT residents via SLG Operaties / Korian Belgium path"
                ),
                "legal_basis": (
                    f"NV private care / publiek gesubsidieerde ROB-RVT "
                    f"(KBO {KBO}; NACE 87.301+87.101; 9 VE)"
                ),
                "decision_date": "2026-07-28",
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
                    "Private residential elderly care operations (SLG / Korian Belgium)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain omzet/FTE JUMP consolidation "
                    "matrix vs Korian Belgium / SLG Vlaanderen"
                ),
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>SLG_Operaties>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "DISTINCT Armonea/Always Home/emeis/Colisée; Korian bestuurder"
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
                    "SLG Operaties omzet JUMP 58.28m / FTE JUMP 1095.3 (YE2025)"
                ),
                "level": "L5",
                "type": "wzc_nv_statutory_private_care",
                "hierarchy_path": (
                    "Vlaanderen>Antwerpen>Kontich>SLG_Operaties>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} {OMZET_YOY} (primary); bruto {BRUTO} "
                    f"{BRUTO_YOY}; pnl PROFIT {PNL} {PNL_YOY}; equity {EQUITY} "
                    f"{EQUITY_YOY}; FTE {FTE} {FTE_YOY}; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_slg_operaties_jr2025_cw_en",
                "beneficiaries": "WZC/ROB/RVT residents (9 VE); public Zorgkas day-price path",
                "stated_goal": "Private residential elderly care ops (Korian/SLG)",
                "measured_outcome": (
                    f"omzet {OMZET_YOY}; bruto {BRUTO_YOY}; pnl {PNL_YOY}; "
                    f"equity {EQUITY_YOY}; FTE {FTE_YOY} — consolidation-scale jump"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "FOI NBB PDF + consolidation/overname matrix + Zorgkas split; "
                    "map Korian Belgium / SLG Vlaanderen related-party flows"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
                    "DISTINCT Armonea/Always Home/emeis"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "SLG Operaties Vlaanderen NV (Kontich / Korian)",
                "name_fr": "SLG Operaties Vlaanderen SA (Kontich / Korian)",
                "name_en": "SLG Operaties Vlaanderen NV (Kontich / Korian)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV "
                    f"9 VE; NACE 87.301 ROB + 87.101 RVT; omzet JUMP {OMZET/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP "
                    f"{EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; neerlegging "
                    f"{FILED}; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    f"{ADDR}; bestuurder Korian Belgium 0869.769.702; {EMAIL}; "
                    "DISTINCT Armonea/Always Home/emeis/Colisée"
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
                    "Vlaanderen>Antwerpen>Kontich>SLG_Operaties>NBB_PDF_assets_debt_omzet_fte_jump"
                ),
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); "
                    "omzet/FTE JUMP consolidation/overname matrix; ROB vs RVT vs other split; "
                    "Zorgkas/IFIC vs private; Korian Belgium / SLG Vlaanderen related-party map"
                ),
                "why_it_matters": (
                    "Medium CW shows 58.28m omzet Korian-path NV with FTE JUMP 101.7→1095.3 "
                    "and omzet JUMP +424% — public-care day-price continuity risk without "
                    "balance-sheet transparency"
                ),
                "priority": "8",
                "recipient_body": "SLG Operaties Vlaanderen NV / Korian Belgium",
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
                    f"tick{TICK}; human-send only; Medium CW; next every-10 2100"
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
