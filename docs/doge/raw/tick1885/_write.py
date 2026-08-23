# tick 1885 — LRM NV leftover after Thor Park (official VL Parlement JR2025 Strong)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]  # .../AIpolitics
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

TICK = 1885
UTC = "2026-08-26T13:45:00Z"
ENTITY = "nv_lrm"
GAP = "gap_lrm_nbb_pdf_fva_516m_portfolio_l5"

# Official VO form amounts are in thousands EUR — convert to euros
# Source: docs.vlaamsparlement.be/files/pfile?id=2321629 (AV 18.05.2026)
ASSETS = 543_203_000
FVA = 516_066_000
EQUITY = 521_192_000
CAPITAL = 343_047_000
DEBT = 21_745_000
CASH = 10_400_000
OMZET = 2_189_000
BEDRIJFSOPBR = 2_707_000
BEDRIJFSKOST = 11_687_000
STAFF = 6_978_000
EXPL = -8_980_000  # 9901
FIN_OPBR = 33_793_000
PNL = 17_829_000  # 9905 te bestemmen resultaat boekjaar
DIVIDEND = 6_000_000
VTE_CW = 46.7  # Companyweb NBB-derived (VO form VTE page sparse)


def append_rows(path, rows, fieldnames=None):
    path = Path(path)
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = fieldnames or r.fieldnames
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
        for row in rows:
            w.writerow({k: row.get(k, "") for k in cols})


def update_research_queue():
    path = DATA / "research_queue.csv"
    rows = []
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        for row in r:
            if row["task_id"] == "rq_1885":
                row["status"] = "done"
                row["entity_id"] = ENTITY
                row["title"] = (
                    "Leftover dual residual hole-fill after Thor Park "
                    "(AGB/Dijk92-if-200 / FARO-if-YE2025 / Westhoek-if-PDF / other HVZ-IGS)"
                )
                row["instructions"] = (
                    "Completed: LRM NV leftover VL EVA-PR parent after Thor Park campus stack; "
                    "preferred AGB Bornem JR2024 / Dijk92 CDN FOI / FARO NBB YE2025 unpublished / "
                    "OP-TIL+VI.BE taken — took LRM parent official VL Parlement JR2025 Strong."
                )
                row["updated_utc"] = UTC
                row["notes"] = (
                    f"tick{TICK} DONE LRM NV KBO 0452.138.972 Strong VL Parlement JR2025; "
                    f"assets 543.2m FVA 516.1m equity 521.2m omzet 2.19m staff 6.98m "
                    f"expl NEG 8.98m pnl 17.83m dividend 6m; NBB PDF+FVA portfolio FOI; "
                    f"next rq_1886; next every-10 1890"
                )
            rows.append(row)
    # spawn next
    rows.append(
        {
            "task_id": "rq_1886",
            "title": (
                "Leftover dual residual hole-fill after LRM NV "
                "(AGB/Dijk92-if-200 / FARO-if-YE2025 / Westhoek-if-PDF / other HVZ-IGS/IOED/Mijnen)"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Vlaanderen>leftover_dual",
            "entity_id": "",
            "instructions": (
                f"Tick 1886 after {TICK} LRM NV. Prefer leftover AGB/APB if PDF live, "
                "else Dijk92/Enebra if CDN 200, else FARO if TRUE NBB YE2025, "
                "else other HVZ/IGS/IOED/Mijnen / Campus EnergyVille if YE2025 live. "
                "LRM parent + ThorPark+Corda20+CordaCampus+BioVille+Agropolis+Droneport+"
                "CMineCrib+IncubaThor+Greenville+BCMEC+HangarK+BCTIEN+Werkpand+iCUBES taken. "
                "Skip done/privatized. Prefer NON-Eneco. Next every-10 1890."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"spawned after tick{TICK}; next every-10 1890",
        }
    )
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    # sources
    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_lrm_jr2025_vp",
                "title": "LRM NV Jaarrekening 2025 (Vlaams Parlement / DFB VO form)",
                "url": "https://docs.vlaamsparlement.be/files/pfile?id=2321629",
                "publisher": "Vlaams Parlement / Departement F&B",
                "accessed_date": "2026-08-26",
                "source_class": "primary_official",
                "notes": (
                    f"tick{TICK}; AV 18.05.2026; amounts in thousands EUR; "
                    "EVA PR Limburg investment company; Strong"
                ),
            },
            {
                "source_id": "src_lrm_repertorium_vl",
                "title": "DFB Repertorium Rechtspersonen — LRM NV page",
                "url": (
                    "https://www.vlaanderen.be/departement-financien-en-begroting/"
                    "uitvoering/rechtspersonen/repertorium-rechtspersonen/"
                    "limburgse-reconversiemaatschappij-lrm-nv"
                ),
                "publisher": "Vlaanderen DFB",
                "accessed_date": "2026-08-26",
                "source_class": "primary_official",
                "notes": f"tick{TICK}; links JR2025 VP PDF; EVA PR minister Diependaele",
            },
            {
                "source_id": "src_lrm_jr2025_cw",
                "title": "Companyweb LRM NV YE2025 NBB-derived summary",
                "url": "https://www.companyweb.be/nl/0452138972/limburgse-reconversie-maatschappij",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": "2026-08-26",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; neerlegging 12.06.2026; omzet 2189489.25 VTE 46.7; "
                    "cross-check vs VP thousands"
                ),
            },
            {
                "source_id": "src_lrm_kbo",
                "title": "KBO Public Search LRM NV 0452.138.972",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/"
                    "toonondernemingps.html?ondernemingsnummer=452138972"
                ),
                "publisher": "KBO",
                "accessed_date": "2026-08-26",
                "source_class": "primary_official",
                "notes": f"tick{TICK}; Limburgse Reconversie Maatschappij NV Hasselt",
            },
            {
                "source_id": "src_lrm_site",
                "title": "LRM official site",
                "url": "https://lrm.be/",
                "publisher": "official_web",
                "accessed_date": "2026-08-26",
                "source_class": "official_web",
                "notes": f"tick{TICK}; VL public investment company Limburg campuses Corda/Thor/Droneport",
            },
        ],
    )

    # entity
    append_rows(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": (
                    "Limburgse Reconversie Maatschappij NV (LRM; leftover VL EVA-PR "
                    "investeringsmaatschappij parent Corda/Thor/Droneport)"
                ),
                "name_fr": "Société de reconversion du Limbourg SA (LRM; EVA PR residuel)",
                "name_en": "LRM NV leftover Flemish EVA-PR Limburg investment company parent",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": "https://lrm.be/",
                "foi_email": "info@lrm.be",
                "foi_postal": "Kempische steenweg 311 bus 4.01 3500 Hasselt",
                "notes": (
                    f"tick{TICK} leftover after Thor Park campus stack; KBO 0452.138.972; "
                    "EVA PR Decreet 07.05.2004; Strong VL Parlement JR2025; FOI NBB PDF+FVA portfolio"
                ),
            }
        ],
    )

    # budgets (Strong from VP thousands×1000)
    bud_rows = [
        ("bud_lrm_assets_jr2025", ASSETS, "VO 3.1 code 20/58 totaal activa 543203 kEUR"),
        ("bud_lrm_fva_jr2025", FVA, "VO 3.1 code 28 FVA 516066 kEUR (deelnemingen+vorderingen)"),
        ("bud_lrm_equity_jr2025", EQUITY, "VO 3.2 code 10/15 eigen vermogen 521192 kEUR"),
        ("bud_lrm_capital_jr2025", CAPITAL, "VO 3.2 code 10 geplaatst kapitaal 343047 kEUR"),
        ("bud_lrm_debt_jr2025", DEBT, "VO 3.2 code 17/49 schulden 21745 kEUR (mostly ST)"),
        ("bud_lrm_cash_jr2025", CASH, "VO 3.1 code 54/58 liquide middelen 10400 kEUR"),
        ("bud_lrm_omzet_jr2025", OMZET, "VO 4 code 70 omzet 2189 kEUR"),
        ("bud_lrm_bedrijfsopbr_jr2025", BEDRIJFSOPBR, "VO 4 code 70/76A bedrijfsopbrengsten 2707 kEUR"),
        ("bud_lrm_bedrijfskost_jr2025", BEDRIJFSKOST, "VO 4 code 60/66A bedrijfskosten 11687 kEUR"),
        ("bud_lrm_staff_jr2025", STAFF, "VO 4 code 62 bezoldigingen 6978 kEUR"),
        ("bud_lrm_expl_neg_jr2025", EXPL, "VO 4 code 9901 bedrijfsresultaat NEG -8980 kEUR"),
        ("bud_lrm_fin_opbr_jr2025", FIN_OPBR, "VO 4 code 75/76B financiële opbrengsten 33793 kEUR"),
        ("bud_lrm_pnl_jr2025", PNL, "VO 5 code 9905 te bestemmen resultaat boekjaar 17829 kEUR"),
        ("bud_lrm_dividend_jr2025", DIVIDEND, "VO 5 code 694 vergoeding kapitaal / dividend 6000 kEUR"),
    ]
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(amt),
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": basis,
                "source_id": "src_lrm_jr2025_vp",
                "confidence": "strong",
                "notes": f"tick{TICK}; VP form in kEUR ×1000; not TE-additive holding",
            }
            for bid, amt, basis in bud_rows
        ],
    )

    # commitments
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_lrm_jr2025_eva_holding",
                "title": (
                    "LRM NV JR2025 leftover VL EVA-PR investment holding "
                    "(assets 543m / FVA 516m / equity 521m / pnl 17.8m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "Limburg economy / Corda Thor Droneport campuses / portfolio firms",
                "legal_basis": (
                    "WVV NV; Decreet 07.05.2004 investeringsmaatschappijen VL; "
                    "EVA PR; Bestuursdecreet openbaarheid"
                ),
                "decision_date": "2026-05-18",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(ASSETS),
                "cash_by_year": f"2025:assets={ASSETS};fva={FVA};pnl={PNL};dividend={DIVIDEND}",
                "remaining_eur": "",
                "status": "observed",
                "evaluation_url": "https://docs.vlaamsparlement.be/files/pfile?id=2321629",
                "stated_goal": "Limburg reconversion / smart money / campus development",
                "cut_option": (
                    "Publish full FVA portfolio + NBB PDF cents; "
                    "review dividend vs operating NEG; campus daughter transparency"
                ),
                "source_id": "src_lrm_jr2025_vp",
                "confidence": "strong",
                "hierarchy_path": "Vlaanderen>Limburg>LRM>JR2025",
                "notes": f"tick{TICK}; Strong VP; VTE {VTE_CW} Medium CW cross-check",
            }
        ],
    )

    # leaderboard
    # priority_index ≈ 0.55*absurdity + 0.35*cost + 0.10*(10-difficulty)
    abs_s, cost_s, diff = 6.5, 7.5, 4.0
    prio = round(0.55 * abs_s + 0.35 * cost_s + 0.10 * (10 - diff), 2)
    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_lrm_fva_516m_assets_543m_expl_neg_9m_jr2025",
                "name": (
                    "LRM NV JR2025 leftover VL EVA-PR: FVA 516m / assets 543m / "
                    "expl NEG 9.0m / staff 7.0m / pnl 17.8m"
                ),
                "level": "L5",
                "type": "agency_holding",
                "hierarchy_path": "Vlaanderen>Limburg>LRM>JR2025_L5",
                "annual_cost_eur": str(BEDRIJFSKOST),
                "total_cost_eur": str(FVA),
                "tco_notes": (
                    f"bedrijfskosten {BEDRIJFSKOST}; FVA {FVA}; assets {ASSETS}; "
                    f"equity {EQUITY}; expl {EXPL}; staff {STAFF}; pnl {PNL}; "
                    f"dividend {DIVIDEND}; cash {CASH}; debt {DEBT}; VTE~{VTE_CW}"
                ),
                "confidence": "strong",
                "source_id": "src_lrm_jr2025_vp",
                "beneficiaries": "Limburg portfolio / campuses / Vlaamse overheid shareholder",
                "stated_goal": "Reconversion + smart money Limburg",
                "measured_outcome": (
                    "Operating NEG 9m covered by financial income 33.8m; "
                    "FVA 516m portfolio opacity; dividend 6m"
                ),
                "absurdity_score": str(abs_s),
                "cost_score": str(cost_s),
                "difficulty": str(diff),
                "priority_index": str(prio),
                "cut_proposal": (
                    "Publish NBB PDF + full FVA portfolio L5; "
                    "benchmark campus daughter losses vs parent dividend"
                ),
                "status": "active",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Strong VP form kEUR; not TE-additive holding shell; "
                    "corrupt AGB/Metro3/OWV filter N/A"
                ),
            }
        ],
    )

    # foi_queue
    append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Vlaanderen>Limburg>LRM>nbb_fva_portfolio_L5",
                "entity_id": ENTITY,
                "what_is_missing": (
                    "NBB deposit id + full JR2025 PDF (exact cents vs VP kEUR rounding); "
                    "full FVA portfolio line-list (deelnemingen 280/282/284 + vorderingen); "
                    "VTE exact; public subsidies received 2025 if any"
                ),
                "why_it_matters": (
                    "VL EVA-PR investment holding — FVA 516m + operating NEG 9m + dividend 6m "
                    "hides dual campus/portfolio public money flows after mined LRM daughters"
                ),
                "priority": "8",
                "recipient_body": "LRM NV / raad van bestuur / Departement F&B / minister Diependaele",
                "recipient_email": "info@lrm.be",
                "recipient_postal": "Kempische steenweg 311 bus 4.01 3500 Hasselt",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-26",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_lrm_jr2025_eva_holding",
                "linked_leaderboard_id": "lb_lrm_fva_516m_assets_543m_expl_neg_9m_jr2025",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK}; human-send only; Strong VP; AGB Bornem JR2024; "
                    "Dijk92 FOI; FARO NBB YE2025 unpublished"
                ),
            }
        ],
    )

    update_research_queue()

    # loop_state
    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
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
            lineterminator="\n",
        )
        w.writeheader()
        w.writerow(
            {
                "state_id": "main",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "last_tick_utc": UTC,
                "last_unit_id": "rq_1885",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover LRM NV 0452.138.972 Strong VL Parlement JR2025 "
                    f"(assets 543.2m FVA 516.1m equity 521.2m omzet 2.19m staff 6.98m "
                    f"expl NEG 8.98m pnl 17.83m dividend 6m); NBB PDF+FVA portfolio FOI; "
                    f"AGB Bornem JR2024; Dijk92 FOI; FARO YE2024/NBB YE2025 miss; "
                    f"next rq_1886; next every-10 1890; continuous hole_fill"
                ),
            }
        )

    print("OK tick", TICK, "LRM NV Strong")


if __name__ == "__main__":
    main()
