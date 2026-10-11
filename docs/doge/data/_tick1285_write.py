# -*- coding: utf-8 -*-
"""Tick 1285 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Houthalen-Helchteren JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T12:25:00Z"
TICK = 1285
SRC = "src_hh_jr2025_bbc"
SRC2 = "src_hh_jr2025_doc"
SRC3 = "src_kbo_ocmw_hh_0216773125"
SRC4 = "src_hh_jr2025_gr"
ENT = "city_houthalen_helchteren"
OCMW = "ocmw_houthalen_helchteren"
SRC_URL = "https://houthalen-helchteren.meetingburger.net/Pages/HandleFile.ashx?id=2e4f018a-6b76-4e2d-b3b7-e1663823f722&download=1"
SRC2_URL = "https://houthalen-helchteren.meetingburger.net/Pages/HandleFile.ashx?id=783045ce-28ff-4174-968b-e294fa593080&download=1"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0216773125"
SRC4_URL = "https://houthalen-helchteren.meetingburger.net/gr/40b9d958-dc55-46cd-9f84-d73d9a24e0f0"
GAP = "gap_hh_fin_debt_17_37m_pension_3_69m_ocmw_neg_12_89m_l5"
HIER = "Vlaanderen>Gemeenten>Houthalen-Helchteren"

ASSETS = 181571902
ASSETS_2024 = 174406210
CASH = 4828159
CASH_2024 = 6041237
FVA = 45613559.22
EVA = 980000.00
IGS = 40120429.26
OCMW_VER = 669806.81
OTHER_FVA = 3843323.15
MVA = 101146928.37
LEASING = 12302838.13
FIN_DEBT = 17365513
FIN_DEBT_2024 = 18008236
FIN_DEBT_LT = 15041134
FIN_DEBT_ST_DUE = 1774379
FIN_DEBT_ST = 550000
PENSION = 3687588
PENSION_2024 = 2496896
EQUITY = 148675726.23
CITY_EQUITY = 161567969.82
OCMW_EQUITY = -12892243.59
CUM_PNL = 19528444.74
REVAL = 28824.33
EXPL = 4380653
EXPL_ONTV = 59872254
EXPL_UITG = 55491601
CITY_EXPL = 7340862
OCMW_EXPL = -2960209
INVEST = -5440832
INVEST_ONTV = 6716434
INVEST_UITG = 12157266
BBR = -1731800
AVAIL = 3867091
UNAVAIL = 320000
CUM_BBR = 4187091
AFM = 3194894
GECORR = 3461096
NEW_LOANS = 514138
AFL = 1706861
PNL = -277212.60
CITY_PNL = 3183224.11
OCMW_PNL = -3460436.71
PERS = 28694821
PERS_2024 = 27499206
ONDERWIJS = 7026755
FISCAL = 28036671
OV = 11670431
APB = 10552956
GEMFONDS = 10886347
POLICE = 5654923
HVZ = 1280724
IGS_SUB = 1513883
AGB_SUB = 578868
AGB_SPORT_SUB = 373110
AGB_MP_SUB = 205758
DIVIDEND = 2311043
WAARBORG = 19824181.05
SCHOOL_INV = 4808669
AGION = 3283656
LIMBURGNET = 1422562
GAS5_CARMA = 1966451
POLICE_BASE = 3607522
CONSOL_AVAIL = 7241144
CONSOL_AFM = 3308518
CONSOL_GECORR = 2048479
CITY_BBR = 1520349
OCMW_BBR = -3252149
VTE = 261.70
VTE_CITY = 242.05
VTE_OCMW = 19.65


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


assert abs((FIN_DEBT_LT + FIN_DEBT_ST_DUE + FIN_DEBT_ST) - FIN_DEBT) < 0.02
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 0.02
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 0.02
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 0.02
assert abs((CITY_EQUITY + OCMW_EQUITY) - EQUITY) < 0.02
assert abs((EVA + IGS + OCMW_VER + OTHER_FVA) - FVA) < 0.02
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 0.02
assert abs((CITY_BBR + OCMW_BBR) - BBR) < 0.02
assert abs((AGB_SPORT_SUB + AGB_MP_SUB) - AGB_SUB) < 0.02
assert abs((POLICE_BASE + GAS5_CARMA + 80950) - POLICE) < 0.02
assert abs((CUM_BBR - UNAVAIL) - AVAIL) < 0.02

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Houthalen-Helchteren BBC jaarrekening 2025 (text PDF 121p)",
            "url": SRC_URL,
            "publisher": "Lokaal bestuur Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1285; 2.36MB text PDF BBC_JR_2025_G&O; GR+RVMW 22.06.2026; pub 23.06.2026; "
                "KBO 0216.773.026 / 0216.773.125; assets 181.572m fin debt 17.366m "
                "pension 3.688m OCMW equity -12.892m AFM +3.195m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Stad+OCMW Houthalen-Helchteren documentatie JR2025 (187p VTE/subsidies)",
            "url": SRC2_URL,
            "publisher": "Lokaal bestuur Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1285; Documentatie_JR_2025_G&O.pdf; VTE paid 261.70; "
                "Carma 5.655m; AGB prijs 0.579m; fiscal table 28.037m"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO OCMW Houthalen-Helchteren 0216.773.125",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1285; OCMW since 01.04.1977; seat Pastorijstraat 30 3530; 4 VE; "
                "AD Wim Haest since 23.04.2018; voorzitter Alain Yzermans since 04.01.2019; "
                "NACE 84.115; KBO dump 16.08.2026"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Gemeenteraad Houthalen-Helchteren 22.06.2026 vaststelling jaarrekening 2025 G&O",
            "url": SRC4_URL,
            "publisher": "Gemeente Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1285; GR 22.06.2026 / pub 23.06.2026; same sitting as AGB Masterplan 1282 "
                "and AGB Sport 1283; BBC_JR_2025_G&O.pdf + Documentatie_JR_2025_G&O.pdf"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Houthalen-Helchteren",
            "name_fr": "CPAS de Houthalen-Helchteren",
            "name_en": "OCMW Houthalen-Helchteren",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.houthalen-helchteren.be/",
            "foi_email": "financien@houthalen-helchteren.be",
            "foi_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "notes": (
                "tick1285 JR2025; KBO 0216.773.125; 4 VE; equity NEG 12.892m PnL -3.460m "
                "tussenkomst 0; expl J3 -2.960m BBR -3.252m; VTE paid 19.65; "
                "FOI " + GAP
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_hh_assets_2025", "2025", ASSETS, "J4 consol assets 181.571902m vs 174.406210m"),
    ("bud_hh_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 174.406210m"),
    ("bud_hh_cash_2025", "2025", CASH, "J4 cash 4.828159m DROP vs 6.041237m"),
    ("bud_hh_fva_2025", "2025", FVA, "J4 FVA 45.613559m EVA 0.980 IGS 40.120 OCMW-ver 0.670 other 3.843"),
    ("bud_hh_eva_2025", "2025", EVA, "J4 EVA FVA 0.980000m = AGB MP 0.900 + AGB Sport 0.080"),
    ("bud_hh_igs_2025", "2025", IGS, "J4 IGS FVA 40.120429m reval +0.020544m"),
    ("bud_hh_mva_2025", "2025", MVA, "J4 MVA 101.146928m leasing 12.303m"),
    ("bud_hh_leasing_2025", "2025", LEASING, "J4 leasing 2.528+9.775=12.303m"),
    ("bud_hh_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 17.365513m (LT 15.041 + ST due 1.774 + ST 0.550) vs 18.008m"),
    ("bud_hh_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4/T4 LT fin debt 15.041134m"),
    ("bud_hh_fin_debt_st_2025", "2025", FIN_DEBT_ST, "J4/T4 ST fin 0.550000m (was 0; thesaurie FOI)"),
    ("bud_hh_pension_2025", "2025", PENSION, "J4 pension LT 3.687588m JUMP vs 2.496896m"),
    ("bud_hh_equity_2025", "2025", EQUITY, "J4/T5 nettoactief 148.675726m (city 161.568 / OCMW -12.892)"),
    ("bud_hh_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW nettoactief -12.892244m NEG"),
    ("bud_hh_cum_pnl_2025", "2025", CUM_PNL, "T5 cum P&L 19.528445m"),
    ("bud_hh_reval_2025", "2025", REVAL, "T5 herwaarderingsreserve 0.028824m (IGS chg +0.020544)"),
    ("bud_hh_expl_2025", "2025", EXPL, "J2/T2 expl +4.380653m (J3 city +7.341 / OCMW -2.960)"),
    ("bud_hh_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 59.872254m"),
    ("bud_hh_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 55.491601m"),
    ("bud_hh_invest_2025", "2025", INVEST, "J2/T2 invest -5.440832m (ontv 6.716 / uitg 12.157 vs MJP 28.195)"),
    ("bud_hh_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 12.157266m vs MJP 28.195m"),
    ("bud_hh_bbr_2025", "2025", BBR, "J2 BBR year -1.731800m vs MJP +5.673m"),
    ("bud_hh_avail_2025", "2025", AVAIL, "J2 avail BBR 3.867091m (onbeschikbaar 0.320m)"),
    ("bud_hh_afm_2025", "2025", AFM, "J2 AFM +3.194894m"),
    ("bud_hh_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +3.461096m; consol +AGB +2.048m"),
    ("bud_hh_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.514138m leasing; MJP 21.474m not drawn"),
    ("bud_hh_afl_2025", "2025", AFL, "T2/T4 periodieke aflossingen 1.706861m"),
    ("bud_hh_pnl_2025", "2025", PNL, "J5/T5 PnL -0.277213m (city +3.183 / OCMW -3.460)"),
    ("bud_hh_pers_2025", "2025", PERS, "J5/T2 personeel 28.694821m vs 27.499m; VTE paid 261.70"),
    ("bud_hh_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 28.036671m (OV 11.670 + APB 10.553 + GAS5 2.110)"),
    ("bud_hh_apb_2025", "2025", APB, "T2 APB 10.552956m"),
    ("bud_hh_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 10.886347m"),
    ("bud_hh_police_2025", "2025", POLICE, "T2 politiezone Carma 5.654923m (werking 3.608 + GAS5 1.966 + NAC 0.081)"),
    ("bud_hh_hvz_2025", "2025", HVZ, "T2 HVZ Oost-Limburg 1.280724m"),
    ("bud_hh_igs_sub_2025", "2025", IGS_SUB, "T2 IGS werksub 1.513883m (Limburg.net 1.423m)"),
    ("bud_hh_agb_sub_2025", "2025", AGB_SUB, "T2 AGB prijssub 0.578868m (Sport 0.373 / MP 0.206) vs 1.287m"),
    ("bud_hh_dividend_2025", "2025", DIVIDEND, "doc/BBC dividends 2.311043m Fluvius+NUHMA"),
    ("bud_hh_school_inv_2025", "2025", SCHOOL_INV, "T3 school t Centrum 2025 uitg 4.808669m / AGION 3.283656m"),
    ("bud_hh_waarborg_2025", "2025", WAARBORG, "BBC waarborgen 19.824181m (AGB MP 17.403m)"),
    ("bud_hh_consol_avail_2025", "2025", CONSOL_AVAIL, "J2 consol avail +AGB 7.241144m"),
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
            "notes": note + f"; tick{TICK}",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_hh_fin_debt_17_37m_2025",
        "Stad+OCMW HH YE2025 fin debt 17.366m",
        "17365513",
        "T4 17.365513m down vs 18.008m; new 0.514m leasing; ST 0.550m; MJP 21.474m not drawn",
        "Publish T4 creditor + why 21.5m loans not drawn beside cash 4.8m FOI",
    ),
    (
        "comm_hh_pension_3_69m_2025",
        "Stad+OCMW HH YE2025 pension LT 3.688m JUMP",
        "3687588",
        "J4 pension 3.687588m vs 2.497m; OCMW respo 0.173m vs budget 0; Ethias FOI",
        "Publish wettelijk vs extra-wettelijk + city/OCMW split FOI",
    ),
    (
        "comm_hh_ocmw_neg_12_89m_2025",
        "OCMW HH YE2025 equity -12.892m / PnL -3.460m / tussenkomst 0",
        "12892244",
        "T5 OCMW equity -12.892m; city +3.183m; J3 OCMW BBR -3.252m; no 2025 tussenkomst",
        "Publish why no tussenkomst + 2026-2031 pad FOI",
    ),
    (
        "comm_hh_carma_5_65m_2025",
        "HH 2025 politiezone Carma 5.655m + HVZ 1.281m",
        "6935647",
        "T2 dual 6.936m; Carma 3.608+GAS5 1.966+NAC 0.081; GAS5 boetes 2.110m",
        "Keep nominative 2026-2031 lock public; publish KUL-norm FOI",
    ),
    (
        "comm_hh_agb_sub_0_58m_2025",
        "HH 2025 AGB prijssub 0.579m (halved) + waarborg 19.824m",
        "578868",
        "Sport 0.373 / MP 0.206 vs 1.287m 2024; MP liquidity hold; waarborg MP 17.403m",
        "Publish hold vs 2026 restart + AGB dual already 1282/1283",
    ),
    (
        "comm_hh_school_4_81m_2025",
        "HH 2025 school t Centrum 4.809m / AGION 3.284m",
        "4808669",
        "T3 4.808669m uitg / 3.283656m AGION; MJP rest 1.000m; VTE 261.70",
        "Publish eindafrekening + restant FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners HH / politiezone Carma / HVZ Oost-Limburg / AGB MP+Sport / Fluvius / Limburg.net / OCMW / Zorg",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 GR+RVMW 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Houthalen-Helchteren after AGB 1282/1283",
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
        "lb_hh_fin_debt_17_37m_2025",
        "Stad+OCMW HH YE2025 fin debt 17.37m",
        "17365513",
        "6.0",
        "7.0",
        "Publish T4 creditor + why 21.5m MJP loans not drawn beside cash 4.8m",
        "fin debt 17.366m after 0.514m leasing; stock not TCO; ST 0.550m",
    ),
    (
        "lb_hh_pension_3_69m_2025",
        "Stad+OCMW HH YE2025 pension 3.69m JUMP",
        "3687588",
        "6.5",
        "6.0",
        "Publish actuarial note + OCMW respo 0.173m vs budget 0",
        "pension LT 3.688m vs 2.497m; stock not TCO",
    ),
    (
        "lb_hh_ocmw_neg_12_89m_2025",
        "OCMW HH YE2025 equity -12.89m / PnL -3.46m / tussenkomst 0",
        "12892244",
        "7.5",
        "7.0",
        "Publish why no 2025 tussenkomst while OCMW equity stays NEG",
        "city PnL +3.183m; equity city 161.568m / OCMW -12.892m",
    ),
    (
        "lb_hh_carma_5_65m_2025",
        "HH 2025 politiezone Carma 5.65m + HVZ 1.28m",
        "6935647",
        "6.5",
        "6.5",
        "Publish KUL-norm + GAS5 1.966m pass-through vs boetes 2.110m",
        "T2 dual 6.936m; AGB dual already 1282/1283",
    ),
    (
        "lb_hh_agb_sub_0_58m_2025",
        "HH 2025 AGB prijssub 0.58m halved + waarborg 19.82m",
        "578868",
        "6.5",
        "6.0",
        "Publish MP liquidity hold vs 2026 restart + 17.40m MP borg",
        "Sport 0.373 / MP 0.206 vs 1.287m; EVA FVA 0.980m",
    ),
    (
        "lb_hh_igs_40_12m_2025",
        "HH IGS FVA 40.12m + dividends 2.31m",
        "40120429",
        "5.5",
        "6.5",
        "Publish Fluvius/Limburg.net/NUHMA split vs reval +0.021m",
        "IGS stock 40.120m; dividends 2.311m; cash/AFM unchanged by book entry",
    ),
    (
        "lb_hh_school_4_81m_2025",
        "HH 2025 school t Centrum 4.81m / AGION 3.28m",
        "4808669",
        "5.5",
        "6.0",
        "Publish eindafrekening + MJP rest 1.00m",
        "T3 4.809m uitg / 3.284m AGION; VTE 261.70",
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
            "beneficiaries": "inwoners HH / politiezone Carma / HVZ Oost-Limburg / AGB MP+Sport / Fluvius / Limburg.net / OCMW / Zorg",
            "stated_goal": "Local GE residual map VL JR2025 Houthalen-Helchteren after AGB 1282/1283 + Kraainem 1284",
            "measured_outcome": (
                "assets 181.572m / fin debt 17.366m / pension 3.688m / "
                "AFM +3.195m / OCMW equity -12.892m / AGB sub 0.579m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; T4/OCMW FOI",
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
                "T4 per-loan creditors for 17.365513m (new leasing 0.514m + ST 0.550m; "
                "MJP 21.474m not drawn) + pension 3.687588m city/OCMW actuarial JUMP "
                "+1.191m + OCMW respo 0.173m + OCMW equity -12.892m vs tussenkomst 0 "
                "+ IGS FVA 40.120429m Fluvius/Limburg.net/NUHMA split + Carma 5.654923m "
                "KUL-norm vs GAS5 1.966m + AGB hold 0.579m vs 1.287m + school 4.809m"
            ),
            "why_it_matters": (
                "Unmined HH city+OCMW GE after AGB Masterplan 1282 and AGB Sport 1283 "
                "(same GR 22.06.2026). OCMW equity NEG 12.9m with no 2025 tussenkomst. "
                "MJP 21.5m loans not drawn. Distinct from Kraainem 1284."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Houthalen-Helchteren / OCMW Houthalen-Helchteren",
            "recipient_email": "financien@houthalen-helchteren.be",
            "recipient_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_hh_fin_debt_17_37m_2025",
            "linked_leaderboard_id": "lb_hh_fin_debt_17_37m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1285",
    "title": "Stad+OCMW Houthalen-Helchteren JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW HH JR2025 BBC text + documentatie + KBO; "
        "KBO 0216.773.026 / 0216.773.125; assets 181.572m / fin debt 17.366m / "
        "pension 3.688m / OCMW equity -12.892m / AGB sub 0.579m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1285 Stad+OCMW HH JR2025 GE residual; KBO 0216.773.026/"
        "0216.773.125; assets 181.572m fin debt 17.366m pension 3.688m "
        "AFM +3.195m gecorr +3.461m BBR -1.732m avail 3.867m cash 4.828m DROP "
        "Carma 5.655m HVZ 1.281m new loan 0.514m PnL -0.277m OCMW equity -12.892m "
        "AGB sub 0.579m VTE 261.70; FOI ready not sent; next rq_1286 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1286",
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
        "+ Stad+OCMW Kraainem 1284 + Stad+OCMW Houthalen-Helchteren 1285 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(Welzijnsvereniging Zorg HH / Audio only if a fetchable JR2025 PDF appears); "
        "AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
        "Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST unless a fetchable "
        "JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; skip AGB "
        "Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1285 after Stad+OCMW Houthalen-Helchteren JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1285", rq_new, rq_spawn)
print("research_queue 1285", found, "spawned_1286", spawned)

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
            "last_unit_id": "rq_1285",
            "ticks_completed": "1285",
            "paused": "no",
            "notes": (
                "tick1285 Stad+OCMW HH JR2025 GE residual; KBO 0216.773.026/"
                "0216.773.125; assets 181.572m fin debt 17.366m pension 3.688m "
                "OCMW equity -12.892m AGB sub 0.579m; FOI ready; next rq_1286 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1285 - 2026-08-17 - rq_1285 Stad+OCMW Houthalen-Helchteren GE residual
- Unit: Stad + OCMW Houthalen-Helchteren JR2025 GE package after AGB Masterplan tick1282 + AGB Sport tick1283 (same GR **22.06.2026** / pub **23.06.2026**; KBO **0216.773.026** / **0216.773.125**; BBC text PDF `BBC_JR_2025_G&O.pdf` 121p / 2.36MB + documentatie 187p / 2.60MB on meetingburger). Dual AGB FVA EVA **0.980m**. Seat Pastorijstraat 30 3530. AD Wim Haest / FD Ellen Janssen / burgemeester Alain Yzermans. NIS 72039. 8+4 VE. **Distinct from** mined AGB Masterplan / AGB Sport. City/OCMW J2 **is** in this PDF. PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone. Not an every-10 tick.
- EUR strong (primary BBC text PDF + documentatie): assets **181.572m** (was 174.406m); cash **4.828m** DROP vs **6.041m**; FVA **45.614m** (EVA **0.980m** + IGS **40.120m**); MVA **101.147m** leasing **12.303m**; fin debt **17.366m** (LT **15.041m** + ST due **1.774m** + ST **0.550m**) vs **18.008m**; new loans **0.514m** (leasing; MJP **21.474m** not drawn); pension LT **3.688m** JUMP vs **2.497m**; expl **+4.381m** (ontv **59.872m** / uitg **55.492m**; J3 city **+7.341m** / OCMW **−2.960m**); invest **−5.441m** (ontv **6.716m** / uitg **12.157m** vs MJP 28.195m); BBR year **−1.732m** / avail **3.867m**; AFM **+3.195m** / gecorr **+3.461m** (consol +AGB gecorr **+2.048m**); PnL **−0.277m** (city **+3.183m** / OCMW **−3.460m**; tussenkomst **0**); OCMW equity **−12.892m NEG**; pers **28.695m**; VTE paid **261.70** (city **242.05** / OCMW **19.65**); fiscal **28.037m** (OV **11.670m** + APB **10.553m** + GAS5 **2.110m**); gemeentefonds **10.886m**; politiezone Carma **5.655m** + HVZ **1.281m** + IGS **1.514m**; AGB prijssub **0.579m** (halved vs 1.287m); dividends **2.311m**; school 't Centrum **4.809m** / AGION **3.284m**; waarborgen **19.824m**.
- CSVs: sources+4/entities(new OCMW; city already 1282)/budgets+40/commitments+6/leaderboard+7 + FOI ready `gap_hh_fin_debt_17_37m_pension_3_69m_ocmw_neg_12_89m_l5` (not sent); rq_1285=done; spawn rq_1286; ticks=1285. Not a *0 tick — no progress refresh.
- Next: rq_1286 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined HH GE 1285 unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
