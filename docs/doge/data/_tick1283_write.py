# -*- coding: utf-8 -*-
"""Tick 1283 (research_queue patched surgically — last line + spawn only).
AGB Sport Houthalen-Helchteren JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:25:00Z"
TICK = 1283
SRC = "src_agbsp_jr2025_nbb"
SRC2 = "src_agbsp_jr2025_gr"
SRC3 = "src_kbo_agbsp_0898822982"
ENT = "agb_houthalen_sport"
CITY = "city_houthalen_helchteren"
SRC_URL = "https://houthalen-helchteren.meetingburger.net/Pages/HandleFile.ashx?id=f568a02f-381e-48c5-bff8-743af13ad22f&download=1"
SRC2_URL = "https://houthalen-helchteren.meetingburger.net/gr/40b9d958-dc55-46cd-9f84-d73d9a24e0f0"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0898822982"
GAP = "gap_agbsp_fin_debt_10_72m_lease_10_19m_div_0_11m_l5"
HIER = "Vlaanderen>Gemeenten>Houthalen-Helchteren>AGB_Sport"

ASSETS = 10964190.41
ASSETS_2024 = 12223606.55
FIXED = 10809854.03
MVA = 10808604.03
BUILDINGS = 541084.87
INSTALL = 82400.43
LEASING = 10185118.73
FVA = 1250.00
CURRENT = 154336.38
TRADE_REC = 36776.28
OTHER_REC = 5021.12
OTHER_REC_2024 = 911905.08
REC_ST = 41797.40
CASH = 112538.98
CASH_2024 = 229400.21
EQUITY = 114298.57
EQUITY_2024 = 200532.04
CAPITAL = 80000.00
SUBSIDY = 34298.57
RETAINED_2024 = 81441.15
DEBT_TOTAL = 10849891.84
DEBT_2024 = 12023074.51
LT_FIN = 10525001.78
ST_DUE = 195970.50
TRADE_PAY = 125711.46
TRADE_PAY_2024 = 1100505.06
ST_TOTAL = 321681.96
ACCRUAL = 3208.10
FIN_DEBT = 10720972.28
FIN_DEBT_2024 = 10915737.31
GROSS = 240971.52
GROSS_2024 = 256483.27
DEPR = 203202.50
OPEX = 1907.06
EBIT = 35861.96
EBIT_2024 = 93203.29
FIN_INC = 4792.32
FIN_COST = 13908.32
PNL = 26745.96
PNL_2024 = 81747.17
DIVIDEND = 108187.11
CAPEX = 33612.74
MVA_GROSS = 12777091.18
MVA_DEP = 1968487.15


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


assert abs((FIXED + CURRENT) - ASSETS) < 0.02
assert abs((MVA + FVA) - FIXED) < 0.02
assert abs((BUILDINGS + INSTALL + LEASING) - MVA) < 0.02
assert abs((TRADE_REC + OTHER_REC) - REC_ST) < 0.02
assert abs((REC_ST + CASH) - CURRENT) < 0.02
assert abs((CAPITAL + SUBSIDY) - EQUITY) < 0.02
assert abs((LT_FIN + ST_TOTAL + ACCRUAL) - DEBT_TOTAL) < 0.02
assert abs((ST_DUE + TRADE_PAY) - ST_TOTAL) < 0.02
assert abs((EQUITY + DEBT_TOTAL) - ASSETS) < 0.02
assert abs((LT_FIN + ST_DUE) - FIN_DEBT) < 0.02
assert abs((GROSS - DEPR - OPEX) - EBIT) < 0.02
assert abs((EBIT + FIN_INC - FIN_COST) - PNL) < 0.02
assert abs((RETAINED_2024 + PNL) - DIVIDEND) < 0.02
assert abs((MVA_GROSS - MVA_DEP) - MVA) < 0.02

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB Sport Houthalen-Helchteren NBB jaarrekening 2025 (MIC-kap text PDF)",
            "url": SRC_URL,
            "publisher": "AGB Sport / Gemeente Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1283; 168kB text PDF; AV 23.06.2026; GR 22.06.2026; "
                "KBO 0898.822.982; assets 10.964m equity 0.114m "
                "fin debt 10.721m leasing MVA 10.185m dividend 0.108m PnL +0.027m; BBC J2 not in file"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Gemeenteraad Houthalen-Helchteren 22.06.2026 AGB JR2025 goedkeuring",
            "url": SRC2_URL,
            "publisher": "Gemeente Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1283; attachment 2.0_NBB_JR_2025_-_AGB_Houthalen-Helchteren.PDF is AGB Sport; "
                "also BBC_JR_2025_G&O city package not mined this tick"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB SPORT HOUTHALEN-HELCHTEREN 0898.822.982",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1283; AGB since 23.02.2006; seat Pastorijstraat 30 3530 since 25.09.2013; "
                "1 VE; bestuurder Alain Yzermans since 02.01.2013; NACE 93.110/93.299/91.420; "
                "aanbestedende overheid; KBO dump 16.08.2026"
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
            "name_nl": "Autonoom Gemeentebedrijf Sport Houthalen-Helchteren (AGB Sport)",
            "name_fr": "Regie communale autonome Sport (Houthalen-Helchteren)",
            "name_en": "AGB Sport Houthalen-Helchteren",
            "level": "municipality",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.houthalen-helchteren.be/agb",
            "foi_email": "financien@houthalen-helchteren.be",
            "foi_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "notes": (
                "tick1283 JR2025 dual residual; KBO 0898.822.982 AGB since 23.02.2006; "
                "1 VE; sport exploitatie; assets 10.964m equity 0.114m fin debt 10.721m "
                "leasing MVA 10.185m dividend 0.108m cash 0.113m PnL +0.027m; BBC J2 opaque; "
                "distinct AGB Masterplan 0811.923.652; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbsp_assets_2025", "2025", ASSETS, "NBB 20/58 assets 10.964190m vs 12.223607m"),
    ("bud_agbsp_assets_2024", "2024", ASSETS_2024, "NBB YE2024 assets 12.223607m"),
    ("bud_agbsp_mva_2025", "2025", MVA, "NBB 22/27 MVA 10.808604m; leasing 10.185m; buildings 0.541m"),
    ("bud_agbsp_leasing_2025", "2025", LEASING, "NBB 25 leasingrechten 10.185119m vs 10.301661m"),
    ("bud_agbsp_buildings_2025", "2025", BUILDINGS, "NBB 22 terreinen en gebouwen 0.541085m"),
    ("bud_agbsp_cash_2025", "2025", CASH, "NBB 54/58 cash 0.112539m DROP vs 0.229400m"),
    ("bud_agbsp_other_rec_2025", "2025", OTHER_REC, "NBB 41 overige vorderingen 0.005021m DROP vs 0.911905m"),
    ("bud_agbsp_trade_rec_2025", "2025", TRADE_REC, "NBB 40 handelsvorderingen 0.036776m vs 0.102857m"),
    ("bud_agbsp_equity_2025", "2025", EQUITY, "NBB 10/15 EV 0.114299m vs 0.200532m after dividend"),
    ("bud_agbsp_capital_2025", "2025", CAPITAL, "NBB 10 kapitaal 0.080000m"),
    ("bud_agbsp_subsidy_2025", "2025", SUBSIDY, "NBB 15 kapitaalsubsidies 0.034299m vs 0.039091m"),
    ("bud_agbsp_fin_debt_2025", "2025", FIN_DEBT, "NBB 17+42 fin debt 10.720972m vs 10.915737m"),
    ("bud_agbsp_fin_debt_lt_2025", "2025", LT_FIN, "NBB 172/3 LT bank/leasing 10.525002m"),
    ("bud_agbsp_st_due_2025", "2025", ST_DUE, "NBB 42 ST due of LT 0.195971m"),
    ("bud_agbsp_trade_pay_2025", "2025", TRADE_PAY, "NBB 44 handelsschulden 0.125711m DROP vs 1.100505m"),
    ("bud_agbsp_debt_total_2025", "2025", DEBT_TOTAL, "NBB 17/49 schulden 10.849892m vs 12.023075m"),
    ("bud_agbsp_gross_2025", "2025", GROSS, "NBB 9900 brutomarge 0.240972m vs 0.256483m"),
    ("bud_agbsp_ebit_2025", "2025", EBIT, "NBB 9901 EBIT 0.035862m vs 0.093203m"),
    ("bud_agbsp_depr_2025", "2025", DEPR, "NBB 630 afschrijvingen 0.203203m vs 0.161448m"),
    ("bud_agbsp_fin_cost_2025", "2025", FIN_COST, "NBB 65 fin kost 0.013908m vs 0.014490m"),
    ("bud_agbsp_pnl_2025", "2025", PNL, "NBB 9904/9905 PnL +0.026746m vs +0.081747m"),
    ("bud_agbsp_dividend_2025", "2025", DIVIDEND, "NBB 694 vergoeding van de inbreng 0.108187m empties retained+PnL"),
    ("bud_agbsp_capex_2025", "2025", CAPEX, "NBB 8169 aanschaffingen 0.033613m"),
    ("bud_agbsp_mva_gross_2025", "2025", MVA_GROSS, "NBB 8199 MVA gross 12.777091m / accum dep 1.968487m"),
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
            "notes": note + f"; tick{TICK}; NBB not BBC J2",
        }
        for bid, year, amt, note in bud_rows
    ],
)
print("budgets", n)

crows = [
    (
        "comm_agbsp_fin_debt_10_72m_2025",
        "AGB Sport YE2025 fin debt 10.721m",
        "10720972",
        "NBB 17+42 10.720972m vs 10.916m; LT bank/leasing 10.525 + ST due 0.196; 6.6 remaining not filed",
        "Publish T4/6.6 creditor + remaining 2026-2031 pad FOI",
    ),
    (
        "comm_agbsp_leasing_10_19m_2025",
        "AGB Sport YE2025 leasing MVA 10.185m",
        "10185119",
        "NBB 25 10.185119m of MVA 10.809m; sport-facility lease shell; lessor unpublished",
        "Publish lessor identity + remaining lease schedule FOI",
    ),
    (
        "comm_agbsp_dividend_0_11m_2025",
        "AGB Sport 2025 dividend/vergoeding inbreng 0.108m",
        "108187",
        "NBB 694 0.108187m = retained 0.081441 + PnL 0.026746; EV DROP 0.201 to 0.114m",
        "Publish city dual vs dividend lock 2025-2031 FOI",
    ),
    (
        "comm_agbsp_thin_equity_0_11m_2025",
        "AGB Sport YE2025 thin equity 0.114m on 10.964m assets",
        "114299",
        "EV 0.114299m (capital 0.080 + subsidies 0.034); 1.0pct of assets; lease-repay shell",
        "Keep thin equity / going-concern path public FOI",
    ),
    (
        "comm_agbsp_other_rec_drop_0_91m_2025",
        "AGB Sport YE2025 other rec DROP 0.912m to 0.005m",
        "911905",
        "NBB 41 0.911905m -> 0.005021m; trade pay 1.101m -> 0.126m; cash DROP 0.117m",
        "Confirm city receivable collected + payables FOI",
    ),
    (
        "comm_agbsp_bbc_j2_opaque_2025",
        "AGB Sport JR2025 BBC J2 AFM/BBR unpublished this box",
        "",
        "Public GR attachment is NBB MIC-kap only; city GE BBC on same GR not this unit",
        "Publish BBC J2/J4/J5 + documentatie FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Houthalen-Helchteren / sportaccommodaties AGB",
            "legal_basis": "Decreet Lokaal Bestuur; WVV NBB JR2025 AV 23.06.2026 / GR 22.06.2026",
            "decision_date": "2026-06-23",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Houthalen-Helchteren Sport",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong" if env else "medium",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_agbsp_fin_debt_10_72m_2025",
        "AGB Sport YE2025 fin debt 10.72m",
        "10720972",
        "7.0",
        "7.0",
        "Publish T4/6.6 creditors + remaining lease pad",
        "fin debt 10.721m on assets 10.964m; almost all bank/leasing; 6.6 not filed",
    ),
    (
        "lb_agbsp_leasing_10_19m_2025",
        "AGB Sport YE2025 leasing MVA 10.19m",
        "10185119",
        "6.5",
        "7.0",
        "Publish lessor + remaining sport-facility lease",
        "leasing 10.185m of MVA 10.809m; sport exploitatie shell",
    ),
    (
        "lb_agbsp_dividend_0_11m_2025",
        "AGB Sport 2025 dividend 0.11m empties retained",
        "108187",
        "6.5",
        "5.5",
        "Publish city dual vs vergoeding van de inbreng 0.108m",
        "dividend 0.108m = all retained+PnL; EV DROP 0.201 to 0.114m",
    ),
    (
        "lb_agbsp_thin_equity_0_11m_2025",
        "AGB Sport YE2025 thin equity 0.11m",
        "114299",
        "6.0",
        "5.5",
        "Keep thin equity 1.0pct of assets public",
        "EV 0.114m on 10.964m assets after emptying retained",
    ),
    (
        "lb_agbsp_other_rec_drop_0_91m_2025",
        "AGB Sport YE2025 other rec DROP 0.91m",
        "911905",
        "5.5",
        "5.5",
        "Confirm city receivable collected + payables drop",
        "other rec 0.912m -> 0.005m; trade pay 1.101m -> 0.126m; cash 0.113m",
    ),
    (
        "lb_agbsp_cash_drop_0_12m_2025",
        "AGB Sport YE2025 cash 0.11m DROP 0.12m",
        "112539",
        "5.0",
        "5.0",
        "Keep cash vs fin debt 10.72m / thin equity path public",
        "cash 0.113m vs 0.229m; ST bank 0; ST due 0.196m",
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
            "beneficiaries": "inwoners Houthalen-Helchteren / sportaccommodaties AGB",
            "stated_goal": "Local AGB residual map VL JR2025 Houthalen-Helchteren Sport after Masterplan 1282",
            "measured_outcome": (
                "assets 10.964m / equity 0.114m / fin debt 10.721m / "
                "leasing 10.185m / dividend 0.108m / PnL +0.027m / BBC J2 opaque"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.5",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary NBB JR2025 text PDF; not TE-additive of 348bn; BBC J2 FOI",
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
                "BBC J2 AFM/BBR/gecorr/avail + T4/6.6 per-loan creditors for "
                "fin debt 10.720972m (LT bank/leasing 10.525002 + ST due 0.195971) + "
                "lessor of leasing MVA 10.185119 + city dual vs dividend 0.108187 + "
                "VTE/pers (code 62 blank) + why other rec 0.911905 vanished + "
                "NBB consult working URL"
            ),
            "why_it_matters": (
                "Unmined Houthalen-Helchteren AGB Sport after sibling Masterplan 1282. "
                "Thin equity 0.114m on 10.721m fin debt / 10.964m assets. "
                "Lease shell 10.185m. City GE BBC not this unit."
            ),
            "priority": "8",
            "recipient_body": "AGB Sport / Gemeente Houthalen-Helchteren",
            "recipient_email": "financien@houthalen-helchteren.be",
            "recipient_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbsp_fin_debt_10_72m_2025",
            "linked_leaderboard_id": "lb_agbsp_fin_debt_10_72m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary NBB euros; BBC J2 opaque",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1283",
    "title": "AGB Sport Houthalen-Helchteren JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Sport HH JR2025 NBB MIC text + KBO; "
        "KBO 0898.822.982; assets 10.964m / equity 0.114m / "
        "fin debt 10.721m / leasing 10.185m / dividend 0.108m; BBC J2 opaque; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T10:50:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1283 AGB Sport HH JR2025 dual residual; KBO 0898.822.982; "
        "assets 10.964m equity 0.114m fin debt 10.721m leasing 10.185m "
        "dividend 0.108m cash 0.113m PnL +0.027m; BBC J2 opaque; "
        "distinct AGB Masterplan 0811.923.652; FOI ready not sent; "
        "next rq_1284 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1284",
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
        "+ Stad+OCMW Wezembeek-Oppem 1281 + AGB Masterplan HH 1282 + AGB Sport HH 1283 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "Kraainem city+OCMW JR2025 BBC live on ocmw.kraainem.be download.ashx?id=16927; "
        "city+OCMW HH GE BBC_JR_2025_G&O on same GR only if taken as a new unit; "
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
    "notes": "spawned tick1283 after AGB Sport HH JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1283", rq_new, rq_spawn)
print("research_queue 1283", found, "spawned_1284", spawned)

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
            "last_unit_id": "rq_1283",
            "ticks_completed": "1283",
            "paused": "no",
            "notes": (
                "tick1283 AGB Sport HH JR2025 dual residual; KBO 0898.822.982; "
                "assets 10.964m equity 0.114m fin debt 10.721m leasing 10.185m dividend 0.108m; "
                "FOI ready; next rq_1284 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1283 - 2026-08-17 - rq_1283 AGB Sport Houthalen-Helchteren dual residual
- Unit: Autonoom Gemeentebedrijf Sport Houthalen-Helchteren (AGB Sport) JR2025 Entity II after sibling AGB Masterplan tick1282 (KBO **0898.822.982**; AGB since 23.02.2006; NBB MIC-kap text PDF on meetingburger; AV **23.06.2026**; GR **22.06.2026**). **Distinct from** sibling AGB Masterplan (**0811.923.652**; mined 1282) and city+OCMW GE (**0216.773.026** / **0216.773.125**; BBC_JR_2025_G&O on same GR still not mined). Seat Pastorijstraat 30 3530. 1 VE. Voorzitter Alain Yzermans / ondervoorzitter Jef Verpoorten. Sportaccommodaties / exploitatie. NACE 93.110 / 93.299 / 91.420. **BBC J2 not in this NBB file.** PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare; Bau-huis / Maaseik / Diepenbeek still unpublished — not redone. Kraainem city GE BBC still live (download.ashx?id=16927) — left for a later unit. Not an every-10 tick.
- EUR strong (primary NBB text PDF): assets **10.964m** (was 12.224m); cash **0.113m** DROP vs **0.229m**; MVA **10.809m** (leasing **10.185m**; gebouwen **0.541m**; installaties **0.082m**); FVA **0.001m**; EV **0.114m** (was 0.201m; kapitaal **0.080m** + kapitaalsubsidies **0.034m**; overgedragen current blank after dividend); schulden **10.850m**; fin debt **10.721m** (LT bank/leasing **10.525m** + ST due **0.196m**) vs **10.916m**; brutomarge **0.241m**; EBIT **0.036m**; depr **0.203m**; fin kost **0.014m**; PnL **+0.027m** (was +0.082m); dividend / vergoeding van de inbreng **0.108m** (empties retained 0.081m + current 0.027m); capex **0.034m**. Overige vorderingen DROP **0.912m → 0.005m**. Handelsschulden DROP **1.101m → 0.126m**. Personeel (code 62) unpublished. Remaining >5y (sectie 6.6) not filed. City dual (huur/prijssub vs dividend 0.108m) FOI. Do not invent BBC AFM/BBR.
- CSVs: sources+3/entities(new AGB Sport; city already 1282)/budgets+24/commitments+6/leaderboard+6 + FOI ready `gap_agbsp_fin_debt_10_72m_lease_10_19m_div_0_11m_l5` (not sent); rq_1283=done; spawn rq_1284; ticks=1283. Not a *0 tick — no progress refresh.
- Next: rq_1284 residual dual L5 VL JR2025 hole_fill (prefer Kraainem GE or city+OCMW HH GE or other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
