# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-26T00:00:00Z"

ENTITY = "vzw_salvator_welzijnscentrum_hasselt"
OMZET = 18233452
BRUTO = 16096582
PNL = -505732
EQUITY = 13414850
FTE = 203.2
OMZET_PY = 17794000
PNL_PY = 1209492
EQUITY_PY = 13882378
BRUTO_PY = 16407384


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added)


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_salvator_jr2025_cw_nl",
            title="Companyweb NL Salvator Welzijnscentrum YE2025 statutory",
            url="https://www.companyweb.be/nl/0423571581/salvator-welzijnscentrum",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; YE2025 omzet 18233452 pnl LOSS flip -505732 equity DROP 13414850 bruto 16096582 FTE 203.2; neerlegging 12.08.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_salvator_jr2025_cw_en",
            title="Companyweb EN Salvator Welzijnscentrum YE2025 statutory",
            url="https://www.companyweb.be/en/0423571581",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; EN mirror YE2025 Medium; filed 12-08-2026; FTE 203.2",
        ),
        dict(
            source_id="src_salvator_jr2025_cw_fr",
            title="Companyweb FR Salvator Welzijnscentrum YE2025 statutory",
            url="https://www.companyweb.be/fr/0423571581",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_salvator_kbo_2162",
            title="KBO Salvator Welzijnscentrum 0423.571.581 Actief VZW Hasselt",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0423571581",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2162; Actief VZW; Ekkelgaarden 17 bus 101 3500 Hasselt; 1 VE; NACE 87.101; KBO email empty",
        ),
        dict(
            source_id="src_salvator_foi_contact_2162",
            title="Salvator FOI contact info@salvator.be",
            url="https://www.salvator.be/",
            publisher="Salvator Welzijnscentrum",
            accessed_date="2026-08-25",
            source_class="foi_contact",
            notes="tick2162; info@salvator.be; site salvator.be",
        ),
    ],
)

for bid, amount, basis, notes in [
    ("bud_salvator_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025", "tick2162; Medium CW; omzet JUMP +2.47% vs YE2024 17794000"),
    ("bud_salvator_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", "tick2162; Medium CW; bruto DROP -1.89% vs YE2024 16407384"),
    ("bud_salvator_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025", "tick2162; Medium CW; pnl LOSS FLIP from YE2024 PROFIT 1209492"),
    ("bud_salvator_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", "tick2162; Medium CW; equity DROP -3.37% vs YE2024 13882378"),
    ("bud_salvator_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 203.2", "tick2162; Medium CW; assets/debt Unknown pending NBB PDF"),
]:
    append_csv(
        ROOT / "budgets.csv",
        [
            dict(
                budget_id=bid,
                entity_id=ENTITY,
                year="2025",
                amount_eur=str(amount),
                amount_min_eur=str(amount),
                amount_max_eur=str(amount),
                basis=basis,
                source_id="src_salvator_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_salvator_jr2025_statutory_wzc_pnl_loss_flip_omzet_18m",
            title="Salvator Welzijnscentrum YE2025 leftover dual (omzet JUMP 18.23m / pnl LOSS flip -506k / FTE 203)",
            entity_id=ENTITY,
            beneficiary="WZC residents Hasselt (Salvatorrusthuis)",
            legal_basis="VZW RVT (KBO 0423.571.581; Actief; 1 VE; NACE 87.101)",
            decision_date="2026-08-12",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(OMZET),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": OMZET,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": OMZET_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_bruto": BRUTO_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0423571581",
            stated_goal="Residential elderly care Hasselt (Salvator)",
            cut_option="Publish NBB PDF assets/debt FOI; explain LOSS flip after YE2024 profit 1.21m; RIZIV/dagprijs split",
            source_id="src_salvator_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>Salvator>JR2025_statutory_L5",
            notes="tick2162; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Hof ter Lande YE2024 skipped; not TE-additive of 348bn; DISTINCT WZND/Foyer De Lork/Lindeboom/HERTOG JAN/OLV Kempen",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_salvator_omzet_18m_pnl_loss_flip_506k_jr2025",
            name="Salvator Welzijnscentrum omzet JUMP 18.23m / pnl LOSS flip -506k (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>Salvator>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 18.23m / 203 FTE; pnl LOSS flip after YE2024 profit 1.21m; equity DROP -3.4%; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id="src_salvator_jr2025_cw_en",
            beneficiaries="WZC clients Hasselt Salvatorrusthuis",
            stated_goal="Residential elderly care Hasselt",
            measured_outcome="omzet JUMP +2.47%; bruto DROP -1.89%; pnl LOSS FLIP; equity DROP -3.37%; FTE 203.2",
            absurdity_score="6.7",
            cost_score="5.5",
            difficulty="4.0",
            priority_index="6.0",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose LOSS flip path after large YE2024 profit",
            status="open",
            struck_reason="",
            notes="tick2162; Medium CW; FOI gap_salvator_nbb_pdf_assets_debt_pnl_loss_flip_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Salvator Welzijnscentrum VZW (Hasselt / Salvatorrusthuis)",
            name_fr="Salvator Welzijnscentrum ASBL (Hasselt)",
            name_en="Salvator nursing home (Hasselt)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.salvator.be/",
            foi_email="info@salvator.be",
            foi_postal="Ekkelgaarden 17 bus 101, 3500 Hasselt",
            notes="tick2162 YE2025 Medium CW NL+EN+FR + Strong KBO 0423.571.581 Actief VZW 1 VE NACE 87.101; omzet JUMP 18.23m pnl LOSS FLIP -506k equity DROP 13.41m bruto DROP 16.10m FTE 203.2; assets/debt Unknown; FOI gap_salvator_nbb_pdf_assets_debt_pnl_loss_flip_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT WZND/Foyer De Lork/Lindeboom/HERTOG JAN/OLV Kempen",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_salvator_nbb_pdf_assets_debt_pnl_loss_flip_matrix_l5",
            hierarchy_path="Vlaanderen>Limburg>Hasselt>Salvator>NBB_PDF_assets_debt_pnl_loss_flip",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); RIZIV/Vlaams vs dagprijs split; explanation of pnl LOSS flip -506k after YE2024 profit 1.21m and equity DROP -3.4%",
            why_it_matters="Medium CW shows EUR18.23m Hasselt VZW WZC with dramatic LOSS flip from large prior-year profit — no balanstotaal/assets/debt published",
            priority="8",
            recipient_body="vzw Salvator Welzijnscentrum",
            recipient_email="info@salvator.be",
            recipient_postal="Ekkelgaarden 17 bus 101, 3500 Hasselt",
            draft_letter_path="docs/doge/foi/drafts/gap_salvator_nbb_pdf_assets_debt_pnl_loss_flip_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_salvator_jr2025_statutory_wzc_pnl_loss_flip_omzet_18m",
            linked_leaderboard_id="lb_salvator_omzet_18m_pnl_loss_flip_506k_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2162; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2162":
        row["title"] = "leftover dual — Salvator Welzijnscentrum Hasselt YE2025 Medium (omzet JUMP 18.23m / pnl LOSS flip -506k)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover Salvator after WZND; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Hof ter Lande YE2024 skipped; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_salvator_nbb_pdf_assets_debt_pnl_loss_flip_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2162 Salvator Medium omzet JUMP 18.23m (+2.47%) bruto DROP 16.10m pnl LOSS FLIP -506k equity DROP 13.41m FTE 203.2; KBO Actief VZW 1 VE Hasselt; FOI info@salvator.be; next every-10 2170"

if not any(x["task_id"] == "rq_2163" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2163",
            title="leftover dual hole-fill after Salvator — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2163 after Salvator Welzijnscentrum Hasselt YE2025 Medium (omzet 18.23m / pnl LOSS flip -506k). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (Hof ter Lande YE2024-only; WZC Foyer De Lork Hoeselt BV YE2025 empty-omzet NEG equity optional). "
                "Do NOT redo Salvator Welzijnscentrum Hasselt, Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, Rusthuis Sint Jozef Ninove, Zilverlinde Olen."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2162 Salvator; FARO/AIESH/REW still YE2024; next every-10 2170",
        )
    )
    print("spawned rq_2163")

with (ROOT / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    st = list(r)
    scols = r.fieldnames
st[0].update(
    dict(
        mode="continuous",
        current_sprint="hole_fill",
        last_tick_utc=TS,
        last_unit_id="rq_2162",
        ticks_completed="2162",
        paused="no",
        notes="tick2162 leftover Salvator Welzijnscentrum 0423.571.581 Medium (omzet JUMP 18.23m; pnl LOSS flip -506k; equity DROP -3.4%; FTE 203; Hasselt); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2163; next every-10 2170; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2162")
