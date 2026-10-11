# -*- coding: utf-8 -*-
"""Tick 1293 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Oud-Heverlee JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:50:00Z"
TICK = 1293
SRC = "src_oudhev_jr2025_bbc"
SRC2 = "src_oudhev_jr2025_gr"
SRC3 = "src_kbo_oudhev_0207523679"
ENT = "city_oud_heverlee"
OCMW = "ocmw_oud_heverlee"
SRC_URL = "https://www.oud-heverlee.be/file/download/23284/BC5DB0D13783C7D8A9576E413E31C280"
SRC2_URL = "https://www.oud-heverlee.be/file/download/23317/6AC9F1E2BCAB98583FE8ECA6840B7E1C"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207523679"
GAP = "gap_oudhev_fin_debt_15_18m_pension_5_49m_ocmw_tussen_0_94m_l5"
HIER = "Vlaanderen>Gemeenten>Oud-Heverlee"

ASSETS = 81660928
ASSETS_2024 = 69467174
CASH = 12445617
CASH_2024 = 11649621
CURRENT = 15547900
FIXED = 66113028
FVA = 17705280
IGS = 16173268
OTHER_FVA = 1532012
EVA = 0
MVA = 48051598
LEASING = 2265923
IVA = 120796
LT_RECV = 235354
SCHULDEN = 23081113
EQUITY = 58579815
CAP_SUBS = 6542057
CUM_PNL = 20551869
REVAL = 8920599
OTHER_EQ = 22565290
FIN_DEBT = 15183264
FIN_DEBT_LT = 13868822
FIN_DEBT_ST = 1314442
FIN_DEBT_2024 = 15288421
NEW_LOANS = 1336745
PENSION = 5485793
PENSION_2024 = 5266726
PENSION_RESPO = 1370000
ST_PROV = 670186
EXPL = 4809493
EXPL_ONTV = 26408127
EXPL_UITG = 21598634
CITY_EXPL = 5763180
OCMW_EXPL = -953687
INVEST = -3386076
BBR = 1600520
CUM_PREV = 12167265
AVAIL = 13767785
AFM = 3449851
GECORR = 3668679
PNL = 2482528
CITY_PNL = 3354167
OCMW_PNL = -871639
TUSSEN = 936177
PERS = 13418914
FISCAL = 13341897
OV = 4205558
APB = 7788464
GEMFONDS = 2278934
POLITIE = 1134229
HVZ = 572528
AFL = 1441902
OCMW_EQUITY = 1603731
OCMW_CUM = -2040424
BANK_REM = 13801812
LEASE_DEBT = 1381452
FLUVIUS_REVAL = 8912221


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
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 2
assert abs((BANK_REM + LEASE_DEBT) - FIN_DEBT) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Oud-Heverlee BBC jaarrekening 2025 (PDF 197p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Oud-Heverlee",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1293; 9.79MB BBC PDF; GR+RVMW 30.06.2026 pub 03.07.2026; "
                "KBO 0207.523.679 / 0212.207.096; assets 81.661m fin debt 15.183m "
                "pension 5.486m OCMW tussen 0.936m AFM +3.450m avail 13.768m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Oud-Heverlee GR 30.06.2026 vaststelling JR2025",
            "url": SRC2_URL,
            "publisher": "Gemeente Oud-Heverlee",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1293; JR2025 vaststelling GR 30.06.2026; BBR +1.601m cum 13.768m AFM 3.450m; "
                "no AGB; siblings Huldenberg 1292 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Oud-Heverlee 0207.523.679",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1293; Stad/gemeente since 01.01.1968; seat Gemeentestraat 2 3054; 8 VE; "
                "burgemeester Bart Clerckx since 01.01.2021; NACE 84.114; "
                "OCMW sibling 0212.207.096 (1 VE; voorzitter Diane Grauwels since 07.01.2013); "
                "AD Marijke Pertz since 01.06.2010 / FD Yannic Vanderplanken (BBC cover)"
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
            "name_nl": "Gemeente Oud-Heverlee",
            "name_fr": "Commune d'Oud-Heverlee",
            "name_en": "Municipality of Oud-Heverlee",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.oud-heverlee.be",
            "foi_email": "info@oud-heverlee.be",
            "foi_postal": "Gemeentestraat 2 3054 Oud-Heverlee",
            "notes": (
                "tick1293 JR2025 GE residual; KBO 0207.523.679 / OCMW 0212.207.096; NIS 24086; "
                "8+1 VE; no AGB; assets 81.661m fin debt 15.183m pension 5.486m "
                "OCMW tussen 0.936m AFM +3.450m avail 13.768m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Oud-Heverlee",
            "name_fr": "CPAS Oud-Heverlee",
            "name_en": "OCMW Oud-Heverlee",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.oud-heverlee.be",
            "foi_email": "info@oud-heverlee.be",
            "foi_postal": "Gemeentestraat 10 3054 Oud-Heverlee",
            "notes": (
                "tick1293 JR2025 dual residual; KBO 0212.207.096; kengetallen expl -0.954m; "
                "city tussenkomst 0.936m; T5 cum PnL -2.040m NEG equity 1.604m; cash 0.887m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_oudhev_assets_2025", "2025", ASSETS, "J4 assets 81.660928m vs 69.467174m"),
    ("bud_oudhev_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 69.467174m"),
    ("bud_oudhev_cash_2025", "2025", CASH, "J4 cash 12.445617m vs 11.649621m"),
    ("bud_oudhev_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 11.649621m"),
    ("bud_oudhev_fva_2025", "2025", FVA, "J4/T5 FVA 17.705280m; EVA 0 + IGS 16.173268"),
    ("bud_oudhev_igs_2025", "2025", IGS, "J4/T5 IGS FVA 16.173268m"),
    ("bud_oudhev_fluvius_reval_2025", "2025", FLUVIUS_REVAL, "T5 Fluvius Zenne-Dijle IGS reval +8.912221m"),
    ("bud_oudhev_mva_2025", "2025", MVA, "J4 MVA 48.051598m; leasing 2.265923m"),
    ("bud_oudhev_leasing_2025", "2025", LEASING, "T5 leasing MVA 2.265923m vs 2.043074m"),
    ("bud_oudhev_equity_2025", "2025", EQUITY, "J4 nettoactief 58.579815m vs 46.379138m"),
    ("bud_oudhev_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 15.183264m (LT 13.869 + ST due 1.314)"),
    ("bud_oudhev_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 15.288421m"),
    ("bud_oudhev_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 1.336745m"),
    ("bud_oudhev_pension_2025", "2025", PENSION, "J4 LT pension 5.485793m vs 5.266726m"),
    ("bud_oudhev_pension_respo_2025", "2025", PENSION_RESPO, "proefbalans responsabilisering 1.370m"),
    ("bud_oudhev_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 0.670186m"),
    ("bud_oudhev_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +4.809493m"),
    ("bud_oudhev_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 26.408127m"),
    ("bud_oudhev_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 21.598634m"),
    ("bud_oudhev_city_expl_2025", "2025", CITY_EXPL, "kengetallen city expl +5.763180m (25.029/19.265)"),
    ("bud_oudhev_ocmw_expl_2025", "2025", OCMW_EXPL, "kengetallen OCMW expl -0.953687m (1.380/2.334)"),
    ("bud_oudhev_invest_2025", "2025", INVEST, "J2 invest -3.386076m vs eindkrediet 6.615m"),
    ("bud_oudhev_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +1.600520m"),
    ("bud_oudhev_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 13.767785m"),
    ("bud_oudhev_afm_2025", "2025", AFM, "J2 AFM +3.449851m"),
    ("bud_oudhev_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +3.668679m"),
    ("bud_oudhev_pnl_2025", "2025", PNL, "J5 PnL +2.482528m (city +3.354 / OCMW -0.872)"),
    ("bud_oudhev_tussen_2025", "2025", TUSSEN, "kengetallen/T5 city->OCMW tussenkomst 0.936177m"),
    ("bud_oudhev_pers_2025", "2025", PERS, "J5 bezoldigingen 13.418914m"),
    ("bud_oudhev_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 13.341897m"),
    ("bud_oudhev_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.278934m"),
    ("bud_oudhev_politie_2025", "2025", POLITIE, "T2 politiediensten 1.134229m"),
    ("bud_oudhev_hvz_2025", "2025", HVZ, "T2 brandweer/HVZ 0.572528m"),
    ("bud_oudhev_afl_2025", "2025", AFL, "T4 periodieke aflossingen 1.441902m"),
    ("bud_oudhev_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity 1.603731m"),
    ("bud_oudhev_ocmw_cum_2025", "2025", OCMW_CUM, "T5 OCMW cum PnL -2.040424m NEG"),
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
        "comm_oudhev_fin_debt_15_18m_2025",
        "Oud-Heverlee YE2025 fin debt 15.183m",
        "15183264",
        "T4 15.183264m (LT 13.869 + ST due 1.314) declining vs 15.288m; new loans 1.337m; bank 13.802m + leasing 1.381m",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_oudhev_pension_5_49m_2025",
        "Oud-Heverlee YE2025 pension LT 5.486m",
        "5485793",
        "J4 LT pension 5.485793m vs 5.266726m; respo 1.370m; ST prov 0.670m; city/OCMW split unpublished",
        "Publish city/OCMW split + responsabilisering FOI",
    ),
    (
        "comm_oudhev_ocmw_tussen_0_94m_2025",
        "Oud-Heverlee 2025 OCMW tussenkomst 0.936m",
        "936177",
        "T5/kengetallen city->OCMW 0.936177m vs OCMW expl -0.954m; T5 OCMW cum -2.040m NEG; cash 0.887m",
        "Publish cash vs book transfer + 2026-2031 pad FOI",
    ),
    (
        "comm_oudhev_pers_13_42m_2025",
        "Oud-Heverlee 2025 personeel 13.419m",
        "13418914",
        "J5 13.418914m; paid VTE unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_oudhev_politie_hvz_1_71m_2025",
        "Oud-Heverlee 2025 politie+HVZ 1.707m",
        "1706757",
        "T2 politiediensten 1.134229 + brandweer/HVZ 0.572528",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_oudhev_fluvius_reval_8_91m_2025",
        "Oud-Heverlee 2025 Fluvius Zenne-Dijle reval 8.912m",
        "8912221",
        "T5 IGS reval +8.912221m (Fluvius 02.04.2026); assets JUMP 81.661 vs 69.467",
        "Publish IGS inventory + aanschaf vs herwaardering FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Oud-Heverlee / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Oud-Heverlee GR 30.06.2026",
            "decision_date": "2026-06-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Oud-Heverlee (no AGB)",
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
        "lb_oudhev_fin_debt_15_18m_2025",
        "Oud-Heverlee YE2025 fin debt 15.18m",
        "15183264",
        "6.5",
        "7.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 15.183m declining vs 15.288m; new loans 1.337m",
    ),
    (
        "lb_oudhev_pension_5_49m_2025",
        "Oud-Heverlee YE2025 pension LT 5.49m",
        "5485793",
        "6.5",
        "6.5",
        "Publish city/OCMW split + responsabilisering",
        "pension 5.486m vs 5.267m; respo 1.370m; ST prov 0.670m",
    ),
    (
        "lb_oudhev_ocmw_tussen_0_94m_2025",
        "Oud-Heverlee 2025 OCMW tussenkomst 0.94m",
        "936177",
        "7.0",
        "6.0",
        "Publish cash vs book transfer + 2026-2031 pad",
        "tussen 0.936m vs OCMW expl -0.954m; cum -2.040m NEG",
    ),
    (
        "lb_oudhev_pers_13_42m_2025",
        "Oud-Heverlee 2025 personeel 13.42m",
        "13418914",
        "5.5",
        "7.0",
        "Publish paid VTE vs formatie",
        "pers 13.419m; VTE unpublished",
    ),
    (
        "lb_oudhev_politie_hvz_1_71m_2025",
        "Oud-Heverlee 2025 politie+HVZ 1.71m",
        "1706757",
        "6.0",
        "6.0",
        "Publish zone split + 2026-2031",
        "politie 1.134 + HVZ 0.573",
    ),
    (
        "lb_oudhev_fluvius_reval_8_91m_2025",
        "Oud-Heverlee 2025 Fluvius reval 8.91m",
        "8912221",
        "6.5",
        "7.0",
        "Publish IGS inventory + aanschaf vs herwaardering",
        "Fluvius Zenne-Dijle reval +8.912m; assets JUMP 81.661 vs 69.467",
    ),
    (
        "lb_oudhev_avail_13_77m_2025",
        "Oud-Heverlee YE2025 avail BBR 13.77m",
        "13767785",
        "5.0",
        "7.0",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 13.768m; BBR year +1.601m; AFM +3.450m; cash 12.446m",
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
            "beneficiaries": "Inwoners Oud-Heverlee / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Oud-Heverlee (no AGB)",
            "measured_outcome": (
                "assets 81.661m / fin debt 15.183m / pension 5.486m / "
                "OCMW tussen 0.936m / AFM +3.450m / avail 13.768m"
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
                "T4/LT-S per-loan creditors for fin debt 15.183264m + bank 13.801812 "
                "+ leasing 1.381452 + pension LT 5.485793 city/OCMW split "
                "+ responsabilisering 1.370m + OCMW tussenkomst 0.936177m cash vs book "
                "+ 2026-2031 pad + IGS FVA 16.173268 inventory + Fluvius reval 8.912221 "
                "+ EVA 0 confirm + paid VTE behind pers 13.418914m "
                "+ politiediensten/HVZ 1.706757m zone split "
                "+ invest gap 4.821m vs eindkrediet 6.615m"
            ),
            "why_it_matters": (
                "Unmined Oud-Heverlee GE after residual dual hunt. No AGB. "
                "Fin debt 15.183m declining; new loans 1.337m. "
                "OCMW dual 0.936m vs expl -0.954m / cum -2.040m NEG. "
                "Avail 13.768m with BBR year +1.601m. Fluvius reval +8.912m. VTE unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Oud-Heverlee (gemeente + OCMW)",
            "recipient_email": "info@oud-heverlee.be",
            "recipient_postal": "Gemeentestraat 2 3054 Oud-Heverlee",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_oudhev_fin_debt_15_18m_2025",
            "linked_leaderboard_id": "lb_oudhev_fin_debt_15_18m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1293",
    "title": "Stad+OCMW Oud-Heverlee JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Oud-Heverlee JR2025 BBC text + KBO; "
        "KBO 0207.523.679 / 0212.207.096; assets 81.661m / fin debt 15.183m / "
        "pension 5.486m / OCMW tussen 0.936m / AFM +3.450m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1293 Stad+OCMW Oud-Heverlee JR2025 GE residual; KBO 0207.523.679/0212.207.096; "
        "assets 81.661m fin debt 15.183m pension 5.486m AFM +3.450m gecorr +3.669m "
        "BBR +1.601m avail 13.768m cash 12.446m OCMW tussen 0.936m "
        "pers 13.419m politie 1.134m new loans 1.337m Fluvius reval 8.912m; no AGB; FOI ready not sent; "
        "next rq_1294 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1294",
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
        "+ Stad+OCMW Kapelle-op-den-Bos 1291 + Stad+OCMW Huldenberg 1292 "
        "+ Stad+OCMW Oud-Heverlee 1293 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen city+OCMW JR2025 only if PDF fetches; "
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
    "notes": "spawned tick1293 after Stad+OCMW Oud-Heverlee JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1293", rq_new, rq_spawn)
print("research_queue 1293", found, "spawned_1294", spawned)

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
            "last_unit_id": "rq_1293",
            "ticks_completed": "1293",
            "paused": "no",
            "notes": (
                "tick1293 Stad+OCMW Oud-Heverlee JR2025 GE residual; KBO 0207.523.679/0212.207.096; "
                "assets 81.661m fin debt 15.183m pension 5.486m OCMW tussen 0.936m; "
                "FOI ready; next rq_1294 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1293_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
