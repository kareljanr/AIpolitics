# -*- coding: utf-8 -*-
"""Tick 1294 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Heusden-Zolder JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T12:10:00Z"
TICK = 1294
SRC = "src_hzolder_jr2025_bbc"
SRC2 = "src_hzolder_jr2025_gr"
SRC3 = "src_kbo_hzolder_0216772432"
ENT = "city_heusden_zolder"
OCMW = "ocmw_heusden_zolder"
SRC_URL = "https://heusden-zolder.meetingburger.net/Pages/HandleFile.ashx?id=d6419e27-0a4f-43c8-9d35-66cc8c24fb69"
SRC2_URL = "https://heusden-zolder.meetingburger.net/Gemeenteraad/78d8509f-7e0c-4755-a02d-bdca86f8fa85"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0216772432"
GAP = "gap_hzolder_fin_debt_37_85m_igs_reval_31_12m_ocmw_equity_neg_11_0m_l5"
HIER = "Vlaanderen>Gemeenten>Heusden-Zolder"

ASSETS = 248035653
ASSETS_2024 = 205630978
CASH = 15384515
CASH_2024 = 14233604
CURRENT = 23483324
FIXED = 224552329
FVA = 54551888
IGS = 52513588
OTHER_FVA = 2035023
EVA = 0
MVA = 168777087
LEASING = 9177660
IVA = 742585
LT_RECV = 480769
SCHULDEN = 49064437
EQUITY = 198971216
CAP_SUBS = 35505961
CUM_PNL = 46249224
REVAL = 31171380
OTHER_EQ = 86044652
FIN_DEBT = 37846697
FIN_DEBT_LT = 34230882
FIN_DEBT_ST = 3615815
FIN_DEBT_2024 = 32324971
NEW_LOANS = 9385810
PENSION = 0
PENSION_2024 = 447823
OCMW_VER = 3277
ST_PROV = 1208349
EXPL = 11664363
EXPL_ONTV = 78054321
EXPL_UITG = 66389958
CITY_EXPL = 15453048
OCMW_EXPL = -3788685
INVEST = -17582200
BBR = -261949
CUM_PREV = 13646333
AVAIL = 12016523
AFM = 8075812
GECORR = 9159030
PNL = 2434949
CITY_PNL = 5168952
OCMW_PNL = -2734003
TUSSEN = 0
PERS = 38766812
FISCAL = 30750925
OV = 13623090
APB = 12547337
GEMFONDS = 11767088
POLITIE = 3530000
HVZ = 1626555
AFL = 3669215
OCMW_EQUITY = -10981739
OCMW_CUM = -14943405
NEW_LOANS_BANK = 8000000
FLUVIUS_REVAL = 31120890


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
assert abs((IGS + OTHER_FVA + OCMW_VER + EVA) - FVA) < 2
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - 13384384) < 2
assert abs((13384384 - 1367861) - AVAIL) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Heusden-Zolder BBC jaarrekening 2025 (PDF 196p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Heusden-Zolder",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1294; 11.38MB BBC PDF meetingburger; GR 25.06.2026 pub 26.06.2026; "
                "KBO 0216.772.432 / 0216.772.531; assets 248.036m fin debt 37.847m "
                "IGS reval 31.121m OCMW equity -10.982m NEG AFM +8.076m avail 12.017m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Heusden-Zolder GR 25.06.2026 vaststelling JR2025",
            "url": SRC2_URL,
            "publisher": "Gemeente Heusden-Zolder",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1294; JR2025 vaststelling GR 25.06.2026; BBR year -0.262m avail 12.017m AFM 8.076m assets 248.036m; "
                "no AGB; siblings Houthalen-Helchteren 1285 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Heusden-Zolder 0216.772.432",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1294; Stad/gemeente since 01.01.1977; seat Heldenplein 1 3550; 15 VE; "
                "burgemeester Mario Borremans since 01.01.2013; NACE 84.114; "
                "OCMW sibling 0216.772.531 (10 VE; voorzitter Mario Borremans since 01.01.2019); "
                "AD Rony Herlitska / FD Ine Thoelen (BBC cover)"
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
            "name_nl": "Gemeente Heusden-Zolder",
            "name_fr": "Commune de Heusden-Zolder",
            "name_en": "Municipality of Heusden-Zolder",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.heusden-zolder.be",
            "foi_email": "gemeente@heusden-zolder.be",
            "foi_postal": "Heldenplein 1 3550 Heusden-Zolder",
            "notes": (
                "tick1294 JR2025 GE residual; KBO 0216.772.432 / OCMW 0216.772.531; NIS 71070; "
                "15+10 VE; no AGB; assets 248.036m fin debt 37.847m IGS reval 31.121m "
                "OCMW equity -10.982m NEG AFM +8.076m avail 12.017m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Heusden-Zolder",
            "name_fr": "CPAS Heusden-Zolder",
            "name_en": "OCMW Heusden-Zolder",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.heusden-zolder.be",
            "foi_email": "gemeente@heusden-zolder.be",
            "foi_postal": "Sint-Willibrordusplein 4 3550 Heusden-Zolder",
            "notes": (
                "tick1294 JR2025 dual residual; KBO 0216.772.531; J3 expl -3.789m; "
                "T5 tussenkomst 0; T5 cum PnL -14.943m NEG equity -10.982m NEG; FOI ready"
            ),
        },
    ],
)
print("entities", n)


bud_rows = [
    ("bud_hzolder_assets_2025", "2025", ASSETS, "J4 assets 248.035653m vs 205.630978m"),
    ("bud_hzolder_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 205.630978m"),
    ("bud_hzolder_cash_2025", "2025", CASH, "J4 cash 15.384515m vs 14.233604m"),
    ("bud_hzolder_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 14.233604m"),
    ("bud_hzolder_fva_2025", "2025", FVA, "J4/T5 FVA 54.551888m; EVA 0 + IGS 52.513588 + OCMW-ver 0.003277"),
    ("bud_hzolder_igs_2025", "2025", IGS, "J4/T5 IGS FVA 52.513588m"),
    ("bud_hzolder_fluvius_reval_2025", "2025", FLUVIUS_REVAL, "T5 Fluvius Limburg IGS reval +31.120890m"),
    ("bud_hzolder_mva_2025", "2025", MVA, "J4 MVA 168.777087m; leasing 9.177660m"),
    ("bud_hzolder_leasing_2025", "2025", LEASING, "T5 leasing MVA 9.177660m vs 8.482211m"),
    ("bud_hzolder_equity_2025", "2025", EQUITY, "J4 nettoactief 198.971216m vs 162.831660m"),
    ("bud_hzolder_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 37.846697m (LT 34.231 + ST due 3.616)"),
    ("bud_hzolder_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 32.324971m"),
    ("bud_hzolder_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 9.385810m (bank 8.000 + other/leasing 1.386)"),
    ("bud_hzolder_pension_2025", "2025", PENSION, "J4 LT pension 0 (was 0.447823m; zeroed)"),
    ("bud_hzolder_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 1.208349m"),
    ("bud_hzolder_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +11.664363m"),
    ("bud_hzolder_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 78.054321m"),
    ("bud_hzolder_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 66.389958m"),
    ("bud_hzolder_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +15.453048m (68.014/52.561)"),
    ("bud_hzolder_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -3.788685m (10.040/13.829)"),
    ("bud_hzolder_invest_2025", "2025", INVEST, "J2 invest -17.582200m vs MJP -17.102m"),
    ("bud_hzolder_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar -0.261949m"),
    ("bud_hzolder_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 12.016523m"),
    ("bud_hzolder_afm_2025", "2025", AFM, "J2 AFM +8.075812m"),
    ("bud_hzolder_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +9.159030m"),
    ("bud_hzolder_pnl_2025", "2025", PNL, "J5 PnL +2.434949m (city +5.169 / OCMW -2.734)"),
    ("bud_hzolder_tussen_2025", "2025", TUSSEN, "T5 city->OCMW tussenkomst 0"),
    ("bud_hzolder_pers_2025", "2025", PERS, "J5 bezoldigingen 38.766812m / 321.33 VTE"),
    ("bud_hzolder_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 30.750925m"),
    ("bud_hzolder_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 11.767088m"),
    ("bud_hzolder_politie_2025", "2025", POLITIE, "T2 politiezone Heusden-Zolder 3.530000m"),
    ("bud_hzolder_hvz_2025", "2025", HVZ, "T2 HVZ Zuid-West-Limburg 1.626555m"),
    ("bud_hzolder_afl_2025", "2025", AFL, "T4 periodieke aflossingen 3.669215m"),
    ("bud_hzolder_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -10.981739m NEG"),
    ("bud_hzolder_ocmw_cum_2025", "2025", OCMW_CUM, "T5 OCMW cum PnL -14.943405m NEG"),
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
        "comm_hzolder_fin_debt_37_85m_2025",
        "Heusden-Zolder YE2025 fin debt 37.847m",
        "37846697",
        "T4 37.846697m (LT 34.231 + ST due 3.616) rising vs 32.325m; new loans 9.386m (bank 8.000 + other 1.386)",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_hzolder_igs_reval_31_12m_2025",
        "Heusden-Zolder 2025 Fluvius Limburg IGS reval 31.121m",
        "31120890",
        "T5 IGS reval +31.120890m (Fluvius Limburg EV ELEK/GAS/andere); assets JUMP 248.036 vs 205.631",
        "Publish IGS inventory + aanschaf vs herwaardering FOI",
    ),
    (
        "comm_hzolder_ocmw_equity_neg_11_0m_2025",
        "Heusden-Zolder YE2025 OCMW equity -10.982m NEG",
        "10981739",
        "T5 OCMW equity -10.981739m NEG; cum PnL -14.943405m NEG; tussenkomst 0 vs J3 expl -3.789m",
        "Publish why tussenkomst 0 + 2026-2031 pad FOI",
    ),
    (
        "comm_hzolder_pers_38_77m_2025",
        "Heusden-Zolder 2025 personeel 38.767m",
        "38766812",
        "J5 38.766812m; VTE 321.33 (vast 31.33 / contractueel 290.00); city/OCMW split unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_hzolder_politie_hvz_5_16m_2025",
        "Heusden-Zolder 2025 politie+HVZ 5.157m",
        "5156555",
        "T2 politiezone Heusden-Zolder 3.530 + HVZ Zuid-West-Limburg 1.627",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_hzolder_pension_zeroed_2025",
        "Heusden-Zolder YE2025 LT pension 0 (was 0.448m)",
        "447823",
        "J4 LT pension zeroed from 0.447823m; ST prov 1.208349m remain; T2 pension cost 0.423m",
        "Publish why LT pension zeroed + remaining risk FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Heusden-Zolder / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Heusden-Zolder GR 25.06.2026",
            "decision_date": "2026-06-25",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Heusden-Zolder (no AGB)",
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
        "lb_hzolder_fin_debt_37_85m_2025",
        "Heusden-Zolder YE2025 fin debt 37.85m",
        "37846697",
        "7.0",
        "8.0",
        "Publish per-loan amort 2026-2031",
        "fin debt 37.847m rising vs 32.325m; new loans 9.386m",
    ),
    (
        "lb_hzolder_igs_reval_31_12m_2025",
        "Heusden-Zolder 2025 Fluvius Limburg reval 31.12m",
        "31120890",
        "6.5",
        "8.0",
        "Publish IGS inventory + aanschaf vs herwaardering",
        "Fluvius Limburg IGS reval +31.121m; assets JUMP 248.036 vs 205.631",
    ),
    (
        "lb_hzolder_ocmw_equity_neg_11_0m_2025",
        "Heusden-Zolder YE2025 OCMW equity -10.98m NEG",
        "10981739",
        "8.0",
        "7.0",
        "Publish why tussenkomst 0 + 2026-2031 pad",
        "OCMW equity -10.982m NEG; cum -14.943m NEG; tussen 0 vs expl -3.789m",
    ),
    (
        "lb_hzolder_pers_38_77m_2025",
        "Heusden-Zolder 2025 personeel 38.77m / 321 VTE",
        "38766812",
        "5.5",
        "8.0",
        "Publish paid VTE vs formatie city/OCMW",
        "pers 38.767m; VTE 321.33 (vast 31.33 / contract 290)",
    ),
    (
        "lb_hzolder_politie_hvz_5_16m_2025",
        "Heusden-Zolder 2025 politie+HVZ 5.16m",
        "5156555",
        "6.0",
        "6.5",
        "Publish zone split + 2026-2031",
        "politiezone HZ 3.530 + HVZ Zuid-West-Limburg 1.627",
    ),
    (
        "lb_hzolder_pension_zeroed_2025",
        "Heusden-Zolder YE2025 LT pension zeroed (was 0.45m)",
        "447823",
        "7.0",
        "5.0",
        "Publish why LT pension zeroed + remaining risk",
        "LT pension 0 vs 0.448m; ST prov 1.208m; T2 pension cost 0.423m",
    ),
    (
        "lb_hzolder_avail_12_02m_2025",
        "Heusden-Zolder YE2025 avail BBR 12.02m",
        "12016523",
        "5.0",
        "7.0",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 12.017m; BBR year -0.262m; AFM +8.076m; cash 15.385m",
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
            "beneficiaries": "Inwoners Heusden-Zolder / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Heusden-Zolder (no AGB)",
            "measured_outcome": (
                "assets 248.036m / fin debt 37.847m / IGS reval 31.121m / "
                "OCMW equity -10.982m NEG / AFM +8.076m / avail 12.017m"
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
                "T4/LT-S per-loan creditors for fin debt 37.846697m + new loans 9.385810 "
                "(bank 8.000 + other/leasing 1.386) + why LT pension zeroed from 0.447823 "
                "+ ST prov 1.208349 composition + OCMW tussenkomst 0 vs expl -3.788685 "
                "+ OCMW equity -10.981739 NEG / cum -14.943405 NEG + 2026-2031 pad "
                "+ IGS FVA 52.513588 inventory + Fluvius Limburg reval 31.120890 "
                "+ EVA 0 confirm + city/OCMW VTE split behind 321.33 / pers 38.766812 "
                "+ politiezone/HVZ 5.156555m 2026-2031 verdeelsleutel"
            ),
            "why_it_matters": (
                "Unmined Heusden-Zolder GE after residual dual hunt. No AGB. "
                "Fin debt 37.847m rising; new loans 9.386m. "
                "OCMW dual tussen 0 vs expl -3.789m / equity -10.982m NEG. "
                "Avail 12.017m with BBR year -0.262m. Fluvius reval +31.121m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Heusden-Zolder (gemeente + OCMW)",
            "recipient_email": "gemeente@heusden-zolder.be",
            "recipient_postal": "Heldenplein 1 3550 Heusden-Zolder",
            "draft_letter_path": "docs/doge/foi/drafts/gap_hzolder_fin_debt_37_85m_igs_reval_31_12m_ocmw_equity_neg_11_0m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_hzolder_fin_debt_37_85m_2025",
            "linked_leaderboard_id": "lb_hzolder_fin_debt_37_85m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1294",
    "title": "Stad+OCMW Heusden-Zolder JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Heusden-Zolder JR2025 BBC text + KBO; "
        "KBO 0216.772.432 / 0216.772.531; assets 248.036m / fin debt 37.847m / "
        "IGS reval 31.121m / OCMW equity -10.982m NEG / AFM +8.076m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1294 Stad+OCMW Heusden-Zolder JR2025 GE residual; KBO 0216.772.432/0216.772.531; "
        "assets 248.036m fin debt 37.847m IGS reval 31.121m AFM +8.076m gecorr +9.159m "
        "BBR -0.262m avail 12.017m cash 15.385m OCMW equity -10.982m NEG tussen 0 "
        "pers 38.767m VTE 321.33 politie 3.530m new loans 9.386m; no AGB; FOI ready not sent; "
        "next rq_1295 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1295",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1294 done including Stad+OCMW Heusden-Zolder 1294); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Heusden-Zolder 1294 / Oud-Heverlee 1293 / Huldenberg 1292 / "
        "Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / Zwaan 1288 / "
        "Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen/Zwalm city+OCMW JR2025 only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; "
        "skip Dilbeek/Wijnegem city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1294 after Stad+OCMW Heusden-Zolder JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1294", rq_new, rq_spawn)
print("research_queue 1294", found, "spawned_1295", spawned)

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
            "last_unit_id": "rq_1294",
            "ticks_completed": "1294",
            "paused": "no",
            "notes": (
                "tick1294 Stad+OCMW Heusden-Zolder JR2025 GE residual; KBO 0216.772.432/0216.772.531; "
                "assets 248.036m fin debt 37.847m IGS reval 31.121m OCMW equity -10.982m NEG; "
                "FOI ready; next rq_1295 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1294_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
