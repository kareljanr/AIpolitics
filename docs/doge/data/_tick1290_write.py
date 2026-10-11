# -*- coding: utf-8 -*-
"""Tick 1290 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Bekkevoort JR2025 GE residual + every-10 progress."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:40:00Z"
TICK = 1290
SRC = "src_bekkevoort_jr2025_bbc"
SRC2 = "src_bekkevoort_jr2025_portal"
SRC3 = "src_kbo_bekkevoort_0207516157"
ENT = "city_bekkevoort"
OCMW = "ocmw_bekkevoort"
SRC_URL = "https://bekkevoort.meetingburger.net/Pages/HandleFile.ashx?id=8a135359-8d80-44b7-9219-92dff635097c&download=1"
SRC2_URL = "https://bekkevoort.meetingburger.net/bekendmakingen/beleidsdocumenten/e697c574-11af-43ba-b581-0db0453e50b3"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207516157"
GAP = "gap_bekkevoort_fin_debt_9_77m_pension_2_91m_igs_reval_5_90m_l5"
HIER = "Vlaanderen>Gemeenten>Bekkevoort"

ASSETS = 40650234
ASSETS_2024 = 32382933
CASH = 7665643
CASH_2024 = 7553061
CURRENT = 11613752
FIXED = 29036482
FVA = 10682602
IGS = 8276798
OTHER_FVA = 2405804
EVA = 0
MVA = 16720072
LEASING = 840085
IVA = 394380
LT_RECV = 1239428
SCHULDEN = 16783198
EQUITY = 23867036
CAP_SUBS = 3719082
CUM_PNL = 3655770
REVAL = 5906857
OTHER_EQ = 10585327
FIN_DEBT = 9765763
FIN_DEBT_LT = 9271682
FIN_DEBT_ST = 494081
FIN_DEBT_2024 = 10204103
NEW_LOANS = 98496
PENSION = 2908967
PENSION_2024 = 2785118
ST_PROV = 422997
EXPL = 2641303
EXPL_ONTV = 16043199
EXPL_UITG = 13401896
CITY_EXPL = 3270945
OCMW_EXPL = -629642
INVEST = -1625594
BBR = 691708
CUM_PREV = 7453213
AVAIL = 8140556
UNAVAIL = 4365
AFM = 2146106
GECORR = 1824975
PNL = 1146157
PNL_CITY = 2017633
PNL_OCMW = -871476
TUSSEN = 800000
PERS = 6655804
FISCAL = 8694647
OV = 2441600
APB = 3312807
OTHER_TAX = 2811520
GEMFONDS = 2153511
POLITIE = 617968
HVZ = 402145
IGS_SUB = 151281
IGS_REVAL = 5902111
OCMW_EQUITY = -51472
VTE = "60.96"


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
assert abs((IGS + OTHER_FVA) - FVA) < 2
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - (AVAIL + UNAVAIL)) < 2
assert abs((PNL_CITY + PNL_OCMW) - PNL) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
assert abs((EXPL - 495197) - AFM) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Bekkevoort BBC jaarrekening 2025 (text PDF 96p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Bekkevoort",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1290; 5.49MB text PDF; GR+RVMW 29.06.2026 pub 03.07.2026; "
                "KBO 0207.516.157 / 0212.239.166; assets 40.650m fin debt 9.766m "
                "pension 2.909m IGS reval 5.902m OCMW tussen 0.800m AFM +2.146m avail 8.141m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Bekkevoort meetingburger bekendmaking JR2025 gemeente",
            "url": SRC2_URL,
            "publisher": "Gemeente Bekkevoort",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1290; JR2025 vaststelling GR 29.06.2026 pub 03.07.2026; "
                "BBR 0.692m cum 8.145m AFM 2.146m; no AGB; siblings Tielt-Winge 1289 / Glabbeek 1224 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Bekkevoort 0207.516.157",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1290; Stad/gemeente since 01.01.1968; seat Eugeen Coolsstraat 17 3460; 3 VE; "
                "burgemeester Hans Vandenberg since 01.01.2013; NACE 84.114; "
                "OCMW sibling 0212.239.166 (1 VE; voorzitter Hans Vandenberg since 01.01.2019); "
                "AD Hilde Goedhuys / FD Mandy Lekens (BBC cover)"
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
            "name_nl": "Gemeente Bekkevoort",
            "name_fr": "Commune de Bekkevoort",
            "name_en": "Municipality of Bekkevoort",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.bekkevoort.be",
            "foi_email": "financien@bekkevoort.be",
            "foi_postal": "Eugeen Coolsstraat 17 3460 Bekkevoort",
            "notes": (
                "tick1290 JR2025 GE residual; KBO 0207.516.157 / OCMW 0212.239.166; NIS 24008; "
                "3+1 VE; no AGB; assets 40.650m fin debt 9.766m pension 2.909m "
                "IGS reval 5.902m OCMW tussen 0.800m AFM +2.146m avail 8.141m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Bekkevoort",
            "name_fr": "CPAS Bekkevoort",
            "name_en": "OCMW Bekkevoort",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.bekkevoort.be",
            "foi_email": "financien@bekkevoort.be",
            "foi_postal": "Eugeen Coolsstraat 17 3460 Bekkevoort",
            "notes": (
                "tick1290 JR2025 dual residual; KBO 0212.239.166; J5 PnL -0.871m; "
                "city tussenkomst 0.800m; J3 expl -0.630m; equity -0.051m NEG; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_bek_assets_2025", "2025", ASSETS, "J4 assets 40.650234m vs 32.382933m jump 8.267m"),
    ("bud_bek_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 32.382933m"),
    ("bud_bek_cash_2025", "2025", CASH, "J4 cash 7.665643m vs 7.553061m"),
    ("bud_bek_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 7.553061m"),
    ("bud_bek_fva_2025", "2025", FVA, "J4/T5 FVA 10.682602m; EVA 0 + IGS 8.276798"),
    ("bud_bek_igs_2025", "2025", IGS, "J4/T5 IGS FVA 8.276798m"),
    ("bud_bek_igs_reval_2025", "2025", IGS_REVAL, "T5 IGS EV-reval 5.902111m (no cash)"),
    ("bud_bek_mva_2025", "2025", MVA, "J4 MVA 16.720072m; leasing 0.840085m"),
    ("bud_bek_leasing_2025", "2025", LEASING, "T5 leasing MVA 0.840085m vs 0.806914m"),
    ("bud_bek_equity_2025", "2025", EQUITY, "T5 nettoactief 23.867036m vs 16.818594m"),
    ("bud_bek_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 9.765763m (LT 9.272 + ST due 0.494)"),
    ("bud_bek_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 10.204103m"),
    ("bud_bek_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.098496m leasing"),
    ("bud_bek_pension_2025", "2025", PENSION, "J4 LT pension 2.908967m vs 2.785118m"),
    ("bud_bek_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 0.422997m"),
    ("bud_bek_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +2.641303m"),
    ("bud_bek_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 16.043199m"),
    ("bud_bek_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 13.401896m"),
    ("bud_bek_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +3.270945m (14.401/11.130)"),
    ("bud_bek_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -0.629642m (1.642/2.272)"),
    ("bud_bek_invest_2025", "2025", INVEST, "J2 invest -1.625594m"),
    ("bud_bek_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +0.691708m"),
    ("bud_bek_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 8.140556m"),
    ("bud_bek_afm_2025", "2025", AFM, "J2 AFM +2.146106m"),
    ("bud_bek_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1.824975m"),
    ("bud_bek_pnl_2025", "2025", PNL, "J5 PnL +1.146157m (city +2.018 / OCMW -0.871)"),
    ("bud_bek_tussen_2025", "2025", TUSSEN, "mutatiestaat city->OCMW tussenkomst 0.800000m"),
    ("bud_bek_pers_2025", "2025", PERS, "T2/J5 bezoldigingen 6.655804m; VTE 60.96"),
    ("bud_bek_fiscal_2025", "2025", FISCAL, "J5 fiscal 8.694647m (OV 2.442 + APB 3.313 + other 2.812)"),
    ("bud_bek_ov_2025", "2025", OV, "T2 opcentiemen OV 2.441600m"),
    ("bud_bek_apb_2025", "2025", APB, "T2 aanvullende PB 3.312807m"),
    ("bud_bek_other_tax_2025", "2025", OTHER_TAX, "T2 andere belastingen/boetes 2.811520m (GAS5 2.237m)"),
    ("bud_bek_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.153511m"),
    ("bud_bek_politie_2025", "2025", POLITIE, "T2 politiezone Hageland 0.617968m JUMP vs 0.520299m"),
    ("bud_bek_hvz_2025", "2025", HVZ, "T2 HVZ 0.402145m vs 0.351440m"),
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
        "comm_bek_fin_debt_9_77m_2025",
        "Bekkevoort YE2025 fin debt 9.766m",
        "9765763",
        "T4 9.765763m (LT 9.272 + ST due 0.494) declining vs 10.204m; new lease 0.098m; extra repay 0.042m",
        "Publish per-loan creditors + 2026-2031 amort FOI",
    ),
    (
        "comm_bek_pension_2_91m_2025",
        "Bekkevoort YE2025 pension LT 2.909m",
        "2908967",
        "J4 LT pension 2.908967m vs 2.785118m; ST prov 0.423m; city/OCMW split unpublished",
        "Publish city/OCMW split + 2e pijler korting FOI",
    ),
    (
        "comm_bek_ocmw_tussen_0_80m_2025",
        "Bekkevoort 2025 OCMW tussenkomst 0.800m",
        "800000",
        "Mutatiestaat city->OCMW 0.800m vs OCMW J5 -0.871m; J3 OCMW expl -0.630m; OCMW equity -0.051m NEG",
        "Publish cash vs book transfer + 2026-2031 pad FOI",
    ),
    (
        "comm_bek_pers_6_66m_2025",
        "Bekkevoort 2025 personeel 6.656m",
        "6655804",
        "T2/J5 6.655804m; VTE paid 60.96 (city 37.46 / OCMW 23.50)",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_bek_politie_hvz_1_02m_2025",
        "Bekkevoort 2025 politie+HVZ 1.020m",
        "1020113",
        "T2 politie Hageland 0.617968 JUMP vs 0.520 + HVZ 0.402 vs 0.351; IGS 0.151",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_bek_igs_reval_5_90m_2025",
        "Bekkevoort YE2025 IGS EV-reval 5.902m",
        "5902111",
        "T5 IGS reval 5.902111m lifts IGS FVA 2.368->8.277m and reval reserves 0.005->5.907m; no cash; EVA 0",
        "Publish IGS inventory + Fluvius/Iverlek split FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Bekkevoort / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Bekkevoort GR+RVMW 29.06.2026",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Bekkevoort (no AGB)",
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
        "lb_bek_fin_debt_9_77m_2025",
        "Bekkevoort YE2025 fin debt 9.77m",
        "9765763",
        "6.5",
        "7.0",
        "Publish per-loan creditors + amort 2026-2031",
        "fin debt 9.766m declining vs 10.204m; new lease 0.098m",
    ),
    (
        "lb_bek_pension_2_91m_2025",
        "Bekkevoort YE2025 pension LT 2.91m",
        "2908967",
        "6.5",
        "6.0",
        "Publish city/OCMW split + responsabilisering",
        "pension 2.909m vs 2.785m; ST prov 0.423m",
    ),
    (
        "lb_bek_ocmw_tussen_0_80m_2025",
        "Bekkevoort 2025 OCMW tussenkomst 0.80m",
        "800000",
        "7.0",
        "6.0",
        "Publish cash vs book transfer + 2026-2031 pad",
        "tussen 0.800m vs OCMW PnL -0.871m; equity -0.051m NEG",
    ),
    (
        "lb_bek_pers_6_66m_2025",
        "Bekkevoort 2025 personeel 6.66m",
        "6655804",
        "5.5",
        "6.5",
        "Publish paid VTE vs formatie",
        "pers 6.656m; VTE 60.96 city 37.46 / OCMW 23.50",
    ),
    (
        "lb_bek_politie_hvz_1_02m_2025",
        "Bekkevoort 2025 politie+HVZ 1.02m",
        "1020113",
        "6.0",
        "6.0",
        "Publish zone split + 2026-2031",
        "politie Hageland 0.618 JUMP + HVZ 0.402",
    ),
    (
        "lb_bek_igs_reval_5_90m_2025",
        "Bekkevoort YE2025 IGS EV-reval 5.90m",
        "5902111",
        "7.0",
        "6.5",
        "Publish IGS inventory + Fluvius/Iverlek split",
        "IGS reval 5.902m no cash; IGS FVA 8.277m EVA 0",
    ),
    (
        "lb_bek_avail_8_14m_2025",
        "Bekkevoort YE2025 avail BBR 8.14m",
        "8140556",
        "5.0",
        "7.0",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 8.141m; BBR year +0.692m; AFM +2.146m; cash 7.666m",
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
            "beneficiaries": "Inwoners Bekkevoort / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Bekkevoort (no AGB)",
            "measured_outcome": (
                "assets 40.650m / fin debt 9.766m / pension 2.909m / "
                "IGS reval 5.902m / OCMW tussen 0.800m / AFM +2.146m / avail 8.141m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; OCMW dual FOI",
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
                "T4 per-loan creditors for fin debt 9.765763m + lease 0.098496m "
                "+ pension LT 2.908967 city/OCMW split + responsabilisering "
                "+ OCMW tussenkomst 0.800000m cash vs book + 2026-2031 pad "
                "+ IGS FVA 8.276798 inventory after EV-reval 5.902111 "
                "+ paid VTE behind pers 6.655804m (table 60.96) "
                "+ politiezone Hageland/HVZ 1.020113m zone split "
                "+ other tax/GAS5 2.811520m"
            ),
            "why_it_matters": (
                "Unmined Bekkevoort GE after residual dual hunt. No AGB. "
                "Fin debt 9.766m declining. IGS EV-reval 5.902m no cash. "
                "OCMW dual 0.800m vs PnL -0.871m / equity -0.051m NEG. "
                "Avail 8.141m. VTE 60.96 published but formatie unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Bekkevoort (gemeente + OCMW)",
            "recipient_email": "financien@bekkevoort.be",
            "recipient_postal": "Eugeen Coolsstraat 17 3460 Bekkevoort",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_bek_fin_debt_9_77m_2025",
            "linked_leaderboard_id": "lb_bek_fin_debt_9_77m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1290",
    "title": "Stad+OCMW Bekkevoort JR2025 GE residual + every-10 progress",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Bekkevoort JR2025 BBC text + KBO; "
        "KBO 0207.516.157 / 0212.239.166; assets 40.650m / fin debt 9.766m / "
        "pension 2.909m / IGS reval 5.902m / OCMW tussen 0.800m / AFM +2.146m; "
        "every-10 refresh; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:20:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1290 Stad+OCMW Bekkevoort JR2025 GE residual + every-10; KBO 0207.516.157/0212.239.166; "
        "assets 40.650m fin debt 9.766m pension 2.909m AFM +2.146m gecorr +1.825m "
        "BBR +0.692m avail 8.141m cash 7.666m IGS reval 5.902m OCMW tussen 0.800m "
        "pers 6.656m VTE 60.96 politie 0.618m JUMP; no AGB; FOI ready not sent; "
        "next rq_1291 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1291",
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
        "+ Stad+OCMW Tielt-Winge 1289 + Stad+OCMW Bekkevoort 1290 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / AGB Heist 1209 / city Heist 857; "
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
    "notes": "spawned tick1290 after Stad+OCMW Bekkevoort JR2025 GE residual + every-10; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1290", rq_new, rq_spawn)
print("research_queue 1290", found, "spawned_1291", spawned)

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
            "last_unit_id": "rq_1290",
            "ticks_completed": "1290",
            "paused": "no",
            "notes": (
                "tick1290 Stad+OCMW Bekkevoort JR2025 GE residual + every-10; KBO 0207.516.157/0212.239.166; "
                "assets 40.650m fin debt 9.766m pension 2.909m IGS reval 5.902m OCMW tussen 0.800m; "
                "FOI ready; next rq_1291 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1290_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
