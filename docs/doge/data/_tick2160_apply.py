# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
TS = "2026-08-25T23:20:00Z"
TICK = 2160

ENTITY = "vzw_olv_kempen_ravels"
OMZET = 8918056
BRUTO = 7548680
PNL = -149810
EQUITY = 7242263
FTE = 90.6
OMZET_PY = 7646690
BRUTO_PY = 6424146
PNL_PY = -570269
EQUITY_PY = 7432597
FTE_PY = 81.1


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
            source_id="src_olv_kempen_jr2025_cw_nl",
            title="Companyweb NL Home OLV van de Kempen YE2025 statutory",
            url="https://www.companyweb.be/nl/0433440342/home-o-l-vrouw-van-de-kempen",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160; YE2025 omzet 8918056 pnl LOSS -149810 equity 7242263 bruto 7548680 FTE 90.6; neerlegging 17.07.2026; assets/debt Unknown; raw tick2160/",
        ),
        dict(
            source_id="src_olv_kempen_jr2025_cw_en",
            title="Companyweb EN Home OLV van de Kempen YE2025 statutory",
            url="https://www.companyweb.be/en/0433440342/home-o-l-vrouw-van-de-kempen",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160; EN mirror YE2025 Medium; filed 17-07-2026; Last balance sheet year 2025; Big 90.6 FTE; raw tick2160/",
        ),
        dict(
            source_id="src_olv_kempen_jr2025_cw_fr",
            title="Companyweb FR Home OLV van de Kempen YE2025 statutory",
            url="https://www.companyweb.be/fr/0433440342",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2160; FR mirror YE2025 Medium; Dernier bilan 2025; raw tick2160/",
        ),
        dict(
            source_id="src_olv_kempen_kbo_2160",
            title="KBO Home O.-L.-Vrouw van de Kempen 0433.440.342 Actief VZW Ravels",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0433440342",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2160; Actief VZW; O.L.Vrouwstraat 3 2380 Ravels; 1 VE; NACE ROB 87.301 class; sinds 05.03.1987",
        ),
        dict(
            source_id="src_olv_kempen_site_contact_2160",
            title="WZC Ravels site contact info@wzc-ravels.be FOI channel",
            url="https://www.wzc-ravels.be/contact",
            publisher="WZC Home OLV van de Kempen",
            accessed_date="2026-08-25",
            source_class="official_org",
            notes="tick2160; FOI info@wzc-ravels.be; tel 014 65 85 63; Onze-Lieve-Vrouwstraat 1-5 2380 Ravels",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_olv_kempen_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2160; Medium CW; omzet JUMP +16.63% vs YE2024 7646690",
    ),
    (
        "bud_olv_kempen_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2160; Medium CW; bruto JUMP +17.5% vs YE2024 6424146",
    ),
    (
        "bud_olv_kempen_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2160; Medium CW; pnl LOSS NARROW from YE2024 LOSS -570269 (improvement +73.73%)",
    ),
    (
        "bud_olv_kempen_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2160; Medium CW; equity DROP -2.56% vs YE2024 7432597",
    ),
    (
        "bud_olv_kempen_fte_jr2025_statutory",
        "2025",
        FTE,
        "CW social-balance FTE / Employees 90.6",
        "tick2160; Medium CW; FTE JUMP vs YE2024 81.1; assets/debt Unknown pending NBB PDF",
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
            source_id="src_olv_kempen_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_olv_kempen_jr2025_statutory_wzc_omzet_jump_pnl_loss_narrow",
            title="Home OLV van de Kempen Ravels YE2025 leftover dual (omzet JUMP 8.92m / pnl LOSS narrow -150k / FTE JUMP 90.6)",
            entity_id=ENTITY,
            beneficiary="WZC/ROB residents Home OLV van de Kempen Ravels",
            legal_basis="VZW/ASBL ROB (KBO 0433.440.342; Actief; 1 VE; NACE 87.301 class)",
            decision_date="2026-07-17",
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
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0433440342/home-o-l-vrouw-van-de-kempen",
            stated_goal="Residential elderly care Ravels (Home OLV van de Kempen)",
            cut_option="Publish NBB PDF assets/debt FOI; map RIZIV/zorgkas vs dagprijs; explain LOSS despite omzet+FTE JUMP",
            source_id="src_olv_kempen_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>Ravels>WZC_OLV_Kempen>JR2025_statutory_L5",
            notes="tick2160 EVERY-10; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Hof ter Lande YE2024 probed unused; not TE-additive of 348bn; DISTINCT Hertog Jan/Lindeboom/Epinette/Parc de Forest/Le Hanois",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_olv_kempen_omzet_jump_8_92m_pnl_loss_narrow_jr2025",
            name="Home OLV Kempen Ravels omzet JUMP 8.92m / pnl LOSS narrow -150k / FTE JUMP 90.6 (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>Ravels>WZC_OLV_Kempen>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(abs(PNL)),
            tco_notes="CW omzet envelope 8.92m JUMP +16.6% with continued LOSS -150k (narrowed from -570k) + FTE JUMP 90.6; assets/debt Unknown",
            confidence="medium",
            source_id="src_olv_kempen_jr2025_cw_en",
            beneficiaries="WZC/ROB clients Home OLV van de Kempen Ravels",
            stated_goal="Residential elderly care Ravels",
            measured_outcome="omzet JUMP +16.63%; bruto JUMP +17.5%; pnl LOSS NARROW; equity DROP -2.56%; FTE JUMP 90.6",
            absurdity_score="6.8",
            cost_score="3.8",
            difficulty="4.0",
            priority_index="5.07",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; map RIZIV/zorgkas vs dagprijs; explain LOSS path despite growth",
            status="open",
            struck_reason="",
            notes="tick2160 EVERY-10; Medium CW; FOI gap_olv_kempen_nbb_pdf_assets_debt_pnl_loss_narrow_omzet_jump_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Home O.-L.-Vrouw van de Kempen (Ravels / WZC OLV van de Kempen)",
            name_fr="Home O.-L.-Vrouw van de Kempen (Ravels)",
            name_en="Home OLV van de Kempen nursing home (Ravels)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://www.wzc-ravels.be/",
            foi_email="info@wzc-ravels.be",
            foi_postal="Onze-Lieve-Vrouwstraat 1-5, 2380 Ravels",
            notes="tick2160 YE2025 Medium CW NL+EN+FR + Strong KBO 0433.440.342 Actief VZW 1 VE ROB; omzet JUMP 8.92m (+16.63%) bruto JUMP 7.55m pnl LOSS NARROW -150k equity DROP 7.24m FTE JUMP 90.6; assets/debt Unknown; FOI gap_olv_kempen_nbb_pdf_assets_debt_pnl_loss_narrow_omzet_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Hertog Jan/Lindeboom/Epinette/Parc/Hanois",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_olv_kempen_nbb_pdf_assets_debt_pnl_loss_narrow_omzet_jump_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>Ravels>WZC_OLV_Kempen>NBB_PDF_assets_debt_pnl_loss_narrow_omzet_jump",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); RIZIV/zorgkas vs dagprijs split; explanation of continued LOSS -150k despite omzet JUMP +16.6% and FTE JUMP to 90.6; plaatsen matrix",
            why_it_matters="Medium CW shows VZW ROB/WZC with strong omzet/FTE growth while LOSS persists and no balanstotaal/assets/debt published — material dual residual",
            priority="8",
            recipient_body="Home O.-L.-Vrouw van de Kempen vzw / WZC Home OLV van de Kempen Ravels",
            recipient_email="info@wzc-ravels.be",
            recipient_postal="Onze-Lieve-Vrouwstraat 1-5, 2380 Ravels",
            draft_letter_path="docs/doge/foi/drafts/gap_olv_kempen_nbb_pdf_assets_debt_pnl_loss_narrow_omzet_jump_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_olv_kempen_jr2025_statutory_wzc_omzet_jump_pnl_loss_narrow",
            linked_leaderboard_id="lb_olv_kempen_omzet_jump_8_92m_pnl_loss_narrow_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2160 EVERY-10; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW YE2024; site tel 014 65 85 63; next every-10 2170",
        )
    ],
)

# research_queue: close 2160, spawn 2161
with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2160":
        row["title"] = (
            "EVERY-10 + leftover dual — Home OLV van de Kempen Ravels YE2025 Medium "
            "(omzet JUMP 8.92m / pnl LOSS narrow -150k)"
        )
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover Home OLV van de Kempen after Hertog Jan/Lindeboom; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024 / Hof ter Lande YE2024; "
            "Medium CW YE2025 + Strong KBO; FOI ready not sent."
        )
        row["blocked_gap_id"] = (
            "gap_olv_kempen_nbb_pdf_assets_debt_pnl_loss_narrow_omzet_jump_matrix_l5"
        )
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2160 EVERY-10 OLV Kempen Medium omzet JUMP 8.92m (+16.63%) bruto JUMP 7.55m "
            "pnl LOSS NARROW -150k equity DROP 7.24m FTE JUMP 90.6; KBO Actief VZW 1 VE Ravels; "
            "FOI info@wzc-ravels.be; next every-10 2170"
        )

if not any(x["task_id"] == "rq_2161" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2161",
            title="leftover dual hole-fill after OLV Kempen — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2161 after Home OLV van de Kempen Ravels YE2025 Medium (omzet JUMP 8.92m / pnl LOSS narrow -150k). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS FTE-only). "
                "Do NOT redo Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, De Lindeboom Knokke, Seniorie de l'Epinette Comines, "
                "MRS Parc de Forest Ixelles/Saint-Gilles, MRS Le Hanois Fontaine-l'Évêque, WZC d'Eycken Brug Bierbeek, "
                "WZC Sint-Felix Pajottegem/Herne, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, "
                "WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, "
                "Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, "
                "Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, Hof ter Lande Vorselaar (YE2024-only), "
                "AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, "
                "OLV Lourdes Kortenberg, De Linde Lievegem, Huize Sint-Jozef Ieper, Rusthuis Sint Jozef Ninove."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2160 EVERY-10 OLV Kempen; FARO/AIESH/REW still YE2024; next every-10 2170",
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
        notes=(
            "tick2160 EVERY-10 leftover Home OLV van de Kempen 0433.440.342 Medium "
            "(omzet JUMP 8.92m; pnl LOSS narrow -150k; FTE JUMP 90.6; Ravels); "
            "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2161; next every-10 2170; continuous hole_fill"
        ),
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2160")
