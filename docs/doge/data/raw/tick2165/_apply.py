# -*- coding: utf-8 -*-
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"docs/doge/data")
TS = "2026-08-26T01:00:00Z"

ENTITY = "vzw_t_hofke_puurs"
BRUTO = 7664
PNL = -87076
EQUITY = -559511
FTE = 0
BRUTO_PY = 62677
PNL_PY = -88019
EQUITY_PY = -472435
BRUTO_2023 = 2090980


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


def upsert_entity(row):
    path = ROOT / "entities.csv"
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    found = False
    for i, erow in enumerate(existing):
        if erow.get("entity_id") == row["entity_id"]:
            existing[i] = {c: row.get(c, "") for c in cols}
            found = True
            break
    if not found:
        existing.append({c: row.get(c, "") for c in cols})
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("entity", "update" if found else "append", row["entity_id"])


append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_t_hofke_jr2025_cw_nl",
            title="Companyweb NL 't Hofke Puurs YE2025 statutory",
            url="https://www.companyweb.be/nl/0823488131/-t-hofke",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2165; YE2025 omzet empty bruto DROP 7664 pnl LOSS -87076 equity NEG -559511 FTE 0; neerlegging 07.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2165/",
        ),
        dict(
            source_id="src_t_hofke_jr2025_cw_en",
            title="Companyweb EN 't Hofke Puurs YE2025 statutory",
            url="https://www.companyweb.be/en/0823488131",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2165; EN mirror YE2025 Medium; filed 07-07-2026; Last balance sheet year 2025; FTE empty/0",
        ),
        dict(
            source_id="src_t_hofke_jr2025_cw_fr",
            title="Companyweb FR 't Hofke Puurs YE2025 statutory",
            url="https://www.companyweb.be/fr/0823488131",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-26",
            source_class="secondary_aggregator",
            notes="tick2165; FR mirror YE2025 Medium",
        ),
        dict(
            source_id="src_t_hofke_kbo_2165",
            title="KBO 't Hofke 0823.488.131 Actief VZW Puurs-Sint-Amands",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0823488131",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-26",
            source_class="official_register",
            notes="tick2165; Actief VZW; Lippeloseweg(OPP) 58 2890 Puurs-Sint-Amands; 0 VE; directors Ham Joost + Pede Els; KBO email/tel empty; RVT activity via CW/FinCheck NACE 87.101",
        ),
        dict(
            source_id="src_t_hofke_foi_contact_2165",
            title="'t Hofke / Sauvegarde-Skobbegaar FOI contact info.sauvegarde@cura-care.be",
            url="https://sauvegardewzc.be/",
            publisher="WZC Sauvegarde / Cura Care / 't Hofke VZW",
            accessed_date="2026-08-26",
            source_class="foi_contact",
            notes="tick2165; info.sauvegarde@cura-care.be / info@cura-care.be; tel 03 500 83 36; zetel Lippeloseweg 58 2890 Puurs-Sint-Amands; related Residentie Skobbegaar Ruisbroek-Dorp 40",
        ),
    ],
)

for bid, amount, basis, notes in [
    (
        "bud_t_hofke_bruto_jr2025_statutory",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025 (omzet empty)",
        "tick2165; Medium CW; bruto DROP -87.77% vs YE2024 62677; collapsed from YE2023 2090980",
    ),
    (
        "bud_t_hofke_pnl_jr2025_statutory",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        "tick2165; Medium CW; pnl LOSS NARROW -87076 vs YE2024 LOSS -88019 (+1.07%)",
    ),
    (
        "bud_t_hofke_equity_jr2025_statutory",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        "tick2165; Medium CW; equity NEG DEEPEN -18.43% vs YE2024 -472435",
    ),
    (
        "bud_t_hofke_fte_jr2025_statutory",
        FTE,
        "CW social-balance FTE / Employees empty→0 YE2025",
        "tick2165; Medium CW; FTE empty YE2025 (was 33.8 YE2023); assets/debt Unknown pending NBB PDF",
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
                source_id="src_t_hofke_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            )
        ],
    )

append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id="comm_t_hofke_jr2025_statutory_wzc_bruto_collapse_equity_neg",
            title="'t Hofke Puurs YE2025 leftover dual (bruto DROP 7.7k / omzet empty / equity NEG -560k)",
            entity_id=ENTITY,
            beneficiary="Residual RVT shell Puurs-Sint-Amands (related Sauvegarde/Skobbegaar/Cura Care path)",
            legal_basis="VZW RVT (KBO 0823.488.131; Actief; 0 VE; NACE 87.101 RVT)",
            decision_date="2026-07-07",
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
                    "2023_bruto": BRUTO_2023,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0823488131",
            stated_goal="Residential elderly care residual VZW ('t Hofke / historic Sauvegarde path)",
            cut_option="Publish NBB PDF assets/debt FOI; disclose empty omzet + bruto collapse vs Sauvegarde/Skobbegaar/Cura Care related-party matrix; continuity/NEG equity plan",
            source_id="src_t_hofke_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>Antwerpen>PuursSintAmands>tHofke>JR2025_statutory_L5",
            notes="tick2165; Medium CW; bruto primary envelope (omzet empty); assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped Lork Hoeselt BV NACE 68 RE shell; not TE-additive of 348bn; DISTINCT Zorg-Saam/Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof",
        )
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id="lb_t_hofke_bruto_7_7k_equity_neg_560k_omzet_empty_jr2025",
            name="'t Hofke Puurs bruto DROP 7.7k / equity NEG -560k / omzet empty (YE2025)",
            level="L5",
            type="wzc_vzw_statutory",
            hierarchy_path="Vlaanderen>Antwerpen>PuursSintAmands>tHofke>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(abs(EQUITY)),
            tco_notes="CW bruto envelope 7.7k / omzet empty / FTE 0 / 0 VE; equity NEG deepen -560k; bruto collapsed from 2.09m YE2023; residual shell vs Sauvegarde/Skobbegaar; assets/debt Unknown",
            confidence="medium",
            source_id="src_t_hofke_jr2025_cw_en",
            beneficiaries="Historic RVT clients Puurs-Sint-Amands / related Skobbegaar path",
            stated_goal="Residential elderly care residual VZW",
            measured_outcome="omzet empty; bruto DROP -87.77%; pnl LOSS narrow; equity NEG deepen -18.43%; FTE 0",
            absurdity_score="6.8",
            cost_score="2.0",
            difficulty="3.5",
            priority_index="5.2",
            cut_proposal="Publish NBB PDF assets/debt/omzet FOI; disclose related-party matrix vs Sauvegarde/Skobbegaar/Cura Care; NEG equity continuity plan",
            status="open",
            struck_reason="",
            notes="tick2165; Medium CW; FOI gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5; small € envelope but high opacity residual",
        )
    ],
)

upsert_entity(
    dict(
        entity_id=ENTITY,
        name_nl="'t Hofke VZW (Puurs-Sint-Amands / residual RVT)",
        name_fr="'t Hofke ASBL (Puurs-Sint-Amands / MRS résiduelle)",
        name_en="'t Hofke nursing-home residual non-profit (Puurs-Sint-Amands)",
        level="parastatal",
        parent_id="sec_flanders",
        community_language="nl",
        website="https://sauvegardewzc.be/",
        foi_email="info.sauvegarde@cura-care.be",
        foi_postal="Lippeloseweg(OPP) 58, 2890 Puurs-Sint-Amands",
        notes="tick2165 YE2025 Medium CW NL+EN+FR + Strong KBO 0823.488.131 Actief VZW 0 VE NACE 87.101 RVT; omzet empty bruto DROP 7.7k pnl LOSS -87k equity NEG -560k FTE 0; neerlegging 07.07.2026; related Sauvegarde/Skobbegaar/Cura Care; FOI gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped Lork Hoeselt BV NACE 68; do not redo Zorg-Saam/Sint-Bernardus/Ruggeveld/Salvator/Boterlaarhof/WZND/Foyer De Lork Geel/OLV Kempen",
    )
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id="gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5",
            hierarchy_path="Vlaanderen>Antwerpen>PuursSintAmands>tHofke>NBB_PDF_assets_debt_omzet_empty_bruto_collapse_equity_neg",
            entity_id=ENTITY,
            what_is_missing="NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); omzet/code70 empty behind bruto collapse; related-party matrix vs WZC Sauvegarde / Residentie Skobbegaar / Cura Care; NEG equity continuity plan; FTE 0 vs historic staff",
            why_it_matters="Medium CW shows residual RVT VZW with empty omzet, bruto collapsed from millions to EUR7.7k, equity NEG deepen to -EUR560k and FTE 0 while related Sauvegarde/Skobbegaar still operates care at same Lippeloseweg/Ruisbroek path — opacity on where public/care euros moved",
            priority="8",
            recipient_body="'t Hofke VZW / WZC Sauvegarde / Cura Care",
            recipient_email="info.sauvegarde@cura-care.be",
            recipient_postal="Lippeloseweg(OPP) 58, 2890 Puurs-Sint-Amands",
            draft_letter_path="docs/doge/foi/drafts/gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5.md",
            status="ready",
            date_ready="2026-08-26",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id="comm_t_hofke_jr2025_statutory_wzc_bruto_collapse_equity_neg",
            linked_leaderboard_id="lb_t_hofke_bruto_7_7k_equity_neg_560k_omzet_empty_jr2025",
            created_utc=TS,
            updated_utc=TS,
            notes="tick2165; ready NOT sent; Medium CW + Strong KBO; next every-10 2170",
        )
    ],
)

# research_queue: close rq_2165 + spawn rq_2166
path = ROOT / "research_queue.csv"
with path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames
for row in rows:
    if row.get("task_id") == "rq_2165":
        row["title"] = "leftover dual — 't Hofke Puurs YE2025 Medium (bruto DROP 7.7k / omzet empty / equity NEG -560k)"
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "Completed leftover 't Hofke Puurs YE2025 Medium CW after Zorg-Saam; preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
            "skipped Lork Hoeselt BV 0755.822.317 NACE 68 RE shell (same skip as Oudenburg); live YE2025 Medium CW NL+EN+FR + Strong KBO 0823.488.131; "
            "FOI gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5 ready not sent."
        )
        row["blocked_gap_id"] = "gap_t_hofke_nbb_pdf_assets_debt_omzet_empty_bruto_collapse_equity_neg_matrix_l5"
        row["updated_utc"] = TS
        row["notes"] = (
            "tick2165 't Hofke Medium bruto DROP 7.7k omzet empty pnl LOSS -87k equity NEG -560k FTE 0; KBO Actief VZW 0 VE NACE 87.101; "
            "FOI info.sauvegarde@cura-care.be; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next every-10 2170"
        )
have_ids = {row.get("task_id") for row in rows}
if "rq_2166" not in have_ids:
    rows.append(
        {
            "task_id": "rq_2166",
            "title": "leftover dual hole-fill after 't Hofke — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2166 after 't Hofke Puurs YE2025 Medium (bruto DROP 7.7k / equity NEG -560k). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused IGS/DSO/WZC/MRS/hospital/psych/creche/disability with live euros "
                "(optional: WZC Foyer De Lork Hoeselt BV 0755.822.317 YE2025 empty-omzet NEG equity bruto 0.79m but NACE 68 RE — prefer care NACE 87; "
                "Haagwinde Maarkedal 0410.219.433 still YE2024; Maria Boodschap Niel still YE2024). "
                "Do NOT redo 't Hofke 0823.488.131, Zorg-Saam Zusters Kindsheid Jesu 0470.673.890, WZC Sint-Bernardus De Panne 0432.582.485, "
                "Residentie Ruggeveld Antwerpen, Salvator Welzijnscentrum Hasselt, Boterlaarhof Deurne, Woonzorgnet-Dijleland, "
                "Foyer De Lork Geel, Home OLV van de Kempen Ravels, HERTOG JAN Kortenberg, De Lindeboom Knokke-Heist/OLVO/Lindenhove, "
                "Seniorie de l'Epinette, MRS Parc de Forest, MRS Le Hanois, WZC d'Eycken Brug, WZC Sint-Felix, "
                "Zone de secours Hainaut-Est/Brabant wallon/Vesdre/Val de Sambre/HEMECO/Wallonie Picarde/Hesbaye/Hainaut-Centre/Dinaphi, "
                "Zonnelied, Seniors Care-Ion, Groep Sint-Franciscus, Denderrust*, Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, "
                "Armonea/emeis/Korian holdings, Molenheide, De Verlosser Dilbeek, WZC Sint-Jozef Rumst, De Foyer Gent, Psychogeriatrisch Centrum, "
                "Seniorencentrum OLV Bornem, Veilige Have, De Linde Lievegem, Huize Sint-Jozef Ieper, Ocura, Rusthuis Sint Jozef Ninove, "
                "Zilverlinde Olen, De Medemens Antwerpen, Emmaüs Mechelen, Famifamenne, Residentie Oudenburg 0450.755.634 (NACE 55/68), "
                "Home Vrijzicht Ieper, WZC Sint-Jozef Rillaar/Aarschot, AZORG, Prinsenhof Vivalto."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick2165 't Hofke; FARO/AIESH/REW still YE2024; next every-10 2170",
        }
    )
with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2165=done rq_2166=open")

# loop_state
path = ROOT / "loop_state.csv"
with path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = list(r)
    cols = r.fieldnames
rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": TS,
    "last_unit_id": "rq_2165",
    "ticks_completed": "2165",
    "paused": "no",
    "notes": (
        "tick2165 leftover 't Hofke Puurs 0823.488.131 Medium (omzet empty; bruto DROP 7.7k; pnl LOSS -87k; equity NEG -560k; FTE 0; 0 VE NACE 87.101); "
        "AGB Bornem JR2024; FARO/AIESH/REW YE2024; skipped Lork Hoeselt BV NACE 68; next rq_2166; next every-10 2170; continuous hole_fill"
    ),
}
with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state ticks=2165")
