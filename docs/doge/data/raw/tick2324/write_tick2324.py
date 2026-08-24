# tick 2324: leftover dual aPart Gent YE2025 after Dominiek Savio@2323
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
UTC = "2026-08-24T13:30:00Z"
ENTITY = "vzw_apart_gent"
GAP = "gap_apart_nbb_pdf_assets_debt_bruto_gt_omzet_419_67x_pnl_drop_99pct_jeugdhulp_matrix_l5"
LB = "lb_apart_bruto_8_79m_omzet_20_9k_419_67x_pnl_drop_99pct_jr2025"
COMM = "comm_apart_jr2025_statutory_jeugdhulp_bruto_gt_omzet_419_67x"
OMZET, BRUTO, PNL, EQUITY, FTE = 20940, 8787800, 3607, 4025991, 115.7
OMZET24, BRUTO24, PNL24, EQUITY24, FTE24 = 26679, 8354144, 856164, 4037002, 110.8
RATIO = round(BRUTO / OMZET, 2)
PI = "6.71"


def append_csv(path, row):
    p = Path(path)
    with p.open(newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    data = p.read_bytes()
    if data and not data.endswith(b"\n"):
        p.write_bytes(data + b"\n")
    out = {k: row.get(k, "") for k in fields}
    with p.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def has_id(path, key, val):
    with open(path, encoding="utf-8", newline="") as f:
        return any(row.get(key) == val for row in csv.DictReader(f))


rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

for row in rows:
    if row["task_id"] == "rq_2324":
        if row["status"] == "done":
            raise SystemExit("rq_2324 already done: " + (row.get("title") or "")[:90])
        if row["status"] == "in_progress" and (row.get("entity_id") or "").strip() not in ("", ENTITY):
            raise SystemExit("rq_2324 claimed by other: " + (row.get("entity_id") or ""))

if not has_id(ROOT / "sources.csv", "source_id", "src_apart_jr2025_cw_en"):
    for sid, title, url, pub, klass, notes in [
        (
            "src_apart_jr2025_cw_nl",
            "Companyweb NL aPart YE2025 statutory",
            "https://www.companyweb.be/nl/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2324; YE2025 omzet {OMZET} bruto {BRUTO} ~{RATIO}x pnl DROP {PNL} equity {EQUITY} FTE {FTE}",
        ),
        (
            "src_apart_jr2025_cw_en",
            "Companyweb EN aPart YE2025 statutory",
            "https://www.companyweb.be/en/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            f"tick2324; EN Medium; filed 24-06-2026; Turnover {OMZET} Gross {BRUTO} P/L {PNL} Equity {EQUITY} FTE {FTE}",
        ),
        (
            "src_apart_jr2025_cw_fr",
            "Companyweb FR aPart YE2025 statutory",
            "https://www.companyweb.be/fr/0567657460/apart",
            "Companyweb (NBB-derived)",
            "secondary_aggregator",
            "tick2324; FR mirror",
        ),
        (
            "src_apart_kbo_2324",
            "KBO aPart 0567.657.460",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0567657460",
            "KBO FOD Economie",
            "official_register",
            "tick2324; Actief 12 VE aPart Gent RSZ 87.991 integrale jeugdhulp",
        ),
        (
            "src_apart_site_contact_2324",
            "aPart FOI info.vzwapart@vzwapart.be",
            "https://vzwapart.be/contacteer-ons",
            "aPart VZW",
            "foi_contact",
            "tick2324; info.vzwapart@vzwapart.be; Brandstraat 3 Gent; T 09 225 01 59",
        ),
    ]:
        append_csv(
            ROOT / "sources.csv",
            dict(
                source_id=sid,
                title=title,
                url=url,
                publisher=pub,
                accessed_date="2026-08-24",
                source_class=klass,
                notes=notes,
            ),
        )

if not has_id(ROOT / "entities.csv", "entity_id", ENTITY):
    append_csv(
        ROOT / "entities.csv",
        dict(
            entity_id=ENTITY,
            name_nl="aPart VZW (Gent / integrale jeugdhulp)",
            name_fr="aPart ASBL (Gand / aide à la jeunesse avec hébergement)",
            name_en="aPart VZW (Ghent / residential youth care)",
            level="parastatal",
            parent_id="sec_flanders",
            community_language="nl",
            website="https://vzwapart.be/",
            foi_email="info.vzwapart@vzwapart.be",
            foi_postal="Brandstraat 3, 9000 Gent",
            notes=(
                f"tick2324 YE2025 Medium CW NL+EN+FR + Strong KBO 0567.657.460 Actief 12 VE RSZ 87.991; "
                f"omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} (-99.58%); equity {EQUITY}; "
                f"FTE JUMP {FTE}; FOI {GAP}; after Dominiek Savio@2323; AGB/FARO YE2024; not TE-additive"
            ),
        ),
    )

if not has_id(ROOT / "budgets.csv", "budget_id", "bud_apart_omzet_jr2025_statutory"):
    for bid, amt, basis, notes in [
        ("bud_apart_omzet_jr2025_statutory", OMZET, "CW statutory omzet YE2025 DROP", f"tick2324; Medium CW; omzet -21.51% vs {OMZET24}"),
        ("bud_apart_bruto_jr2025_statutory", BRUTO, f"CW statutory bruto_marge YE2025 ~{RATIO}x omzet", f"tick2324; Medium CW; bruto +5.19% vs {BRUTO24}"),
        ("bud_apart_pnl_jr2025_statutory", PNL, "CW statutory winst/verlies YE2025 DROP -99.58%", f"tick2324; Medium CW; pnl DROP vs {PNL24}"),
        ("bud_apart_equity_jr2025_statutory", EQUITY, "CW statutory eigen_vermogen YE2025", f"tick2324; Medium CW; equity -0.27% vs {EQUITY24}"),
        ("bud_apart_fte_jr2025_statutory", FTE, "CW social-balance FTE 115.7", f"tick2324; Medium CW; FTE JUMP vs {FTE24}"),
    ]:
        append_csv(
            ROOT / "budgets.csv",
            dict(
                budget_id=bid,
                entity_id=ENTITY,
                year="2025",
                amount_eur=amt,
                amount_min_eur=amt,
                amount_max_eur=amt,
                basis=basis,
                source_id="src_apart_jr2025_cw_en",
                confidence="medium",
                notes=notes,
            ),
        )

if not has_id(ROOT / "commitments.csv", "commitment_id", COMM):
    cash = json.dumps(
        {
            "2025_omzet": OMZET,
            "2025_bruto": BRUTO,
            "2025_pnl": PNL,
            "2025_equity": EQUITY,
            "2025_fte": FTE,
            "2024_omzet": OMZET24,
            "2024_bruto": BRUTO24,
            "2024_pnl": PNL24,
            "2024_equity": EQUITY24,
            "2024_fte": FTE24,
            "ratio_bruto_omzet": RATIO,
        },
        separators=(",", ":"),
    )
    append_csv(
        ROOT / "commitments.csv",
        dict(
            commitment_id=COMM,
            title=f"aPart YE2025 leftover dual (omzet {OMZET} / bruto {BRUTO} ~{RATIO}x / pnl DROP -99.58% / FTE {FTE} / Medium)",
            entity_id=ENTITY,
            beneficiary="kinderen/jongeren/jongvolwassenen kwetsbare positie Gent / VL jeugdhulp",
            legal_basis="VZW aPart (KBO 0567.657.460)",
            decision_date="2026-06-24",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=BRUTO,
            cash_by_year=cash,
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0567657460/apart",
            stated_goal="Integrale jeugdhulp met huisvesting (aPart Gent)",
            cut_option=f"Publish NBB PDF assets/debt FOI; explain bruto~{RATIO}x omzet + pnl DROP -99.58%",
            source_id="src_apart_jr2025_cw_en",
            confidence="medium",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart_jeugdhulp>JR2025_statutory_L5",
            notes="tick2324; Medium CW; after Dominiek Savio@2323; not TE-additive",
        ),
    )

if not has_id(ROOT / "leaderboard.csv", "item_id", LB):
    append_csv(
        ROOT / "leaderboard.csv",
        dict(
            item_id=LB,
            name=f"aPart bruto 8.79m / omzet 20.9k ~{RATIO}x / pnl DROP -99.58% (YE2025)",
            level="L5",
            type="jeugdhulp_vzw_statutory",
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart>JR2025",
            annual_cost_eur=BRUTO,
            total_cost_eur=BRUTO,
            tco_notes=(
                f"CW omzet DROP {OMZET} / bruto JUMP {BRUTO} (~{RATIO}x) / pnl DROP {PNL} from {PNL24} / "
                f"equity {EQUITY} / FTE JUMP {FTE} / filed 24.06.2026"
            ),
            confidence="medium",
            source_id="src_apart_jr2025_cw_en",
            beneficiaries="VL jeugdhulp Gent minors/youth",
            stated_goal="Integrale jeugdhulp met huisvesting",
            measured_outcome=f"bruto÷omzet ~{RATIO}x; pnl DROP -99.58%; FTE JUMP {FTE24}→{FTE}",
            absurdity_score="9.0",
            cost_score="5.2",
            difficulty="3.0",
            priority_index=PI,
            cut_proposal=f"Publish NBB PDF assets/debt FOI; reconcile bruto÷omzet ~{RATIO}x + pnl crash",
            status="open",
            struck_reason="",
            notes=f"tick2324; Medium CW; FOI {GAP}; after Dominiek Savio@2323; AGB/FARO YE2024",
        ),
    )

if not has_id(ROOT / "foi_queue.csv", "gap_id", GAP):
    append_csv(
        ROOT / "foi_queue.csv",
        dict(
            gap_id=GAP,
            hierarchy_path="Vlaanderen>OostVlaanderen>Gent>aPart>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF YE2025 full (assets/debt/cash); why bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) — "
                f"OJW/agentschap Opgroeien subsidy matrix; pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-99.58%); FTE JUMP"
            ),
            why_it_matters=(
                f"Medium CW shows Gent jeugdhulp VZW (bruto 8.79m / omzet 20.9k ~{RATIO}x / pnl DROP -99.58% / FTE 115.7) "
                "under public youth-care path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="aPart VZW",
            recipient_email="info.vzwapart@vzwapart.be",
            recipient_postal="Brandstraat 3, 9000 Gent",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-24",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=UTC,
            updated_utc=UTC,
            notes="tick2324; ready NOT sent; Medium CW + Strong KBO; after Dominiek Savio@2323",
        ),
    )

out_rows = []
has_2325 = False
for row in rows:
    if row["task_id"] == "rq_2324":
        row["title"] = (
            f"leftover dual — aPart YE2025 Medium (bruto JUMP 8.79m / ~{RATIO}x omzet / pnl DROP -99.58% / FTE JUMP 115.7)"
        )
        row["status"] = "done"
        row["hierarchy_target"] = "L5"
        row["entity_id"] = ENTITY
        row["instructions"] = (
            "After Dominiek Savio. Prefer AGB/FARO YE2025 else unused. Do NOT redo Dominiek Savio/Merlijn/Humival/Heder stack."
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = (
            f"tick2324; aPart 0567.657.460 Medium CW; omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
            f"pnl DROP {PNL}; equity {EQUITY}; FTE JUMP {FTE}; FOI {GAP} ready NOT sent; after Dominiek Savio@2323; next EVERY-10 2330"
        )
    if row["task_id"] == "rq_2325":
        has_2325 = True
    out_rows.append(row)

if not has_2325:
    out_rows.append(
        {
            "task_id": "rq_2325",
            "title": "leftover dual after aPart — prefer AGB/FARO-YE2025/AIESH/Citeco/or-unused ETA-VAPH-WZC-maatwerk",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "After aPart. Prefer AGB/FARO YE2025 else unused (Manupal/Aralea/Vlotter/Gandae/De Ploeg/Het Eepos if YE2025). "
                "Do NOT redo aPart/Dominiek Savio/Merlijn/Humival/Heder/Kindervriend/Homevil stack."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2324 aPart; next every-10 2330",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(out_rows)

with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_2324",
            "ticks_completed": "2324",
            "paused": "no",
            "notes": (
                f"tick2324 leftover dual aPart 0567.657.460 Medium (omzet DROP {OMZET}; bruto JUMP {BRUTO} ~{RATIO}x; "
                f"pnl DROP {PNL}; equity {EQUITY}; FTE JUMP {FTE}; 12 VE Gent jeugdhulp); after Dominiek Savio@2323; "
                "AGB Bornem JR2024; FARO/AIESH YE2024; next rq_2325; next EVERY-10 2330; continuous hole_fill"
            ),
        }
    )

raw = ROOT / "raw" / "tick2324"
raw.mkdir(parents=True, exist_ok=True)
(raw / "summary.json").write_text(
    json.dumps(
        {
            "tick": "2324",
            "unit": "rq_2324",
            "entity": ENTITY,
            "kbo": "0567.657.460",
            "omzet": OMZET,
            "bruto": BRUTO,
            "pnl": PNL,
            "equity": EQUITY,
            "fte": FTE,
            "ratio": RATIO,
            "confidence": "medium",
            "gap": GAP,
            "pi": float(PI),
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
(raw / "cw_en_excerpt.txt").write_text(
    f"aPart YE2025 CW EN/NL/FR: omzet {OMZET} bruto {BRUTO} (~{RATIO}x) pnl {PNL} equity {EQUITY} FTE {FTE} filed 24.06.2026\n",
    encoding="utf-8",
)

print("OK tick2324 aPart", RATIO, "x", PI)
