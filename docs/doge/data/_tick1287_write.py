# -*- coding: utf-8 -*-
"""Tick 1287 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Ronse JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T13:20:00Z"
TICK = 1287
SRC = "src_ronse_jr2025_bbc"
SRC2 = "src_ronse_jr2025_portal"
SRC3 = "src_kbo_stad_ronse_0207460432"
SRC4 = "src_kbo_ocmw_ronse_0212165922"
ENT = "city_ronse"
OCMW = "ocmw_ronse"
SRC_URL = "https://www.ronse.be/sites/ronse/files/2026-07/Jaarrekening%202025%20Lokaal%20Bestuur%20Ronse%20-%20definitief.pdf"
SRC2_URL = "https://www.ronse.be/nl/meerjarenplan-2020-2025"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207460432"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212165922"
GAP = "gap_ronse_fin_debt_25_02m_pension_19_50m_ocmw_tussen_5_10m_l5"
HIER = "Vlaanderen>Gemeenten>Ronse"

ASSETS = 172786692
ASSETS_2024 = 171302780
CASH = 4131356
CASH_2024 = 2774122
CURRENT = 22524304
FIXED = 150262388
FVA = 44267784
EVA = 3054638
IGS = 41155449
OTHER_FVA = 57697
MVA = 75342535
LEASING = 2973067
IVA = 970306
LT_REC = 29681763
SCHULDEN = 54012282
EQUITY = 118774410
CAP_SUBS = 8867433
CUM_PNL = 2594194
REVAL = 15247136
REVAL_2024 = 14541052
OTHER_EQUITY = 92065647
FIN_DEBT = 25018179
FIN_DEBT_2024 = 25022320
FIN_DEBT_LT = 19906219
FIN_DEBT_ST_DUE = 2611961
FIN_DEBT_ST = 2500000
NEW_LOANS = 6587668
NEW_BANK = 6000000
NEW_LEASE = 587668
AFL = 2591809
PENSION = 19501000
PENSION_2024 = 21005065
PENS_MAND = 2127575
PENS_STAT = 11349341
EXPL = 4790479
EXPL_ONTV = 57851995
EXPL_UITG = 53061516
CITY_EXPL = 10138736
OCMW_EXPL = -5348258
INVEST = -3556074
INVEST_ONTV = 1957461
INVEST_UITG = 5513535
BBR = 7361499
AVAIL = 12475617
UNAVAIL = 186667
CUM_BBR = 12662284
AFM = 4467292
GECORR = 5057315
AANGEWEZEN = 2001786
PNL = 653618
PERS_T2 = 28558510
PERS_J5 = 28513750
FISCAL = 24722707
OV = 10929307
APB = 8182946
GEMFONDS = 12823289
POLICE = 5141868
HVZ = 833236
HVZ_INV = 1008676
AGB_SUB = 2300865
AGB_SCO_SPORT = 1578100
AGB_SOB = 485721
AGB_SCO_CULT = 237044
AGB_INV = 128289
AGB_LOAN_NEW = 137387
AGB_LOANS = 28528777
OCMW_TUSSEN = 5102638
IGS_SUB = 28258
IVLA_RECLASS = 1404911
GOEDEREN = 9505245
LEEFLOON = 3645308
FORMATIE = 257.50
CONSOL_AVAIL = 13352488
CONSOL_AFM = 4589449
CONSOL_GECORR = 3815694
KERK_INV = 737246


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
assert abs((LT_REC + FVA + MVA + IVA) - FIXED) < 2
assert abs((EVA + IGS + OTHER_FVA) - FVA) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQUITY) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST_DUE + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 2
assert abs((EXPL + INVEST) - 1234405) < 2
assert abs((1234405 + 6127094) - BBR) < 2
assert abs((BBR + 5300785) - CUM_BBR) < 2
assert abs((CUM_BBR - UNAVAIL) - AVAIL) < 2
assert abs((EXPL - 323187) - AFM) < 2
assert abs((AFL - AANGEWEZEN) - 590023) < 2
assert abs((AFM + 590023) - GECORR) < 2
assert abs((AGB_SCO_SPORT + AGB_SOB + AGB_SCO_CULT) - AGB_SUB) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 3
assert abs((NEW_BANK + NEW_LEASE) - NEW_LOANS) < 2

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Ronse BBC jaarrekening 2025 (text PDF 301p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Ronse",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1287; 13.98MB text PDF; print 05.06.2026; pub 09.07.2026; GR 29.06.2026; "
                "KBO 0207.460.432/0212.165.922; assets 172.787m fin debt 25.018m pension 19.501m "
                "AFM +4.467m gecorr +5.057m OCMW tussen 5.103m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Stad Ronse MJP/JR portal — JR2025 Lokaal Bestuur pub 09.07.2026",
            "url": SRC2_URL,
            "publisher": "Stad Ronse",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1287; Jaarrekening 2025 lokaal bestuur gepubliceerd 09.07.2026; "
                "siblings AGB SCO 1286 / AGB SOB 1194 / OVERO 1062 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Stad Ronse 0207.460.432",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1287; Stad since 01.01.1968; seat Grote Markt 12 9600 since 01.01.2005; "
                "14 VE; burgemeester Ignace Michaux since 01.09.2022; NACE 84.114; "
                "aanbestedende overheid; RSZ werkgever since 01.01.2022"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO OCMW Ronse 0212.165.922",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1287; OCMW since 01.01.1968; seat Oscar Delghuststraat 62 9600 since 01.01.1995; "
                "4 VE; voorzitter Wim Vandevelde since 07.11.2013; NACE 84.115; "
                "aanbestedende overheid; RSZ werkgever since 01.01.2022"
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
            "name_nl": "OCMW Ronse",
            "name_fr": "CPAS Renaix",
            "name_en": "OCMW Ronse (public social welfare centre)",
            "level": "local",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.ronse.be",
            "foi_email": "jurgen.soetens@ronse.be",
            "foi_postal": "Oscar Delghuststraat 62 9600 Ronse",
            "notes": (
                "tick1287 JR2025 GE residual with city; KBO 0212.165.922; 4 VE; "
                "voorzitter Wim Vandevelde; J3 expl -5.348m; tussenkomst 5.103m "
                "(avail BBR -5.103m); leefloon 3.645m; city/OCMW J4 split FOI; "
                "OVERO dual already 1062"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_ronse_assets_2025", "2025", ASSETS, "J4 assets 172.786692m vs 171.302780m"),
    ("bud_ronse_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 171.302780m"),
    ("bud_ronse_cash_2025", "2025", CASH, "J4 cash 4.131356m JUMP vs 2.774122m"),
    ("bud_ronse_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 2.774122m"),
    ("bud_ronse_fva_2025", "2025", FVA, "J4 FVA 44.267784m; EVA 3.055m + IGS 41.155m"),
    ("bud_ronse_eva_2025", "2025", EVA, "J4 EVA FVA 3.054638m (SCO+SOB)"),
    ("bud_ronse_igs_2025", "2025", IGS, "J4 IGS FVA 41.155449m"),
    ("bud_ronse_mva_2025", "2025", MVA, "J4 MVA 75.342535m; leasing 2.973m"),
    ("bud_ronse_leasing_2025", "2025", LEASING, "J4 leasing MVA 2.973067m"),
    ("bud_ronse_equity_2025", "2025", EQUITY, "J4 nettoactief 118.774410m vs 116.491086m"),
    ("bud_ronse_reval_2025", "2025", REVAL, "J4 herwaard 15.247136m vs 14.541052m"),
    ("bud_ronse_schulden_2025", "2025", SCHULDEN, "J4 schulden 54.012282m vs 54.811695m"),
    ("bud_ronse_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 25.018179m vs 25.022320m"),
    ("bud_ronse_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 25.022320m"),
    ("bud_ronse_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin 19.906219m"),
    ("bud_ronse_st_due_2025", "2025", FIN_DEBT_ST_DUE, "T4/J4 ST due 2.611961m"),
    ("bud_ronse_cp_2025", "2025", FIN_DEBT_ST, "T4/J4 commercial paper 2.500m DROP vs 6.500m"),
    ("bud_ronse_new_loans_2025", "2025", NEW_LOANS, "T4/T2 new loans 6.587668m (bank 6.000 + lease 0.588)"),
    ("bud_ronse_afl_2025", "2025", AFL, "T4/J2 periodieke aflossingen 2.591809m"),
    ("bud_ronse_pension_2025", "2025", PENSION, "J4 pension LT 19.501000m DROP vs 21.005065m"),
    ("bud_ronse_pension_2024", "2024", PENSION_2024, "J4 YE2024 pension 21.005065m"),
    ("bud_ronse_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +4.790479m"),
    ("bud_ronse_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 57.851995m"),
    ("bud_ronse_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 53.061516m"),
    ("bud_ronse_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +10.138736m (ontv 49.280 / uitg 39.142)"),
    ("bud_ronse_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -5.348258m (ontv 8.572 / uitg 13.920)"),
    ("bud_ronse_invest_2025", "2025", INVEST, "J2 invest saldo -3.556074m"),
    ("bud_ronse_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +7.361499m"),
    ("bud_ronse_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 12.475617m (onbeschikbaar 0.187m)"),
    ("bud_ronse_afm_2025", "2025", AFM, "J2 AFM +4.467292m"),
    ("bud_ronse_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +5.057315m (aangewezen 2.002m)"),
    ("bud_ronse_pnl_2025", "2025", PNL, "J5 PnL +0.653618m vs -6.379435m"),
    ("bud_ronse_pers_2025", "2025", PERS_T2, "T2 bezoldigingen 28.558510m (J5 28.513750m)"),
    ("bud_ronse_fiscal_2025", "2025", FISCAL, "T2 fiscale 24.722707m (OV 10.929 + APB 8.183)"),
    ("bud_ronse_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 12.823289m"),
    ("bud_ronse_police_2025", "2025", POLICE, "T2 politiezone 5.141868m"),
    ("bud_ronse_hvz_2025", "2025", HVZ, "T2 HVZ Vlaamse Ardennen 0.833236m"),
    ("bud_ronse_agb_sub_2025", "2025", AGB_SUB, "T2 AGB werksub 2.300865m (SCO 1.578+0.237 + SOB 0.486)"),
    ("bud_ronse_agb_loans_2025", "2025", AGB_LOANS, "TB 2903004 toegestane AGB-leningen 28.528777m"),
    ("bud_ronse_ocmw_tussen_2025", "2025", OCMW_TUSSEN, "Kengetallen/AR tussenkomst OCMW 5.102638m"),
    ("bud_ronse_leefloon_2025", "2025", LEEFLOON, "T2/J5 individuele hulp 3.645308m vs 3.060259m"),
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
        "comm_ronse_fin_debt_25_02m_2025",
        "Ronse YE2025 fin debt 25.018m",
        "25018179",
        "T4 25.018179m vs 25.022m; LT 19.906 + ST due 2.612 + CP 2.500; new 6.588m (bank 6.000 + lease 0.588)",
        "Publish T4 per-loan creditors + why CP drop vs new 6m bank FOI",
    ),
    (
        "comm_ronse_pension_19_50m_2025",
        "Ronse YE2025 pension LT 19.501m",
        "19501000",
        "J4 19.501000m DROP vs 21.005065m; fonds mand 2.128 + statutair 11.349; city/OCMW split FOI",
        "Publish actuarial DROP + city/OCMW split FOI",
    ),
    (
        "comm_ronse_ocmw_tussen_5_10m_2025",
        "Ronse 2025 OCMW tussenkomst 5.103m",
        "5102638",
        "OCMW avail BBR -5.102638m; J3 OCMW expl -5.348m; leefloon 3.645m JUMP",
        "Publish 2026-2031 tussenkomst lock + city/OCMW J4 split FOI",
    ),
    (
        "comm_ronse_agb_dual_2_30m_2025",
        "Ronse 2025 AGB werksub 2.301m + loans 28.529m",
        "2300865",
        "T2 SCO sport 1.578 + SOB 0.486 + SCO cult 0.237; new SCO loan 0.137; rec 28.529m",
        "Publish remaining AGB erfpacht/TIO3 schedule FOI",
    ),
    (
        "comm_ronse_igs_41_16m_2025",
        "Ronse YE2025 IGS FVA 41.155m",
        "41155449",
        "J4 IGS 41.155449m + EVA 3.055m; reval +0.706m; IVLA reclass 1.405m to goods",
        "Publish Fluvius/IVLA split vs reval FOI",
    ),
    (
        "comm_ronse_police_hvz_5_98m_2025",
        "Ronse 2025 politiezone 5.142m + HVZ 0.833m",
        "5975104",
        "T2 PZ 5.141868 + HVZ 0.833236; HVZ invest 1.009m; kerkfabriek invest 0.737m",
        "Publish KUL-norm + HVZ invest 1.009m pad FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Ronse / OCMW / AGB SCO / AGB SOB / OVERO / politiezone / HVZ Vlaamse Ardennen",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Lokaal Bestuur Ronse print 05.06.2026 / pub 09.07.2026 / GR 29.06.2026",
            "decision_date": "2026-06-29",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Ronse after SCO 1286 + SOB 1194 + OVERO 1062",
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
        "lb_ronse_fin_debt_25_02m_2025",
        "Ronse YE2025 fin debt 25.02m",
        "25018179",
        "7.0",
        "7.5",
        "Publish T4 per-loan + CP 2.50m vs new bank 6.00m",
        "fin debt 25.018m flat vs 25.022m; new 6.588m; CP DROP 6.5 to 2.5",
    ),
    (
        "lb_ronse_pension_19_50m_2025",
        "Ronse YE2025 pension LT 19.50m",
        "19501000",
        "7.0",
        "7.5",
        "Publish actuarial DROP 1.50m + city/OCMW split",
        "pension 19.501m DROP vs 21.005m; fonds 13.477m",
    ),
    (
        "lb_ronse_ocmw_tussen_5_10m_2025",
        "Ronse 2025 OCMW tussenkomst 5.10m",
        "5102638",
        "6.5",
        "6.5",
        "Publish 2026-2031 tussenkomst + J4 city/OCMW split",
        "OCMW avail BBR -5.103m; J3 expl -5.348m; leefloon 3.645m",
    ),
    (
        "lb_ronse_agb_dual_2_30m_2025",
        "Ronse 2025 AGB werksub 2.30m + loans 28.53m",
        "2300865",
        "6.5",
        "6.5",
        "Publish remaining SCO/SOB erfpacht + TIO3 schedule",
        "werksub 2.301m; new SCO loan 0.137m; rec 28.529m; EVA 3.055m",
    ),
    (
        "lb_ronse_igs_41_16m_2025",
        "Ronse IGS FVA 41.16m + IVLA reclass 1.40m",
        "41155449",
        "5.5",
        "6.5",
        "Publish Fluvius/IVLA split vs reval +0.706m",
        "IGS 41.155m; IVLA 1.405m moved to goods; IGS sub 0.028m",
    ),
    (
        "lb_ronse_police_hvz_5_98m_2025",
        "Ronse 2025 politiezone 5.14m + HVZ 0.83m",
        "5975104",
        "6.0",
        "6.0",
        "Publish KUL-norm + HVZ invest 1.01m",
        "PZ 5.142 + HVZ 0.833; HVZ invest 1.009; kerk 0.737",
    ),
    (
        "lb_ronse_pers_28_56m_2025",
        "Ronse 2025 personeel 28.56m / formatie 257.50",
        "28558510",
        "5.5",
        "6.5",
        "Publish paid VTE city vs OCMW vs formatie 257.50",
        "T2 28.559m / J5 28.514m; formatie Dec 2025 257.50; paid VTE FOI",
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
            "beneficiaries": "inwoners Ronse / OCMW / AGB SCO / AGB SOB / OVERO / politiezone / HVZ Vlaamse Ardennen",
            "stated_goal": "Local GE residual map VL JR2025 Ronse after SCO 1286 + SOB 1194 + OVERO 1062",
            "measured_outcome": (
                "assets 172.787m / fin debt 25.018m / pension 19.501m / "
                "AFM +4.467m / gecorr +5.057m / OCMW tussen 5.103m / AGB sub 2.301m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.5",
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
                "T4 per-loan creditors for 25.018179m (new bank 6.000m + lease 0.588m + "
                "CP DROP 6.500 to 2.500) + pension 19.501000m city/OCMW actuarial DROP "
                "1.504m + fonds mand 2.128/stat 11.349 + city vs OCMW J2/J4/J5 split "
                "+ OCMW tussenkomst 5.102638m pad 2026-2031 + IGS 41.155449m Fluvius/IVLA "
                "split reval +0.706m + AGB dual werksub 2.300865 / loans 28.528777 + "
                "paid VTE vs formatie 257.50"
            ),
            "why_it_matters": (
                "Unmined Ronse city+OCMW GE after sibling AGB SCO 1286 + SOB 1194 + OVERO 1062. "
                "Fin debt 25.018m with new 6.588m bank/lease vs CP drop. Pension stock 19.501m. "
                "OCMW tussenkomst 5.103m. AGB loans 28.529m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Ronse / OCMW Ronse",
            "recipient_email": "jurgen.soetens@ronse.be",
            "recipient_postal": "Grote Markt 12 9600 Ronse",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_ronse_fin_debt_25_02m_2025",
            "linked_leaderboard_id": "lb_ronse_fin_debt_25_02m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1287",
    "title": "Stad+OCMW Ronse JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Ronse JR2025 BBC text + KBO; "
        "KBO 0207.460.432 / 0212.165.922; assets 172.787m / fin debt 25.018m / "
        "pension 19.501m / OCMW tussen 5.103m / AGB sub 2.301m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:05:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1287 Stad+OCMW Ronse JR2025 GE residual; KBO 0207.460.432/"
        "0212.165.922; assets 172.787m fin debt 25.018m pension 19.501m "
        "AFM +4.467m gecorr +5.057m BBR +7.361m avail 12.476m cash 4.131m JUMP "
        "new loan 6.588m CP 2.500m OCMW tussen 5.103m AGB sub 2.301m "
        "AGB loans 28.529m formatie 257.50; FOI ready not sent; "
        "next rq_1288 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1288",
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
        "+ AGB SCO Ronse 1286 + Stad+OCMW Ronse 1287 done; prefer other unmined "
        "AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(Welzijnsvereniging Zorg HH / Audio only if a fetchable JR2025 PDF appears); "
        "Steenokkerzeel city+OCMW JR2025 approved 18.06.2026 on echo raadpleegomgeving only if PDF fetches; "
        "AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
        "Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only / Oosterzele De Kluize "
        "unless a fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; skip AGB "
        "Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "skip Dilbeek/Wijnegem city GE already mined; skip Wingene/Genk/Brasschaat AGB; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1287 after Stad+OCMW Ronse JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1287", rq_new, rq_spawn)
print("research_queue 1287", found, "spawned_1288", spawned)

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
            "last_unit_id": "rq_1287",
            "ticks_completed": "1287",
            "paused": "no",
            "notes": (
                "tick1287 Stad+OCMW Ronse JR2025 GE residual; KBO 0207.460.432/"
                "0212.165.922; assets 172.787m fin debt 25.018m pension 19.501m "
                "OCMW tussen 5.103m AGB sub 2.301m; FOI ready; next rq_1288 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1287 - 2026-08-17 - rq_1287 Stad+OCMW Ronse GE residual
- Unit: Stad + OCMW Ronse JR2025 GE package after sibling AGB SCO tick1286 + AGB SOB tick1194 + OVERO tick1062 (KBO **0207.460.432** / **0212.165.922**; BBC text PDF on ronse.be 301p / 13.98MB; print **05.06.2026**; pub **09.07.2026**; GR **29.06.2026**). Dual AGB FVA EVA **3.055m**. Seat Grote Markt 12 / OCMW Oscar Delghuststraat 62. AD Julien Vandenhoucke / FD Jurgen Soetens / burgemeester Ignace Michaux / OCMW-voorzitter Wim Vandevelde. NIS 45041. 14+4 VE. **Distinct from** mined AGB SCO / AGB SOB / OVERO. City/OCMW J2 **is** in this PDF (consol). Dilbeek/Wijnegem city GE already mined; Steenokkerzeel city GE still echo-SPA; PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone. Not an every-10 tick.
- EUR strong (primary BBC text PDF): assets **172.787m** (was 171.303m); cash **4.131m** JUMP vs **2.774m**; FVA **44.268m** (EVA **3.055m** + IGS **41.155m**); MVA **75.343m** leasing **2.973m**; fin debt **25.018m** (LT **19.906m** + ST due **2.612m** + CP **2.500m**) vs **25.022m**; new loans **6.588m** (bank **6.000m** + leasing **0.588m**); pension LT **19.501m** DROP vs **21.005m**; expl **+4.790m** (ontv **57.852m** / uitg **53.062m**; J3 city **+10.139m** / OCMW **−5.348m**); invest **−3.556m** (ontv **1.957m** / uitg **5.514m**); BBR year **+7.361m** / avail **12.476m**; AFM **+4.467m** / gecorr **+5.057m** (consol +AGB gecorr **+3.816m**); PnL **+0.654m** (was −6.379m); OCMW tussenkomst **5.103m**; pers T2 **28.559m** / J5 **28.514m**; formatie **257.50** (paid VTE unpublished); fiscal **24.723m** (OV **10.929m** + APB **8.183m**); gemeentefonds **12.823m**; politiezone **5.142m** + HVZ **0.833m** + HVZ invest **1.009m**; AGB werksub **2.301m** (SCO sport **1.578m** + SOB **0.486m** + SCO cult **0.237m**); AGB loans rec **28.529m**; IVLA reclass **1.405m**.
- CSVs: sources+4/entities(new OCMW; city already present)/budgets+41/commitments+6/leaderboard+7 + FOI ready `gap_ronse_fin_debt_25_02m_pension_19_50m_ocmw_tussen_5_10m_l5` (not sent); rq_1287=done; spawn rq_1288; ticks=1287. Not a *0 tick — no progress refresh.
- Next: rq_1288 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; Steenokkerzeel city GE only if a fetchable JR appears; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Bau-huis / Maaseik / Diepenbeek / already-mined Ronse GE 1287 unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
