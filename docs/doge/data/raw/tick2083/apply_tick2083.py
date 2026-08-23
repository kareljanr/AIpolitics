# tick 2083 — rq_2083 Home Stuyvenberg Herzele YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T01:50:00Z"
TICK = 2083
ENTITY = "nv_home_stuyvenberg_herzele"
GAP = "gap_stuyvenberg_nbb_pdf_assets_debt_omzet_empty_fte_bruto_collapse_matrix_l5"
LB = "lb_stuyvenberg_bruto_0_50m_pnl_jump_equity_jump_omzet_empty_jr2025"
COMM = "comm_stuyvenberg_jr2025_statutory_wzc"

# Omzet empty all years on CW abbreviated schema — use bruto as cost proxy
OMZET = None
PNL = 390004
EQUITY = 3091145
BRUTO = 500069
FTE = None  # CW reports "0 FTE" — treat as Unknown
PNL24 = 340073
EQUITY24 = 2701141
BRUTO24 = 478591
BRUTO22 = 2401813
PNL_YOY = "JUMP +14.68%"
EQUITY_YOY = "JUMP +14.44%"
BRUTO_YOY = "JUMP +4.49%"
BRUTO_VS22 = "DROP -79.18% vs YE2022"
FILED = "23.07.2026"
KBO = "0424.830.108"
EMAIL = "info.stuyvenberg@cura-care.be"
ADDR = "Provincieweg 549, 9550 Herzele"
SITE = "https://stuyvenberg.be/"
CW_NL = "https://www.companyweb.be/nl/0424830108/home-stuyvenberg"
CW_EN = "https://www.companyweb.be/en/0424830108/home-stuyvenberg"
CW_FR = "https://www.companyweb.be/fr/0424830108/home-stuyvenberg"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424830108"
PI = "4.4"
ABSURD = "5.2"
COST = "3.8"
DIFF = "4.0"

DO_NOT_REDO = (
    "Do NOT redo Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, "
    "WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
    "WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren Rumst (Stopgezet), IPFBW, IGRETEC, Aquiris, SPGE, IRE*, "
    "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
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
    for r in rows:
        if r["task_id"] == "rq_2083":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2083 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Home Stuyvenberg Herzele YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Home Stuyvenberg Herzele YE2025 Medium CW; "
                f"KBO {KBO}; omzet empty pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE Unknown (CW 0); FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Vaeren Rumst Stopgezet skipped"
            )
            r["notes"] = (
                f"tick{TICK} Stuyvenberg Medium bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m omzet empty FTE Unknown; "
                f"bruto vs YE2022 {BRUTO_VS22}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2084; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2084" for r in rows):
        rows.append(
            {
                "task_id": "rq_2084",
                "title": "leftover dual hole-fill after Stuyvenberg — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2083 after Home Stuyvenberg Herzele YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2083 Stuyvenberg; next every-10 2090",
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
                "last_unit_id": "rq_2083",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Home Stuyvenberg Herzele {KBO} Medium CW "
                    f"(omzet empty pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE Unknown; bruto vs YE2022 {BRUTO_VS22}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Vaeren Stopgezet skipped; "
                    "next rq_2084; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - rq_2083 Home Stuyvenberg (bruto JUMP 0.50m / pnl JUMP 0.39m / omzet empty / Medium)

- Unit: **rq_2083** leftover dual after **rq_2082 Wijshage** (already on main; this fire found rq_2083 in_progress after Vaeren Stopgezet dead-end). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. De Vaeren Rumst 0444.313.151 probed — **Stopgezet / BJ2016** — skipped. Took unused leftover **Home Stuyvenberg** YE2025 (KBO **{KBO}**; Provincieweg 549 Herzele; Oost-Vlaanderen **NV** RVT/WZC / **1 VE**; ~52 beds; **CuraCare**; DISTINCT De Zwaluw). Do not redo Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/.../AGB Bornem/Armonea/Always Home.
- Found: Companyweb NL+EN+FR YE2025 — omzet **empty** (abbreviated schema all years); pnl **EUR{PNL}** JUMP +14.68% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +14.44%; bruto **EUR{BRUTO}** JUMP +4.49% vs YE2024 EUR{BRUTO24} but **DROP -79.18% vs YE2022 EUR{BRUTO22}**; FTE **Unknown** (CW reports 0); neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+4 pnl/equity/bruto + note omzet/FTE Unknown); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2083=done + rq_2084 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2083/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2084 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_stuyvenberg_jr2025_cw",
                "title": "Companyweb NL — Home Stuyvenberg Herzele YE2025",
                "url": CW_NL,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet empty pnl {PNL} bruto {BRUTO}",
            },
            {
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "title": "Companyweb EN — Home Stuyvenberg Herzele YE2025",
                "url": CW_EN,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed {FILED}; FTE Unknown (CW 0); Last balance sheet year 2025",
            },
            {
                "source_id": "src_stuyvenberg_jr2025_cw_fr",
                "title": "Companyweb FR — Home Stuyvenberg Herzele YE2025",
                "url": CW_FR,
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check",
            },
            {
                "source_id": f"src_stuyvenberg_kbo_{TICK}",
                "title": f"KBO — Home Stuyvenberg {KBO}",
                "url": KBO_URL,
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": f"tick{TICK}; Actief NV 1 VE sinds 18.01.1992; zetel Provincieweg 549 Herzele; RVT activity on CW",
            },
            {
                "source_id": f"src_stuyvenberg_site_{TICK}",
                "title": "WZC Stuyvenberg website (CuraCare)",
                "url": SITE,
                "publisher": "Home Stuyvenberg / CuraCare",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; Provincieweg 549 Herzele; {EMAIL}; ~52 beds; CuraCare (distinct De Zwaluw)",
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_stuyvenberg_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP vs YE2024 {PNL24} ({PNL_YOY})",
            },
            {
                "budget_id": "bud_stuyvenberg_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {EQUITY_YOY} vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_stuyvenberg_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin (omzet empty — bruto cost proxy)",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP {BRUTO_YOY} vs YE2024 {BRUTO24}; {BRUTO_VS22} ({BRUTO22})",
            },
            {
                "budget_id": "bud_stuyvenberg_omzet_jr2025_statutory_unknown",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": "",
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "CW YE2025 omzet / Turnover — EMPTY abbreviated schema",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; omzet empty all CW years; FOI NBB PDF for statutory turnover",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Home Stuyvenberg Herzele YE2025 leftover dual (bruto JUMP 0.50m / pnl JUMP / omzet empty)",
                "entity_id": ENTITY,
                "beneficiary": "Herzele elderly residents (~52 beds; CuraCare Home Stuyvenberg; DISTINCT De Zwaluw)",
                "legal_basis": f"NV RVT/WZC / publiek erkende zorg (Departement Zorg) (KBO {KBO})",
                "decision_date": "2026-07-23",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    f'{{"2025_omzet":null,"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                    f'"2025_bruto":{BRUTO},"2025_fte":null}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": CW_EN,
                "stated_goal": "WZC/RVT residential elderly care Herzele (Provincieweg 549)",
                "cut_option": "Publish NBB PDF assets/debt + omzet + FTE FOI; explain bruto collapse -79pct vs YE2022 while pnl/equity JUMP",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Herzele>Home_Stuyvenberg>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; assets/debt/omzet/FTE Unknown; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; CuraCare NV; not TE-additive of 348bn; DISTINCT De Zwaluw"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Home Stuyvenberg Herzele bruto JUMP 0.50m / pnl JUMP / omzet empty (YE2025)",
                "level": "L5",
                "type": "wzc_nv_statutory",
                "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Herzele>Home_Stuyvenberg>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": "CW bruto proxy (omzet empty abbreviated); assets/debt/FTE Unknown pending NBB PDF FOI; bruto -79pct vs YE2022",
                "confidence": "medium",
                "source_id": "src_stuyvenberg_jr2025_cw_en",
                "beneficiaries": "WZC/RVT clients Herzele (~52 beds; CuraCare)",
                "stated_goal": "Residential elderly care Herzele",
                "measured_outcome": (
                    f"omzet empty; pnl JUMP {PNL_YOY}; equity JUMP {EQUITY_YOY}; "
                    f"bruto JUMP {BRUTO_YOY} but {BRUTO_VS22}; FTE Unknown (CW 0)"
                ),
                "absurdity_score": ABSURD,
                "cost_score": COST,
                "difficulty": DIFF,
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/omzet/FTE FOI; explain bruto collapse "
                    f"YE2022 {BRUTO22}→YE2025 {BRUTO} (-79pct) while pnl JUMP {PNL24}→{PNL} and equity JUMP; map IFIC/Alivia vs dagprijs"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Oost-Vlaanderen CuraCare NV; DISTINCT De Zwaluw",
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Home Stuyvenberg NV (Herzele)",
                "name_fr": "Home Stuyvenberg SA (Herzele)",
                "name_en": "Home Stuyvenberg NV (Herzele)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SITE,
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV 1 VE; "
                    f"omzet empty pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE Unknown; bruto vs YE2022 {BRUTO_VS22}; "
                    f"assets/debt Unknown; neerlegging {FILED}; FOI {GAP}; preferred AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; CuraCare; ~52 beds; DISTINCT De Zwaluw Pajottegem"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Herzele>Home_Stuyvenberg>NBB_PDF_assets_debt_omzet_empty_fte_bruto_collapse",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/omzet/FTE); public subsidy vs dagprijs split; "
                    f"explanation of bruto collapse YE2022 EUR{BRUTO22} → YE2025 EUR{BRUTO} (-79.18%) while pnl JUMP "
                    f"EUR{PNL24}→EUR{PNL} (+14.68%) and equity JUMP EUR{EQUITY24}→EUR{EQUITY} (+14.44%); why CW omzet empty + FTE 0"
                ),
                "why_it_matters": (
                    "Medium CW shows 0.50m bruto CuraCare NV RVT/WZC (~52 beds) with empty omzet, FTE Unknown, "
                    "and multi-year bruto collapse without balanstotaal/assets/debt; material L5 residual for FOI"
                ),
                "priority": "8",
                "recipient_body": "Home Stuyvenberg NV / CuraCare",
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

    update_research_queue()
    write_loop_state()
    append_log()
    print(f"OK tick{TICK} {ENTITY} bruto={BRUTO} pnl={PNL} gap={GAP}")


if __name__ == "__main__":
    main()
