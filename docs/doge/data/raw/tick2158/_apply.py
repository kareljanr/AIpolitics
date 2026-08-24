# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-25T22:40:00Z"
TICK = 2158

ENTITY = "nv_seniorie_epinette_comines"
OMZET = 171456
BRUTO = 180236
PNL = -1329357
EQUITY = 1320279
FTE = 50
OMZET_PY = 168180
PNL_PY = 217479
EQUITY_PY = 2649636
BRUTO_PY = 193118


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
            source_id="src_epinette_jr2025_cw_nl",
            title="Companyweb NL Seniorie de l'Epinette YE2025 statutory",
            url="https://www.companyweb.be/nl/0447771695/seniorie-de-l-epinette",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2158; YE2025 omzet 171456 pnl LOSS -1329357 equity DROP 1320279 bruto 180236 FTE 50; neerlegging 02.04.2026; assets/debt Unknown; raw tick2158/",
        ),
        dict(
            source_id="src_epinette_jr2025_cw_en",
            title="Companyweb EN Seniorie de l'Epinette YE2025 statutory",
            url="https://www.companyweb.be/en/0447771695/seniorie-de-l-epinette",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2158; EN mirror YE2025 Medium; filed 02-04-2026; Last balance sheet year 2025; Commercial name La Serenite; FTE 50; raw tick2158/",
        ),
        dict(
            source_id="src_epinette_jr2025_cw_fr",
            title="Companyweb FR Seniorie de l'Epinette YE2025 statutory",
            url="https://www.companyweb.be/fr/0447771695",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-25",
            source_class="secondary_aggregator",
            notes="tick2158; FR mirror YE2025 Medium; Dernier bilan 2025; raw tick2158/",
        ),
        dict(
            source_id="src_epinette_kbo_2158",
            title="KBO Seniorie de l'Epinette 0447.771.695 Actief NV Comines-Warneton",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0447771695",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-25",
            source_class="official_register",
            notes="tick2158; Actief NV; commercial LA SERENITE; Steenweg op Rijsel(WAA) 36 7784 Comines-Warneton since 03.02.2026; 1 VE; NACE 87.301 ROB; KBO email empty",
        ),
        dict(
            source_id="src_epinette_emeis_contact_2158",
            title="emeis Belgium FOI channel accueil.belgique@emeis.com (Epinette/La Sérénité path)",
            url="https://emeis.be/fr/le-management-demeis-belgium",
            publisher="emeis Belgium",
            accessed_date="2026-08-25",
            source_class="official_org",
            notes="tick2158; FOI accueil.belgique@emeis.com; HQ Alsembergsesteenweg 1037 Ukkel; site phone 056/58 76 76; Dec2025 branch-cession Sérénité Comines context",
        ),
    ],
)

budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_epinette_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        "tick2158; Medium CW; omzet JUMP +1.95% vs YE2024 168180; thin residual CA after branch path",
    ),
    (
        "bud_epinette_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        "tick2158; Medium CW; bruto DROP -6.67% vs YE2024 193118",
    ),
    (
        "bud_epinette_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2158; Medium CW; pnl LOSS FLIP from YE2024 PROFIT 217479",
    ),
    (
        "bud_epinette_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2158; Medium CW; equity DROP -50.17% vs YE2024 2649636",
    ),
    (
        "bud_epinette_fte_jr2025_statutory",
        "2025",
        FTE,
        "CW social-balance FTE / Employees 50",
        "tick2158; Medium CW; assets/debt Unknown pending NBB PDF",
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
            source_id="src_epinette_jr2025_cw_en",
            confidence="medium",
            notes=notes,
        )
    )
append_csv(ROOT / "budgets.csv", budgets)

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_epinette_jr2025_statutory_mrs_pnl_loss_flip_equity_drop",
            title="Seniorie de l'Epinette YE2025 leftover dual (omzet 171k / pnl LOSS flip -1.33m / equity DROP -50%)",
            entity_id=ENTITY,
            beneficiary="MRS/ROB residents La Sérénité Comines-Warneton (emeis-path)",
            legal_basis="NV/SA ROB/MRS (KBO 0447.771.695; Actief; 1 VE; NACE 87.301; commercial LA SERENITE)",
            decision_date="2026-04-02",
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
            evaluation_url="https://www.companyweb.be/en/0447771695/seniorie-de-l-epinette",
            stated_goal="Residential elderly care Comines-Warneton (La Sérénité)",
            cut_option="Publish NBB PDF assets/debt FOI; reconcile tiny omzet vs FTE 50; disclose Dec2025 Sérénité branch-cession path and residual entity purpose",
            source_id="src_epinette_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Wallonie>Hainaut>CominesWarneton>Seniorie_Epinette>JR2025_statutory_L5",
            notes="tick2158; Medium CW; omzet primary envelope; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped opaque ZS; not TE-additive of 348bn; DISTINCT Parc de Forest / Le Hanois / Eycken Brug / Sint-Felix",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_epinette_pnl_loss_flip_1_33m_equity_drop_50pct_jr2025",
            name="Seniorie de l'Epinette pnl LOSS flip -1.33m / equity DROP -50% / omzet thin 171k (YE2025)",
            level="L5",
            type="mrs_nv_statutory",
            hierarchy_path="Wallonie>Hainaut>CominesWarneton>Seniorie_Epinette>JR2025",
            annual_cost_eur=str(OMZET),
            total_cost_eur=str(abs(PNL)),
            tco_notes="CW omzet envelope thin 171k vs FTE 50 + LOSS 1.33m + equity crater -50%; assets/debt Unknown; Dec2025 Sérénité branch-cession context — residual entity opacity",
            confidence="medium",
            source_id="src_epinette_jr2025_cw_en",
            beneficiaries="MRS/ROB clients La Sérénité Comines-Warneton",
            stated_goal="Residential elderly care Comines-Warneton",
            measured_outcome="omzet JUMP +1.95%; bruto DROP -6.67%; pnl LOSS FLIP; equity DROP -50.17%; FTE 50",
            absurdity_score="7.4",
            cost_score="3.8",
            difficulty="4.0",
            priority_index="6.55",
            cut_proposal="Publish NBB PDF assets/debt/cash FOI; map INAMI/AVI vs dagprijs; disclose branch-cession residual economics vs FTE 50",
            status="open",
            struck_reason="",
            notes="tick2158; Medium CW; FOI gap_epinette_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_branch_cession_matrix_l5; stall FARO/AIESH/REW YE2024",
        )
    ],
)

append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="Seniorie de l'Epinette (Comines-Warneton / La Sérénité)",
            name_fr="Seniorie de l'Epinette (Comines-Warneton / La Sérénité)",
            name_en="Seniorie de l'Epinette nursing home (Comines-Warneton)",
            level="parastatal",
            parent_id="sec_wallonia",
            community_language="fr",
            website="https://emeis.be/",
            foi_email="accueil.belgique@emeis.com",
            foi_postal="Steenweg op Rijsel(WAA) 36, 7784 Comines-Warneton",
            notes="tick2158 YE2025 Medium CW NL+EN+FR + Strong KBO 0447.771.695 Actief NV 1 VE NACE 87.301 commercial LA SERENITE; omzet JUMP 171k (+1.95%) bruto DROP 180k pnl LOSS FLIP -1.33m equity DROP 1.32m (-50.17%) FTE 50; assets/debt Unknown; FOI gap_epinette_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_branch_cession_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Parc de Forest/Le Hanois/Eycken Brug/Sint-Felix/Hainaut-Est; emeis-path",
        )
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_epinette_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_branch_cession_matrix_l5",
            hierarchy_path="Wallonie>Hainaut>CominesWarneton>Seniorie_Epinette>NBB_PDF_assets_debt_pnl_loss_flip_equity_drop_branch_cession",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); INAMI/AVI vs dagprijs split; explanation of pnl LOSS flip -1.33m and equity DROP -50%; reconcile omzet 171k vs FTE 50; Dec2025 Sérénité branch-cession terms and residual entity purpose",
            why_it_matters="Medium CW shows NV ROB/MRS with catastrophic LOSS flip and equity crater while omzet stays thin vs 50 FTE — likely branch-cession residual; no balanstotaal/assets/debt published",
            priority="8",
            recipient_body="Seniorie de l'Epinette NV / emeis Belgium (La Sérénité path)",
            recipient_email="accueil.belgique@emeis.com",
            recipient_postal="Steenweg op Rijsel(WAA) 36, 7784 Comines-Warneton (HQ: Alsembergsesteenweg 1037, 1180 Ukkel)",
            draft_letter_path="docs/doge/foi/drafts/gap_epinette_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_branch_cession_matrix_l5.md",
            status="ready",
            date_ready="2026-08-25",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_epinette_jr2025_statutory_mrs_pnl_loss_flip_equity_drop",
            linked_leaderboard_id="lb_epinette_pnl_loss_flip_1_33m_equity_drop_50pct_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2158; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW YE2024; site tel 056/58 76 76; next every-10 2160",
        )
    ],
)

# research_queue: close 2158, spawn 2159
with (ROOT / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames

for row in rows:
    if row["task_id"] == "rq_2158":
        row["title"] = "leftover dual — Seniorie de l'Epinette Comines YE2025 Medium (omzet 171k / pnl LOSS flip -1.33m / equity DROP -50%)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = "Completed leftover Seniorie de l'Epinette after Parc de Forest; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent."
        row["blocked_gap_id"] = "gap_epinette_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_branch_cession_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = "tick2158 Epinette Medium omzet JUMP 171k (+1.95%) bruto DROP 180k pnl LOSS FLIP -1.33m equity DROP 1.32m (-50.17%) FTE 50; KBO Actief NV 1 VE NACE 87.301 LA SERENITE Comines-Warneton; FOI accueil.belgique@emeis.com; next every-10 2160"

if not any(x["task_id"] == "rq_2159" for x in rows):
    rows.append({c: "" for c in cols})
    rows[-1].update(
        dict(
            task_id="rq_2159",
            title="leftover dual hole-fill after Epinette — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2159 after Seniorie de l'Epinette Comines YE2025 Medium (omzet 171k / pnl LOSS flip -1.33m / equity DROP -50%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros (prefer sourced € over opaque ZS FTE-only). "
                "Do NOT redo Seniorie de l'Epinette Comines-Warneton/La Sérénité, MRS Parc de Forest Ixelles/Saint-Gilles, MRS Le Hanois Fontaine-l'Évêque, WZC d'Eycken Brug Bierbeek, WZC Sint-Felix Pajottegem/Herne, Zone de secours Hainaut-Est, Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, Molenheide, Heilig Hart Grimbergen, Maria's Rustoord, Cassiers, OLV Lourdes, Vander Stokken, Hof ter Waarbeek, Sint-Carolus Ternat, Van Lierde, Sint-Augustinus Halle, WZC De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, Seniorencentrum OLV Bornem, Veilige Have."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2158 Epinette; FARO/AIESH/REW still YE2024; next every-10 2160",
        )
    )
    print("spawned rq_2159")

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
        last_unit_id="rq_2158",
        ticks_completed="2158",
        paused="no",
        notes="tick2158 leftover Seniorie de l'Epinette 0447.771.695 Medium (omzet 171k; pnl LOSS flip -1.33m; equity DROP -50%; FTE 50; Comines-Warneton LA SERENITE); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2159; next every-10 2160; continuous hole_fill",
    )
)
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=scols, lineterminator="\n")
    w.writeheader()
    w.writerows(st)

print("DONE apply tick2158")
