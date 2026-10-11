# -*- coding: utf-8 -*-
"""Tick 1282 (research_queue patched surgically — last line + spawn only).
AGB Masterplan Houthalen-Helchteren JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T10:50:00Z"
TICK = 1282
SRC = "src_agbmp_jr2025_nbb"
SRC2 = "src_agbmp_jr2025_gr"
SRC3 = "src_kbo_agbmp_0811923652"
SRC4 = "src_hh_agb_portal"
SRC5 = "src_kbo_city_hh_0216773026"
ENT = "agb_houthalen_masterplan"
CITY = "city_houthalen_helchteren"
SRC_URL = "https://houthalen-helchteren.meetingburger.net/Pages/HandleFile.ashx?id=fab6013a-a196-4f58-9185-45949b75ed51&download=1"
SRC2_URL = "https://houthalen-helchteren.meetingburger.net/gr/40b9d958-dc55-46cd-9f84-d73d9a24e0f0"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0811923652"
SRC4_URL = "https://www.houthalen-helchteren.be/agb"
SRC5_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0216773026"
GAP = "gap_agbmp_equity_neg_0_66m_fin_debt_27_81m_city_loan_8_50m_l5"
HIER = "Vlaanderen>Gemeenten>Houthalen-Helchteren>AGB_Masterplan"

ASSETS = 27292775.30
ASSETS_2024 = 28375023.47
FIXED = 22301038.34
MVA = 22299788.34
BUILDINGS = 21538371.24
INSTALL = 591985.95
FURN = 147851.46
CIP = 21579.69
FVA = 1250.00
CURRENT = 4991736.96
TRADE_REC = 3090714.64
CASH = 1888247.90
CASH_2024 = 2952425.10
INVEST = 6594.12
EQUITY = -657807.49
EQUITY_2024 = -953385.75
CAPITAL = 900000.00
RETAINED = -1557807.49
RETAINED_2024 = -1853385.75
DEBT_TOTAL = 27950582.79
DEBT_2024 = 29328409.22
LT_FIN = 24905786.65
LT_BANK = 16410048.79
LT_OTHER = 8495737.86
ST_DUE = 1397728.76
ST_FIN = 1504544.49
TRADE_PAY = 141764.14
FIN_DEBT = 27808059.90
FIN_DEBT_2024 = 29173858.28
GROSS = 2499759.83
GROSS_2024 = 3045415.49
DEPR = 1266071.65
OPEX = 226837.89
EBIT = 1006850.29
EBIT_2024 = 1565791.42
FIN_INC = 13779.03
FIN_COST = 725051.06
PNL = 295578.26
PNL_2024 = 882215.06
CAPEX = 681909.91
MVA_GROSS = 42313506.50
MVA_DEP = 20013718.16
LT_1_5 = 5786108.24
LT_GT5 = 19119678.41


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
            "title": "AGB Masterplan Houthalen-Helchteren NBB jaarrekening 2025 (VKT-kap text PDF)",
            "url": SRC_URL,
            "publisher": "AGB Masterplan / Gemeente Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1282; 184kB text PDF; AV 23.06.2026; GR 22.06.2026; "
                "KBO 0811.923.652; assets 27.293m equity NEG 0.658m "
                "fin debt 27.808m other loans 8.496m PnL +0.296m; BBC J2 not in file"
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
                "tick1282; attachments 2.0_NBB_JR_2025_AGB_Masterplan + AGB Sport; "
                "also BBC_JR_2025_G&O city package not mined this tick"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB MASTERPLAN 0811.923.652",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1282; AGB since 12.01.2009; seat Pastorijstraat 30 3530 since 25.09.2013; "
                "1 VE; bestuurder Alain Yzermans since 02.01.2013; NACE 90.312/84.130; "
                "aanbestedende overheid; KBO dump 16.08.2026"
            ),
        },
        {
            "source_id": SRC4,
            "title": "Houthalen-Helchteren AGB Masterplan & AGB Sport portal",
            "url": SRC4_URL,
            "publisher": "Gemeente Houthalen-Helchteren",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": "tick1282; NAC + patrimonium vs sibling AGB Sport exploitatie; statuten on site",
        },
        {
            "source_id": SRC5,
            "title": "KBO Gemeente Houthalen-Helchteren 0216.773.026 (city stub)",
            "url": SRC5_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1282 city stub; KBO 0216.773.026 / OCMW 0216.773.125 from official "
                "BBC 2024 header; city GE JR2025 BBC on same GR not mined this tick"
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
            "name_nl": "Autonoom Gemeentebedrijf Masterplan (Houthalen-Helchteren)",
            "name_fr": "Regie communale autonome Masterplan (Houthalen-Helchteren)",
            "name_en": "AGB Masterplan Houthalen-Helchteren",
            "level": "municipality",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.houthalen-helchteren.be/agb",
            "foi_email": "financien@houthalen-helchteren.be",
            "foi_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "notes": (
                "tick1282 JR2025 dual residual; KBO 0811.923.652 AGB since 12.01.2009; "
                "1 VE; NAC+patrimonium; assets 27.293m equity NEG 0.658m fin debt 27.808m "
                "other loans 8.496m cash 1.888m PnL +0.296m; BBC J2 opaque; "
                "distinct AGB Sport 0898.822.982; FOI " + GAP
            ),
        },
        {
            "entity_id": CITY,
            "name_nl": "Gemeente Houthalen-Helchteren",
            "name_fr": "Commune de Houthalen-Helchteren",
            "name_en": "Municipality of Houthalen-Helchteren",
            "level": "municipality",
            "parent_id": "sec_local",
            "community_language": "nl",
            "website": "https://www.houthalen-helchteren.be/",
            "foi_email": "financien@houthalen-helchteren.be",
            "foi_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "notes": (
                "tick1282 stub for AGB Masterplan dual residual; KBO 0216.773.026 / "
                "OCMW 0216.773.125; NIS 72039; politiezone Carma / HVZ Oost-Limburg; "
                "city GE JR2025 BBC on GR 22.06.2026 not mined this tick; "
                "sibling AGB Sport 0898.822.982 unmined"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbmp_assets_2025", "2025", ASSETS, "NBB 20/58 assets 27.292775m vs 28.375023m"),
    ("bud_agbmp_assets_2024", "2024", ASSETS_2024, "NBB YE2024 assets 28.375023m"),
    ("bud_agbmp_mva_2025", "2025", MVA, "NBB 22/27 MVA 22.299788m; buildings 21.538m; leasing 0"),
    ("bud_agbmp_buildings_2025", "2025", BUILDINGS, "NBB 22 terreinen en gebouwen 21.538371m"),
    ("bud_agbmp_cash_2025", "2025", CASH, "NBB 54/58 cash 1.888248m DROP vs 2.952425m"),
    ("bud_agbmp_trade_rec_2025", "2025", TRADE_REC, "NBB 40 handelsvorderingen 3.090715m vs 2.530873m"),
    ("bud_agbmp_equity_2025", "2025", EQUITY, "NBB 10/15 EV NEG -0.657807m vs -0.953386m"),
    ("bud_agbmp_capital_2025", "2025", CAPITAL, "NBB 10 kapitaal 0.900000m"),
    ("bud_agbmp_retained_2025", "2025", RETAINED, "NBB 14 overgedragen verlies -1.557807m vs -1.853386m"),
    ("bud_agbmp_fin_debt_2025", "2025", FIN_DEBT, "NBB 17+42+43 fin debt 27.808060m vs 29.173858m"),
    ("bud_agbmp_fin_debt_lt_2025", "2025", LT_FIN, "NBB 170/4 LT fin 24.905787m (bank/leasing 16.410 + other 8.496)"),
    ("bud_agbmp_lt_bank_2025", "2025", LT_BANK, "NBB 172/3 kredietinstellingen/leasing 16.410049m"),
    ("bud_agbmp_lt_other_2025", "2025", LT_OTHER, "NBB 174/0 overige leningen 8.495738m (city-like; confirm FOI)"),
    ("bud_agbmp_st_due_2025", "2025", ST_DUE, "NBB 42 ST due of LT 1.397729m"),
    ("bud_agbmp_st_bank_2025", "2025", ST_FIN, "NBB 430/8 ST bank 1.504544m"),
    ("bud_agbmp_debt_total_2025", "2025", DEBT_TOTAL, "NBB 17/49 schulden 27.950583m vs 29.328409m"),
    ("bud_agbmp_gross_2025", "2025", GROSS, "NBB 9900 brutomarge 2.499760m vs 3.045415m"),
    ("bud_agbmp_ebit_2025", "2025", EBIT, "NBB 9901 EBIT 1.006850m vs 1.565791m"),
    ("bud_agbmp_depr_2025", "2025", DEPR, "NBB 630 afschrijvingen 1.266072m"),
    ("bud_agbmp_fin_cost_2025", "2025", FIN_COST, "NBB 65 fin kost 0.725051m vs 0.762636m"),
    ("bud_agbmp_pnl_2025", "2025", PNL, "NBB 9904/9905 PnL +0.295578m vs +0.882215m; no dividend"),
    ("bud_agbmp_capex_2025", "2025", CAPEX, "NBB 8169 aanschaffingen 0.681910m"),
    ("bud_agbmp_mva_gross_2025", "2025", MVA_GROSS, "NBB 8199 MVA gross 42.313507m / accum dep 20.014m"),
    ("bud_agbmp_lt_gt5_2025", "2025", LT_GT5, "NBB 8913 remaining >5y 19.119678m"),
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
        "comm_agbmp_fin_debt_27_81m_2025",
        "AGB Masterplan YE2025 fin debt 27.808m",
        "27808060",
        "NBB 17+42+43 27.808060m vs 29.174m; LT bank/leasing 16.410 + other 8.496 + ST due 1.398 + ST bank 1.505; >5y 19.120m",
        "Publish T4 creditor schedule + remaining 2026-2031 pad FOI",
    ),
    (
        "comm_agbmp_equity_neg_0_66m_2025",
        "AGB Masterplan YE2025 equity NEG 0.658m",
        "657807",
        "EV -0.657807m vs -0.953386m; capital 0.900 + retained -1.558; PnL +0.296 still leaves NEG equity",
        "Publish going-concern / city support + BBC nettoactief FOI",
    ),
    (
        "comm_agbmp_other_loans_8_50m_2025",
        "AGB Masterplan YE2025 overige leningen 8.496m (city-like)",
        "8495738",
        "NBB 174/0 8.495738m vs 8.900297m; not confirmed city in this NBB file; trade rec 3.091m",
        "Confirm city loan vs bank + huur/prijssub lock FOI",
    ),
    (
        "comm_agbmp_fin_cost_0_73m_2025",
        "AGB Masterplan 2025 financial cost 0.725m",
        "725051",
        "NBB 65 0.725051m vs 0.762636m; EBIT 1.007m after depr 1.266m; cash DROP 1.064m",
        "Publish interest vs city dual vs bank rate FOI",
    ),
    (
        "comm_agbmp_buildings_21_54m_2025",
        "AGB Masterplan YE2025 buildings 21.538m / MVA 22.300m",
        "21538371",
        "NAC+patrimonium shell; leasing 0; capex 0.682m; gross 42.314m / accum dep 20.014m",
        "Publish venue inventory + city gebruiksrecht FOI",
    ),
    (
        "comm_agbmp_bbc_j2_opaque_2025",
        "AGB Masterplan JR2025 BBC J2 AFM/BBR unpublished this box",
        "",
        "Public GR attachment is NBB VKT only; city GE BBC on same GR not this unit",
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
            "beneficiary": "inwoners Houthalen-Helchteren / NAC / patrimonium AGB",
            "legal_basis": "Decreet Lokaal Bestuur; WVV NBB JR2025 AV 23.06.2026 / GR 22.06.2026",
            "decision_date": "2026-06-23",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Houthalen-Helchteren Masterplan",
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
        "lb_agbmp_fin_debt_27_81m_2025",
        "AGB Masterplan YE2025 fin debt 27.81m",
        "27808060",
        "7.0",
        "7.5",
        "Publish T4 creditors + remaining >5y 19.12m schedule",
        "fin debt 27.808m on assets 27.293m; stock not TCO; BBC J2 opaque",
    ),
    (
        "lb_agbmp_equity_neg_0_66m_2025",
        "AGB Masterplan YE2025 equity NEG 0.66m",
        "657807",
        "7.5",
        "6.5",
        "Publish going-concern / city support path; keep NEG equity public",
        "EV -0.658m after +0.296m PnL; capital 0.900 vs retained -1.558",
    ),
    (
        "lb_agbmp_other_loans_8_50m_2025",
        "AGB Masterplan YE2025 overige leningen 8.50m (city-like)",
        "8495738",
        "6.5",
        "6.5",
        "Confirm city vs bank + publish huur/prijssub 2025-2031",
        "NBB 174/0 8.496m; trade rec 3.091m; city dual FOI",
    ),
    (
        "lb_agbmp_fin_cost_0_73m_2025",
        "AGB Masterplan 2025 financial cost 0.73m",
        "725051",
        "6.0",
        "6.0",
        "Publish interest split bank vs city other loans",
        "fin kost 0.725m eats most of EBIT 1.007m after depr 1.266m",
    ),
    (
        "lb_agbmp_buildings_21_54m_2025",
        "AGB Masterplan YE2025 buildings 21.54m",
        "21538371",
        "5.5",
        "6.5",
        "Publish NAC/patrimonium inventory + city gebruiksrecht",
        "MVA 22.300m leasing 0; capex 0.682m; cash DROP to 1.888m",
    ),
    (
        "lb_agbmp_cash_drop_1_06m_2025",
        "AGB Masterplan YE2025 cash 1.89m DROP 1.06m",
        "1888248",
        "5.5",
        "5.5",
        "Keep cash vs fin debt 27.81m / NEG equity path public",
        "cash 1.888m vs 2.952m; ST bank 1.505m still drawn",
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
            "beneficiaries": "inwoners Houthalen-Helchteren / NAC / patrimonium AGB",
            "stated_goal": "Local AGB residual map VL JR2025 Houthalen-Helchteren Masterplan after Wezembeek 1281",
            "measured_outcome": (
                "assets 27.293m / equity NEG 0.658m / fin debt 27.808m / "
                "other loans 8.496m / PnL +0.296m / BBC J2 opaque"
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
                "BBC J2 AFM/BBR/gecorr/avail + T4 per-loan creditors for "
                "fin debt 27.808060m (LT bank/leasing 16.410049 + overige "
                "leningen 8.495738 + ST due 1.397729 + ST bank 1.504544) + "
                "confirm city dual vs trade rec 3.090715 + VTE/pers (code 62 blank) + "
                "NBB consult working URL"
            ),
            "why_it_matters": (
                "Unmined Houthalen-Helchteren AGB Masterplan after Wezembeek-Oppem 1281. "
                "NEG equity 0.658m on 27.808m fin debt / 27.293m assets. "
                "Sibling AGB Sport 0898.822.982 and city GE BBC not this unit."
            ),
            "priority": "8",
            "recipient_body": "AGB Masterplan / Gemeente Houthalen-Helchteren",
            "recipient_email": "financien@houthalen-helchteren.be",
            "recipient_postal": "Pastorijstraat 30 3530 Houthalen-Helchteren",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbmp_fin_debt_27_81m_2025",
            "linked_leaderboard_id": "lb_agbmp_fin_debt_27_81m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary NBB euros; BBC J2 opaque",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1282",
    "title": "AGB Masterplan Houthalen-Helchteren JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Masterplan HH JR2025 NBB VKT text + KBO; "
        "KBO 0811.923.652; assets 27.293m / equity NEG 0.658m / "
        "fin debt 27.808m / other loans 8.496m; BBC J2 opaque; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T10:45:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1282 AGB Masterplan HH JR2025 dual residual; KBO 0811.923.652; "
        "assets 27.293m equity NEG 0.658m fin debt 27.808m other loans 8.496m "
        "cash 1.888m PnL +0.296m buildings 21.538m; BBC J2 opaque; "
        "distinct AGB Sport 0898.822.982; FOI ready not sent; "
        "next rq_1283 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1283",
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
        "+ Stad+OCMW Wezembeek-Oppem 1281 + AGB Masterplan HH 1282 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "AGB Sport HH (0898.822.982) and city+OCMW HH GE BBC only if taken as a new unit; "
        "Kraainem city+OCMW JR2025 BBC live on ocmw.kraainem.be download.ashx?id=16927; "
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
    "notes": "spawned tick1282 after AGB Masterplan HH JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1282", rq_new, rq_spawn)
print("research_queue 1282", found, "spawned_1283", spawned)

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
            "last_unit_id": "rq_1282",
            "ticks_completed": "1282",
            "paused": "no",
            "notes": (
                "tick1282 AGB Masterplan HH JR2025 dual residual; KBO 0811.923.652; "
                "assets 27.293m equity NEG 0.658m fin debt 27.808m other loans 8.496m; "
                "FOI ready; next rq_1283 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1282 - 2026-08-17 - rq_1282 AGB Masterplan Houthalen-Helchteren dual residual
- Unit: Autonoom Gemeentebedrijf Masterplan (Houthalen-Helchteren) JR2025 Entity II after Stad+OCMW Wezembeek-Oppem tick1281 (KBO **0811.923.652**; AGB since 12.01.2009; NBB VKT-kap text PDF on meetingburger; AV **23.06.2026**; GR **22.06.2026**). **Distinct from** sibling AGB Sport (**0898.822.982**; NBB JR2025 also public, not mined) and city+OCMW GE (**0216.773.026** / **0216.773.125**; BBC_JR_2025_G&O on same GR, not mined). Seat Pastorijstraat 30 3530. 1 VE. Voorzitter Alain Yzermans / ondervoorzitter Jef Verpoorten. NAC + patrimonium / culture-tourism-sport infrastructure. NACE 90.312 / 84.130. **BBC J2 not in this NBB file.** PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare; Bau-huis / Maaseik / Diepenbeek still unpublished — not redone. Kraainem city GE BBC also live (download.ashx?id=16927) — left for a later unit. Not an every-10 tick.
- EUR strong (primary NBB text PDF): assets **27.293m** (was 28.375m); cash **1.888m** DROP vs **2.952m**; MVA **22.300m** (gebouwen **21.538m**; leasing **0**); FVA **0.001m**; EV **−0.658m NEG** (was −0.953m; kapitaal **0.900m** + overgedragen **−1.558m**); schulden **27.951m**; fin debt **27.808m** (LT **24.906m** = bank/leasing **16.410m** + overige leningen **8.496m** + ST due **1.398m** + ST bank **1.505m**) vs **29.174m**; brutomarge **2.500m**; EBIT **1.007m**; depr **1.266m**; fin kost **0.725m**; PnL **+0.296m** (was +0.882m); capex **0.682m**; remaining >5y **19.120m**. Personeel (code 62) unpublished. City dual (huur/prijssub vs overige leningen 8.496m + handelsvorderingen 3.091m) FOI. Do not invent BBC AFM/BBR.
- CSVs: sources+5/entities(new AGB + city stub)/budgets+24/commitments+6/leaderboard+6 + FOI ready `gap_agbmp_equity_neg_0_66m_fin_debt_27_81m_city_loan_8_50m_l5` (not sent); rq_1282=done; spawn rq_1283; ticks=1282. Not a *0 tick — no progress refresh.
- Next: rq_1283 residual dual L5 VL JR2025 hole_fill (prefer AGB Sport HH or Kraainem GE or other unmined AGB/zorg/EVA with direct PDF; skip Motena / Trupark / PATRI / Zorgbedrijf ST unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
