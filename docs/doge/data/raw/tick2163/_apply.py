# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-26T00:20:00Z"

ENTITY = "bv_residentie_ruggeveld_antwerpen"
BRUTO = 4619469
PNL = 28022
EQUITY = 282348
FTE = 68.8
BRUTO_PY = 4314312
PNL_PY = -9209
EQUITY_PY = 254326


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
            source_id="src_ruggeveld_jr2025_cw_nl",
            title="Companyweb NL Residentie Ruggeveld YE2025 statutory",
            url="https://www.companyweb.be/nl/0473694748/residentie-ruggeveld",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; YE2025 omzet empty bruto JUMP 4619469 pnl FLIP PROFIT 28022 equity JUMP 282348 FTE 68.8; neerlegging 13.07.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_ruggeveld_jr2025_cw_en",
            title="Companyweb EN Residentie Ruggeveld YE2025 statutory",
            url="https://www.companyweb.be/en/0473694748/residentie-ruggeveld",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; EN mirror YE2025 Medium; filed 13-07-2026; Turnover unpublished; FTE 68.8",
        ),
        dict(
            source_id="src_ruggeveld_jr2025_cw_fr",
            title="Companyweb FR Residentie Ruggeveld YE2025 statutory",
            url="https://www.companyweb.be/fr/0473694748",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_ruggeveld_kbo_2163",
            title="KBO Residentie Ruggeveld 0473.694.748 Actief BV Antwerpen",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0473694748",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2163; Actief BV; Ruggeveldlaan 55 2100 Antwerpen; 1 VE; NACE 87.301 ROB; KBO email empty",
        ),
        dict(
            source_id="src_ruggeveld_foi_zorgfamilie_2163",
            title="De Zorgfamilie FOI channel vragen@dezorgfamilie.be (Ruggeveld+Boterlaarhof)",
            url="https://www.dezorgfamilie.be/",
            publisher="De Zorgfamilie",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2163; vragen@dezorgfamilie.be; tel 03 380 12 12; sibling of Boterlaarhof",
        ),
    ],
)

for bid, amount, basis, notes in [
    ("bud_ruggeveld_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025 (omzet empty)", "tick2163; Medium CW; bruto JUMP +7.07% vs YE2024 4314312; omzet unpublished"),
    ("bud_ruggeveld_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025", "tick2163; Medium CW; pnl FLIP PROFIT from YE2024 LOSS -9209"),
    ("bud_ruggeveld_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", "tick2163; Medium CW; equity JUMP +11.02% vs YE2024 254326"),
    ("bud_ruggeveld_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 68.8", "tick2163; Medium CW; assets/debt Unknown; De Zorgfamilie sibling Boterlaarhof"),
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
                source_id="src_ruggeveld_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_ruggeveld_jr2025_statutory_wzc_bruto_jump_omzet_empty",
            title="Residentie Ruggeveld YE2025 leftover dual (bruto JUMP 4.62m / omzet empty / pnl FLIP PROFIT)",
            entity_id=ENTITY,
            beneficiary="WZC residents Antwerpen Ruggeveldlaan (De Zorgfamilie)",
            legal_basis="BV ROB (KBO 0473.694.748; Actief; 1 VE; NACE 87.301)",
            decision_date="2026-07-13",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": "Unknown",
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0473694748/residentie-ruggeveld",
            stated_goal="Residential elderly care Antwerpen (Residentie Ruggeveld / De Zorgfamilie)",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty omzet behind bruto; map related-party vs Boterlaarhof",
            source_id="src_ruggeveld_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ResidentieRuggeveld>JR2025_statutory_L5",
            notes="tick2163; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; sibling Boterlaarhof; not TE-additive of 348bn; DISTINCT Salvator/WZND/Foyer De Lork",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_ruggeveld_bruto_4_62m_omzet_empty_pnl_flip_jr2025",
            name="Residentie Ruggeveld bruto JUMP 4.62m / omzet empty / pnl FLIP PROFIT (YE2025)",
            level="L5",
            type="wzc_bv_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ResidentieRuggeveld>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto envelope 4.62m / omzet unpublished / 69 FTE; pnl FLIP PROFIT after YE2024 LOSS; De Zorgfamilie dual with Boterlaarhof; assets/debt Unknown",
            confidence="medium",
            source_id="src_ruggeveld_jr2025_cw_en",
            beneficiaries="WZC clients Residentie Ruggeveld Antwerpen",
            stated_goal="Residential elderly care Antwerpen (De Zorgfamilie)",
            measured_outcome="omzet empty; bruto JUMP +7.07%; pnl FLIP PROFIT; equity JUMP +11.02%; FTE 68.8",
            absurdity_score="5.8",
            cost_score="3.5",
            difficulty="4.0",
            priority_index="5.4",
            cut_proposal="Publish NBB PDF assets/debt/omzet FOI; disclose related-party matrix vs Boterlaarhof",
            status="open",
            struck_reason="",
            notes="tick2163; Medium CW; FOI gap_ruggeveld_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Residentie Ruggeveld BV (Antwerpen / De Zorgfamilie)",
            name_fr="Residentie Ruggeveld SRL (Anvers)",
            name_en="Residentie Ruggeveld nursing home (Antwerp)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.dezorgfamilie.be/",
            foi_email="vragen@dezorgfamilie.be",
            foi_postal="Ruggeveldlaan 55, 2100 Antwerpen",
            notes="tick2163 YE2025 Medium CW NL+EN+FR + Strong KBO 0473.694.748 Actief BV 1 VE NACE 87.301; omzet empty bruto JUMP 4.62m pnl FLIP PROFIT 28k equity JUMP 0.28m FTE 68.8; assets/debt Unknown; FOI gap_ruggeveld_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; sibling bv_boterlaarhof_deurne; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Salvator/WZND/Foyer De Lork",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_ruggeveld_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>ResidentieRuggeveld>NBB_PDF_assets_debt_omzet_empty_bruto_jump",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); omzet/code70 behind bruto 4.62m; RIZIV/Vlaams vs dagprijs; related-party flows vs Boterlaarhof/De Zorgfamilie",
            why_it_matters="Medium CW shows De Zorgfamilie BV WZC sibling of Boterlaarhof with empty omzet + bruto JUMP 4.62m — same opacity class; no balanstotaal/assets/debt published",
            priority="8",
            recipient_body="Residentie Ruggeveld BV / De Zorgfamilie",
            recipient_email="vragen@dezorgfamilie.be",
            recipient_postal="Ruggeveldlaan 55, 2100 Antwerpen",
            draft_letter_path="docs/doge/foi/drafts/gap_ruggeveld_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_ruggeveld_jr2025_statutory_wzc_bruto_jump_omzet_empty",
            linked_leaderboard_id="lb_ruggeveld_bruto_4_62m_omzet_empty_pnl_flip_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2163; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2163":
        row["title"] = "leftover dual — Residentie Ruggeveld YE2025 Medium (bruto JUMP 4.62m / omzet empty / pnl FLIP PROFIT)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover Residentie Ruggeveld (De Zorgfamilie sibling) after Boterlaarhof/Salvator race; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_ruggeveld_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2163 Ruggeveld Medium bruto JUMP 4.62m (+7.07%) omzet empty pnl FLIP PROFIT 28k equity JUMP 0.28m FTE 68.8; KBO Actief BV 1 VE Antwerpen; FOI vragen@dezorgfamilie.be; sibling Boterlaarhof; next every-10 2170"

if not any(x["task_id"] == "rq_2164" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2164",
            title="leftover dual hole-fill after Ruggeveld — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2164 after Residentie Ruggeveld YE2025 Medium (bruto 4.62m / omzet empty). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (Hof ter Lande YE2024-only; Lork Hoeselt BV YE2025 empty-omzet NEG equity optional). "
                "Do NOT redo Residentie Ruggeveld Antwerpen, Salvator Welzijnscentrum Hasselt, Boterlaarhof Deurne, Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, Rusthuis Sint Jozef Ninove, Zilverlinde Olen."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2163 Ruggeveld; FARO/AIESH/REW still YE2024; next every-10 2170",
        )
    )
    print("spawned rq_2164")

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
        last_unit_id="rq_2163",
        ticks_completed="2163",
        paused="no",
        notes="tick2163 leftover Residentie Ruggeveld 0473.694.748 Medium (bruto JUMP 4.62m; omzet empty; pnl FLIP PROFIT 28k; FTE 69; De Zorgfamilie sibling Boterlaarhof); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2164; next every-10 2170; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2163")
