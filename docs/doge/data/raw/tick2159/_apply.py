# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T23:00:00Z"

ENTITY = "vzw_de_lindeboom_knokke"
OMZET = 25261224
BRUTO = 22613680
PNL = -170090
EQUITY = 26648267
FTE = 290.9
OMZET_PY = 25389920
PNL_PY = 1208976
EQUITY_PY = 26930872
BRUTO_PY = 23902697


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
            source_id="src_lindeboom_jr2025_cw_nl",
            title="Companyweb NL De Lindeboom VZW YE2025 statutory",
            url="https://www.companyweb.be/nl/0435015702",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; YE2025 omzet 25261224 pnl LOSS -170090 equity 26648267 bruto 22613680 FTE 290.9; neerlegging 31.07.2026; assets/debt Unknown; raw tick2159/",
        ),
        dict(
            source_id="src_lindeboom_jr2025_cw_en",
            title="Companyweb EN De Lindeboom ASBL YE2025 statutory",
            url="https://www.companyweb.be/en/0435015702",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; EN mirror YE2025 Medium; filed 31-07-2026; Last balance sheet year 2025; FTE 290.9; raw tick2159/",
        ),
        dict(
            source_id="src_lindeboom_jr2025_cw_fr",
            title="Companyweb FR De Lindeboom ASBL YE2025 statutory",
            url="https://www.companyweb.be/fr/0435015702",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; FR mirror YE2025 Medium; Dernier bilan 2025; raw tick2159/",
        ),
        dict(
            source_id="src_lindeboom_kbo_2159",
            title="KBO De Lindeboom 0435.015.702 Actief VZW Knokke-Heist",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0435015702",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2159; Actief VZW; Bremlaan 5 8300 Knokke-Heist; 8 VE; NACE 87.301/87.101; aanbestedende overheid; email info@lindeboom.be; www.lindeboom.be",
        ),
        dict(
            source_id="src_lindeboom_site_foi_2159",
            title="De Lindeboom official site + OLVO FOI contacts",
            url="https://lindeboom.be/",
            publisher="vzw De Lindeboom",
            accessed_date="2026-08-25",
            source_class="official_org",
            notes="tick2159; FOI info@lindeboom.be; OLVO wzc.olvo@lindeboom.be; Lindenhove onthaal@lindeboom.be; OLVO Kursaalstraat under heightened supervision/intake ban press context",
        ),
    ],
)

budgets = []
for bid, amount, basis, notes in [
    (
        "bud_lindeboom_omzet_jr2025_statutory",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2159; Medium CW; omzet DROP -0.51% vs YE2024 25389920",
    ),
    (
        "bud_lindeboom_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2159; Medium CW; bruto DROP -5.39% vs YE2024 23902697",
    ),
    (
        "bud_lindeboom_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2159; Medium CW; pnl LOSS FLIP from YE2024 PROFIT 1208976",
    ),
    (
        "bud_lindeboom_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2159; Medium CW; equity DROP -1.05% vs YE2024 26930872",
    ),
    (
        "bud_lindeboom_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees 290.9",
        "tick2159; Medium CW; assets/debt Unknown pending NBB PDF; 8 VE multi-site Knokke-Heist",
    ),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year="2025",
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id="src_lindeboom_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_lindeboom_jr2025_statutory_wzc_pnl_loss_flip_omzet_25m",
            title="De Lindeboom Knokke YE2025 leftover dual (omzet 25.26m / pnl LOSS flip -170k / FTE 290.9)",
            entity_id=ENTITY,
            beneficiary="WZC residents Knokke-Heist multi-site (OLVO / Lindenhove / other VE)",
            legal_basis="VZW RVT/ROB (KBO 0435.015.702; Actief; 8 VE; NACE 87.101/87.301; aanbestedende overheid)",
            decision_date="2026-07-31",
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
            evaluation_url="https://www.companyweb.be/en/0435015702",
            stated_goal="Multi-site residential elderly care Knokke-Heist (De Lindeboom)",
            cut_option="Publish NBB PDF assets/debt FOI; per-site OLVO vs Lindenhove P&L split; disclose supervision/intake-ban cost path",
            source_id="src_lindeboom_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>WestVlaanderen>KnokkeHeist>DeLindeboom>JR2025_statutory_L5",
            notes="tick2159; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLVO heightened supervision press context; not TE-additive of 348bn; DISTINCT Epinette / Parc de Forest / Le Hanois / Eycken Brug / Sint-Felix",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_lindeboom_omzet_25m_pnl_loss_flip_olvo_supervision_jr2025",
            name="De Lindeboom omzet 25.26m / pnl LOSS flip -170k / OLVO supervision dual (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>WestVlaanderen>KnokkeHeist>DeLindeboom>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(OMZET),
            tco_notes="CW omzet envelope 25.26m multi-site VZW; pnl LOSS flip after YE2024 profit 1.21m; assets/debt Unknown; OLVO Kursaalstraat under heightened supervision/intake ban — quality+finance opacity",
            confidence="medium",
            source_id="src_lindeboom_jr2025_cw_en",
            beneficiaries="WZC clients Knokke-Heist (OLVO/Lindenhove/other VE)",
            stated_goal="Multi-site residential elderly care Knokke-Heist",
            measured_outcome="omzet DROP -0.51%; bruto DROP -5.39%; pnl LOSS FLIP; equity DROP -1.05%; FTE 290.9",
            absurdity_score="6.6",
            cost_score="6.8",
            difficulty="4.0",
            priority_index="6.45",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; per-site P&L matrix; disclose Departement Zorg supervision remediation TCO",
            status="open",
            struck_reason="",
            notes="tick2159; Medium CW; FOI gap_lindeboom_nbb_pdf_assets_debt_pnl_loss_flip_olvo_supervision_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="De Lindeboom VZW (Knokke-Heist / OLVO+Lindenhove)",
            name_fr="De Lindeboom ASBL (Knokke-Heist)",
            name_en="De Lindeboom nursing-home group (Knokke-Heist)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://lindeboom.be/",
            foi_email="info@lindeboom.be",
            foi_postal="Bremlaan 5, 8300 Knokke-Heist",
            notes="tick2159 YE2025 Medium CW NL+EN+FR + Strong KBO 0435.015.702 Actief VZW 8 VE aanbestedende overheid NACE 87.101/87.301; omzet DROP 25.26m pnl LOSS FLIP -170k equity DROP 26.65m bruto DROP 22.61m FTE 290.9; assets/debt Unknown; FOI gap_lindeboom_nbb_pdf_assets_debt_pnl_loss_flip_olvo_supervision_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Epinette/Parc de Forest/Le Hanois/Eycken Brug/Sint-Felix; OLVO VE Kursaalstraat 42",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_lindeboom_nbb_pdf_assets_debt_pnl_loss_flip_olvo_supervision_matrix_l5",
            hierarchy_path="Vlaanderen>WestVlaanderen>KnokkeHeist>DeLindeboom>NBB_PDF_assets_debt_pnl_loss_flip_olvo_supervision",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); per-site P&L (OLVO vs Lindenhove vs other VE); RIZIV/Vlaams vs dagprijs split; explanation of pnl LOSS flip -170k after YE2024 profit 1.21m; Departement Zorg heightened-supervision / intake-ban cost and remediation spend",
            why_it_matters="Medium CW shows 25.26m multi-site aanbestedende VZW with LOSS flip and OLVO under public quality sanctions — no balanstotaal/assets/debt or per-site matrix published",
            priority="8",
            recipient_body="vzw De Lindeboom",
            recipient_email="info@lindeboom.be",
            recipient_postal="Bremlaan 5, 8300 Knokke-Heist",
            draft_letter_path="docs/doge/foi/drafts/gap_lindeboom_nbb_pdf_assets_debt_pnl_loss_flip_olvo_supervision_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_lindeboom_jr2025_statutory_wzc_pnl_loss_flip_omzet_25m",
            linked_leaderboard_id="lb_lindeboom_omzet_25m_pnl_loss_flip_olvo_supervision_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2159; ready NOT sent; Medium CW + Strong KBO; cc wzc.olvo@lindeboom.be; preferred stall FARO/AIESH/REW YE2024; next every-10 2160",
        )
    ],
)

with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2159":
        row["title"] = "leftover dual — De Lindeboom Knokke YE2025 Medium (omzet 25.26m / pnl LOSS flip -170k / OLVO supervision)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover De Lindeboom after Epinette; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_lindeboom_nbb_pdf_assets_debt_pnl_loss_flip_olvo_supervision_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2159 Lindeboom Medium omzet DROP 25.26m (-0.51%) bruto DROP 22.61m pnl LOSS FLIP -170k equity DROP 26.65m FTE 290.9; KBO Actief VZW 8 VE Knokke-Heist aanbestedende; FOI info@lindeboom.be; OLVO supervision context; next every-10 2160"

if not any(x["task_id"] == "rq_2160" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2160",
            title="EVERY-10 + leftover dual hole-fill after Lindeboom — prefer AGB/FARO-YE2025/AIESH-REW/unused",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2160 EVERY-10 (refresh progress_every_10_ticks.md + doge_waste_top10_current.md) after De Lindeboom Knokke YE2025 Medium (omzet 25.26m / pnl LOSS flip). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS FTE-only). "
                "Do NOT redo De Lindeboom Knokke-Heist/OLVO/Lindenhove, Seniorie de l'Epinette Comines-Warneton/La Sérénité, MRS Parc de Forest Ixelles/Saint-Gilles, MRS Le Hanois Fontaine-l'Évêque, WZC d'Eycken Brug Bierbeek, WZC Sint-Felix Pajottegem/Herne, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, Cassiers, OLV Lourdes, Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, Van Lierde, Sint-Augustinus Halle, WZC De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2159 Lindeboom; EVERY-10 due; FARO/AIESH/REW still YE2024; next every-10 after this is 2170",
        )
    )
    print("spawned rq_2160 EVERY-10")

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
        last_unit_id="rq_2159",
        ticks_completed="2159",
        paused="no",
        notes="tick2159 leftover De Lindeboom 0435.015.702 Medium (omzet 25.26m; pnl LOSS flip -170k; FTE 290.9; 8 VE Knokke-Heist; OLVO supervision); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2160 EVERY-10; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2159")
