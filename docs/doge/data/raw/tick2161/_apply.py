# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T23:40:00Z"

ENTITY = "vzw_woonzorgnet_dijleland"
OMZET = 29365960
BRUTO = 30398232
PNL = -923158
EQUITY = 34409304
FTE = 366.1
OMZET_PY = 29054923
PNL_PY = 3354735
EQUITY_PY = 36259763
BRUTO_PY = 30312482


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
            source_id="src_wznd_jr2025_cw_nl",
            title="Companyweb NL Woonzorgnet-Dijleland YE2025 statutory",
            url="https://www.companyweb.be/nl/0500952540/woonzorgnet-dijleland",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2161; YE2025 omzet 29365960 pnl LOSS flip -923158 equity DROP 34409304 bruto 30398232 FTE 366.1; neerlegging 15.08.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_wznd_jr2025_cw_en",
            title="Companyweb EN Woonzorgnet-Dijleland YE2025 statutory",
            url="https://www.companyweb.be/en/0500952540/woonzorgnet-dijleland",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2161; EN mirror YE2025 Medium; filed 15-08-2026; FTE 366.1",
        ),
        dict(
            source_id="src_wznd_jr2025_cw_fr",
            title="Companyweb FR Woonzorgnet-Dijleland YE2025 statutory",
            url="https://www.companyweb.be/fr/0500952540",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2161; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_wznd_kbo_2161",
            title="KBO Woonzorgnet-Dijleland 0500.952.540 Actief VZW Leuven 5 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0500952540",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2161; Actief VZW; Wingerdstraat 14 3000 Leuven; 5 VE; NACE 87.101; aanbestedende overheid; KBO email empty",
        ),
        dict(
            source_id="src_wznd_foi_contact_2161",
            title="Woonzorgnet-Dijleland FOI contact info@wznd.be",
            url="https://woonzorgnet-dijleland.be/contact/",
            publisher="Woonzorgnet-Dijleland vzw",
            accessed_date="2026-08-25",
            source_class="foi_contact",
            notes="tick2161; info@wznd.be; T 016 28 47 90; Wingerdstraat 14 Leuven",
        ),
    ],
)

for bid, amount, basis, notes in [
    ("bud_wznd_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025", "tick2161; Medium CW; omzet JUMP +1.07% vs YE2024 29054923"),
    ("bud_wznd_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", "tick2161; Medium CW; bruto JUMP +0.28% vs YE2024 30312482"),
    ("bud_wznd_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025", "tick2161; Medium CW; pnl LOSS FLIP from YE2024 PROFIT 3354735"),
    ("bud_wznd_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", "tick2161; Medium CW; equity DROP -5.10% vs YE2024 36259763"),
    ("bud_wznd_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 366.1", "tick2161; Medium CW; assets/debt Unknown; 5 VE Vlaams-Brabant"),
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
                source_id="src_wznd_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_wznd_jr2025_statutory_wzc_pnl_loss_flip_omzet_29m",
            title="Woonzorgnet-Dijleland YE2025 leftover dual (omzet JUMP 29.37m / pnl LOSS flip -923k / FTE 366)",
            entity_id=ENTITY,
            beneficiary="WZC residents Vlaams-Brabant (Ter Meeren / Keyhof / other VE)",
            legal_basis="VZW RVT (KBO 0500.952.540; Actief; 5 VE; NACE 87.101; aanbestedende overheid)",
            decision_date="2026-08-15",
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
                    "ve": 5,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0500952540/woonzorgnet-dijleland",
            stated_goal="Multi-site residential elderly care Vlaams-Brabant (Woonzorgnet-Dijleland)",
            cut_option="Publish NBB PDF assets/debt FOI; per-site 5-VE P&L matrix; explain LOSS flip after YE2024 profit 3.35m",
            source_id="src_wznd_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>WoonzorgnetDijleland>JR2025_statutory_L5",
            notes="tick2161; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; deferred after Foyer De Lork EVERY-10; not TE-additive of 348bn; DISTINCT Foyer De Lork/Lindeboom/HERTOG JAN/OLV Kempen",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_wznd_omzet_29m_pnl_loss_flip_923k_jr2025",
            name="Woonzorgnet-Dijleland omzet JUMP 29.37m / pnl LOSS flip -923k / equity DROP -5% (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>WoonzorgnetDijleland>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 29.37m / 5 VE / 366 FTE aanbestedende; pnl LOSS flip after YE2024 profit 3.35m; equity DROP -5%; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id="src_wznd_jr2025_cw_en",
            beneficiaries="WZC clients Vlaams-Brabant (Ter Meeren/Keyhof/other)",
            stated_goal="Multi-site residential elderly care Vlaams-Brabant",
            measured_outcome="omzet JUMP +1.07%; bruto JUMP +0.28%; pnl LOSS FLIP; equity DROP -5.10%; FTE 366.1",
            absurdity_score="6.8",
            cost_score="5.5",
            difficulty="4.0",
            priority_index="6.0",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; 5-VE P&L matrix; disclose LOSS flip path after large YE2024 profit",
            status="open",
            struck_reason="",
            notes="tick2161; Medium CW; FOI gap_wznd_nbb_pdf_assets_debt_pnl_loss_flip_persite_matrix_l5; stall FARO/AIESH/REW YE2024; preferred deferred after Foyer De Lork",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Woonzorgnet-Dijleland VZW (Leuven / Ter Meeren+Keyhof)",
            name_fr="Woonzorgnet-Dijleland ASBL (Leuven)",
            name_en="Woonzorgnet-Dijleland nursing-home network (Leuven)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://woonzorgnet-dijleland.be/",
            foi_email="info@wznd.be",
            foi_postal="Wingerdstraat 14, 3000 Leuven",
            notes="tick2161 YE2025 Medium CW NL+EN+FR + Strong KBO 0500.952.540 Actief VZW 5 VE aanbestedende overheid NACE 87.101; omzet JUMP 29.37m pnl LOSS FLIP -923k equity DROP 34.41m bruto JUMP 30.40m FTE 366.1; assets/debt Unknown; FOI gap_wznd_nbb_pdf_assets_debt_pnl_loss_flip_persite_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Foyer De Lork/Lindeboom/HERTOG JAN/OLV Kempen Ravels",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_wznd_nbb_pdf_assets_debt_pnl_loss_flip_persite_matrix_l5",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Leuven>WoonzorgnetDijleland>NBB_PDF_assets_debt_pnl_loss_flip_persite",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); per-site P&L across 5 VE (Ter Meeren/Keyhof/other); RIZIV/Vlaams vs dagprijs split; explanation of pnl LOSS flip -923k after YE2024 profit 3.35m and equity DROP -5%",
            why_it_matters="Medium CW shows EUR29.37m aanbestedende VZW zorgnetwerk with dramatic LOSS flip from large prior-year profit — no balanstotaal/assets/debt or per-site matrix published",
            priority="8",
            recipient_body="vzw Woonzorgnet-Dijleland",
            recipient_email="info@wznd.be",
            recipient_postal="Wingerdstraat 14, 3000 Leuven",
            draft_letter_path="docs/doge/foi/drafts/gap_wznd_nbb_pdf_assets_debt_pnl_loss_flip_persite_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_wznd_jr2025_statutory_wzc_pnl_loss_flip_omzet_29m",
            linked_leaderboard_id="lb_wznd_omzet_29m_pnl_loss_flip_923k_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2161; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2161":
        row["title"] = "leftover dual — Woonzorgnet-Dijleland YE2025 Medium (omzet JUMP 29.37m / pnl LOSS flip -923k / FTE 366)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover Woonzorgnet-Dijleland after Foyer De Lork EVERY-10; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_wznd_nbb_pdf_assets_debt_pnl_loss_flip_persite_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2161 WZND Medium omzet JUMP 29.37m (+1.07%) bruto JUMP 30.40m pnl LOSS FLIP -923k equity DROP 34.41m (-5.10%) FTE 366.1; KBO Actief VZW 5 VE Leuven aanbestedende; FOI info@wznd.be; next every-10 2170"

if not any(x["task_id"] == "rq_2162" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2162",
            title="leftover dual hole-fill after WZND — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2162 after Woonzorgnet-Dijleland YE2025 Medium (omzet 29.37m / pnl LOSS flip -923k). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS). "
                "Do NOT redo Woonzorgnet-Dijleland, Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, Rusthuis Sint Jozef Ninove, Hof ter Lande if taken."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2161 WZND; FARO/AIESH/REW still YE2024; next every-10 2170",
        )
    )
    print("spawned rq_2162")

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
        last_unit_id="rq_2161",
        ticks_completed="2161",
        paused="no",
        notes="tick2161 leftover Woonzorgnet-Dijleland 0500.952.540 Medium (omzet JUMP 29.37m; pnl LOSS flip -923k; equity DROP -5%; FTE 366; 5 VE Leuven); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2162; next every-10 2170; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2161")
