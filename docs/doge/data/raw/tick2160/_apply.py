# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T23:20:00Z"

ENTITY = "vzw_foyer_de_lork_geel"
OMZET = 153485994
BRUTO = 108293805
PNL = -1743649
EQUITY = 10310740
FTE = 1540.9
OMZET_PY = 143067120
PNL_PY = -3476500
EQUITY_PY = 12143144
BRUTO_PY = 102574482


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
            source_id="src_lork_jr2025_cw_nl",
            title="Companyweb NL Foyer De Lork YE2025 statutory",
            url="https://www.companyweb.be/nl/0446022331/foyer-de-lork",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160 EVERY-10; YE2025 omzet 153485994 pnl LOSS -1743649 equity DROP 10310740 bruto 108293805 FTE 1540.9; neerlegging 28.07.2026; assets/debt Unknown",
        ),
        dict(
            source_id="src_lork_jr2025_cw_en",
            title="Companyweb EN Foyer De Lork YE2025 statutory",
            url="https://www.companyweb.be/en/0446022331",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160 EVERY-10; EN mirror YE2025 Medium; filed 28-07-2026; Last balance sheet year 2025; FTE 1540.9",
        ),
        dict(
            source_id="src_lork_jr2025_cw_fr",
            title="Companyweb FR Foyer De Lork YE2025 statutory",
            url="https://www.companyweb.be/fr/0446022331",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160 EVERY-10; FR mirror YE2025 Medium; Dernier bilan 2025",
        ),
        dict(
            source_id="src_lork_kbo_2160",
            title="KBO Foyer De Lork 0446.022.331 Actief VZW Geel 34 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0446022331",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2160; Actief VZW; Hazenhout 1 bus D 2440 Geel; 34 VE; NACE 87.101/87.301; KBO email/web empty",
        ),
        dict(
            source_id="src_lork_foi_contact_2160",
            title="Foyer De Lork FOI channel (info@foyerdelork.be conventional + tel 014/25 77 25)",
            url="https://www.companyweb.be/en/0446022331",
            publisher="Foyer De Lork / public directories",
            accessed_date="2026-08-25",
            source_class="foi_contact",
            notes="tick2160; KBO email empty; official site SSL/503 at tick; FOI info@foyerdelork.be conventional; tel 014 25 77 25 (directory)",
        ),
    ],
)

for bid, amount, basis, notes in [
    ("bud_lork_omzet_jr2025_statutory", OMZET, "CW statutory omzet / Turnover YE2025", "tick2160; Medium CW; omzet JUMP +7.28% vs YE2024 143067120"),
    ("bud_lork_bruto_jr2025_statutory", BRUTO, "CW statutory bruto_marge / Gross margin YE2025", "tick2160; Medium CW; bruto JUMP +5.58% vs YE2024 102574482"),
    ("bud_lork_pnl_jr2025_statutory", PNL, "CW statutory winst / Profit-Loss after tax YE2025", "tick2160; Medium CW; pnl LOSS narrowed vs YE2024 LOSS -3476500"),
    ("bud_lork_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen / Equity YE2025", "tick2160; Medium CW; equity DROP -15.09% vs YE2024 12143144"),
    ("bud_lork_fte_jr2025_statutory", FTE, "CW social-balance FTE / Employees 1540.9", "tick2160; Medium CW; assets/debt Unknown; 34 VE Limburg-belt"),
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
                source_id="src_lork_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_lork_jr2025_statutory_wzc_omzet_153m_pnl_loss",
            title="Foyer De Lork YE2025 leftover dual (omzet JUMP 153.5m / pnl LOSS -1.74m / FTE 1541)",
            entity_id=ENTITY,
            beneficiary="WZC/GAW residents across 34 VE Limburg-belt (Geel HQ)",
            legal_basis="VZW RVT/ROB (KBO 0446.022.331; Actief; 34 VE; NACE 87.101/87.301)",
            decision_date="2026-07-28",
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
                    "ve": 34,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0446022331",
            stated_goal="Multi-site residential elderly care Limburg-belt (Foyer De Lork)",
            cut_option="Publish NBB PDF assets/debt FOI; per-site 34-VE P&L matrix; explain sustained LOSS + equity crater despite omzet JUMP",
            source_id="src_lork_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Limburg>Geel>FoyerDeLork>JR2025_statutory_L5",
            notes="tick2160 EVERY-10; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Lindeboom/Epinette/HERTOG JAN/Parc de Forest",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_lork_omzet_153m_pnl_loss_1_74m_equity_drop_jr2025",
            name="Foyer De Lork omzet JUMP 153.5m / pnl LOSS -1.74m / equity DROP -15% (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>Limburg>Geel>FoyerDeLork>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 153.5m / 34 VE / 1541 FTE; sustained LOSS path (narrowed vs YE2024 -3.48m); equity DROP -15%; assets/debt Unknown pending NBB PDF",
            confidence="medium",
            source_id="src_lork_jr2025_cw_en",
            beneficiaries="WZC/GAW clients Limburg-belt (34 VE)",
            stated_goal="Multi-site residential elderly care Limburg-belt",
            measured_outcome="omzet JUMP +7.28%; bruto JUMP +5.58%; pnl LOSS narrowed; equity DROP -15.09%; FTE 1540.9",
            absurdity_score="6.8",
            cost_score="7.5",
            difficulty="4.0",
            priority_index="7.1",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; 34-VE P&L matrix; disclose LOSS/equity remediation path",
            status="open",
            struck_reason="",
            notes="tick2160 EVERY-10; Medium CW; FOI gap_foyer_de_lork_nbb_pdf_assets_debt_pnl_loss_equity_drop_persite_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Foyer De Lork VZW (Geel / Limburg-belt WZC+GAW)",
            name_fr="Foyer De Lork ASBL (Geel)",
            name_en="Foyer De Lork nursing-home group (Geel)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.foyerdelork.be/",
            foi_email="info@foyerdelork.be",
            foi_postal="Hazenhout 1 bus D, 2440 Geel",
            notes="tick2160 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0446.022.331 Actief VZW 34 VE NACE 87.101/87.301; omzet JUMP 153.5m pnl LOSS -1.74m equity DROP 10.3m bruto JUMP 108.3m FTE 1540.9; assets/debt Unknown; FOI gap_foyer_de_lork_nbb_pdf_assets_debt_pnl_loss_equity_drop_persite_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Lindeboom/Epinette/HERTOG JAN",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_foyer_de_lork_nbb_pdf_assets_debt_pnl_loss_equity_drop_persite_matrix_l5",
            hierarchy_path="Vlaanderen>Limburg>Geel>FoyerDeLork>NBB_PDF_assets_debt_pnl_loss_equity_drop_persite",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); per-site P&L across 34 VE; RIZIV/Vlaams vs dagprijs split; explanation of sustained LOSS path and equity DROP -15% despite omzet JUMP +7.3%",
            why_it_matters="Medium CW shows EUR153.5m multi-site VZW zorgkoepel with second consecutive LOSS year and equity crater — no balanstotaal/assets/debt or per-site matrix published",
            priority="8",
            recipient_body="vzw Foyer De Lork",
            recipient_email="info@foyerdelork.be",
            recipient_postal="Hazenhout 1 bus D, 2440 Geel",
            draft_letter_path="docs/doge/foi/drafts/gap_foyer_de_lork_nbb_pdf_assets_debt_pnl_loss_equity_drop_persite_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_lork_jr2025_statutory_wzc_omzet_153m_pnl_loss",
            linked_leaderboard_id="lb_lork_omzet_153m_pnl_loss_1_74m_equity_drop_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2160 EVERY-10; ready NOT sent; Medium CW + Strong KBO; KBO email empty / site 503; conventional info@; tel 014/25 77 25; next every-10 2170",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2160":
        row["title"] = "EVERY-10 + leftover dual — Foyer De Lork YE2025 Medium (omzet JUMP 153.5m / pnl LOSS -1.74m / FTE 1541)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed EVERY-10 progress+top10 + leftover Foyer De Lork after Lindeboom/Hertog race; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_foyer_de_lork_nbb_pdf_assets_debt_pnl_loss_equity_drop_persite_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2160 EVERY-10 Foyer De Lork Medium omzet JUMP 153.5m (+7.28%) bruto JUMP 108.3m pnl LOSS -1.74m (narrowed) equity DROP 10.3m (-15%) FTE 1540.9; KBO Actief VZW 34 VE Geel; FOI info@foyerdelork.be; progress+top10 refreshed; next every-10 2170"

if not any(x["task_id"] == "rq_2161" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2161",
            title="leftover dual hole-fill after Foyer De Lork EVERY-10 — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2161 after Foyer De Lork YE2025 EVERY-10 Medium (omzet 153.5m / pnl LOSS -1.74m). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS (prefer Woonzorgnet-Dijleland 0500.952.540 YE2025 live if still unused) /hospital/psych/creche/disability with live euros. "
                "Do NOT redo Foyer De Lork Geel, HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, Rusthuis Sint Jozef Ninove."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2160 Foyer De Lork EVERY-10; WZND YE2025 deferred live unused; FARO/AIESH/REW still YE2024; next every-10 2170",
        )
    )
    print("spawned rq_2161")

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
        last_unit_id="rq_2160",
        ticks_completed="2160",
        paused="no",
        notes="tick2160 EVERY-10 Foyer De Lork 0446.022.331 Medium (omzet JUMP 153.5m; pnl LOSS -1.74m; equity DROP -15%; FTE 1541; 34 VE Geel); progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2161; next every-10 2170; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2160")
