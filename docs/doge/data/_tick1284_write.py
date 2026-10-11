# -*- coding: utf-8 -*-
"""Tick 1284 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Kraainem JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:50:00Z"
TICK = 1284
SRC = "src_kraainem_jr2025_bbc"
SRC2 = "src_kraainem_jr2025_portal"
SRC3 = "src_kbo_kraainem_0207484285"
SRC4 = "src_kbo_ocmw_kraainem_0212189973"
SRC5 = "src_kraainem_jr2025_gr"
ENT = "city_kraainem"
OCMW = "ocmw_kraainem"
SRC_URL = "https://ocmw.kraainem.be/download.ashx?id=16927"
SRC2_URL = "https://ocmw.kraainem.be/nl/product/934/jaarrekening"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207484285"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212189973"
SRC5_URL = "https://kraainem.meetingburger.net/gr/19e8bdaa-4015-4d01-ac1c-803d6e88a634"
GAP = "gap_kraainem_fin_debt_6_40m_pension_3_15m_wokra_3_38m_l5"
HIER = "Vlaanderen>Gemeenten>Kraainem"

ASSETS = 70465814.07
ASSETS_2024 = 67941257.12
CASH = 10217763.24
CASH_2024 = 7792624.15
FVA = 16224935.27
IGS = 8648327.97
OTHER_FVA = 7569923.30
OCMW_VER = 6684.00
MVA = 40645702.73
LEASING = 0.00
FIN_DEBT = 6404601.30
FIN_DEBT_2024 = 5060653.23
FIN_DEBT_LT = 5223897.99
FIN_DEBT_ST = 1180703.31
PENSION = 3151151.53
PENSION_2024 = 3463712.87
CITY_PENS = 2339669.40
OCMW_PENS = 811482.13
EQUITY = 57095403.17
CITY_EQUITY = 55042390.72
OCMW_EQUITY = 2053012.45
CUM_PNL = 31392378.07
REVAL = 3945385.18
REVAL_CHG = -34185.00
EXPL = 3466350.49
EXPL_ONTV = 29919598.44
EXPL_UITG = 26453247.95
CITY_EXPL = 3405395.28
OCMW_EXPL = 60955.21
INVEST = -1923613.22
INVEST_ONTV = 361812.54
INVEST_UITG = 2285425.76
BBR = 2894593.66
AVAIL = 10267457.57
AFM = 2318206.88
GECORR = 3069406.55
NEW_LOANS = 2500000.00
PNL = 969579.41
CITY_PNL = 1905769.76
OCMW_PNL = -936190.35
OCMW_INT = 1403307.63
PERS = 13090451.00
PERS_2024 = 8971298.63
ONDERWIJS = 4558070.02
FISCAL = 18045981.76
OV = 7845968.24
APB = 9246754.11
GEMFONDS = 2222325.66
POLICE = 3378886.92
HVZ = 894686.94
IGS_SUB = 798689.52
CITY_ASSETS = 67883743.13
OCMW_ASSETS = 3841217.26
CITY_CASH = 10045906.01
OCMW_CASH = 171857.23
CITY_AVAIL = 8612360.66
OCMW_AVAIL = 1655096.91
AFL = 1156051.93


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


assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 0.02
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 0.02
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 0.02
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 0.02
assert abs((CITY_PENS + OCMW_PENS) - PENSION) < 0.02
assert abs((CITY_EQUITY + OCMW_EQUITY) - EQUITY) < 0.02
assert abs((IGS + OTHER_FVA + OCMW_VER) - FVA) < 0.02
assert abs((CITY_CASH + OCMW_CASH) - CASH) < 0.02
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 0.02
assert abs((CITY_AVAIL + OCMW_AVAIL) - AVAIL) < 0.02
assert abs((OV + APB + 189592.51 + 763666.90) - FISCAL) < 0.02

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Kraainem BBC jaarrekening 2025 (text PDF 264p)",
            "url": SRC_URL,
            "publisher": "Lokaal bestuur Kraainem / OCMW Kraainem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1284; 6.08MB text PDF; GR+RVMW 19.05.2026; pub 28-29.05.2026; "
                "KBO 0207.484.285 / 0212.189.973; assets 70.466m fin debt 6.405m "
                "pension 3.151m WOKRA 3.379m AFM +2.318m AGB 0"
            ),
        },
        {
            "source_id": SRC2,
            "title": "OCMW Kraainem jaarrekening portal (JR2025 download id=16927)",
            "url": SRC2_URL,
            "publisher": "OCMW Kraainem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1284; JR2025 5.8Mb listed; city kraainem.be page still 2024-only",
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Kraainem 0207.484.285",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1284; stad/gemeente since 01.01.1968; seat Arthur Dezangrélaan 17 1950; "
                "9 VE; AD Sophie Mary since 08.01.2024; burgemeester Bertrand Waucquez since 22.02.2019; "
                "NACE 84.114; KBO dump 16.08.2026"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO OCMW Kraainem 0212.189.973",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1284; OCMW since 01.01.1968 / name 01.04.1977; same seat; 1 VE; "
                "AD Sophie Mary since 08.01.2024; voorzitter Françoise Devleeschouwer since 08.01.2019; "
                "NACE 84.115; KBO dump 16.08.2026"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Gemeenteraad Kraainem 19.05.2026 vaststelling jaarrekening 2025",
            "url": SRC5_URL,
            "publisher": "Gemeente Kraainem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1284; GR quotes balanstotaal 70.465814m expl +3.466350m invest -1.923613m "
                "BBR +2.894594m avail 10.267458m AFM +2.318207m — matches BBC J2/J4"
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
            "name_nl": "Gemeente Kraainem",
            "name_fr": "Commune de Kraainem",
            "name_en": "Municipality of Kraainem",
            "level": "municipality",
            "parent_id": "",
            "community_language": "nl",
            "website": "https://www.kraainem.be",
            "foi_email": "info@kraainem.be",
            "foi_postal": "Arthur Dezangrélaan 17 1950 Kraainem",
            "notes": (
                "tick1284 JR2025 GE residual; KBO 0207.484.285; 9 VE; NIS 23099; "
                "AD Sophie Mary / FD Dimitri Das / burgemeester Bertrand Waucquez; "
                "consol assets 70.466m fin debt 6.405m pension 3.151m WOKRA 3.379m AGB 0; "
                "shared PZ WOKRA with Wezembeek-Oppem; FOI " + GAP
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Kraainem",
            "name_fr": "CPAS de Kraainem",
            "name_en": "OCMW Kraainem",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://ocmw.kraainem.be",
            "foi_email": "info@ocmw.kraainem.be",
            "foi_postal": "Arthur Dezangrélaan 17 1950 Kraainem",
            "notes": (
                "tick1284 JR2025; KBO 0212.189.973; 1 VE; assets 3.841m cash 0.172m "
                "fin debt 0 pension 0.811m PnL -0.936m city tussenkomst 1.403m; "
                "J2 BBR 0 after tussenkomst; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_kraainem_assets_2025", "2025", ASSETS, "J4 consol assets 70.465814m vs 67.941257m"),
    ("bud_kraainem_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 67.941257m"),
    ("bud_kraainem_city_assets_2025", "2025", CITY_ASSETS, "J4 city assets 67.883743m"),
    ("bud_kraainem_ocmw_assets_2025", "2025", OCMW_ASSETS, "J4 OCMW assets 3.841217m"),
    ("bud_kraainem_cash_2025", "2025", CASH, "J4 cash 10.217763m JUMP vs 7.792624m"),
    ("bud_kraainem_fva_2025", "2025", FVA, "J4 FVA 16.224935m EVA 0 IGS 8.648m other 7.570m"),
    ("bud_kraainem_igs_2025", "2025", IGS, "J4 IGS FVA 8.648328m reval -0.034185m"),
    ("bud_kraainem_mva_2025", "2025", MVA, "J4 MVA 40.645703m leasing 0"),
    ("bud_kraainem_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 6.404601m (LT 5.224 + ST due 1.181) vs 5.061m"),
    ("bud_kraainem_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4/T4 LT fin debt 5.223898m"),
    ("bud_kraainem_pension_2025", "2025", PENSION, "J4 pension LT 3.151152m vs 3.463713m (city 2.340 / OCMW 0.811)"),
    ("bud_kraainem_equity_2025", "2025", EQUITY, "J4/T5 nettoactief 57.095403m (city 55.042 / OCMW 2.053)"),
    ("bud_kraainem_cum_pnl_2025", "2025", CUM_PNL, "J4 cum P&L 31.392378m"),
    ("bud_kraainem_reval_2025", "2025", REVAL, "J4 herwaarderingsreserve 3.945385m (IGS chg -0.034185)"),
    ("bud_kraainem_expl_2025", "2025", EXPL, "J2/T2 expl +3.466350m (city +3.405 / OCMW +0.061)"),
    ("bud_kraainem_expl_ontv_2025", "2025", EXPL_ONTV, "T2 consol expl ontv 29.919598m after 1.403m tussenkomst elim"),
    ("bud_kraainem_expl_uitg_2025", "2025", EXPL_UITG, "T2 consol expl uitg 26.453248m"),
    ("bud_kraainem_invest_2025", "2025", INVEST, "J2/T2 invest -1.923613m (ontv 0.362 / uitg 2.285)"),
    ("bud_kraainem_invest_uitg_2025", "2025", INVEST_UITG, "T2 invest uitg 2.285426m ~ MJP 2.279m; narrative realisatie 47.42pct vs old envelope"),
    ("bud_kraainem_bbr_2025", "2025", BBR, "J2 BBR year +2.894594m vs MJP city -0.025m"),
    ("bud_kraainem_avail_2025", "2025", AVAIL, "J2 avail BBR 10.267458m (city 8.612 / OCMW 1.655)"),
    ("bud_kraainem_afm_2025", "2025", AFM, "J2 AFM +2.318207m (city 2.257 / OCMW 0.061)"),
    ("bud_kraainem_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +3.069407m (city 3.008 / OCMW 0.061)"),
    ("bud_kraainem_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 2.500000m bank"),
    ("bud_kraainem_afl_2025", "2025", AFL, "T2/T4 periodieke aflossingen 1.156052m"),
    ("bud_kraainem_pnl_2025", "2025", PNL, "J5 PnL +0.969579m (city +1.906 / OCMW -0.936)"),
    ("bud_kraainem_pers_2025", "2025", PERS, "J5/T2 personeel 13.090451m JUMP vs 8.971m; onderwijs andere ov 4.558m; VTE unpublished"),
    ("bud_kraainem_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 18.045982m (OV 7.846 + APB 9.247)"),
    ("bud_kraainem_apb_2025", "2025", APB, "T2 APB 9.246754m vs 8.042m 2024"),
    ("bud_kraainem_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.222326m"),
    ("bud_kraainem_police_2025", "2025", POLICE, "T2 politiezone WOKRA 3.378887m + invest 0.224m"),
    ("bud_kraainem_hvz_2025", "2025", HVZ, "T2 HVZ Vlaams-Brabant West 0.894687m + invest 0.063m"),
    ("bud_kraainem_igs_sub_2025", "2025", IGS_SUB, "T2 IGS Interza werksub 0.798690m"),
    ("bud_kraainem_ocmw_int_2025", "2025", OCMW_INT, "T5 city tussenkomst OCMW tekort 1.403308m"),
    ("bud_kraainem_agb_sub_2025", "2025", 0, "J4 EVA FVA 0; T2 AGB werksub 0; consol = GE+OCMW"),
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
        "comm_kraainem_fin_debt_6_40m_2025",
        "Stad+OCMW Kraainem YE2025 fin debt 6.405m",
        "6404601",
        "T4 6.404601m up vs 5.061m; new 2.500m bank; ST due 1.181m; OCMW 0; 6.9 remaining FOI",
        "Publish T4 creditor schedule + 2026-2031 pad FOI",
    ),
    (
        "comm_kraainem_pension_3_15m_2025",
        "Stad+OCMW Kraainem YE2025 pension LT 3.151m",
        "3151152",
        "J4 pension 3.151152m vs 3.464m; city 2.340 / OCMW 0.811 drop from 1.298; actuarial FOI",
        "Publish wettelijk vs extra-wettelijk + VTE FOI",
    ),
    (
        "comm_kraainem_wokra_3_38m_2025",
        "Kraainem 2025 politiezone WOKRA 3.379m + HVZ 0.895m",
        "4273574",
        "T2 dual 4.274m + invest 0.287m; vs Wezembeek WOKRA 3.085m; initieel 3.583m naar 3.379m",
        "Keep nominative 2026-2031 lock public; publish KUL-norm update FOI",
    ),
    (
        "comm_kraainem_new_loan_2_50m_2025",
        "Kraainem 2025 new bank loan 2.500m / cash JUMP 10.218m",
        "2500000",
        "T4 new 2.500m bank; cash 7.793 to 10.218; BBR +2.895m; invest only 2.285m",
        "Publish why 2.5m drawn beside cash 10.2m FOI",
    ),
    (
        "comm_kraainem_ocmw_int_1_40m_2025",
        "OCMW Kraainem 2025 PnL -0.936m / city tussenkomst 1.403m",
        "1403308",
        "city PnL +1.906m; OCMW J2 BBR 0 after tussenkomst; T5 1.403m; equity OCMW 2.053m",
        "Publish tussenkomst vs J5 reconcilatie FOI",
    ),
    (
        "comm_kraainem_onderwijs_4_56m_2025",
        "Kraainem 2025 onderwijs andere overheden 4.558m (pers JUMP)",
        "4558070",
        "T2 onderwijs andere ov 1.123 to 4.558; VL spec werksub 2.180 to 5.562; Klimboom/Diabolo",
        "Publish VTE + pass-through note FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Kraainem / politiezone WOKRA / HVZ VBW / Interza / Fluvius / OCMW",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 GR+RVMW 19.05.2026",
            "decision_date": "2026-05-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Kraainem (no AGB)",
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
        "lb_kraainem_fin_debt_6_40m_2025",
        "Stad+OCMW Kraainem YE2025 fin debt 6.40m",
        "6404601",
        "6.0",
        "6.0",
        "Publish T4 creditor + why 2.5m bank drawn beside cash 10.2m",
        "fin debt 6.405m after new 2.5m bank; stock not TCO",
    ),
    (
        "lb_kraainem_pension_3_15m_2025",
        "Stad+OCMW Kraainem YE2025 pension 3.15m",
        "3151152",
        "6.0",
        "5.5",
        "Publish actuarial note + OCMW drop 1.298 to 0.811",
        "pension LT 3.151m vs 3.464m; stock not TCO",
    ),
    (
        "lb_kraainem_wokra_3_38m_2025",
        "Kraainem 2025 politiezone WOKRA 3.38m + HVZ 0.89m",
        "4273574",
        "6.5",
        "6.0",
        "Publish KUL-norm vs Wezembeek 3.085m + 2026-2031 lock",
        "T2 dual 4.274m + invest 0.287m; AGB 0",
    ),
    (
        "lb_kraainem_new_loan_2_50m_2025",
        "Kraainem 2025 new bank loan 2.50m beside cash 10.22m",
        "2500000",
        "6.5",
        "6.0",
        "Publish liquidity vs 2.5m draw + invest 2.29m",
        "cash JUMP 7.79 to 10.22 after 2.5m loan; BBR +2.895m",
    ),
    (
        "lb_kraainem_ocmw_int_1_40m_2025",
        "OCMW Kraainem YE2025 PnL -0.94m / city tussenkomst 1.40m",
        "1403308",
        "6.5",
        "5.5",
        "Publish T5 tussenkomst vs OCMW J5 -0.936m / J2 BBR 0",
        "city PnL +1.906m; equity OCMW 2.053m / city 55.042m",
    ),
    (
        "lb_kraainem_onderwijs_4_56m_2025",
        "Kraainem 2025 onderwijs andere overheden 4.56m (pers JUMP)",
        "4558070",
        "6.0",
        "6.0",
        "Publish Klimboom/Diabolo pass-through + VTE",
        "pers 13.090m vs 8.971m; VL spec 5.562m; not extra own-staff TCO until FOI",
    ),
    (
        "lb_kraainem_igs_8_65m_2025",
        "Kraainem IGS FVA 8.65m + other FVA 7.57m",
        "8648328",
        "5.5",
        "5.5",
        "Publish Fluvius/Interza/Iverlek split vs reval -0.034m",
        "IGS stock 8.648m after -0.034m reval; cash/AFM unchanged by book entry",
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
            "beneficiaries": "inwoners Kraainem / politiezone WOKRA / HVZ VBW / Interza / Fluvius / OCMW",
            "stated_goal": "Local GE residual map VL JR2025 Kraainem after Wezembeek 1281 + AGB Sport HH 1283",
            "measured_outcome": (
                "assets 70.466m / fin debt 6.405m / pension 3.151m / "
                "AFM +2.318m / WOKRA 3.379m / AGB 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; T4/VTE FOI",
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
                "T4 per-loan creditors for 6.404601m (new bank 2.500m) + pension "
                "3.151152m city/OCMW actuarial (OCMW drop 1.298 to 0.811) + VTE "
                "behind pers 13.090451m / onderwijs 4.558070m JUMP + IGS FVA "
                "8.648328m Fluvius/Interza/Iverlek split reval -0.034185m + "
                "WOKRA 3.378887m KUL-norm vs Wezembeek 3.085m + tussenkomst "
                "1.403308m vs OCMW J5 -0.936m"
            ),
            "why_it_matters": (
                "Unmined Kraainem GE after Wezembeek-Oppem 1281 (shared WOKRA) "
                "and AGB Sport HH 1283. No AGB. New 2.5m bank loan beside cash "
                "10.2m. Distinct from Zaventem / Machelen / Wezembeek."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Kraainem / OCMW Kraainem",
            "recipient_email": "info@kraainem.be",
            "recipient_postal": "Arthur Dezangrélaan 17 1950 Kraainem",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_kraainem_fin_debt_6_40m_2025",
            "linked_leaderboard_id": "lb_kraainem_fin_debt_6_40m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1284",
    "title": "Stad+OCMW Kraainem JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Kraainem JR2025 BBC text + KBO; "
        "KBO 0207.484.285 / 0212.189.973; assets 70.466m / fin debt 6.405m / "
        "pension 3.151m / WOKRA 3.379m / AGB 0; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T11:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1284 Stad+OCMW Kraainem JR2025 GE residual; KBO 0207.484.285/"
        "0212.189.973; assets 70.466m fin debt 6.405m pension 3.151m "
        "AFM +2.318m gecorr +3.069m BBR +2.895m avail 10.267m cash 10.218m JUMP "
        "WOKRA 3.379m HVZ 0.895m new loan 2.500m PnL +0.970m AGB 0; FOI ready not sent; "
        "next rq_1285 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1285",
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
        "+ Stad+OCMW Kraainem 1284 done; "
        "prefer city+OCMW HH GE BBC_JR_2025_G&O 0216.773.026/0216.773.125 on same GR "
        "or other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
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
    "notes": "spawned tick1284 after Stad+OCMW Kraainem JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1284", rq_new, rq_spawn)
print("research_queue 1284", found, "spawned_1285", spawned)

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
            "last_unit_id": "rq_1284",
            "ticks_completed": "1284",
            "paused": "no",
            "notes": (
                "tick1284 Stad+OCMW Kraainem JR2025 GE residual; KBO 0207.484.285/"
                "0212.189.973; assets 70.466m fin debt 6.405m pension 3.151m "
                "WOKRA 3.379m AGB 0; FOI ready; next rq_1285 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1284 - 2026-08-17 - rq_1284 Stad+OCMW Kraainem GE residual
- Unit: Stad + OCMW Kraainem JR2025 GE package after AGB Sport HH tick1283 + Wezembeek-Oppem tick1281 (KBO **0207.484.285** / **0212.189.973**; BBC text PDF on ocmw.kraainem.be download.ashx?id=16927; 264p / 6.08MB; GR+RVMW **19.05.2026**; pub **28–29.05.2026**). **No AGB** (J4 EVA FVA **0**; T2 AGB werksub **0**; consol = GE+OCMW). Seat Arthur Dezangrélaan 17 1950. AD Sophie Mary / FD Dimitri Das / burgemeester Bertrand Waucquez. NIS 23099. 9+1 VE. **Distinct from** neighbouring Wezembeek-Oppem (shared politiezone WOKRA) and mined Zaventem / Machelen. City/OCMW J2 **is** in this PDF. HH city+OCMW GE BBC still unmined — left for a later unit. PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone. Not an every-10 tick.
- EUR strong (primary BBC text PDF): assets **70.466m** (was 67.941m); cash **10.218m** JUMP vs **7.793m**; FVA **16.225m** (EVA **0** + IGS **8.648m**); MVA **40.646m** leasing **0**; fin debt **6.405m** (LT **5.224m** + ST due **1.181m**) vs **5.061m**; new loans **2.500m** (bank); pension LT **3.151m** (was 3.464m; city **2.340m** / OCMW **0.811m**); expl **+3.466m** (T2 consol ontv **29.920m** / uitg **26.453m**; city **+3.405m** / OCMW **+0.061m**); invest **−1.924m** (ontv **0.362m** / uitg **2.285m**); BBR year **+2.895m** / avail **10.267m**; AFM **+2.318m** / gecorr **+3.069m**; PnL **+0.970m** (city **+1.906m** / OCMW **−0.936m**; tussenkomst **1.403m**); pers **13.090m** JUMP vs **8.971m** (onderwijs andere ov **4.558m** vs **1.123m**); fiscal **18.046m** (OV **7.846m** + APB **9.247m**); gemeentefonds **2.222m**; politiezone WOKRA **3.379m** + HVZ **0.895m** + IGS Interza **0.799m**. IGS reval **−0.034m**. VTE unpublished.
- CSVs: sources+5/entities(new city+OCMW)/budgets+35/commitments+6/leaderboard+7 + FOI ready `gap_kraainem_fin_debt_6_40m_pension_3_15m_wokra_3_38m_l5` (not sent); rq_1284=done; spawn rq_1285; ticks=1284. Not a *0 tick — no progress refresh.
- Next: rq_1285 residual dual L5 VL JR2025 hole_fill (prefer city+OCMW HH GE BBC or other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
