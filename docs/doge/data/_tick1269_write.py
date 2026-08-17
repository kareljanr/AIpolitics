# -*- coding: utf-8 -*-
"""Tick 1269 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Mintus / Zorgvereniging Brugge JR2025 dual residual
 (city JR2025 boekdeel 3 PDF + KBO; Mintus own BBC/NBB PDF opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:40:00Z"
TICK = 1269
SRC = "src_brugge_jr2025_bd3_mintus"
SRC2 = "src_brugge_jr2025_portal"
SRC3 = "src_kbo_mintus_0682844465"
SRC4 = "src_nbb_mintus_consult_0682844465"
SRC5 = "src_mintus_org"
ENT = "mintus_brugge"
CITY = "city_brugge"
SRC_URL = "https://www.brugge.be/sites/default/files/2026-07/Jaarrekening%202025%20boekdeel%203.pdf"
SRC2_URL = "https://www.brugge.be/stad-bestuur/bestuur/jaarrekening-stad-ocmw-brugge"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0682844465"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/0682844465"
SRC5_URL = "https://mintus.be/"
GAP = "gap_mintus_jr2025_pdf_opaque_city_dual_26_36m_l5"
HIER = "Vlaanderen>Gemeenten>Brugge>Mintus"

CREDITOR_2025 = 26356642.00
WERKING_MINTUS_SAS_2025 = 25674330.00
OCMW_VERG_BUD_2025 = 715390.00
OCMW_VERG_EXE_2025 = 643236.00
INVEST_SUB_2025 = 101670.00
DEELNEMING = 56956114.51
THES_LT_MINTUS = 1530000.00  # source: "1,53 mio euro"
REG_2024 = 26186642.03
DELTA_24_25 = CREDITOR_2025 - REG_2024  # 169999.97
KLIMAAT_BUD = 12675.00
KLIMAAT_EXE = -672.51


def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_rq_target_and_append(path, target_id, new_target, spawn_row):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    has_spawn = False
    spawn_id = spawn_row.get("task_id")
    for line in lines[1:]:
        if not line:
            continue
        rid = next(csv.reader([line]))[0]
        if rid == spawn_id:
            has_spawn = True
        if rid == target_id:
            found = True
            out.append(csv_line(fields, new_target))
        else:
            out.append(line)
    if not has_spawn:
        out.append(csv_line(fields, spawn_row))
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found, not has_spawn


def patch_entity_notes_line(path, entity_id, extra, extra_fields=None):
    text = path.read_text(encoding="utf-8")
    ends_nl = text.endswith("\n")
    lines = text.splitlines()
    header = lines[0]
    fields = next(csv.reader([header]))
    out = [header]
    found = False
    for line in lines[1:]:
        if not line:
            continue
        row = next(csv.DictReader([header, line]))
        if row.get("entity_id") == entity_id:
            found = True
            if extra_fields:
                row.update(extra_fields)
            notes = row.get("notes") or ""
            if extra not in notes:
                row["notes"] = (notes + "; " + extra).strip("; ")
            out.append(csv_line(fields, row))
        else:
            out.append(line)
    path.write_text("\n".join(out) + ("\n" if ends_nl else ""), encoding="utf-8")
    return found


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad/OCMW Brugge JR2025 boekdeel 3 documentatie (Mintus dual)",
            "url": SRC_URL,
            "publisher": "Stad Brugge",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1269; published 2026-07-02; 7.19MB text PDF; creditor Mintus "
                "26.356642m; werking Mintus/'t SAS 25.674330m; OCMW vergoeding "
                "0.643236m exe / 0.715390m bud; invest 0.101670m; OCMW deelneming "
                "B4 56.95611451m; LT thes 1.53m Mintus-repaid"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Jaarrekening Stad & OCMW Brugge portal JR2025 3 boekdelen",
            "url": SRC2_URL,
            "publisher": "Stad Brugge",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1269; publicatiedatum JR2025 2 juli 2026; boekdeel 1-3 "
                "downloadable; no separate Mintus BBC PDF on portal"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Mintus 0682.844.465",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1269; Vereniging van OCMW's since 12.10.2017; name Mintus "
                "since 01.01.2019; seat Ruddershove 4 8000 Brugge; 24 VE; RSZ "
                "employer since 01.01.2022; NACE 87.101 RVT; email "
                "zorgverenigingbrugge@ocmw-brugge.be; tel 050 32 70 00; "
                "financials empty"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult Mintus 0682844465 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1269; consult fetch timeout this box; no euro totals extracted; "
                "do not use Belscope/Companyweb"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Mintus org site (bestuur / hoofdzetel; no JR2025 PDF)",
            "url": SRC5_URL,
            "publisher": "Mintus",
            "accessed_date": "2026-08-17",
            "source_class": "org_site",
            "notes": (
                "tick1269; hoofdzetel 050 32 70 00; bestuur points to Stad Brugge "
                "bekendmakingen; no own JR2025 financial statement published"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Mintus (Zorgvereniging Brugge)",
            "name_fr": "Mintus (association de soins Bruges)",
            "name_en": "Mintus Bruges care association (OCMW union)",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://mintus.be/",
            "foi_email": "zorgverenigingbrugge@ocmw-brugge.be",
            "foi_postal": "Ruddershove 4 8000 Brugge",
            "notes": (
                "tick1269 JR2025 dual residual; KBO 0682.844.465 Vereniging van "
                "OCMW's; city/OCMW 2025 creditor 26.357m; werking Mintus/'t SAS "
                "25.674m; OCMW vergoeding 0.643m; deelneming B4 56.956m; LT thes "
                "1.53m Mintus-repaid; own BBC/NBB PDF opaque; FOI " + GAP
            ),
        }
    ],
)
print("entity mintus", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "Mintus dual residual tick1269 (KBO 0682.844.465; 2025 creditor 26.357m; "
        "werking Mintus/'t SAS 25.674m; OCMW deelneming 56.956m; JR own PDF opaque)"
    ),
)
print("city_brugge notes", ok)

bud_rows = [
    ("bud_mintus_city_creditor_2025", "2025", CREDITOR_2025, SRC, "executed", "JR2025 bd3 creditor overview Mintus 26.356642m named"),
    ("bud_mintus_werking_sas_combined_2025", "2025", WERKING_MINTUS_SAS_2025, SRC, "executed", "JR2025 bd3 nominative werkingstoelage Mintus/'t SAS 25.674330m combined label — split FOI"),
    ("bud_mintus_ocmw_vergoeding_exe_2025", "2025", OCMW_VERG_EXE_2025, SRC, "executed", "JR2025 bd3 OCMW 6493140 Vergoeding Mintus aangerekend 0.643236m"),
    ("bud_mintus_ocmw_vergoeding_bud_2025", "2025", OCMW_VERG_BUD_2025, SRC, "budgeted", "JR2025 bd3 OCMW 6493140 Vergoeding Mintus budget 0.715390m"),
    ("bud_mintus_invest_sub_2025", "2025", INVEST_SUB_2025, SRC, "executed", "JR2025 bd3 BV0900 invest subsidy Mintus 0.101670m"),
    ("bud_mintus_ocmw_deelneming_2025", "2025", DEELNEMING, SRC, "executed", "JR2025 bd3 OCMW deelnemingen B4 Mintus 56.95611451m stock 31.12.2024=31.12.2025 not annual spend"),
    ("bud_mintus_thes_lt_repay_2025", "2025", THES_LT_MINTUS, SRC, "executed", "JR2025 bd3 OCMW LT thesauriebewijzen 1.53m fully repaid by Mintus (source rounded 1,53 mio)"),
    ("bud_mintus_creditor_vs_2024_delta", "2025", DELTA_24_25, SRC, "executed", "2025 creditor 26.356642m minus 2024 register 26.18664203m = +0.170000m"),
    ("bud_mintus_klimaat_exe_2025", "2025", KLIMAAT_EXE, SRC, "executed", "JR2025 bd3 BV0350 Mintus-only klimaat aangerekend -672.51 (budget 12675)"),
    ("bud_mintus_klimaat_bud_2025", "2025", KLIMAAT_BUD, SRC, "budgeted", "JR2025 bd3 BV0350 Mintus-only klimaat budget 12675"),
]
n = append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": bid,
            "entity_id": ENT,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": src,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}",
        }
        for bid, year, amt, src, basis, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_mintus_city_dual_26_36m_2025",
        "Mintus 2025 city/OCMW creditor dual 26.357m",
        "26356642",
        "JR2025 bd3 named creditor Mintus 26.356642m; +0.170m vs 2024 register",
        "Publish own JR2025 + split vs 't SAS + 2026 lock FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mintus_werking_25_67m_2025",
        "Mintus/'t SAS 2025 nominative werkingstoelage 25.674m",
        "25674330",
        "Combined label BV0900; do not invent Mintus-only split",
        "Split Mintus vs 't SAS cash FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mintus_ocmw_vergoeding_0_64m_2025",
        "OCMW Vergoeding Mintus 2025 executed 0.643m",
        "643236",
        "6493140 budget 0.715390m / exe 0.643236m",
        "Why underspend 72k vs budget FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mintus_ocmw_deelneming_56_96m",
        "OCMW deelneming Mintus B4 stock 56.956m",
        "56956114.51",
        "Unchanged 31.12.2024 to 31.12.2025; participation not annual spend",
        "Composition inbreng vs vordering FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mintus_alt_debt_repay_1_53m",
        "OCMW LT thesauriebewijzen 1.53m repaid by Mintus",
        "1530000",
        "OCMW thes 20m of which KT 18.46m; LT 1.53m Mintus-repaid; AFM distortion",
        "Mintus share of remaining alt-debt schedule + transferred ordinary loans FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_mintus_jr2025_pdf_opaque",
        "Mintus own BBC/NBB JR2025 PDFs not retrieved",
        "",
        "City dual PDF public; org site no JR; NBB consult timeout; no Belscope",
        "Publish working BBC+NBB JR2025 PDFs FOI",
        SRC4,
        SRC4_URL,
    ),
    (
        "comm_mintus_2026_lock_unknown",
        "Mintus 2026 city/OCMW lock unpublished in retrieved PDFs",
        "",
        "MJP 2026-2031 subsidy annex names Mintus cluster without extractable EUR",
        "Publish 2026 nominative Mintus lock FOI",
        SRC2,
        SRC2_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Mintus (Zorgvereniging Brugge)",
            "legal_basis": "Decreet Lokaal Bestuur + OCMW-vereniging Mintus + JR2025 Stad/OCMW Brugge",
            "decision_date": "2026-07-02",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": f"2025:{env}" if env else "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": evurl,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": src,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary city JR2025 PDF + KBO; own BBC/NBB PDF opaque",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_mintus_city_dual_26_36m_2025", "Mintus 2025 city/OCMW dual 26.36m", "26356642", "6.5", "8.0", "3.0"),
    ("lb_mintus_werking_25_67m_2025", "Mintus/'t SAS 2025 werkingstoelage 25.67m", "25674330", "6.0", "8.0", "3.0"),
    ("lb_mintus_ocmw_deelneming_56_96m", "OCMW deelneming Mintus B4 stock 56.96m", "56956114.51", "7.0", "8.5", "3.0"),
    ("lb_mintus_alt_debt_1_53m", "Mintus-repaid OCMW LT thes 1.53m (AFM tilt)", "1530000", "7.5", "6.0", "3.0"),
    ("lb_mintus_ocmw_vergoeding_0_64m_2025", "OCMW Vergoeding Mintus 2025 exe 0.64m", "643236", "5.5", "5.0", "3.0"),
    ("lb_mintus_jr2025_pdf_opaque", "Mintus own JR2025 BBC/NBB not retrieved", "26356642", "7.5", "7.0", "3.0"),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + "_L5",
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": "Mintus Brugge JR2025 Entity II zorg EVA; OCMW deelneming is stock not TCO; own BBC/NBB internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "WZC / thuiszorg / kinderopvang / beperking Brugge cluster",
            "stated_goal": "Local dual residual zorg-EVA map VL JR2025 Brugge",
            "measured_outcome": "2025 creditor 26.357m / werking 25.674m combined / deelneming 56.956m / own PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish Mintus JR2025 BBC+NBB + split 25.67m vs SAS + alt-debt schedule FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary city JR2025 PDF; not TE-additive without city GE; own internals unknown",
        }
        for iid, name, cost, absurd, cscore, diff in lrows
    ],
)
print("leaderboard", n)

n = append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": HIER + ">jr2025_L5",
            "entity_id": ENT,
            "what_is_missing": (
                "Mintus own BBC JR2025 (J1-J5) + NBB Consult 0682844465 working URL "
                "+ assets/EV/cash/fin debt/subsidies/omzet/personnel/VTE/PnL vs 2024; "
                "split of nominative werkingstoelage 25.674330m Mintus vs 't SAS; "
                "OCMW deelneming 56.95611451m composition; Mintus share of OCMW "
                "alternative debt / LT thes 1.53m schedule + transferred ordinary "
                "loans outstanding 31.12.2025; 2026 city/OCMW nominative lock; "
                "mixed BV0350/BV0119 Mintus cash"
            ),
            "why_it_matters": (
                "Remaining Brugge zorg-EVA Entity II after city GE tick834: city/OCMW "
                "2025 dual 26.36m sits beside an unchanged 56.96m OCMW deelneming and "
                "an AFM-distorting 1.53m LT thes repaid by Mintus. Own JR2025 not on "
                "org site; NBB consult timeout this box. Distinct from Antwerp/Gent "
                "zorg and from sibling SAS/Blauwe Lelie/SPOOR/WOK lines."
            ),
            "priority": "8",
            "recipient_body": "Mintus / Stad Brugge / OCMW Brugge",
            "recipient_email": "zorgverenigingbrugge@ocmw-brugge.be",
            "recipient_postal": "Ruddershove 4 8000 Brugge / Burg 12 8000 Brugge",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_mintus_city_dual_26_36m_2025",
            "linked_leaderboard_id": "lb_mintus_city_dual_26_36m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1269",
    "title": "Mintus Zorgvereniging Brugge JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Mintus JR2025 city dual PDF boekdeel 3 + KBO; KBO 0682.844.465; "
        "2025 creditor 26.357m / werking Mintus/'t SAS 25.674m / OCMW vergoeding "
        "0.643m / deelneming 56.956m; own BBC/NBB PDF opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T09:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1269 Mintus JR2025 dual residual; KBO 0682.844.465; city/OCMW 2025 "
        "creditor 26.357m; werking Mintus/'t SAS 25.674m combined; OCMW vergoeding "
        "0.643m exe; invest 0.102m; deelneming B4 56.956m stock; LT thes 1.53m "
        "Mintus-repaid AFM tilt; +0.170m vs 2024 register; own PDF opaque NBB "
        "timeout; FOI ready not sent; next rq_1270 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1270",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + AG Vespa 1260 + AGSO 1261 + AG CIA Erfgoed 1262 "
        "+ AG CIA Kunsten 1263 + AG Energiebesparingsfonds 1264 + AG Digipolis 1265 + Atlas "
        "Antwerpen 1266 + Amal Gent 1267 + Fietsambassade Gent 1268 + Mintus Brugge 1269 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; WAGSO already mined "
        "tick1199; skip Mobil-O/AG EOS inactive; skip Woonzorgnetwerk Edegem / Zorgbedrijf "
        "Sint-Truiden / Zorgbedrijf Brasschaat unpublished; ebesluit TLS — prefer org sites / "
        "NBB / city HTML). Tick 1270 is a *0 tick: also refresh progress_every_10_ticks.md + "
        "doge_waste_top10_current.md."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1269 after Mintus Brugge JR2025 dual residual; next residual dual L5 VL + every-10 at 1270",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1269", rq_new, rq_spawn)
print("research_queue 1269", found, "spawned_1270", spawned)

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
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
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_1269",
            "ticks_completed": "1269",
            "paused": "no",
            "notes": (
                "tick1269 Mintus Brugge JR2025 dual residual; KBO 0682.844.465; "
                "city/OCMW 2025 creditor 26.357m; werking 25.674m combined; "
                "deelneming 56.956m; LT thes 1.53m Mintus-repaid; own PDF opaque; "
                "FOI ready; next rq_1270 residual dual L5 VL + every-10 progress "
                "(prefer unmined AGB/zorg/EVA JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1269 - 2026-08-17 - rq_1269 Mintus / Zorgvereniging Brugge dual residual
- Unit: Mintus (Zorgvereniging Brugge) JR2025 Entity II after city Brugge GE tick834 + Zorg/WV cluster 1246–1251 + Gent/Antwerp dual 1255–1268 (KBO 0682.844.465; Vereniging van OCMW's; seat Ruddershove 4). **Distinct from** Zorgbedrijf Antwerpen / Rivierenland / Meetjesland / Sakura / Zorg Leuven / ZOG Genk and from sibling SAS / Blauwe Lelie / SPOOR / WOK lines. Primary: Stad/OCMW Brugge JR2025 boekdeel 3 text PDF (published 02.07.2026, 7.19MB). NBB consult timeout this box; org site has no JR2025 financial statement. WAGSO already mined tick1199.
- EUR strong (city JR2025 PDF primary; own BBC/NBB internals unknown): creditor Mintus **26.357m**; nominative werkingstoelage Mintus/'t SAS **25.674m** (combined label — split FOI); OCMW vergoeding Mintus **0.643m** exe / **0.715m** bud; invest-sub **0.102m**; OCMW deelneming B4 **56.956m** stock unchanged vs 31.12.2024; LT thesauriebewijzen **1.53m** fully repaid by Mintus (OCMW thes **20m** / KT **18.46m**; AFM distortion); 2025 creditor vs 2024 register **+0.170m**. Mixed BV0350/BV0119 not attributed. 2026 lock not extractable from MJP annex.
- CSVs: sources+5/entities(new+city note)/budgets+10/commitments+7/leaderboard+6 + FOI ready `gap_mintus_jr2025_pdf_opaque_city_dual_26_36m_l5` (not sent); rq_1269=done; spawn rq_1270; ticks=1269. No every-10 (1269 not a *0 tick).
- Next: rq_1270 residual dual L5 VL JR2025 hole_fill + **every-10 progress refresh** (tick 1270 is a *0 tick). Prefer other unmined AGB/zorg/EVA with direct PDF.

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
