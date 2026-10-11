# -*- coding: utf-8 -*-
"""Tick 1281 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Wezembeek-Oppem JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T10:45:00Z"
TICK = 1281
SRC = "src_wezembeek_jr2025_bbc"
SRC2 = "src_wezembeek_jr2025_portal"
SRC3 = "src_kbo_wezembeek_0207506061"
SRC4 = "src_kbo_ocmw_wezembeek_0212182946"
SRC5 = "src_wezembeek_jr2025_gr"
ENT = "city_wezembeek_oppem"
OCMW = "ocmw_wezembeek_oppem"
SRC_URL = "https://www.wezembeek-oppem.be/file/download/9c75d024-b429-4aa1-b76e-ead63a15b9d6/3MiEB9pCzkjj8XIK4xQkl6HVIXIAjJ4vqf8gg1uDCI3d"
SRC2_URL = "https://www.wezembeek-oppem.be/jaarrekening"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0207506061"
SRC4_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0212182946"
SRC5_URL = "https://www.wezembeek-oppem.be/file/download/57d4007d-a6e7-4563-ad81-b7331db849de/i2kuV77WTWjqEmvxhUzAYxV7JDbEro8q4PsnzRrunM3d"
GAP = "gap_wezembeek_fin_debt_1_25m_pension_3_03m_wokra_3_09m_l5"
HIER = "Vlaanderen>Gemeenten>Wezembeek-Oppem"

ASSETS = 98189430
ASSETS_2024 = 95796211
CASH = 24899125
CASH_2024 = 25514305
FVA = 17398098
IGS = 10034949
OTHER_FVA = 7363148
IVERLEK = 9892496
WATERGROEP = 7311186
MVA = 53522790
LEASING = 1794046
FIN_DEBT = 1252506
FIN_DEBT_2024 = 1024069
FIN_DEBT_LT = 1133042
FIN_DEBT_ST = 119465
PENSION = 3034084
PENSION_2024 = 3023785
EQUITY = 89868797
CITY_EQUITY = 86165826
OCMW_EQUITY = 3702970
CUM_PNL = 35048395
REVAL = 5154157
REVAL_ADD = 219474
EXPL = 3376721
EXPL_ONTV = 28277109
EXPL_UITG = 24900388
INVEST = -5003120
INVEST_ONTV = 82344
INVEST_UITG = 5085464
BBR = -1389906
AVAIL = 23176456
AFM = 3252449
GECORR = 3302851
NEW_LOANS = 360766
PNL = 538217
CITY_PNL = 2183298
OCMW_PNL = -1645082
OCMW_INT = 1764562
PERS = 13589286
FISCAL = 17057651
OV = 6738988
APB = 9501819
GEMFONDS = 2490300
POLICE = 3085408
HVZ = 812171
FLUVIUS_ST = 111917


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


n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Wezembeek-Oppem BBC jaarrekening 2025 (text PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal bestuur Wezembeek-Oppem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1281; 3.7MB text PDF; GR+RVMW 22.06.2026; pub 01.07.2026; "
                "KBO 0207.506.061 / 0212.182.946; assets 98.189m fin debt 1.253m "
                "pension 3.034m AFM +3.252m gecorr +3.303m BBR year -1.390m "
                "avail 23.176m WOKRA 3.085m AGB 0"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Wezembeek-Oppem jaarrekening portal (JR2025 + GR + documentatie)",
            "url": SRC2_URL,
            "publisher": "Lokaal bestuur Wezembeek-Oppem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1281; JR2025 approved 22.06.2026 published 01.07.2026; no AGB",
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Wezembeek-Oppem 0207.506.061",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1281; Stad/gemeente since 01.01.1968; seat Louis Marcelisstraat 140 1970 "
                "since 25.10.2021; 7 VE; AD Geert Raymaekers since 01.06.2019; "
                "burgemeester Nicolas Celis since 10.02.2025; NACE 84.114"
            ),
        },
        {
            "source_id": SRC4,
            "title": "KBO OCMW Wezembeek-Oppem 0212.182.946",
            "url": SRC4_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1281; OCMW Wezembeek-Oppem; KBO seat Jozef De Keyzerstraat 15 1970; "
                "4 VE; voorzitter Antoine Silverberg since 10.02.2025; AD Raymaekers"
            ),
        },
        {
            "source_id": SRC5,
            "title": "Uittreksel GR 22.06.2026 jaarrekening 2025 Wezembeek-Oppem",
            "url": SRC5_URL,
            "publisher": "Lokaal bestuur Wezembeek-Oppem",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1281; GR+RVMW 22.06.2026 20 voor / 2 onthouding; euros from main BBC text PDF",
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENT,
            "name_nl": "Gemeente Wezembeek-Oppem",
            "name_fr": "Commune de Wezembeek-Oppem",
            "name_en": "Municipality of Wezembeek-Oppem",
            "level": "municipality",
            "parent_id": "sec_local",
            "community_language": "nl",
            "website": "https://www.wezembeek-oppem.be/",
            "foi_email": "financien@wezembeek-oppem.be",
            "foi_postal": "Louis Marcelisstraat 140 1970 Wezembeek-Oppem",
            "notes": (
                "tick1281 JR2025 GE residual; KBO 0207.506.061 / OCMW 0212.182.946; "
                "assets 98.189m fin debt 1.253m pension 3.034m AFM +3.252m "
                "gecorr +3.303m BBR year -1.390m avail 23.176m cash 24.899m "
                "WOKRA 3.085m HVZ 0.812m AGB 0; AD Raymaekers FD Moreels "
                "burgemeester Celis; FOI " + GAP
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Wezembeek-Oppem",
            "name_fr": "CPAS de Wezembeek-Oppem",
            "name_en": "OCMW Wezembeek-Oppem",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.wezembeek-oppem.be/",
            "foi_email": "financien@wezembeek-oppem.be",
            "foi_postal": "Louis Marcelisstraat 140 1970 Wezembeek-Oppem",
            "notes": (
                "tick1281; KBO 0212.182.946; KBO seat Jozef De Keyzerstraat 15; "
                "consol in city JR2025; OCMW PnL -1.645m vs city +2.183m; "
                "tussenkomst 1.765m; equity 3.703m; split FOI"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_wezembeek_assets_2025", "2025", ASSETS, "J4 assets 98.189430m vs 95.796211m"),
    ("bud_wezembeek_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 95.796211m"),
    ("bud_wezembeek_cash_2025", "2025", CASH, "J4 cash 24.899125m vs 25.514305m"),
    ("bud_wezembeek_fva_2025", "2025", FVA, "J4 FVA 17.398098m (EVA 0 + IGS 10.034949m + other 7.363148m)"),
    ("bud_wezembeek_igs_2025", "2025", IGS, "J4 IGS FVA 10.034949m vs 9.844577m; Iverlek/Fluvius 9.892m"),
    ("bud_wezembeek_iverlek_2025", "2025", IVERLEK, "J4 Iverlek/Fluvius FVA 9.892496m (sum Iverlek lines)"),
    ("bud_wezembeek_watergroep_2025", "2025", WATERGROEP, "J4 De Watergroep other FVA 7.311186m (riool 6.163 + drink 1.148)"),
    ("bud_wezembeek_mva_2025", "2025", MVA, "J4 MVA 53.522790m; gemeenschapsgoederen 50.780m"),
    ("bud_wezembeek_leasing_2025", "2025", LEASING, "J4 leasing 1.794046m vs 1.743862m; Fluvius LED aankoop 0.361m"),
    ("bud_wezembeek_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 1.252506m (LT 1.133 + ST due 0.119) vs 1.024m"),
    ("bud_wezembeek_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "J4/T4 LT fin debt 1.133042m"),
    ("bud_wezembeek_pension_2025", "2025", PENSION, "J4 pension LT 3.034084m vs 3.023785m"),
    ("bud_wezembeek_equity_2025", "2025", EQUITY, "J4/T5 nettoactief 89.868797m (city 86.166 / OCMW 3.703)"),
    ("bud_wezembeek_cum_pnl_2025", "2025", CUM_PNL, "J4 cum P&L 35.048395m (city 34.753 / OCMW 0.296)"),
    ("bud_wezembeek_reval_2025", "2025", REVAL, "J4/T5 herwaarderingsreserve 5.154157m (add 0.219474 IGS/Iverlek)"),
    ("bud_wezembeek_expl_2025", "2025", EXPL, "J2 expl +3.376721m (ontv 28.277 / uitg 24.900)"),
    ("bud_wezembeek_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 28.277109m"),
    ("bud_wezembeek_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 24.900388m"),
    ("bud_wezembeek_invest_2025", "2025", INVEST, "J2 invest -5.003120m (ontv 0.082 / uitg 5.085) vs MJP -8.707m"),
    ("bud_wezembeek_invest_uitg_2025", "2025", INVEST_UITG, "J2 invest uitg 5.085464m; realisatie 58pct vs MJP 8.760m"),
    ("bud_wezembeek_bbr_2025", "2025", BBR, "J2 BBR year -1.389906m vs MJP -7.587m"),
    ("bud_wezembeek_avail_2025", "2025", AVAIL, "J2 avail BBR 23.176456m; onbeschikbaar 0.187m"),
    ("bud_wezembeek_afm_2025", "2025", AFM, "J2 AFM +3.252449m vs MJP +0.864m"),
    ("bud_wezembeek_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +3.302851m vs MJP +0.906m"),
    ("bud_wezembeek_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.360766m Fluvius OV LED leasing"),
    ("bud_wezembeek_pnl_2025", "2025", PNL, "J5 PnL +0.538217m (city +2.183 / OCMW -1.645)"),
    ("bud_wezembeek_pers_2025", "2025", PERS, "J5/T2 personeel 13.589286m; onderwijs andere ov 3.773m; VTE unpublished"),
    ("bud_wezembeek_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 17.057651m (OV 6.739 + APB 9.502)"),
    ("bud_wezembeek_apb_2025", "2025", APB, "T2 APB 9.501819m vs 7.940m 2024"),
    ("bud_wezembeek_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.490300m"),
    ("bud_wezembeek_police_2025", "2025", POLICE, "T2 politiezone WOKRA 3.085408m (KUL-norm 47.73pct)"),
    ("bud_wezembeek_hvz_2025", "2025", HVZ, "T2 HVZ Vlaams-Brabant West 0.812171m"),
    ("bud_wezembeek_ocmw_int_2025", "2025", OCMW_INT, "T5 city tussenkomst OCMW tekort 1.764562m"),
    ("bud_wezembeek_agb_sub_2025", "2025", 0, "J4 EVA FVA 0; T2 AGB werksub 0; consol = GE+OCMW"),
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
        "comm_wezembeek_fin_debt_1_25m_2025",
        "Stad+OCMW Wezembeek-Oppem YE2025 fin debt 1.253m",
        "1252506",
        "T4 1.252506m up vs 1.024m; new 0.361m Fluvius LED leasing; ST due 0.119m = Fluvius OV 0.112 + internet 0.008",
        "Publish T4 creditor schedule + Fluvius OV lease pad FOI",
    ),
    (
        "comm_wezembeek_pension_3_03m_2025",
        "Stad+OCMW Wezembeek-Oppem YE2025 pension LT 3.034m",
        "3034084",
        "J4 pension 3.034084m vs 3.023785m; actuarial basis FOI",
        "Publish wettelijk vs extra-wettelijk + VTE FOI",
    ),
    (
        "comm_wezembeek_wokra_3_09m_2025",
        "Wezembeek-Oppem 2025 politiezone WOKRA 3.085m + HVZ 0.812m",
        "3897579",
        "T2 dual 3.898m; KUL-norm 47.73pct vs Kraainem 52.27pct; initieel ~3.78m naar 3.08m",
        "Keep nominative 2026-2031 lock public; publish KUL-norm update FOI",
    ),
    (
        "comm_wezembeek_iverlek_9_89m_2025",
        "Wezembeek Iverlek/Fluvius IGS FVA 9.892m + reval 0.219m",
        "9892496",
        "IGS FVA 10.035m; Iverlek 9.892m; herwaardering 0.219m; Watergroep other 7.311m",
        "Publish Iverlek A1e/A1g/Apg split vs dividend FOI",
    ),
    (
        "comm_wezembeek_invest_5_09m_2025",
        "Wezembeek 2025 invest uitg 5.085m vs MJP 8.760m (58pct)",
        "5085464",
        "realisatie 58pct; Fluvius LED 0.361m; sportsite 4m on hold; BBR year -1.390m",
        "Publish 2026 carry 3.706m + Riopact/Fluvius pad FOI",
    ),
    (
        "comm_wezembeek_ocmw_pnl_1_65m_2025",
        "OCMW Wezembeek-Oppem 2025 PnL -1.645m / city tussenkomst 1.765m",
        "1645082",
        "city PnL +2.183m; equity OCMW 3.703m; tussenkomst principle = OCMW book result",
        "Publish city/OCMW J2/J5 split + VTE FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Wezembeek-Oppem / Fluvius Iverlek / politiezone WOKRA / HVZ VBW / eredienst",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 GR+RVMW 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE residual map VL JR2025 Wezembeek-Oppem (no AGB)",
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
        "lb_wezembeek_fin_debt_1_25m_2025",
        "Stad+OCMW Wezembeek-Oppem YE2025 fin debt 1.25m",
        "1252506",
        "5.5",
        "5.0",
        "Publish T4 creditor + Fluvius OV lease schedule; keep low-debt path public",
        "fin debt 1.253m mostly Fluvius LED leasing; stock not TCO",
    ),
    (
        "lb_wezembeek_pension_3_03m_2025",
        "Stad+OCMW Wezembeek-Oppem YE2025 pension 3.03m",
        "3034084",
        "6.0",
        "5.5",
        "Publish actuarial note + wettelijk vs extra-wettelijk",
        "pension LT 3.034m vs 3.024m; stock not TCO",
    ),
    (
        "lb_wezembeek_wokra_3_09m_2025",
        "Wezembeek 2025 politiezone WOKRA 3.09m + HVZ 0.81m",
        "3897579",
        "6.5",
        "6.0",
        "Publish KUL-norm 47.73pct update + 2026-2031 WOKRA/HVZ lock",
        "T2 dual 3.898m; initieel ~3.78m naar 3.08m; AGB 0",
    ),
    (
        "lb_wezembeek_iverlek_9_89m_2025",
        "Wezembeek Iverlek/Fluvius IGS FVA 9.89m + reval 0.22m",
        "9892496",
        "6.0",
        "6.0",
        "Publish Iverlek A1e/A1g/Apg vs dividend + Watergroep 7.31m",
        "IGS stock 10.035m after 0.219m reval; cash/AFM unchanged by book entry",
    ),
    (
        "lb_wezembeek_ocmw_pnl_1_65m_2025",
        "OCMW Wezembeek YE2025 PnL -1.65m / city tussenkomst 1.76m",
        "1645082",
        "6.5",
        "5.5",
        "Publish city/OCMW J2/J5 split + tussenkomst principle",
        "OCMW PnL -1.645m; city +2.183m; equity OCMW 3.703m / city 86.166m",
    ),
    (
        "lb_wezembeek_invest_5_09m_2025",
        "Wezembeek 2025 invest 5.09m vs MJP 8.76m (58pct)",
        "5085464",
        "5.5",
        "5.5",
        "Publish 2026 carry 3.706m of Riopact/Fluvius/sportsite envelopes",
        "underspend vs MJP; BBR year still -1.390m on 5.085m invest; avail 23.176m",
    ),
    (
        "lb_wezembeek_cash_24_90m_2025",
        "Wezembeek YE2025 cash 24.90m / avail BBR 23.18m",
        "24899125",
        "5.0",
        "5.5",
        "Keep cash vs invest 5.09m / fin debt 1.25m path public",
        "cash-rich GE; BBR year -1.390m still leaves avail 23.176m",
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
            "beneficiaries": "inwoners Wezembeek-Oppem / Fluvius Iverlek / politiezone WOKRA / HVZ VBW / eredienst",
            "stated_goal": "Local GE residual map VL JR2025 Wezembeek-Oppem after Gingelom 1280",
            "measured_outcome": (
                "assets 98.189m / fin debt 1.253m / pension 3.034m / "
                "AFM +3.252m / WOKRA 3.085m / AGB 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; city/OCMW split FOI",
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
                "City vs OCMW split of J2/J4/J5 (BBR/AFM/gecorr/assets/cash/"
                "fin debt/pension/pers/VTE) + T4 per-loan creditors for "
                "1.252506m (Fluvius OV lease 0.112m of ST due) + Iverlek "
                "FVA 9.892496m reval 0.219474m + pension 3.034084m + "
                "WOKRA 3.085408m KUL-norm + IGS werksub 0 vs MJP 0.933m"
            ),
            "why_it_matters": (
                "Unmined Wezembeek-Oppem GE after Gingelom 1280 and Machelen 1279. "
                "No AGB. Cash-rich (24.9m) with low fin debt (1.25m Fluvius LED). "
                "WOKRA shared with Kraainem. Distinct from Zaventem / Tienen."
            ),
            "priority": "8",
            "recipient_body": "Lokaal bestuur Wezembeek-Oppem / OCMW Wezembeek-Oppem",
            "recipient_email": "financien@wezembeek-oppem.be",
            "recipient_postal": "Louis Marcelisstraat 140 1970 Wezembeek-Oppem",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_wezembeek_fin_debt_1_25m_2025",
            "linked_leaderboard_id": "lb_wezembeek_fin_debt_1_25m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1281",
    "title": "Stad+OCMW Wezembeek-Oppem JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Wezembeek-Oppem JR2025 BBC text + KBO; "
        "KBO 0207.506.061 / 0212.182.946; assets 98.189m / fin debt 1.253m / "
        "pension 3.034m / WOKRA 3.085m / AGB 0; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T10:20:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1281 Stad+OCMW Wezembeek-Oppem JR2025 GE residual; KBO 0207.506.061/"
        "0212.182.946; assets 98.189m fin debt 1.253m pension 3.034m "
        "AFM +3.252m gecorr +3.303m BBR year -1.390m avail 23.176m cash 24.899m "
        "WOKRA 3.085m HVZ 0.812m Iverlek 9.892m PnL +0.538m AGB 0; FOI ready not sent; "
        "next rq_1282 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1282",
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
        "+ Stad+OCMW Wezembeek-Oppem 1281 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; AGB PATRI "
        "Sint-Truiden (0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
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
    "notes": "spawned tick1281 after Stad+OCMW Wezembeek-Oppem JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1281", rq_new, rq_spawn)
print("research_queue 1281", found, "spawned_1282", spawned)

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
            "last_unit_id": "rq_1281",
            "ticks_completed": "1281",
            "paused": "no",
            "notes": (
                "tick1281 Stad+OCMW Wezembeek-Oppem JR2025 GE residual; KBO 0207.506.061/"
                "0212.182.946; assets 98.189m fin debt 1.253m pension 3.034m "
                "WOKRA 3.085m AGB 0; FOI ready; next rq_1282 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1281 - 2026-08-17 - rq_1281 Stad+OCMW Wezembeek-Oppem GE residual
- Unit: Stad + OCMW Wezembeek-Oppem JR2025 GE package after Stad+OCMW Gingelom tick1280 (KBO **0207.506.061** / **0212.182.946**; BBC text PDF on city site; GR+RVMW 22.06.2026; pub 01.07.2026). **No AGB** (J4 EVA FVA **0**; T2 AGB werksub **0**; consol = GE+OCMW). Seat Louis Marcelisstraat 140 1970. AD Geert Raymaekers / FD Anne-Sophie Moreels / burgemeester Nicolas Celis. NIS 23103. 7+4 VE. **Distinct from** neighbouring Kraainem (shared politiezone WOKRA) and mined Zaventem / Machelen / Tienen / Gingelom. PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare — not redone. Not an every-10 tick.
- EUR strong (primary BBC text PDF): assets **98.189m** (was 95.796m); cash **24.899m** vs **25.514m**; FVA **17.398m** (EVA **0** + IGS **10.035m**); MVA **53.523m** leasing **1.794m**; fin debt **1.253m** (LT **1.133m** + ST due **0.119m**) vs **1.024m**; new loans **0.361m** (Fluvius LED leasing); pension LT **3.034m** (was 3.024m); expl **+3.377m** (ontv **28.277m** / uitg **24.900m**); invest **−5.003m** (ontv **0.082m** / uitg **5.085m**, 58pct vs MJP); BBR year **−1.390m** / avail **23.176m**; AFM **+3.252m** / gecorr **+3.303m**; PnL **+0.538m** (city **+2.183m** / OCMW **−1.645m**; tussenkomst **1.765m**); pers **13.589m**; fiscal **17.058m** (OV **6.739m** + APB **9.502m**); gemeentefonds **2.490m**; politiezone WOKRA **3.085m** + HVZ **0.812m** + IGS **0**. Iverlek/Fluvius FVA **9.892m** + IGS reval **0.219m**. VTE + city/OCMW J2 split unpublished.
- CSVs: sources+5/entities(new city+OCMW)/budgets+34/commitments+6/leaderboard+7 + FOI ready `gap_wezembeek_fin_debt_1_25m_pension_3_03m_wokra_3_09m_l5` (not sent); rq_1281=done; spawn rq_1282; ticks=1281. Not a *0 tick — no progress refresh.
- Next: rq_1282 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
