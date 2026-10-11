# -*- coding: utf-8 -*-
"""Tick 1292 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Huldenberg JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:45:00Z"
TICK = 1292
SRC = "src_huldb_jr2025_bbc"
SRC2 = "src_huldb_jr2025_gr"
SRC3 = "src_kbo_huldb_0207519820"
ENT = "city_huldenberg"
OCMW = "ocmw_huldenberg"
SRC_URL = "https://www.huldenberg.be/sites/default/files/2026-06/Jaarrekening-2025.pdf"
SRC2_URL = "https://www.huldenberg.be/sites/default/files/2026-06/23-06-2026-1603_GR_uittreksel_Vaststelling-van-de-jaarrekening-deel-gemeent.pdf"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207519820"
GAP = "gap_huldb_fin_debt_9_56m_pension_4_37m_ocmw_tussen_1_25m_l5"
HIER = "Vlaanderen>Gemeenten>Huldenberg"

ASSETS = 68709998.63
ASSETS_2024 = 67271944.95
CASH = 5921524.18
CASH_2024 = 5637576.16
CURRENT = 10236762.07
FIXED = 58473236.56
FVA = 10904349.79
IGS = 9540231.54
OTHER_FVA = 1364118.25
EVA = 0
MVA = 47316826.50
LEASING = 318399.82
IVA = 252060.27
SCHULDEN = 16551703.91
EQUITY = 52158294.72
CAP_SUBS = 14216104.76
CUM_PNL = 17870390.34
REVAL = 1781113.59
OTHER_EQ = 18290686.03
FIN_DEBT = 9556788.86
FIN_DEBT_LT = 8740567.72
FIN_DEBT_ST = 816221.14
FIN_DEBT_2024 = 10321927.87
NEW_LOANS = 0
PENSION = 4370175.13
PENSION_2024 = 5251814.86
PENSION_RESPO = 1939000
ST_PROV = 639645.04
EXPL = 3719976.86
EXPL_ONTV = 24901756.14
EXPL_UITG = 21181779.28
CITY_EXPL = 4974264.25
OCMW_EXPL = -1254287.39
INVEST = -909840.43
BBR = 2044997.42
CUM_PREV = 6206669.77
AVAIL = 8251667.19
AFM = 2954837.85
GECORR = 2894222.63
PNL = 2968333.75
CITY_PNL = 4122341
OCMW_PNL = -1154007
TUSSEN = 1254287.39
PERS = 13182150.71
ONDERWIJS = 6639463.94
FISCAL = 11398674.53
OV = 3386320.90
APB = 6843011.37
GEMFONDS = 2412218.55
POLITIE = 1080869.00
HVZ = 533731.86
HVZ_INV = 105684.74
IGS_SUB = 583634.01
AFL = 765139.01
OCMW_EQUITY = -952609
BANK_REM = 9113595.89
OTHER_LOAN = 443192.97


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
assert abs((IGS + OTHER_FVA + EVA) - FVA) < 2
assert abs((FVA + MVA + IVA) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
assert abs((BANK_REM + OTHER_LOAN) - FIN_DEBT) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Huldenberg BBC jaarrekening 2025 (PDF 144p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Huldenberg",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1292; 5.73MB BBC PDF; GR+RVMW 18.06.2026 pub 23.06.2026; "
                "KBO 0207.519.820 / 0212.221.152; assets 68.710m fin debt 9.557m "
                "pension 4.370m OCMW tussen 1.254m AFM +2.955m avail 8.252m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Huldenberg GR 18.06.2026 vaststelling JR2025 + uittreksel",
            "url": SRC2_URL,
            "publisher": "Gemeente Huldenberg",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1292; JR2025 vaststelling GR+RVMW 18.06.2026; BBR +2.045m cum 8.252m AFM 2.955m "
                "tussenkomst 1.25428739m; no AGB; siblings Kapelle-op-den-Bos 1291 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Huldenberg 0207.519.820",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1292; Stad/gemeente since 01.01.1968; seat Gemeenteplein 1 3040; 9 VE; "
                "burgemeester Danny Vangoidtsenhoven since 02.01.2013; NACE 84.114; "
                "OCMW sibling 0212.221.152 (1 VE; voorzitter Danny Vangoidtsenhoven since 01.01.2019); "
                "AD Caroline Peters since 21.06.2018 / FD Hilde De Keyser (BBC cover)"
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
            "name_nl": "Gemeente Huldenberg",
            "name_fr": "Commune de Huldenberg",
            "name_en": "Municipality of Huldenberg",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.huldenberg.be",
            "foi_email": "info@huldenberg.be",
            "foi_postal": "Gemeenteplein 1 3040 Huldenberg",
            "notes": (
                "tick1292 JR2025 GE residual; KBO 0207.519.820 / OCMW 0212.221.152; NIS 24045; "
                "9+1 VE; no AGB; assets 68.710m fin debt 9.557m pension 4.370m "
                "OCMW tussen 1.254m AFM +2.955m avail 8.252m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Huldenberg",
            "name_fr": "CPAS Huldenberg",
            "name_en": "OCMW Huldenberg",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.huldenberg.be",
            "foi_email": "info@huldenberg.be",
            "foi_postal": "Gemeenteplein 1 bus A 3040 Huldenberg",
            "notes": (
                "tick1292 JR2025 dual residual; KBO 0212.221.152; J3 expl -1.254m; "
                "city tussenkomst 1.254m; T5 equity -0.953m NEG; kengetallen cash 0.107m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_huldb_assets_2025", "2025", ASSETS, "J4 assets 68.709999m vs 67.271945m"),
    ("bud_huldb_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 67.271945m"),
    ("bud_huldb_cash_2025", "2025", CASH, "J4 cash 5.921524m vs 5.637576m"),
    ("bud_huldb_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 5.637576m"),
    ("bud_huldb_fva_2025", "2025", FVA, "J4/T5 FVA 10.904350m; EVA 0 + IGS 9.540232"),
    ("bud_huldb_igs_2025", "2025", IGS, "J4/T5 IGS FVA 9.540232m"),
    ("bud_huldb_mva_2025", "2025", MVA, "J4 MVA 47.316827m; leasing 0.318400m"),
    ("bud_huldb_leasing_2025", "2025", LEASING, "T5 leasing MVA 0.318400m vs 0.424533m"),
    ("bud_huldb_equity_2025", "2025", EQUITY, "J4 nettoactief 52.158295m vs 48.187919m"),
    ("bud_huldb_fin_debt_2025", "2025", FIN_DEBT, "T4/J4 fin debt 9.556789m (LT 8.741 + ST due 0.816)"),
    ("bud_huldb_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 10.321928m"),
    ("bud_huldb_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0"),
    ("bud_huldb_pension_2025", "2025", PENSION, "J4 LT pension 4.370175m vs 5.251815m"),
    ("bud_huldb_pension_respo_2025", "2025", PENSION_RESPO, "proefbalans responsabilisering 1.939m"),
    ("bud_huldb_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 0.639645m"),
    ("bud_huldb_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +3.719977m"),
    ("bud_huldb_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 24.901756m"),
    ("bud_huldb_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 21.181779m"),
    ("bud_huldb_city_expl_2025", "2025", CITY_EXPL, "J3/kengetallen city expl +4.974264m (23.799/18.825)"),
    ("bud_huldb_ocmw_expl_2025", "2025", OCMW_EXPL, "J3/kengetallen OCMW expl -1.254287m (1.103/2.357)"),
    ("bud_huldb_invest_2025", "2025", INVEST, "J2 invest -0.909840m vs initieel 12.223m"),
    ("bud_huldb_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +2.044997m"),
    ("bud_huldb_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 8.251667m"),
    ("bud_huldb_afm_2025", "2025", AFM, "J2 AFM +2.954838m"),
    ("bud_huldb_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +2.894223m"),
    ("bud_huldb_pnl_2025", "2025", PNL, "J5 PnL +2.968334m (city +4.122 / OCMW -1.154)"),
    ("bud_huldb_tussen_2025", "2025", TUSSEN, "GR uittreksel city->OCMW tussenkomst 1.25428739m"),
    ("bud_huldb_pers_2025", "2025", PERS, "T2/J5 bezoldigingen 13.182151m; onderwijs andere ov 6.639m JUMP"),
    ("bud_huldb_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 11.398675m"),
    ("bud_huldb_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.412219m"),
    ("bud_huldb_politie_2025", "2025", POLITIE, "T2 politiezone Voer en Dijle 1.080869m"),
    ("bud_huldb_hvz_2025", "2025", HVZ, "T2 HVZ Oost-VB 0.533732m"),
    ("bud_huldb_hvz_inv_2025", "2025", HVZ_INV, "T2 HVZ invest 0.105685m"),
    ("bud_huldb_igs_sub_2025", "2025", IGS_SUB, "T2 IGS werksub 0.583634m"),
    ("bud_huldb_afl_2025", "2025", AFL, "T4 periodieke aflossingen 0.765139m"),
    ("bud_huldb_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -0.952609m NEG"),
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
        "comm_huldb_fin_debt_9_56m_2025",
        "Huldenberg YE2025 fin debt 9.557m",
        "9556788.86",
        "T4/J4 9.556789m (LT 8.741 + ST due 0.816) declining vs 10.322m; new loans 0; bank 9.114m + Iverlek/Finilek 0.443m",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_huldb_pension_4_37m_2025",
        "Huldenberg YE2025 pension LT 4.370m",
        "4370175.13",
        "J4 LT pension 4.370175m vs 5.251815m; respo 1.939m; ST prov 0.640m; city/OCMW split unpublished",
        "Publish city/OCMW split + responsabilisering FOI",
    ),
    (
        "comm_huldb_ocmw_tussen_1_25m_2025",
        "Huldenberg 2025 OCMW tussenkomst 1.254m",
        "1254287.39",
        "GR 18.06.2026 city->OCMW 1.25428739m vs OCMW J3 expl -1.254m; T5 OCMW equity -0.953m NEG; cash 0.107m",
        "Publish cash vs book transfer + 2026-2031 pad FOI",
    ),
    (
        "comm_huldb_pers_13_18m_2025",
        "Huldenberg 2025 personeel 13.182m",
        "13182150.71",
        "T2/J5 13.182151m; onderwijs andere ov 6.639m JUMP vs 0.622m (registratie); paid VTE unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_huldb_politie_hvz_1_61m_2025",
        "Huldenberg 2025 politie+HVZ 1.615m",
        "1614600.86",
        "T2 politiezone Voer en Dijle 1.080869 + HVZ 0.533732; HVZ invest 0.106",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_huldb_invest_gap_2025",
        "Huldenberg 2025 invest vs initieel 12.223m",
        "3052380.51",
        "J2 invest uitg 3.052m vs initieel 12.223m (~25%) / eindkrediet 5.242m; HLN 16.06.2026 debate",
        "Publish unrealised 2025 project list + 2026 carry FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Huldenberg / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Huldenberg GR 18.06.2026",
            "decision_date": "2026-06-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Huldenberg (no AGB)",
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
        "lb_huldb_fin_debt_9_56m_2025",
        "Huldenberg YE2025 fin debt 9.56m",
        "9556788.86",
        "6.5",
        "7.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 9.557m declining vs 10.322m; new loans 0",
    ),
    (
        "lb_huldb_pension_4_37m_2025",
        "Huldenberg YE2025 pension LT 4.37m",
        "4370175.13",
        "6.5",
        "6.5",
        "Publish city/OCMW split + responsabilisering",
        "pension 4.370m vs 5.252m; respo 1.939m; ST prov 0.640m",
    ),
    (
        "lb_huldb_ocmw_tussen_1_25m_2025",
        "Huldenberg 2025 OCMW tussenkomst 1.25m",
        "1254287.39",
        "7.0",
        "6.0",
        "Publish cash vs book transfer + 2026-2031 pad",
        "tussen 1.254m vs OCMW expl -1.254m; equity -0.953m NEG",
    ),
    (
        "lb_huldb_pers_13_18m_2025",
        "Huldenberg 2025 personeel 13.18m",
        "13182150.71",
        "5.5",
        "7.0",
        "Publish paid VTE vs formatie",
        "pers 13.182m; onderwijs andere ov 6.639m JUMP; VTE unpublished",
    ),
    (
        "lb_huldb_politie_hvz_1_61m_2025",
        "Huldenberg 2025 politie+HVZ 1.61m",
        "1614600.86",
        "6.0",
        "6.0",
        "Publish zone split + 2026-2031",
        "politie 1.081 + HVZ 0.534 + HVZ invest 0.106",
    ),
    (
        "lb_huldb_invest_gap_2025",
        "Huldenberg 2025 invest vs initieel 12.22m",
        "3052380.51",
        "6.5",
        "6.5",
        "Publish unrealised 2025 project list + 2026 carry",
        "invest uitg 3.052m vs initieel 12.223m (~25%)",
    ),
    (
        "lb_huldb_avail_8_25m_2025",
        "Huldenberg YE2025 avail BBR 8.25m",
        "8251667.19",
        "5.0",
        "7.0",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 8.252m; BBR year +2.045m; AFM +2.955m; cash 5.922m",
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
            "beneficiaries": "Inwoners Huldenberg / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Huldenberg (no AGB)",
            "measured_outcome": (
                "assets 68.710m / fin debt 9.557m / pension 4.370m / "
                "OCMW tussen 1.254m / AFM +2.955m / avail 8.252m"
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
                "T4/LT-S per-loan creditors for fin debt 9.55678886m + bank 9.11359589 "
                "+ Iverlek/Finilek 0.44319297 + pension LT 4.37017513 city/OCMW split "
                "+ responsabilisering 1.939m + OCMW tussenkomst 1.25428739m cash vs book "
                "+ 2026-2031 pad + IGS FVA 9.54023154 inventory + EVA 0 confirm "
                "+ paid VTE behind pers 13.18215071m (onderwijs andere ov 6.63946394 JUMP) "
                "+ politiezone Voer en Dijle/HVZ 1.61460086m zone split "
                "+ invest gap 3.052m vs initieel 12.223m"
            ),
            "why_it_matters": (
                "Unmined Huldenberg GE after residual dual hunt. No AGB. "
                "Fin debt 9.557m declining; new loans 0. "
                "OCMW dual 1.254m vs expl -1.254m / equity -0.953m NEG. "
                "Avail 8.252m with BBR year +2.045m. Pers 13.182m onderwijs JUMP. VTE unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Huldenberg (gemeente + OCMW)",
            "recipient_email": "info@huldenberg.be",
            "recipient_postal": "Gemeenteplein 1 3040 Huldenberg",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_huldb_fin_debt_9_56m_2025",
            "linked_leaderboard_id": "lb_huldb_fin_debt_9_56m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1292",
    "title": "Stad+OCMW Huldenberg JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Huldenberg JR2025 BBC text + KBO; "
        "KBO 0207.519.820 / 0212.221.152; assets 68.710m / fin debt 9.557m / "
        "pension 4.370m / OCMW tussen 1.254m / AFM +2.955m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:35:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1292 Stad+OCMW Huldenberg JR2025 GE residual; KBO 0207.519.820/0212.221.152; "
        "assets 68.710m fin debt 9.557m pension 4.370m AFM +2.955m gecorr +2.894m "
        "BBR +2.045m avail 8.252m cash 5.922m OCMW tussen 1.254m "
        "pers 13.182m politie 1.081m new loans 0; no AGB; FOI ready not sent; "
        "next rq_1293 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1293",
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
        "+ Stad+OCMW Kapelle-op-den-Bos 1291 + Stad+OCMW Huldenberg 1292 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel city+OCMW JR2025 only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only / "
        "Oosterzele De Kluize unless a fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; "
        "skip AGB Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "skip Dilbeek/Wijnegem city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
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
    "notes": "spawned tick1292 after Stad+OCMW Huldenberg JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1292", rq_new, rq_spawn)
print("research_queue 1292", found, "spawned_1293", spawned)

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
            "last_unit_id": "rq_1292",
            "ticks_completed": "1292",
            "paused": "no",
            "notes": (
                "tick1292 Stad+OCMW Huldenberg JR2025 GE residual; KBO 0207.519.820/0212.221.152; "
                "assets 68.710m fin debt 9.557m pension 4.370m OCMW tussen 1.254m; "
                "FOI ready; next rq_1293 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1292_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
