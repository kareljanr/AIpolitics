# tick 2085 — rq_2085 WZC Sint-Augustinus Halle YE2025 Medium CW
# (research raw lived under tick2084/ while concurrent agent closed rq_2084 Ben)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW = DATA / "raw" / "tick2085"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T02:20:00Z"
TICK = 2085
ENTITY = "vzw_wzc_sint_augustinus_halle"
GAP = "gap_augustinus_halle_nbb_pdf_assets_debt_omzet_drop_equity_jump_fte_drop_matrix_l5"
LB = "lb_augustinus_halle_omzet_drop_8_95m_equity_jump_fte_drop_jr2025"
COMM = "comm_augustinus_halle_jr2025_statutory_wzc"

OMZET = 8948237
PNL = 740431
EQUITY = 3349221
BRUTO = 8376737
FTE = 88.9
OMZET24 = 9046991
PNL24 = 720572
EQUITY24 = 2819641
BRUTO24 = 8195693
FTE24 = 92.7
OMZET_YOY = "-1.09%"
PNL_YOY = "+2.76%"
EQUITY_YOY = "+18.78%"
BRUTO_YOY = "+2.21%"
FTE_YOY = "-4.10%"
FILED = "02.07.2026"
KBO = "0459.770.496"
EMAIL = "info@wzcsintaugustinus.be"
ADDR = "Monseigneur Senciestraat 4, 1500 Halle"
SITE = "https://www.wzcsintaugustinus.be/"
CW_NL = "https://www.companyweb.be/nl/0459770496/woonzorgcentrum-sint-augustinus"
CW_EN = "https://www.companyweb.be/en/0459770496/woonzorgcentrum-sint-augustinus"
CW_FR = "https://www.companyweb.be/fr/0459770496/woonzorgcentrum-sint-augustinus"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0459770496"
PI = "5.0"
ABSURD = "4.5"
COST = "5.5"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, "
    "WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, "
    "Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
    "WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar (absorbed other Sint-Augustinus 0410.469.059), Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, "
    "OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, "
    "Always Home, Armonea, WZC Sint-Barbara Herselt, Molenheide, De Vaeren (CW YE2016-only), "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, "
    "Elia, BNO, SWDE, BRUGEL. Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)


def copy_raw():
    src_dir = DATA / "raw" / "tick2084"
    for name in [
        "aug_nl.html",
        "aug_en.html",
        "aug_fr.html",
        "kbo_aug.html",
        "site.html",
        "faro_probe.html",
        "aiesh_probe.html",
        "rew_probe.html",
        "bornem_probe.html",
        "cand_0459770496_nl.html",
    ]:
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, RAW / name)


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
    for r in rows:
        if r["task_id"] == "rq_2085":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2085 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — WZC Sint-Augustinus Halle YE2025 Medium"
            r["instructions"] = (
                "Completed leftover WZC Sint-Augustinus Halle YE2025 Medium CW; "
                f"KBO {KBO}; omzet DROP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Augustinus Halle Medium omzet DROP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2086; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2086" for r in rows):
        rows.append(
            {
                "task_id": "rq_2086",
                "title": "leftover dual hole-fill after Augustinus Halle — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2085 after WZC Sint-Augustinus Halle YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2085 Augustinus Halle; next every-10 2090",
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
                "last_unit_id": "rq_2085",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover WZC Sint-Augustinus Halle {KBO} Medium CW "
                    f"(omzet DROP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2086; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def main():
    copy_raw()
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_augustinus_halle_jr2025_cw",
                "title": "Companyweb NL — WZC Sint-Augustinus Halle YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "title": "Companyweb EN — WZC Sint-Augustinus Halle YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE {FTE}",
            },
            {
                "source_id": "src_augustinus_halle_jr2025_cw_fr",
                "title": "Companyweb FR — WZC Sint-Augustinus Halle YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_augustinus_halle_kbo_{TICK}",
                "title": "KBO — Woonzorgcentrum- Sint-Augustinus 0459.770.496",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 1 VE; NACE 87.301 ROB; zetel Monseigneur Senciestraat 4 Halle; "
                    f"KBO email empty; site email {EMAIL}; DISTINCT from Zusters Berlaar absorbed 0410.469.059"
                ),
            },
            {
                "source_id": f"src_augustinus_halle_site_{TICK}",
                "title": "WZC Sint-Augustinus Halle website",
                "url": SITE,
                "publisher": "WZC Sint-Augustinus",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; Solidum Groep lid; ~115 wooneenheden + AV + dagverzorging; {EMAIL}",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_augustinus_halle_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP {OMZET_YOY} vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_augustinus_halle_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {PNL_YOY} vs YE2024 PROFIT {PNL24}",
            },
            {
                "budget_id": "bud_augustinus_halle_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_augustinus_halle_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}",
            },
            {
                "budget_id": "bud_augustinus_halle_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE DROP {FTE} ({FTE_YOY}) vs YE2024 {FTE24}",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "WZC Sint-Augustinus Halle YE2025 leftover dual (omzet DROP 8.95m / equity JUMP 3.35m)",
                "entity_id": ENTITY,
                "beneficiary": "Halle / Vlaams-Brabant elderly residents (WZC + AV + dagverzorging / Solidum)",
                "legal_basis": f"VZW WZC / publiek gesubsidieerde zorg (KBO {KBO}); Woonzorgdecreet",
                "decision_date": "2026-07-02",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                    f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": "Residential elderly care Halle (WZC / kortverblijf / dagverzorging / AV)",
                "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain equity JUMP +18.78pct with omzet DROP and FTE DROP",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Halle>WZC_SintAugustinus>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; DISTINCT Berlaar absorbed Sint-Augustinus; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "WZC Sint-Augustinus Halle omzet DROP 8.95m / equity JUMP + FTE DROP (YE2025)",
                "level": "L5",
                "type": "wzc_vzw_statutory",
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Halle>WZC_SintAugustinus>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": "CW omzet proxy; assets/debt Unknown pending NBB PDF FOI; equity JUMP with omzet/FTE DROP",
                "confidence": "medium",
                "source_id": "src_augustinus_halle_jr2025_cw_en",
                "beneficiaries": "WZC/AV/dagverzorging clients Halle (Solidum Groep)",
                "stated_goal": "Residential elderly care Halle centre (basiliek site)",
                "measured_outcome": (
                    f"omzet DROP {OMZET_YOY}; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY}; FTE DROP {FTE} ({FTE_YOY})"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt FOI; explain equity JUMP from EUR2819641 to EUR3349221 (+18.78pct) "
                    "with omzet DROP -1.09pct and FTE DROP 92.7→88.9; map IFIC/Alivia vs dagprijs"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                    "Vlaams-Brabant WZC VZW 1 VE; Solidum; NOT Berlaar absorbed entity"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Woonzorgcentrum- Sint-Augustinus vzw (Halle)",
                "name_fr": "Maison de repos Sint-Augustinus ASBL (Hal)",
                "name_en": "Nursing home Sint-Augustinus VZW (Halle)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 1 VE; "
                    f"omzet DROP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging {FILED}; "
                    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "Solidum Groep; NACE 87.301; DISTINCT from Zusters Berlaar absorbed Sint-Augustinus 0410.469.059"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>VlaamsBrabant>Halle>SintAugustinus>NBB_PDF_assets_debt_omzet_drop_equity_jump_fte_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; "
                    f"explanation of equity JUMP from EUR{EQUITY24} to EUR{EQUITY} (+18.78%) with omzet DROP "
                    f"{OMZET_YOY} and FTE DROP {FTE24}→{FTE} ({FTE_YOY})"
                ),
                "why_it_matters": (
                    "Medium CW shows 8.95m omzet Halle WZC VZW with equity JUMP +18.8pct while omzet and FTE DROP "
                    "without balanstotaal/assets/debt; material L5 residual for FOI; Solidum dual"
                ),
                "priority": "8",
                "recipient_body": "Woonzorgcentrum- Sint-Augustinus vzw",
                "recipient_email": EMAIL,
                "recipient_postal": ADDR,
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
                "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2090",
            }
        ],
    )

    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — WZC Sint-Augustinus Halle (NBB PDF / assets-debt / omzet-drop / equity-jump / FTE-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum- Sint-Augustinus VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** JUMP {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Monseigneur Senciestraat 4 Halle; NACE 87.301 ROB; KBO email empty; site email {EMAIL}.
- Site: Solidum Groep lid; WZC + kortverblijf + dagverzorging Het Binnenhof + assistentiewoningen.
- DISTINCT from Zorggroep Zusters van Berlaar absorbed WZC Sint-Augustinus KBO 0410.469.059.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Concurrent rq_2084 took Ben — this fire continues with unused Augustinus Halle.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum- Sint-Augustinus vzw — Monseigneur Senciestraat 4, 1500 Halle
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Sint-Augustinus Halle + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de equity-stijging van EUR{EQUITY24} (YE2024) naar EUR{EQUITY} (YE2025; +18.78%) bij omzetdaling {OMZET_YOY} en FTE-daling van {FTE24} naar {FTE} ({FTE_YOY}).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )

    update_research_queue()
    write_loop_state()
    shutil.copy2(Path(__file__), RAW / "apply_tick2085.py")

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2085 WZC Sint-Augustinus Halle (omzet DROP 8.95m / equity JUMP 3.35m / Medium)

- Unit: **rq_2085** leftover dual after **rq_2084 Ben** (concurrent race closed Ben on 2084; this fire continues). Prefer NON-stall live: AGB Bornem still **JR2024-only** (bornem.be JR2024 docs); FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **WZC Sint-Augustinus Halle** YE2025 (KBO **{KBO}**; Monseigneur Senciestraat 4 Halle; Vlaams-Brabant **VZW** WZC / **1 VE**; Solidum Groep; **DISTINCT from Zusters Berlaar absorbed Sint-Augustinus 0410.469.059**). Do not redo Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Zusters Berlaar.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** JUMP {PNL_YOY} vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** DROP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2085=done + rq_2086 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2085/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2086 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "equity", EQUITY, "fte", FTE)


if __name__ == "__main__":
    main()
