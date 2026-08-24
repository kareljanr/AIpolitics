# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T23:00:00Z"
TICK = 2159

ENTITY = "vzw_hertog_jan_kortenberg"
BRUTO = 4011594
PNL = 5888
EQUITY = 1070369
FTE = 51.8
BRUTO_PY = 3682990
PNL_PY = 5578
EQUITY_PY = 1064481
FTE_PY = 49.1


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
    print("append", path.name, "+", added, "total", len(existing))


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_hertog_jan_jr2025_cw_nl",
            title="Companyweb NL HERTOG JAN YE2025 statutory",
            url="https://www.companyweb.be/nl/0845895824/hertog-jan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; YE2025 bruto 4011594 pnl 5888 equity 1070369 FTE 51.8; omzet unpublished; neerlegging 25.06.2026; assets/debt Unknown; raw tick2159/",
        ),
        dict(
            source_id="src_hertog_jan_jr2025_cw_en",
            title="Companyweb EN HERTOG JAN YE2025 statutory",
            url="https://www.companyweb.be/en/0845895824/hertog-jan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; EN mirror YE2025 Medium; filed 25-06-2026; Last balance sheet year 2025; omzet not published; Gross margin 4011594; FTE 51.8; raw tick2159/",
        ),
        dict(
            source_id="src_hertog_jan_jr2025_cw_fr",
            title="Companyweb FR HERTOG JAN YE2025 statutory",
            url="https://www.companyweb.be/fr/0845895824/hertog-jan",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2159; FR mirror YE2025 Medium; Dernier bilan 2025; raw tick2159/",
        ),
        dict(
            source_id="src_hertog_jan_kbo_2159",
            title="KBO HERTOG JAN 0845.895.824 Actief VZW Kortenberg",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0845895824",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2159; Actief VZW; Leuvensesteenweg 348 3070 Kortenberg; 1 VE; NACE 87.301 ROB; KBO email empty; RSZ since 01.06.2015",
        ),
        dict(
            source_id="src_hertog_jan_site_contact_2159",
            title="Residentie Hertog Jan FOI channel info@residentiehertogjan.be",
            url="https://www.residentiehertogjan.be/",
            publisher="Residentie Hertog Jan",
            accessed_date="2026-08-25",
            source_class="official_org",
            notes="tick2159; FOI info@residentiehertogjan.be; tel 02 502 03 33; verpleging 02 307 70 80; zorgkamers/zorgflats/assistentiewoningen",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_hertog_jan_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet unpublished)",
        "tick2159; Medium CW; bruto JUMP +8.92% vs YE2024 3682990; omzet empty — bruto used as proxy envelope",
    ),
    (
        "bud_hertog_jan_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2159; Medium CW; pnl JUMP +5.55% vs YE2024 5578; thin absolute profit vs 4.01m bruto",
    ),
    (
        "bud_hertog_jan_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2159; Medium CW; equity JUMP +0.55% vs YE2024 1064481",
    ),
    (
        "bud_hertog_jan_fte_jr2025_statutory",
        "2025",
        FTE,
        "CW social-balance FTE / Employees 51.8",
        "tick2159; Medium CW; FTE JUMP vs YE2024 49.1; assets/debt Unknown pending NBB PDF",
    ),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year=year,
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id="src_hertog_jan_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_hertog_jan_jr2025_statutory_wzc_bruto_jump_omzet_empty",
            title="HERTOG JAN Kortenberg YE2025 leftover dual (bruto JUMP 4.01m / omzet empty / pnl thin 5.9k)",
            entity_id=ENTITY,
            beneficiary="WZC/ROB residents Residentie Hertog Jan Kortenberg",
            legal_basis="VZW ROB/WZC (KBO 0845.895.824; Actief; 1 VE; NACE 87.301)",
            decision_date="2026-06-25",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2025_omzet": "unpublished",
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0845895824/hertog-jan",
            stated_goal="Residential elderly care Kortenberg (zorgkamers/zorgflats/assistentiewoningen)",
            cut_option="Publish NBB PDF assets/debt/omzet FOI; map RIZIV vs dagprijs; disclose why omzet unpublished vs bruto 4.01m",
            source_id="src_hertog_jan_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Kortenberg>WZC_Hertog_Jan>JR2025_statutory_L5",
            notes="tick2159; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS; not TE-additive of 348bn; DISTINCT Epinette/Parc de Forest/Le Hanois/Eycken Brug/Sint-Felix",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_hertog_jan_bruto_4_01m_omzet_empty_pnl_thin_jr2025",
            name="HERTOG JAN Kortenberg bruto JUMP 4.01m / omzet empty / pnl thin 5.9k (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Kortenberg>WZC_Hertog_Jan>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes="CW bruto proxy (omzet unpublished); assets/debt Unknown pending NBB PDF FOI; thin pnl 5.9k vs 4.01m bruto + FTE 51.8 — CA opacity",
            confidence="medium",
            source_id="src_hertog_jan_jr2025_cw_en",
            beneficiaries="WZC/ROB clients Residentie Hertog Jan Kortenberg",
            stated_goal="Residential elderly care Kortenberg",
            measured_outcome="omzet unpublished; bruto JUMP +8.92%; pnl JUMP +5.55%; equity JUMP +0.55%; FTE JUMP 51.8 (vs 49.1)",
            absurdity_score="5.7",
            cost_score="3.6",
            difficulty="4.0",
            priority_index="5.55",
            cut_proposal="Publish NBB PDF assets/debt/cash/omzet FOI; map RIZIV vs dagprijs; disclose unpublished-omzet rationale vs bruto 4.01m",
            status="open",
            struck_reason="",
            notes="tick2159; Medium CW; FOI gap_hertog_jan_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="HERTOG JAN / Residentie Hertog Jan (Kortenberg)",
            name_fr="HERTOG JAN / Résidence Hertog Jan (Kortenberg)",
            name_en="HERTOG JAN nursing home (Kortenberg)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.residentiehertogjan.be/",
            foi_email="info@residentiehertogjan.be",
            foi_postal="Leuvensesteenweg 348, 3070 Kortenberg",
            notes="tick2159 YE2025 Medium CW NL+EN+FR + Strong KBO 0845.895.824 Actief VZW 1 VE NACE 87.301; bruto JUMP 4.01m (+8.92%) pnl JUMP 5.9k (+5.55%) equity JUMP 1.07m (+0.55%) FTE JUMP 51.8 (vs 49.1); omzet unpublished; assets/debt Unknown; FOI gap_hertog_jan_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Epinette/Parc de Forest/Le Hanois/Eycken Brug/Sint-Felix/Annuntiaten; OLV Lourdes Kortenberg already mined separate entity",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_hertog_jan_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5",
            hierarchy_path="Vlaanderen>VlaamsBrabant>Kortenberg>WZC_Hertog_Jan>NBB_PDF_assets_debt_omzet_empty_bruto_jump",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal/omzet code 70); RIZIV vs dagprijs split; explanation of unpublished omzet vs bruto 4.01m; plaatsen matrix zorgkamers/zorgflats/assistentiewoningen",
            why_it_matters="Medium CW shows VZW ROB/WZC with bruto JUMP 4.01m and FTE 51.8 but omzet unpublished and no balanstotaal/assets/debt — CA opacity vs thin pnl 5.9k",
            priority="8",
            recipient_body="HERTOG JAN vzw / Residentie Hertog Jan",
            recipient_email="info@residentiehertogjan.be",
            recipient_postal="Leuvensesteenweg 348, 3070 Kortenberg",
            draft_letter_path="docs/doge/foi/drafts/gap_hertog_jan_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_hertog_jan_jr2025_statutory_wzc_bruto_jump_omzet_empty",
            linked_leaderboard_id="lb_hertog_jan_bruto_4_01m_omzet_empty_pnl_thin_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2159; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW YE2024; site tel 02 502 03 33; next every-10 2160",
        )
    ],
)

# research_queue: close 2159, spawn 2160
with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2159":
        row["title"] = "leftover dual — HERTOG JAN Kortenberg YE2025 Medium (bruto JUMP 4.01m / omzet empty / pnl thin 5.9k)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover HERTOG JAN after Epinette; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_hertog_jan_nbb_pdf_assets_debt_omzet_empty_bruto_jump_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2159 Hertog Jan Medium bruto JUMP 4.01m (+8.92%) pnl JUMP 5.9k (+5.55%) equity JUMP 1.07m (+0.55%) FTE JUMP 51.8; omzet unpublished; KBO Actief VZW 1 VE NACE 87.301 Kortenberg; FOI info@residentiehertogjan.be; next every-10 2160"

if not any(x["task_id"] == "rq_2160" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2160",
            title="EVERY-10 leftover dual hole-fill after Hertog Jan — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2160 EVERY-10 after HERTOG JAN Kortenberg YE2025 Medium (bruto JUMP 4.01m / omzet empty / pnl thin 5.9k). "
                "MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md then hole-fill one unit. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS FTE-only). "
                "Do NOT redo HERTOG JAN Kortenberg, Seniorie de l'Epinette Comines-Warneton/La Sérénité, MRS Parc de Forest Ixelles/Saint-Gilles, MRS Le Hanois Fontaine-l'Évêque, WZC d'Eycken Brug Bierbeek, WZC Sint-Felix Pajottegem/Herne, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, Cassiers, OLV Lourdes, Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, Van Lierde, Sint-Augustinus Halle, WZC De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have, Ocura, Gravenkasteel, Kanunnik Triest, De Linde Lievegem, Huize Sint-Jozef Ieper, Rusthuis Sint Jozef Ninove."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2159 Hertog Jan; FARO/AIESH/REW still YE2024; EVERY-10 required at 2160",
        )
    )
    print("spawned rq_2160")

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
        notes="tick2159 leftover HERTOG JAN 0845.895.824 Medium (bruto JUMP 4.01m; omzet empty; pnl thin 5.9k; FTE JUMP 51.8; Kortenberg); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2160 EVERY-10; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2159")
