# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-26T00:40:00Z"

ENTITY = "vzw_zorg_saam_zusters_kindsheid_jesu"
OMZET = 135893468
BRUTO = 133937585
PNL = 2474247
EQUITY = 91404701
FTE = 1707
OMZET_PY = 131556260
PNL_PY = 3564566
EQUITY_PY = 89657388
BRUTO_PY = 130183641


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
            source_id="src_zorg_saam_jr2025_cw_nl",
            title="Companyweb NL Zorg-Saam Zusters Kindsheid Jesu YE2025 statutory",
            url="https://www.companyweb.be/nl/0470673890/zorg-saam-zusters-kindsheid-jesu",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2164; YE2025 omzet 135893468 pnl DROP 2474247 equity 91404701 bruto 133937585 FTE 1707; neerlegging 23.06.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_zorg_saam_jr2025_cw_en",
            title="Companyweb EN Zorg-Saam Zusters Kindsheid Jesu YE2025 statutory",
            url="https://www.companyweb.be/en/0470673890",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2164; EN mirror YE2025 Medium; filed 23-06-2026; FTE 1707 (CW 1.707 European thousands)",
        ),
        dict(
            source_id="src_zorg_saam_jr2025_cw_fr",
            title="Companyweb FR Zorg-Saam Zusters Kindsheid Jesu YE2025 statutory",
            url="https://www.companyweb.be/fr/0470673890",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2164; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_zorg_saam_kbo_2164",
            title="KBO Zorg-Saam 0470.673.890 Actief VZW Gent-Oostakker aanbestedende overheid",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0470673890",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2164; Actief VZW; Onze Lieve Vrouwstraat 23 9041 Gent; 16 VE; NACE 87.101 RVT + 87.301 ROB; aanbestedende overheid; KBO email/tel empty",
        ),
        dict(
            source_id="src_zorg_saam_foi_contact_2164",
            title="Zorg-Saam FOI contact zorgsaam@zorg-saam.zkj.be",
            url="https://www.zorg-saam.be/",
            publisher="Zorg-Saam Zusters Kindsheid Jesu",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2164; zorgsaam@zorg-saam.zkj.be; tel 09 235 28 12; zetel Onze Lieve Vrouwstraat 23 9041 Gent-Oostakker; NOT zorgsaam.be thuisverpleging Rotselaar",
        ),
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_zorg_saam_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2164; Medium CW; omzet JUMP +3.30% vs YE2024 131556260",
    ),
    (
        "bud_zorg_saam_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2164; Medium CW; bruto JUMP +2.88% vs YE2024 130183641",
    ),
    (
        "bud_zorg_saam_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2164; Medium CW; pnl DROP -30.6% vs YE2024 3564566",
    ),
    (
        "bud_zorg_saam_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2164; Medium CW; equity JUMP +1.95% vs YE2024 89657388",
    ),
    (
        "bud_zorg_saam_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 1707",
        "tick2164; Medium CW; assets/debt Unknown pending NBB PDF",
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
                source_id="src_zorg_saam_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_zorg_saam_jr2025_statutory_wzc_pnl_drop_omzet_135_9m",
            title="Zorg-Saam Zusters Kindsheid Jesu YE2025 leftover dual (omzet JUMP 135.9m / pnl DROP -30.6% / FTE 1707)",
            entity_id=ENTITY,
            beneficiary="WZC/RVT/ROB residents multi-site Gent belt (Zorg-Saam / ZKJ perimeter; 16 VE)",
            legal_basis="VZW RVT/ROB (KBO 0470.673.890; Actief; 16 VE; NACE 87.101/87.301; aanbestedende overheid)",
            decision_date="2026-06-23",
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
            evaluation_url="https://www.companyweb.be/en/0470673890",
            stated_goal="Multi-site residential elderly care (Zorg-Saam Zusters Kindsheid Jesu)",
            cut_option="Publish NBB PDF assets/debt FOI; explain pnl DROP -30.6% despite omzet JUMP +3.3%; RIZIV/dagprijs + per-site matrix",
            source_id="src_zorg_saam_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>ZorgSaam_ZKJ>JR2025_statutory_L5",
            notes="tick2164; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Residentie Oudenburg skipped NACE 55/68; Lork Hoeselt optional unused; not TE-additive of 348bn; DISTINCT De Medemens/Foyer De Lork/Sint-Bernardus/Ruggeveld",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_zorg_saam_omzet_135_9m_pnl_drop_30pct_jr2025",
            name="Zorg-Saam ZKJ omzet JUMP 135.9m / pnl DROP -30.6% (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>ZorgSaam_ZKJ>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 135.9m / 1707 FTE / 16 VE; pnl DROP -30.6% despite omzet JUMP +3.3%; equity +2%; assets/debt Unknown pending NBB PDF; aanbestedende overheid",
            confidence="medium",
            source_id="src_zorg_saam_jr2025_cw_en",
            beneficiaries="WZC clients Zorg-Saam / ZKJ multi-site",
            stated_goal="Multi-site residential elderly care Gent belt",
            measured_outcome="omzet JUMP +3.30%; bruto JUMP +2.88%; pnl DROP -30.6%; equity JUMP +1.95%; FTE 1707",
            absurdity_score="6.2",
            cost_score="8.0",
            difficulty="4.0",
            priority_index="6.7",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose pnl DROP path despite rising omzet; per-site matrix",
            status="open",
            struck_reason="",
            notes="tick2164; Medium CW; FOI gap_zorg_saam_nbb_pdf_assets_debt_pnl_drop_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Zorg-Saam Zusters Kindsheid Jesu VZW",
            name_fr="Zorg-Saam Soeurs de l'Enfance de Jésus ASBL",
            name_en="Zorg-Saam Sisters of the Childhood of Jesus non-profit",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.zorg-saam.be/",
            foi_email="zorgsaam@zorg-saam.zkj.be",
            foi_postal="Onze Lieve Vrouwstraat 23, 9041 Gent-Oostakker",
            notes="tick2164 YE2025 Medium CW NL+EN+FR + Strong KBO 0470.673.890 Actief VZW 16 VE NACE 87.101/87.301 aanbestedende overheid; omzet JUMP 135.9m pnl DROP -30.6% equity 91.4m bruto JUMP 133.9m FTE 1707; assets/debt Unknown; FOI gap_zorg_saam_nbb_pdf_assets_debt_pnl_drop_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT De Medemens/Foyer De Lork Geel/Sint-Bernardus",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_zorg_saam_nbb_pdf_assets_debt_pnl_drop_matrix_l5",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>ZorgSaam_ZKJ>NBB_PDF_assets_debt_pnl_drop",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); RIZIV/Vlaams vs dagprijs split; per-site matrix for 16 VE; explanation of pnl DROP -30.6% (EUR2.47m vs YE2024 EUR3.56m) despite omzet JUMP +3.3%",
            why_it_matters="Medium CW shows EUR135.9m aanbestedende-overheid multi-site WZC VZW with profit down ~31% while turnover rose — no balanstotaal/assets/debt published",
            priority="8",
            recipient_body="vzw Zorg-Saam Zusters Kindsheid Jesu",
            recipient_email="zorgsaam@zorg-saam.zkj.be",
            recipient_postal="Onze Lieve Vrouwstraat 23, 9041 Gent-Oostakker",
            draft_letter_path="docs/doge/foi/drafts/gap_zorg_saam_nbb_pdf_assets_debt_pnl_drop_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_zorg_saam_jr2025_statutory_wzc_pnl_drop_omzet_135_9m",
            linked_leaderboard_id="lb_zorg_saam_omzet_135_9m_pnl_drop_30pct_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2164; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2164":
        row["title"] = (
            "leftover dual — Zorg-Saam Zusters Kindsheid Jesu YE2025 Medium "
            "(omzet JUMP 135.9m / pnl DROP -30.6%)"
        )
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed leftover Zorg-Saam ZKJ after Ruggeveld/Sint-Bernardus race; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; skipped Residentie Oudenburg NACE 55/68; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent."
        )
        row["blocked_gap_id"] = "gap_zorg_saam_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2164 Zorg-Saam Medium omzet JUMP 135.9m (+3.30%) bruto JUMP 133.9m pnl DROP -30.6% "
            "equity JUMP 91.4m FTE 1707; KBO Actief VZW 16 VE Gent-Oostakker aanbestedende overheid; "
            "FOI zorgsaam@zorg-saam.zkj.be; next every-10 2170"
        )

if not any(x["task_id"] == "rq_2165" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2165",
            title=(
                "leftover dual hole-fill after Zorg-Saam — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2165 after Zorg-Saam ZKJ YE2025 Medium (omzet 135.9m / pnl DROP -30.6%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                "(optional: WZC Foyer De Lork Hoeselt BV 0755.822.317 YE2025 empty-omzet NEG equity bruto 0.79m; "
                "'t Hofke Puurs 0823.488.131 YE2025; Maria Boodschap Niel still YE2024). "
                "Do NOT redo Zorg-Saam Zusters Kindsheid Jesu 0470.673.890, WZC Sint-Bernardus De Panne 0432.582.485, "
                "Residentie Ruggeveld Antwerpen, Salvator Welzijnscentrum Hasselt, Boterlaarhof Deurne, "
                "Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, "
                "De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, "
                "WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, "
                "Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, "
                "Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, "
                "Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, "
                "Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, "
                "De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, "
                "Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, "
                "Rusthuis Sint Jozef Ninove, Zilverlinde Olen, De Medemens Antwerpen, Emmaüs Mechelen, Famifamenne, "
                "Residentie Oudenburg 0450.755.634 (NACE 55/68 hospitality-RE)."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2164 Zorg-Saam; FARO/AIESH/REW still YE2024; next every-10 2170",
        )
    )
    print("spawned rq_2165")

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
        last_unit_id="rq_2164",
        ticks_completed="2164",
        paused="no",
        notes=(
            "tick2164 leftover Zorg-Saam ZKJ 0470.673.890 Medium (omzet JUMP 135.9m; pnl DROP -30.6%; "
            "equity 91.4m; FTE 1707; 16 VE aanbestedende overheid); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Residentie Oudenburg skipped NACE 55/68; next rq_2165; next every-10 2170; continuous hole_fill"
        ),
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2164")
