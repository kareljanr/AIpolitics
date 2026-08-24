# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T24:00:00Z"  # will normalize below
TS = "2026-08-26T00:00:00Z"

ENTITY = "bv_boterlaarhof_deurne"
BRUTO = 4659031
PNL = 66370
EQUITY = 1203689
FTE = 61.3
BRUTO_PY = 4394215
PNL_PY = 80613
EQUITY_PY = 1137319
# omzet unpublished both years


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
            source_id="src_boterlaarhof_jr2025_cw_nl",
            title="Companyweb NL Boterlaarhof YE2025 statutory",
            url="https://www.companyweb.be/nl/0412886636/boterlaarhof",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; YE2025 omzet empty bruto 4659031 pnl 66370 equity 1203689 FTE 61.3; neerlegging 13.07.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_boterlaarhof_jr2025_cw_en",
            title="Companyweb EN Boterlaarhof YE2025 statutory",
            url="https://www.companyweb.be/en/0412886636",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; EN mirror YE2025 Medium; filed 13-07-2026; FTE 61.3; omzet unpublished",
        ),
        dict(
            source_id="src_boterlaarhof_jr2025_cw_fr",
            title="Companyweb FR Boterlaarhof YE2025 statutory",
            url="https://www.companyweb.be/fr/0412886636",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2162; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_boterlaarhof_kbo_2162",
            title="KBO Boterlaarhof 0412.886.636 Actief BV Antwerpen/Deurne 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=412886636",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2162; Actief BV sinds 11.12.2023; Boterlaarbaan 11 2100 Antwerpen; 1 VE; NACE 87.101 RVT; KBO email/web empty; not aanbestedende",
        ),
        dict(
            source_id="src_boterlaarhof_foi_contact_2162",
            title="Boterlaarhof / De Zorgfamilie FOI channel vragen@dezorgfamilie.be",
            url="https://www.boterlaarhof.be/",
            publisher="Boterlaarhof / De Zorgfamilie",
            accessed_date="2026-08-25",
            source_class="foi_contact",
            notes="tick2162; site boterlaarhof.be; vragen@dezorgfamilie.be; tel 03 380 12 12",
        ),
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_boterlaarhof_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet 70 empty)",
        "tick2162; Medium CW; bruto JUMP +6.03% vs YE2024 4394215; primary envelope (omzet unpublished)",
    ),
    (
        "bud_boterlaarhof_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2162; Medium CW; pnl DROP -17.67% vs YE2024 80613",
    ),
    (
        "bud_boterlaarhof_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2162; Medium CW; equity JUMP +5.84% vs YE2024 1137319",
    ),
    (
        "bud_boterlaarhof_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 61.3",
        "tick2162; Medium CW; assets/debt Unknown; omzet empty; 1 VE Deurne",
    ),
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
                source_id="src_boterlaarhof_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_boterlaarhof_jr2025_statutory_wzc_bruto_4_66m",
            title="Boterlaarhof YE2025 leftover dual (bruto JUMP 4.66m / omzet empty / pnl DROP)",
            entity_id=ENTITY,
            beneficiary="RVT residents Boterlaarhof Deurne (De Zorgfamilie)",
            legal_basis="BV RVT (KBO 0412.886.636; Actief; 1 VE; NACE 87.101; BV sinds 11.12.2023)",
            decision_date="2026-07-13",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": None,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "ve": 1,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0412886636",
            stated_goal="Residential elderly care RVT Boterlaarhof Deurne",
            cut_option="Publish NBB PDF assets/debt FOI; disclose omzet 70 path; De Zorgfamilie group matrix",
            source_id="src_boterlaarhof_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Boterlaarhof>JR2025_statutory_L5",
            notes="tick2162; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; WZND taken 2161; not TE-additive of 348bn",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_boterlaarhof_bruto_4_66m_omzet_empty_pnl_drop_jr2025",
            name="Boterlaarhof bruto JUMP 4.66m / omzet empty / pnl DROP (YE2025)",
            level="L5",
            type="wzc_bv_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Boterlaarhof>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto envelope 4.66m / 1 VE / 61.3 FTE; omzet 70 unpublished; pnl DROP -17.7%; equity thin 1.20m; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id="src_boterlaarhof_jr2025_cw_en",
            beneficiaries="RVT clients Deurne / De Zorgfamilie",
            stated_goal="Residential elderly care RVT Boterlaarhof",
            measured_outcome="bruto JUMP +6.03%; pnl DROP -17.67%; equity JUMP +5.84%; FTE 61.3; omzet empty",
            absurdity_score="5.3",
            cost_score="5.5",
            difficulty="3.5",
            priority_index="5.4",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose empty-omzet path + De Zorgfamilie group flows",
            status="open",
            struck_reason="",
            notes="tick2162; Medium CW; FOI gap_boterlaarhof_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; stall FARO/AIESH/REW YE2024; WZND done 2161",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Boterlaarhof BV (Deurne / De Zorgfamilie RVT)",
            name_fr="Boterlaarhof SRL (Deurne)",
            name_en="Boterlaarhof nursing home BV (Deurne)",
            level="other",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.boterlaarhof.be/",
            foi_email="vragen@dezorgfamilie.be",
            foi_postal="Boterlaarbaan 11, 2100 Antwerpen (Deurne)",
            notes="tick2162 YE2025 Medium CW NL+EN+FR + Strong KBO 0412.886.636 Actief BV 1 VE NACE 87.101; bruto JUMP 4.66m omzet empty pnl DROP 66.4k equity JUMP 1.20m FTE 61.3; assets/debt Unknown; FOI gap_boterlaarhof_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; WZND taken 2161",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_boterlaarhof_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>Deurne>Boterlaarhof>NBB_PDF_assets_debt_omzet_empty_bruto",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); omzet 70 path vs empty CW field; RIZIV/Vlaams vs dagprijs split; De Zorgfamilie group matrix; AV/bestuur approval YE2025",
            why_it_matters="Medium CW shows EUR4.66m bruto commercial RVT BV with unpublished omzet, pnl DROP and thin equity 1.20m vs 61.3 FTE — no balanstotaal/assets/debt published",
            priority="7",
            recipient_body="Boterlaarhof BV / De Zorgfamilie",
            recipient_email="vragen@dezorgfamilie.be",
            recipient_postal="Boterlaarbaan 11, 2100 Antwerpen (Deurne)",
            draft_letter_path="docs/doge/foi/drafts/gap_boterlaarhof_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_boterlaarhof_jr2025_statutory_wzc_bruto_4_66m",
            linked_leaderboard_id="lb_boterlaarhof_bruto_4_66m_omzet_empty_pnl_drop_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2162; ready NOT sent; Medium CW + Strong KBO; site vragen@dezorgfamilie.be tel 03 380 12 12; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2162":
        row["title"] = (
            "leftover dual — Boterlaarhof Deurne YE2025 Medium (bruto JUMP 4.66m / omzet empty / pnl DROP)"
        )
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed leftover Boterlaarhof after WZND 2161; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent."
        )
        row["blocked_gap_id"] = (
            "gap_boterlaarhof_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5"
        )
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2162 Boterlaarhof Medium bruto JUMP 4.66m (+6.03%) pnl DROP 66.4k (-17.7%) equity JUMP 1.20m "
            "FTE 61.3 omzet unpublished; KBO Actief BV 1 VE Deurne NACE 87.101 De Zorgfamilie; "
            "FOI vragen@dezorgfamilie.be; next every-10 2170"
        )

if not any(x["task_id"] == "rq_2163" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2163",
            title="leftover dual hole-fill after Boterlaarhof — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2163 after Boterlaarhof YE2025 Medium (bruto 4.66m / omzet empty / pnl DROP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS). "
                "Do NOT redo Boterlaarhof Deurne, Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, "
                "HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, "
                "MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, "
                "Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, "
                "Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, "
                "Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, "
                "AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, "
                "Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, "
                "Ocura, Rusthuis Sint Jozef Ninove, Hof ter Lande if taken."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2162 Boterlaarhof; FARO/AIESH/REW still YE2024; next every-10 2170",
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
        notes=(
            "tick2162 leftover Boterlaarhof 0412.886.636 Medium (bruto JUMP 4.66m; omzet empty; pnl DROP 66k; "
            "equity JUMP 1.20m; FTE 61.3; Deurne De Zorgfamilie); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "WZND done 2161; next rq_2163; next every-10 2170; continuous hole_fill"
        ),
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2162")
