# -*- coding: utf-8 -*-
"""Tick 1267 (research_queue patched surgically — do not DictWriter-rewrite other rows):
 Amal / Integratie en Inburgering Gent JR2025 dual residual
 (city GR HTML SWO 2026-2031 + KBO; NBB/JR PDF opaque)."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T08:45:00Z"
TICK = 1267
SRC = "src_amal_swo_2026_gr00594"
SRC2 = "src_amal_av_jr2025_gr00587"
SRC3 = "src_kbo_amal_0507873093"
SRC4 = "src_nbb_amal_consult_0507873093"
SRC5 = "src_amal_jaarverslagen"
ENT = "integratie_inburgering_gent"
CITY = "city_gent"
SRC_URL = "https://raadpleegomgeving.stad.gent/zittingen/25.0902.9427.5248/agendapunten/26.0507.9790.9943"
SRC2_URL = "https://raadpleegomgeving.stad.gent/zittingen/25.0902.9427.5248/agendapunten/26.0429.6475.4267"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0507873093"
SRC4_URL = "https://consult.cbso.nbb.be/consult-enterprise/0507873093"
SRC5_URL = "https://www.amal.gent/publicaties/jaarverslagen-amal"
GAP = "gap_amal_jr2025_pdf_opaque_city_dual_7_37m_l5"
HIER = "Vlaanderen>Gemeenten>Gent>Amal_Integratie"

# 2026 GR 00594 table (EUR)
CITY_2026 = {
    "gelijke": 193439.28,
    "stv": 522989.83,
    "uct": 51184.08,
    "soc": 14512.26,
    "ocg_ed": 6291.68,
    "ocg_tolk": 11741.18,
    "oek": 0.0,
    "stv_eenmalig": 50000.00,
    "instroom": 60300.00,
}
VL_2026_EVI = 5077800.00
VL_2026_TUR = 1386697.60
CITY_OWN_2026 = 910458.31
VL_2026 = 6464497.60
TOTAL_2026 = 7374955.91
CITY_OWN_2027 = 2059884.31
VL_2027 = 910874.40
TOTAL_2027 = 2970758.71
GELIJKE_2027 = 1272900.41
GELIJKE_JUMP = 1079461.13
MY_UITG = 18644791.11
VL_INC_MY = 7375372.00
CITY_OWN_MY = 11269419.11


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
            "title": "2026_GR_00594 EVA Amal SWO 2026-2031 goedkeuring",
            "url": SRC_URL,
            "publisher": "Stad Gent gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1267; GR 23.06.2026; KBO 0507.873.093; 2026 dual 7.37495591m "
                "(city-own 0.91045831 + VL 6.46449760); MY uitgaven 18.64479111m; "
                "VL ontvangsten 7.375372m; SWO PDF bijlage not retrieved"
            ),
        },
        {
            "source_id": SRC2,
            "title": "2026_GR_00587 EVA Amal AV 25.06.2026 dagorde/mandaat JR2025",
            "url": SRC2_URL,
            "publisher": "Stad Gent gemeenteraad",
            "accessed_date": "2026-08-17",
            "source_class": "primary_html",
            "notes": (
                "tick1267; AV 25.06.2026 Teams 20u; JR2025 + SWO/MJP + jaarverslag 2025 "
                "on agenda; bijlagen only 20260319_AV_verslag.pdf + uitnodiging; "
                "JR/SWO/MJP promised after RVB 28.05.2026 — not on HTML"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Integratie Inburgering Gent Amal 0507.873.093",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1267; vzw since 02.01.2015; Amal since 25.05.2022; seat Botermarkt 1 "
                "9000 Gent; 1 VE; RSZ employer since 01.05.2015; aanbestedende overheid; "
                "NACE 88.999; year-end 31 Dec; AV April; 20 functiehouders; financials empty"
            ),
        },
        {
            "source_id": SRC4,
            "title": "NBB Consult Amal 0507873093 JR filings",
            "url": SRC4_URL,
            "publisher": "NBB Central Balance Sheet Office",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1267; consult SPA 200; API 403; loop-brief filing 2026-00211946 "
                "not independently confirmed; no euro totals extracted"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Amal jaarverslagen page (narrative 2025; PDFs to 2022)",
            "url": SRC5_URL,
            "publisher": "Amal vzw",
            "accessed_date": "2026-08-17",
            "source_class": "org_site",
            "notes": (
                "tick1267; jaarverslag 2025 listed as impact narrative; downloadable "
                "PDFs 2015-2022 only; ops Kongostraat 42 / 09 265 78 40 / info@amal.gent; "
                "not a financial statement"
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
            "name_nl": "Integratie en Inburgering Gent vzw (Amal)",
            "name_fr": "Intégration et parcours d'intégration Gand asbl (Amal)",
            "name_en": "Ghent civic integration EVA-vzw Amal",
            "level": "parastatal",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.amal.gent",
            "foi_email": "info@amal.gent",
            "foi_postal": "Kongostraat 42 9000 Gent / Botermarkt 1 9000 Gent",
            "notes": (
                "tick1267 JR2025 dual residual; KBO 0507.873.093 EVA-vzw; distinct Atlas "
                "Antwerpen 0421.722.346; city 2026 dual 7.375m (own 0.910 + VL 6.464); "
                "MY 18.645m; NBB/JR PDF opaque; FOI " + GAP
            ),
        }
    ],
)
print("entity amal", n)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    CITY,
    (
        "Amal dual residual tick1267 (KBO 0507.873.093; 2026 dual 7.375m own 0.910 "
        "+ VL 6.464; MY 18.645m; JR2025 PDF opaque)"
    ),
)
print("city_gent notes", ok)

ok = patch_entity_notes_line(
    DATA / "entities.csv",
    "atlas_amal",
    (
        "tick1267 split: Atlas Antwerpen mined 1266 (KBO 0421.722.346); Amal Gent "
        "mined 1267 (KBO 0507.873.093) as separate Entity II"
    ),
)
print("atlas_amal notes", ok)

bud_rows = [
    ("bud_amal_city_dual_2026", "2026", TOTAL_2026, SRC, "budgeted", "GR 00594 2026 city+VL lock 7.37495591m"),
    ("bud_amal_city_own_2026", "2026", CITY_OWN_2026, SRC, "budgeted", "GR 00594 2026 city-own 0.91045831m excl VL pass-through"),
    ("bud_amal_vl_pass_2026", "2026", VL_2026, SRC, "budgeted", "GR 00594 2026 VL ABB.EVI 5.0778m + ABB.TUR 1.3866976m"),
    ("bud_amal_vl_evi_2026", "2026", VL_2026_EVI, SRC, "budgeted", "GR 00594 2026 algemene werkingssubsidies ABB.EVI 5.0778m"),
    ("bud_amal_vl_tur_2026", "2026", VL_2026_TUR, SRC, "budgeted", "GR 00594 2026 duurzame VL activering ABB.TUR 1.3866976m"),
    ("bud_amal_gelijke_2026", "2026", CITY_2026["gelijke"], SRC, "budgeted", "GR 00594 2026 Gelijke kansen 0.19343928m"),
    ("bud_amal_stv_2026", "2026", CITY_2026["stv"], SRC, "budgeted", "GR 00594 2026 STV 0.52298983m"),
    ("bud_amal_stv_eenmalig_2026", "2026", CITY_2026["stv_eenmalig"], SRC, "budgeted", "GR 00594 2026 eenmalige verhoging STV 0.050m"),
    ("bud_amal_uct_2026", "2026", CITY_2026["uct"], SRC, "budgeted", "GR 00594 2026 UCT 0.05118408m"),
    ("bud_amal_instroom_2026", "2026", CITY_2026["instroom"], SRC, "budgeted", "GR 00594 2026 ondersteuning verhoogde instroom 0.0603m"),
    ("bud_amal_city_own_2027", "2027", CITY_OWN_2027, SRC, "budgeted", "GR 00594 2027 city-own 2.05988431m (Gelijke kansen jump)"),
    ("bud_amal_vl_pass_2027", "2027", VL_2027, SRC, "budgeted", "GR 00594 2027 VL 0.9108744m (EVI 0.5642 + TUR 0.3466744)"),
    ("bud_amal_gelijke_jump_2026_27", "2027", GELIJKE_JUMP, SRC, "budgeted", "Gelijke kansen 0.19343928m (2026) to 1.27290041m (2027) = +1.07946113m"),
    ("bud_amal_swo_my_2026_2031", "2026", MY_UITG, SRC, "budgeted", "GR 00594 voorgestelde uitgaven 18.64479111m 2026-2031"),
    ("bud_amal_vl_income_my_2026_27", "2026", VL_INC_MY, SRC, "budgeted", "GR 00594 verwachte VL ontvangsten 7.375372m 2026-2027"),
    ("bud_amal_city_own_my_2026_2031", "2026", CITY_OWN_MY, SRC, "budgeted", "MY uitgaven 18.64479111 minus VL income 7.375372 = city-own 11.26941911m"),
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
        "comm_amal_city_dual_7_37m_2026",
        "Amal 2026 city+VL dual lock 7.375m",
        "7374955.91",
        "GR 00594; city-own 0.910m + VL 6.464m",
        "Reconcile cash gestort vs vastlegging + VL pass-through FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_amal_vl_pass_6_46m_2026",
        "Amal 2026 VL pass-through 6.464m (EVI+TUR)",
        "6464497.60",
        "ABB.EVI 5.0778m + ABB.TUR 1.3866976m via city budgetplaats 35148AM00",
        "Confirm stad as doorgeefluik vs own load FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_amal_swo_my_18_64m_2026_2031",
        "Amal SWO 2026-2031 envelope 18.645m",
        "18644791.11",
        "GR 00594 voorgestelde uitgaven; VL income 7.375m; city-own 11.269m",
        "Publish SWO PDF + year cash profile FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_amal_gelijke_jump_1_08m_2026_27",
        "Amal Gelijke kansen 0.193m (2026) to 1.273m (2027) jump 1.079m",
        "1079461.13",
        "Front-loaded VL 2026 then city Gelijke kansen takes over 2027",
        "Why 2026 VL 6.46m vs 2027 city Gelijke 1.27m FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_amal_jr2025_pdf_opaque",
        "Amal NBB/JR2025 PDFs not retrieved",
        "",
        "GR 00587 bijlagen invitation+minutes only; NBB API 403; org PDFs stop 2022",
        "Publish working JR2025 + NBB + jaarverslag 2025 PDFs FOI",
        SRC2,
        SRC2_URL,
    ),
    (
        "comm_amal_2025_city_lock_unknown",
        "Amal 2025 city lock from SWO 2020-2025 unpublished in HTML",
        "",
        "GR 24.11.2025 extended prior toelagen through June 2026; amounts not in 00594",
        "Publish 2025 line lock + cash + 2026 nettoverrekening FOI",
        SRC,
        SRC_URL,
    ),
    (
        "comm_amal_swo_pdf_opaque_2026_2031",
        "Amal SWO 2026-2031 PDF bijlage not retrieved",
        "18644791.11",
        "Named Samenwerkingsoverenkomst EVA Amal vzw 2026-2031.pdf on GR 00594",
        "Working download URL + indicatoren + Ad Rem antwoord FOI",
        SRC,
        SRC_URL,
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "EVA vzw Integratie en Inburgering Gent Amal",
            "legal_basis": "2026_GR_00594 SWO 2026-2031 + 2026_GR_00587 AV + Decreet Lokaal Bestuur art. 247",
            "decision_date": "2026-06-23",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": f"2026:{env}" if env else "",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": evurl,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": src,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER,
            "notes": f"tick{TICK}; primary GR+KBO HTML; NBB/JR PDF opaque; distinct Atlas Antwerpen",
        }
        for cid, title, env, goal, cut, src, evurl in crows
    ],
)
print("commitments", n)

lrows = [
    ("lb_amal_city_dual_7_37m_2026", "Amal 2026 city+VL dual 7.37m", "7374955.91", "6.5", "7.5", "3.0"),
    ("lb_amal_vl_pass_6_46m_2026", "Amal 2026 VL pass-through 6.46m via city", "6464497.60", "7.0", "8.0", "3.0"),
    ("lb_amal_swo_my_18_64m_2026_2031", "Amal SWO 2026-2031 envelope 18.64m", "18644791.11", "6.5", "8.5", "3.0"),
    ("lb_amal_gelijke_jump_1_08m_2026_27", "Amal Gelijke kansen jump +1.08m 2026 to 2027", "1079461.13", "7.0", "6.0", "3.0"),
    ("lb_amal_jr2025_pdf_opaque", "Amal JR2025 NBB/PDF not retrieved", "7374955.91", "7.5", "7.0", "3.0"),
    ("lb_amal_2025_city_lock_unknown", "Amal 2025 city lock unpublished", "7374955.91", "6.5", "6.5", "3.0"),
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
            "tco_notes": "EVA vzw Integratie Inburgering Gent Amal JR2025 Entity II; distinct Atlas Antwerpen; NBB/PDF internals FOI",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Newcomers inburgeraars anderstaligen Gent",
            "stated_goal": "Local dual residual EVA-vzw map VL JR2025 civic integration Gent",
            "measured_outcome": "2026 dual 7.375m (own 0.910 + VL 6.464) / MY 18.645m / JR2025 PDF opaque",
            "absurdity_score": absurd,
            "cost_score": cscore,
            "difficulty": diff,
            "priority_index": str(round(0.5 * float(absurd) + 0.5 * float(cscore) - 0.25 * float(diff), 2)),
            "cut_proposal": "Publish JR2025+NBB PDFs + 2025 lock + reconcile 7.37m 2026 vs VL 6.46m FOI",
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary GR+KBO HTML; not TE-additive without city GE; 2025 lock/NBB internals unknown",
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
                "NBB JR2025 PDF/CSV (Consult 0507873093 / loop-ref 2026-00211946 / "
                "GR 2026_GR_00587 bijlagen) working URL + assets/EV/cash/fin debt/"
                "subsidies/omzet/personnel/VTE/PnL vs 2024; jaarverslag 2025 PDF; "
                "SWO 2026-2031 PDF; 2025 city lock from SWO 2020-2025 + GR 24.11.2025 "
                "extension through June 2026; 2026 cash gestort vs vastlegging 7.37495591m; "
                "VL pass-through confirmation ABB.EVI 5.0778m + ABB.TUR 1.3866976m"
            ),
            "why_it_matters": (
                "Remaining Gent Entity II civic-integration EVA-vzw after AGB cluster "
                "1255-1259: city dual 7.37m (2026) of which VL 6.46m sits beside city-own "
                "0.91m that jumps to 2.06m in 2027; MY envelope 18.64m. Distinct from Atlas "
                "Antwerpen (tick1266). JR2025 approved at AV 25.06.2026 but PDFs not "
                "retrievable (NBB 403 / GR bijlagen invitation-only / org PDFs stop 2022)."
            ),
            "priority": "8",
            "recipient_body": "EVA vzw Integratie en Inburgering Gent Amal / Stad Gent",
            "recipient_email": "info@amal.gent",
            "recipient_postal": "Kongostraat 42 9000 Gent / Botermarkt 1 9000 Gent",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_amal_city_dual_7_37m_2026",
            "linked_leaderboard_id": "lb_amal_city_dual_7_37m_2026",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1267",
    "title": "vzw Integratie Inburgering Gent Amal JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Amal JR2025 city dual HTML SWO 2026-2031 + KBO + NBB consult; "
        "KBO 0507.873.093; city 2026 dual 7.375m own 0.910 + VL 6.464 / MY 18.645m; "
        "PDFs opaque"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T08:30:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1267 Amal JR2025 dual residual; KBO 0507.873.093; city 2026 dual 7.375m "
        "own 0.910 VL 6.464; MY 18.645m VL income 7.375m city-own 11.269m; Gelijke "
        "kansen jump +1.079m 2026-27; 2025 lock unknown; PDFs opaque NBB 403; FOI ready "
        "not sent; distinct Atlas Antwerpen; next rq_1268 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1268",
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
        "Antwerpen 1266 + Amal Gent 1267 done; prefer EVA De Fietsambassade Gent JR2025 "
        "KBO 0665.587.076 GR 2026_GR_00655 or other unmined AGB/zorg/EVA with direct "
        "PDF/NBB/city HTML; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Sint-Truiden / Zorgbedrijf Brasschaat "
        "unpublished; ebesluit TLS — prefer org sites / NBB / city HTML)."
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1267 after Amal Gent JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_rq_target_and_append(DATA / "research_queue.csv", "rq_1267", rq_new, rq_spawn)
print("research_queue 1267", found, "spawned_1268", spawned)

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
            "last_unit_id": "rq_1267",
            "ticks_completed": "1267",
            "paused": "no",
            "notes": (
                "tick1267 Amal/Integratie Gent JR2025 dual residual; KBO 0507.873.093; "
                "city 2026 lock 7.375m own 0.910 + VL 6.464; MY 18.645m; NBB/JR PDF opaque; "
                "FOI ready; next rq_1268 residual dual L5 VL (prefer Fietsambassade Gent "
                "JR2025); continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1267 - 2026-08-17 - rq_1267 Amal / Integratie & Inburgering Gent dual residual
- Unit: EVA vzw Integratie en Inburgering Gent (Amal) JR2025 Entity II after Gent AGB cluster 1255–1259 + Atlas Antwerpen tick1266 (KBO 0507.873.093; EVA-vzw; seat Botermarkt 1 / ops Kongostraat 42). **Distinct from Atlas Antwerpen** (KBO 0421.722.346). AV 25.06.2026 / GR 23.06.2026 `2026_GR_00587` + SWO 2026–2031 `2026_GR_00594`. NBB consult exists; API 403; loop-brief filing 2026-00211946 not independently confirmed. WAGSO already mined tick1199.
- EUR strong (city HTML primary; NBB/JR PDF internals unknown): 2026 dual **7.375m** (city-own **0.910m** + VL **6.464m** = ABB.EVI **5.078m** + ABB.TUR **1.387m**); lines Gelijke kansen **0.193m** + STV **0.523m** + eenmalig STV **0.050m** + UCT **0.051m** + instroom **0.060m** + soc/OCG **0.033m**; MY 2026–2031 uitgaven **18.645m** / VL income **7.375m** / city-own **11.269m**; 2027 city-own **2.060m** (Gelijke kansen jump **+1.079m** to **1.273m**) while VL drops to **0.911m**. 2025 city lock unknown (SWO 2020–2025 extended 24.11.2025 through June 2026). BBC/NBB PDFs not retrieved (NBB 403 + GR bijlagen invitation-only + org PDFs stop 2022).
- CSVs: sources+5/entities(new+city/atlas_amal notes)/budgets+16/commitments+7/leaderboard+6 + FOI ready `gap_amal_jr2025_pdf_opaque_city_dual_7_37m_l5` (not sent); rq_1267=done; spawn rq_1268; ticks=1267. No every-10 (1267 not a *0 tick).
- Next: rq_1268 residual dual L5 VL JR2025 hole_fill (prefer EVA De Fietsambassade Gent JR2025 KBO 0665.587.076 GR 2026_GR_00655 or other unmined AGB/zorg/EVA with direct PDF).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
