# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-26T00:20:00Z"

ENTITY = "vzw_wzc_sint_bernardus_de_panne"
OMZET = 8489271
BRUTO = 8882788
PNL = 40101
EQUITY = 8134230
FTE = 111.6
OMZET_PY = 8189802
PNL_PY = 80165
EQUITY_PY = 8158931
BRUTO_PY = 8627751


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
            source_id="src_sint_bernardus_de_panne_jr2025_cw_nl",
            title="Companyweb NL WZC Sint-Bernardus De Panne YE2025 statutory",
            url="https://www.companyweb.be/nl/0432582485/woonzorgcentrum-sint-bernardus-vzw",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; YE2025 omzet 8489271 pnl DROP 40101 equity 8134230 bruto 8882788 FTE 111.6; neerlegging 24.07.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_sint_bernardus_de_panne_jr2025_cw_en",
            title="Companyweb EN WZC Sint-Bernardus De Panne YE2025 statutory",
            url="https://www.companyweb.be/en/0432582485",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; EN mirror YE2025 Medium; filed 24-07-2026; FTE 111.6",
        ),
        dict(
            source_id="src_sint_bernardus_de_panne_jr2025_cw_fr",
            title="Companyweb FR WZC Sint-Bernardus De Panne YE2025 statutory",
            url="https://www.companyweb.be/fr/0432582485",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2163; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_sint_bernardus_de_panne_kbo_2163",
            title="KBO WZC Sint-Bernardus 0432.582.485 Actief VZW De Panne",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0432582485",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2163; Actief VZW; Koninklijke Baan 18 8660 De Panne; 1 VE; NACE 87.101; KBO email empty; start 12.09.1986",
        ),
        dict(
            source_id="src_sint_bernardus_de_panne_foi_contact_2163",
            title="WZC Sint-Bernardus De Panne FOI contact info@sint-bernardus.be",
            url="https://www.sint-bernardus.be/",
            publisher="WZC Sint-Bernardus De Panne",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2163; info@sint-bernardus.be; tel +32 58 41 11 33; NOT brewery sintbernardus.be / NOT wzcsintbernardus.be Gent-path",
        ),
    ],
)

for bid, amount, basis, notes in [
    ("bud_sint_bernardus_de_panne_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025", "tick2163; Medium CW; omzet JUMP +3.66% vs YE2024 8189802"),
    ("bud_sint_bernardus_de_panne_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", "tick2163; Medium CW; bruto JUMP +2.96% vs YE2024 8627751"),
    ("bud_sint_bernardus_de_panne_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025", "tick2163; Medium CW; pnl DROP -50.0% vs YE2024 80165"),
    ("bud_sint_bernardus_de_panne_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", "tick2163; Medium CW; equity DROP -0.30% vs YE2024 8158931"),
    ("bud_sint_bernardus_de_panne_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 111.6", "tick2163; Medium CW; assets/debt Unknown pending NBB PDF"),
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
                source_id="src_sint_bernardus_de_panne_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_sint_bernardus_de_panne_jr2025_statutory_wzc_pnl_drop_omzet_8_49m",
            title="WZC Sint-Bernardus De Panne YE2025 leftover dual (omzet JUMP 8.49m / pnl DROP -50% / FTE 112)",
            entity_id=ENTITY,
            beneficiary="WZC residents De Panne (Sint-Bernardus + assistentiewoningen/thuisverpleging perimeter)",
            legal_basis="VZW RVT (KBO 0432.582.485; Actief; 1 VE; NACE 87.101)",
            decision_date="2026-07-24",
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
            evaluation_url="https://www.companyweb.be/en/0432582485",
            stated_goal="Residential elderly care De Panne (WZC Sint-Bernardus)",
            cut_option="Publish NBB PDF assets/debt FOI; explain pnl DROP -50% despite omzet JUMP +3.7%; RIZIV/dagprijs split",
            source_id="src_sint_bernardus_de_panne_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>WestVlaanderen>DePanne>WZC_SintBernardus>JR2025_statutory_L5",
            notes="tick2163; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Salvator/Boterlaarhof/WZND/Foyer De Lork/OLV Kempen/HERTOG JAN/mined Sint-Bernardus 0445106274",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_sint_bernardus_de_panne_omzet_8_49m_pnl_drop_50pct_jr2025",
            name="WZC Sint-Bernardus De Panne omzet JUMP 8.49m / pnl DROP -50% (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>WestVlaanderen>DePanne>WZC_SintBernardus>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 8.49m / 111.6 FTE; pnl DROP -50% despite omzet JUMP +3.7%; equity flat; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id="src_sint_bernardus_de_panne_jr2025_cw_en",
            beneficiaries="WZC clients De Panne Sint-Bernardus",
            stated_goal="Residential elderly care De Panne",
            measured_outcome="omzet JUMP +3.66%; bruto JUMP +2.96%; pnl DROP -50.0%; equity DROP -0.30%; FTE 111.6",
            absurdity_score="5.5",
            cost_score="4.8",
            difficulty="3.5",
            priority_index="5.1",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; disclose pnl DROP path despite rising omzet",
            status="open",
            struck_reason="",
            notes="tick2163; Medium CW; FOI gap_sint_bernardus_de_panne_nbb_pdf_assets_debt_pnl_drop_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Woonzorgcentrum Sint-Bernardus VZW (De Panne)",
            name_fr="Maison de repos Sint-Bernardus ASBL (La Panne)",
            name_en="WZC Sint-Bernardus nursing home (De Panne)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.sint-bernardus.be/",
            foi_email="info@sint-bernardus.be",
            foi_postal="Koninklijke Baan 18, 8660 De Panne",
            notes="tick2163 YE2025 Medium CW NL+EN+FR + Strong KBO 0432.582.485 Actief VZW 1 VE NACE 87.101; omzet JUMP 8.49m pnl DROP -50% equity flat 8.13m bruto JUMP 8.88m FTE 111.6; assets/debt Unknown; FOI gap_sint_bernardus_de_panne_nbb_pdf_assets_debt_pnl_drop_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Salvator/Boterlaarhof/mined Sint-Bernardus 0445.106.274",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_sint_bernardus_de_panne_nbb_pdf_assets_debt_pnl_drop_matrix_l5",
            hierarchy_path="Vlaanderen>WestVlaanderen>DePanne>WZC_SintBernardus>NBB_PDF_assets_debt_pnl_drop",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); RIZIV/Vlaams vs dagprijs split; explanation of pnl DROP -50% (EUR40k vs YE2024 EUR80k) despite omzet JUMP +3.7%",
            why_it_matters="Medium CW shows EUR8.49m De Panne VZW WZC with profit halved while turnover rose — no balanstotaal/assets/debt published",
            priority="8",
            recipient_body="vzw Woonzorgcentrum Sint-Bernardus",
            recipient_email="info@sint-bernardus.be",
            recipient_postal="Koninklijke Baan 18, 8660 De Panne",
            draft_letter_path="docs/doge/foi/drafts/gap_sint_bernardus_de_panne_nbb_pdf_assets_debt_pnl_drop_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_sint_bernardus_de_panne_jr2025_statutory_wzc_pnl_drop_omzet_8_49m",
            linked_leaderboard_id="lb_sint_bernardus_de_panne_omzet_8_49m_pnl_drop_50pct_jr2025",
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
        row["title"] = "leftover dual — WZC Sint-Bernardus De Panne YE2025 Medium (omzet JUMP 8.49m / pnl DROP -50%)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed leftover WZC Sint-Bernardus De Panne after Boterlaarhof/Salvator race; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        )
        row["blocked_gap_id"] = "gap_sint_bernardus_de_panne_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2163 Sint-Bernardus De Panne Medium omzet JUMP 8.49m (+3.66%) bruto JUMP 8.88m pnl DROP -50% equity flat 8.13m FTE 111.6; "
            "KBO Actief VZW 1 VE De Panne; FOI info@sint-bernardus.be; next every-10 2170"
        )

if not any(x["task_id"] == "rq_2164" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2164",
            title="leftover dual hole-fill after Sint-Bernardus De Panne — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2164 after WZC Sint-Bernardus De Panne YE2025 Medium (omzet 8.49m / pnl DROP -50%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                "(optional: Residentie Oudenburg 0450.755.634 YE2025 omzet 12.9m if NACE care confirmed; "
                "WZC Foyer De Lork Hoeselt BV 0755.822.317 YE2025 empty-omzet NEG equity; Maria Boodschap Niel still YE2024). "
                "Do NOT redo WZC Sint-Bernardus De Panne 0432.582.485, Salvator Welzijnscentrum Hasselt, Boterlaarhof Deurne, "
                "Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, "
                "De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, "
                "WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, "
                "Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, "
                "Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, "
                "Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, "
                "Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, "
                "De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, "
                "Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, "
                "Rusthuis Sint Jozef Ninove, Zilverlinde Olen, mined Sint-Bernardus 0445.106.274, Home Vrijzicht Ieper."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2163 Sint-Bernardus De Panne; FARO/AIESH/REW still YE2024; next every-10 2170",
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
        notes=(
            "tick2163 leftover WZC Sint-Bernardus De Panne 0432.582.485 Medium (omzet JUMP 8.49m; pnl DROP -50%; "
            "equity flat; FTE 111.6); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2164; next every-10 2170; continuous hole_fill"
        ),
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2163")
