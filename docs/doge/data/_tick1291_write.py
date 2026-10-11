# -*- coding: utf-8 -*-
"""Tick 1291 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Kapelle-op-den-Bos JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:35:00Z"
TICK = 1291
SRC = "src_kapelle_jr2025_bbc"
SRC2 = "src_kapelle_jr2025_gr"
SRC3 = "src_kbo_kapelle_0207534468"
ENT = "city_kapelle_op_den_bos"
OCMW = "ocmw_kapelle_op_den_bos"
SRC_URL = "https://kapelle-op-den-bos-echo.cipalschaubroeck.be/raadpleegomgeving/document/532f1eb3-60b9-4fac-8938-a3ff71d0d6d6"
SRC2_URL = "https://kapelle-op-den-bos-echo.cipalschaubroeck.be/raadpleegomgeving/zittingen/66738e2b-01a0-4257-8cb1-a3349e747009/agendapunten/fe86a672-03f4-4a90-93fe-314828f24f44"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207534468"
GAP = "gap_kapelle_fin_debt_18_87m_pension_5_48m_ocmw_tussen_1_13m_l5"
HIER = "Vlaanderen>Gemeenten>Kapelle-op-den-Bos"

ASSETS = 72780708
ASSETS_2024 = 70027023
CASH = 4310931
CASH_2024 = 3955811
CURRENT = 6697341
FIXED = 66083367
FVA = 6021945
IGS = 4743244
OTHER_FVA = 1274250
OCMW_FVA = 4452
EVA = 0
MVA = 54955614
LEASING = 3821441
IVA = 3020475
LT_RECV = 2085333
SCHULDEN = 27050384
EQUITY = 45730324
CAP_SUBS = 7496584
CUM_PNL = 5727572
REVAL = 1961869
OTHER_EQ = 30544299
FIN_DEBT = 18872856
FIN_DEBT_LT = 17822680
FIN_DEBT_ST = 1050176
FIN_DEBT_2024 = 17860690
NEW_LOANS = 2091597
PENSION = 5478264
PENSION_2024 = 5879556
ST_PROV = 619198
EXPL = 3133935
EXPL_ONTV = 19454923
EXPL_UITG = 16320988
CITY_EXPL = 4083744
OCMW_EXPL = -949809
INVEST = -4683725
BBR = -537625
CUM_PREV = 5078526
AVAIL = 4539484
UNAVAIL = 1417
AFM = 2115685
GECORR = 1766261
PNL = 1047426
TUSSEN = 1134205
PERS = 8400713
FISCAL = 10646141
GEMFONDS = 2486419
POLITIE = 1469318
HVZ = 600153
IGS_SUB = 62079


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


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:120]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


assert abs((CURRENT + FIXED) - ASSETS) < 2
assert abs((IGS + OTHER_FVA + OCMW_FVA) - FVA) < 2
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - (AVAIL + UNAVAIL)) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Kapelle-op-den-Bos BBC jaarrekening 2025 (PDF 138p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Kapelle-op-den-Bos",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1291; 46.37MB CSrapportaal PDF; GR 22.06.2026 uittreksel 23.06.2026 2026/GR/126; "
                "KBO 0207.534.468 / 0212.223.330; assets 72.781m fin debt 18.873m "
                "pension 5.478m OCMW tussen 1.134m AFM +2.116m avail 4.539m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Kapelle-op-den-Bos GR 2026/GR/126 vaststelling JR2025 + uittreksel",
            "url": SRC2_URL,
            "publisher": "Gemeente Kapelle-op-den-Bos",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1291; JR2025 vaststelling GR 22.06.2026; BBR -0.538m cum 4.541m AFM 2.116m "
                "PnL 1.047m tussenkomst 1.13420467m; no AGB; siblings Bekkevoort 1290 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Kapelle-op-den-Bos 0207.534.468",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1291; Stad/gemeente since 01.01.1968; seat Marktplein 29 1880; 9 VE; "
                "burgemeester Mathias Diricx since 02.12.2024; NACE 84.114; "
                "OCMW sibling 0212.223.330 (2 VE; voorzitter Mathias Diricx since 02.12.2024); "
                "AD Siebe Ruykens since 01.08.2018 / FD Liesbeth Van Waeyenberghe (BBC cover)"
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
            "name_nl": "Gemeente Kapelle-op-den-Bos",
            "name_fr": "Commune de Kapelle-op-den-Bos",
            "name_en": "Municipality of Kapelle-op-den-Bos",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.kapelle-op-den-bos.be",
            "foi_email": "financien@kapelle-op-den-bos.be",
            "foi_postal": "Marktplein 29 1880 Kapelle-op-den-Bos",
            "notes": (
                "tick1291 JR2025 GE residual; KBO 0207.534.468 / OCMW 0212.223.330; NIS 23009; "
                "9+2 VE; no AGB; assets 72.781m fin debt 18.873m pension 5.478m "
                "OCMW tussen 1.134m AFM +2.116m avail 4.539m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Kapelle-op-den-Bos",
            "name_fr": "CPAS Kapelle-op-den-Bos",
            "name_en": "OCMW Kapelle-op-den-Bos",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.kapelle-op-den-bos.be",
            "foi_email": "financien@kapelle-op-den-bos.be",
            "foi_postal": "Evert Larockstraat 22 1880 Kapelle-op-den-Bos",
            "notes": (
                "tick1291 JR2025 dual residual; KBO 0212.223.330; J3 expl -0.950m; "
                "city tussenkomst 1.134m; kengetallen cash 0.251m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_kap_assets_2025", "2025", ASSETS, "J4 assets 72.780708m vs 70.027023m"),
    ("bud_kap_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 70.027023m"),
    ("bud_kap_cash_2025", "2025", CASH, "J4 cash 4.310931m vs 3.955811m"),
    ("bud_kap_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 3.955811m"),
    ("bud_kap_fva_2025", "2025", FVA, "J4/T5 FVA 6.021945m; EVA 0 + IGS 4.743244 + OCMW-ver 0.004452"),
    ("bud_kap_igs_2025", "2025", IGS, "J4/T5 IGS FVA 4.743244m"),
    ("bud_kap_mva_2025", "2025", MVA, "J4 MVA 54.955614m; leasing 3.821441m"),
    ("bud_kap_leasing_2025", "2025", LEASING, "T5 leasing MVA 3.821441m vs 3.689575m"),
    ("bud_kap_equity_2025", "2025", EQUITY, "J4 nettoactief 45.730324m vs 44.737319m"),
    ("bud_kap_fin_debt_2025", "2025", FIN_DEBT, "T4/J4 fin debt 18.872856m (LT 17.823 + ST due 1.050)"),
    ("bud_kap_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 17.860690m"),
    ("bud_kap_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 2.091597m"),
    ("bud_kap_pension_2025", "2025", PENSION, "J4 LT pension 5.478264m vs 5.879556m"),
    ("bud_kap_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 0.619198m"),
    ("bud_kap_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +3.133935m"),
    ("bud_kap_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 19.454923m"),
    ("bud_kap_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 16.320988m"),
    ("bud_kap_city_expl_2025", "2025", CITY_EXPL, "J3/kengetallen city expl +4.083744m (18.391/14.307)"),
    ("bud_kap_ocmw_expl_2025", "2025", OCMW_EXPL, "J3/kengetallen OCMW expl -0.949809m (1.064/2.014)"),
    ("bud_kap_invest_2025", "2025", INVEST, "J2 invest -4.683725m"),
    ("bud_kap_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar -0.537625m"),
    ("bud_kap_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 4.539484m"),
    ("bud_kap_afm_2025", "2025", AFM, "J2 AFM +2.115685m"),
    ("bud_kap_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1.766261m"),
    ("bud_kap_pnl_2025", "2025", PNL, "J5 PnL +1.047426m (city/OCMW split unpublished)"),
    ("bud_kap_tussen_2025", "2025", TUSSEN, "GR uittreksel city->OCMW tussenkomst 1.13420467m"),
    ("bud_kap_pers_2025", "2025", PERS, "T2/J5 bezoldigingen 8.400713m; VTE unpublished"),
    ("bud_kap_fiscal_2025", "2025", FISCAL, "J5 fiscal 10.646141m"),
    ("bud_kap_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.486419m"),
    ("bud_kap_politie_2025", "2025", POLITIE, "T2 politiezone 1.469318m"),
    ("bud_kap_hvz_2025", "2025", HVZ, "T2 HVZ 0.600153m"),
    ("bud_kap_igs_sub_2025", "2025", IGS_SUB, "T2 IGS werksub 0.062079m"),
    ("bud_kap_afl_2025", "2025", 1079431, "T4 periodieke aflossingen 1.079431m"),
    ("bud_kap_iva_2025", "2025", IVA, "J4 IVA 3.020475m"),
    ("bud_kap_reval_2025", "2025", REVAL, "J4 herwaarderingsreserves 1.961869m"),
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
            "basis": "executed",
            "source_id": SRC,
            "confidence": "strong",
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_kap_fin_debt_18_87m_2025",
        "Kapelle-op-den-Bos YE2025 fin debt 18.873m",
        "18872856",
        "T4/J4 18.872856m (LT 17.823 + ST due 1.050) rising vs 17.861m; new loans 2.092m; MJP 2026 20.844m",
        "Publish per-loan creditors + 2026-2031 amort FOI",
    ),
    (
        "comm_kap_pension_5_48m_2025",
        "Kapelle-op-den-Bos YE2025 pension LT 5.478m",
        "5478264",
        "J4 LT pension 5.478264m vs 5.879556m; ST prov 0.619m; city/OCMW split unpublished",
        "Publish city/OCMW split + responsabilisering FOI",
    ),
    (
        "comm_kap_ocmw_tussen_1_13m_2025",
        "Kapelle-op-den-Bos 2025 OCMW tussenkomst 1.134m",
        "1134205",
        "GR 2026/GR/126 city->OCMW 1.13420467m vs OCMW J3 expl -0.950m; kengetallen OCMW cash 0.251m",
        "Publish cash vs book transfer + 2026-2031 pad FOI",
    ),
    (
        "comm_kap_pers_8_40m_2025",
        "Kapelle-op-den-Bos 2025 personeel 8.401m",
        "8400713",
        "T2/J5 8.400713m; onderwijs andere ov 1.894m; VTE unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_kap_politie_hvz_2_07m_2025",
        "Kapelle-op-den-Bos 2025 politie+HVZ 2.069m",
        "2069471",
        "T2 politiezone 1.469318 + HVZ 0.600153; IGS 0.062",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_kap_new_loans_2_09m_2025",
        "Kapelle-op-den-Bos 2025 new loans 2.092m",
        "2091597",
        "T4 new loans 2.091597m vs invest -4.684m; fin debt jumps 17.861 to 18.873m",
        "Publish creditor + purpose of 2.092m new loans FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Kapelle-op-den-Bos / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Kapelle-op-den-Bos GR 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Kapelle-op-den-Bos (no AGB)",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_kap_fin_debt_18_87m_2025",
        "Kapelle-op-den-Bos YE2025 fin debt 18.87m",
        "18872856",
        "6.5",
        "7.5",
        "Publish per-loan creditors + amort 2026-2031",
        "fin debt 18.873m rising vs 17.861m; new loans 2.092m",
    ),
    (
        "lb_kap_pension_5_48m_2025",
        "Kapelle-op-den-Bos YE2025 pension LT 5.48m",
        "5478264",
        "6.5",
        "6.5",
        "Publish city/OCMW split + responsabilisering",
        "pension 5.478m vs 5.880m; ST prov 0.619m",
    ),
    (
        "lb_kap_ocmw_tussen_1_13m_2025",
        "Kapelle-op-den-Bos 2025 OCMW tussenkomst 1.13m",
        "1134205",
        "7.0",
        "6.0",
        "Publish cash vs book transfer + 2026-2031 pad",
        "tussen 1.134m vs OCMW expl -0.950m",
    ),
    (
        "lb_kap_pers_8_40m_2025",
        "Kapelle-op-den-Bos 2025 personeel 8.40m",
        "8400713",
        "5.5",
        "6.5",
        "Publish paid VTE vs formatie",
        "pers 8.401m; VTE unpublished",
    ),
    (
        "lb_kap_politie_hvz_2_07m_2025",
        "Kapelle-op-den-Bos 2025 politie+HVZ 2.07m",
        "2069471",
        "6.0",
        "6.0",
        "Publish zone split + 2026-2031",
        "politie 1.469 + HVZ 0.600",
    ),
    (
        "lb_kap_new_loans_2_09m_2025",
        "Kapelle-op-den-Bos 2025 new loans 2.09m",
        "2091597",
        "6.5",
        "6.5",
        "Publish creditor + purpose of new loans",
        "new loans 2.092m beside invest -4.684m",
    ),
    (
        "lb_kap_avail_4_54m_2025",
        "Kapelle-op-den-Bos YE2025 avail BBR 4.54m",
        "4539484",
        "5.0",
        "6.5",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 4.539m; BBR year -0.538m; AFM +2.116m; cash 4.311m",
    ),
]
n = append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": iid,
            "name": name,
            "level": "L5",
            "type": "local_budget_line",
            "hierarchy_path": HIER + ">jr2025_L5",
            "annual_cost_eur": amt,
            "total_cost_eur": amt,
            "tco_notes": tco,
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Inwoners Kapelle-op-den-Bos / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Kapelle-op-den-Bos (no AGB)",
            "measured_outcome": (
                "assets 72.781m / fin debt 18.873m / pension 5.478m / "
                "OCMW tussen 1.134m / AFM +2.116m / avail 4.539m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; OCMW dual FOI",
        }
        for iid, name, amt, absu, cost, cut, tco in lb_rows
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
                "T4 per-loan creditors for fin debt 18.872856m + new loans 2.091597m "
                "+ pension LT 5.478264 city/OCMW split + responsabilisering "
                "+ OCMW tussenkomst 1.13420467m cash vs book + 2026-2031 pad "
                "+ IGS FVA 4.743244 inventory + EVA 0 confirm "
                "+ paid VTE behind pers 8.400713m "
                "+ politiezone/HVZ 2.069471m zone split "
                "+ T2 fiscal split behind J5 10.646141m"
            ),
            "why_it_matters": (
                "Unmined Kapelle-op-den-Bos GE after residual dual hunt. No AGB. "
                "Fin debt 18.873m rising with new loans 2.092m. "
                "OCMW dual 1.134m vs expl -0.950m. "
                "Avail 4.539m with BBR year -0.538m. VTE unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Kapelle-op-den-Bos (gemeente + OCMW)",
            "recipient_email": "financien@kapelle-op-den-bos.be",
            "recipient_postal": "Marktplein 29 1880 Kapelle-op-den-Bos",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_kap_fin_debt_18_87m_2025",
            "linked_leaderboard_id": "lb_kap_fin_debt_18_87m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1291",
    "title": "Stad+OCMW Kapelle-op-den-Bos JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Kapelle-op-den-Bos JR2025 BBC text + KBO; "
        "KBO 0207.534.468 / 0212.223.330; assets 72.781m / fin debt 18.873m / "
        "pension 5.478m / OCMW tussen 1.134m / AFM +2.116m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:40:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1291 Stad+OCMW Kapelle-op-den-Bos JR2025 GE residual; KBO 0207.534.468/0212.223.330; "
        "assets 72.781m fin debt 18.873m pension 5.478m AFM +2.116m gecorr +1.766m "
        "BBR -0.538m avail 4.539m cash 4.311m OCMW tussen 1.134m "
        "pers 8.401m politie 1.469m new loans 2.092m; no AGB; FOI ready not sent; "
        "next rq_1292 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1292",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(Gent dual AGB cluster 1255-1259 + Antwerp AG 1260-1265 + Atlas 1266 + Amal 1267 "
        "+ Fietsambassade 1268 + Mintus 1269 + MAC 1270 + AGB Kruibeke/BKZ sport 1271 "
        "+ AGB Tienen 1272 + AG Museum Leuven 1273 + Stad+OCMW Tienen 1274 "
        "+ AGB IBOGEM 1275 + Motena Roeselare 1276 + AGBPB Bonheiden 1277 "
        "+ AGB Trupark 1278 + Stad+OCMW Machelen 1279 + Stad+OCMW Gingelom 1280 "
        "+ Stad+OCMW Wezembeek-Oppem 1281 + AGB Masterplan HH 1282 + AGB Sport HH 1283 "
        "+ Stad+OCMW Kraainem 1284 + Stad+OCMW Houthalen-Helchteren 1285 "
        "+ AGB SCO Ronse 1286 + Stad+OCMW Ronse 1287 + De Zilveren Zwaan 1288 "
        "+ Stad+OCMW Tielt-Winge 1289 + Stad+OCMW Bekkevoort 1290 "
        "+ Stad+OCMW Kapelle-op-den-Bos 1291 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / AGB Heist 1209 / city Heist 857; "
        "Steenokkerzeel city+OCMW JR2025 listed on city site only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only / "
        "Oosterzele De Kluize unless a fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; "
        "skip AGB Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "skip Dilbeek/Wijnegem city GE already mined; skip Wingene/Genk/Brasschaat AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Cultuur Geel 1252; "
        "skip AGB Deinze 941 / AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1291 after Stad+OCMW Kapelle-op-den-Bos JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1291", rq_new, rq_spawn)
print("research_queue 1291", found, "spawned_1292", spawned)

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
            "last_unit_id": "rq_1291",
            "ticks_completed": "1291",
            "paused": "no",
            "notes": (
                "tick1291 Stad+OCMW Kapelle-op-den-Bos JR2025 GE residual; KBO 0207.534.468/0212.223.330; "
                "assets 72.781m fin debt 18.873m pension 5.478m OCMW tussen 1.134m; "
                "FOI ready; next rq_1292 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1291_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
