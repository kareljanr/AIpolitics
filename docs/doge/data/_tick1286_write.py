# -*- coding: utf-8 -*-
"""Tick 1286 (research_queue patched surgically — last line + spawn only).
AGB SCO Ronse JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T13:05:00Z"
TICK = 1286
SRC = "src_agbsco_jr2025_bbc"
SRC2 = "src_agbsco_jr2025_portal"
SRC3 = "src_kbo_agbsco_0882840154"
ENT = "agb_sco_ronse"
CITY = "city_ronse"
SRC_URL = "https://www.ronse.be/sites/ronse/files/2026-06/Jaarrekening%202025%20AGB%20SCO%20definitief.pdf"
SRC2_URL = "https://www.ronse.be/nl/autonome-gemeentebedrijven-en-eva"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0882840154"
GAP = "gap_agbsco_fin_debt_22_65m_lease_21_59m_prijssub_1_70m_l5"
HIER = "Vlaanderen>Gemeenten>Ronse>AGB_SCO"

ASSETS = 23809497
ASSETS_2024 = 24279343
CASH = 299158
CASH_2024 = 239693
CURRENT = 1529398
ST_REC = 1230241
FIXED = 22280099
MVA = 22246226
LEASING = 21585336
BUILDINGS = 492239
INSTALL = 117298
FURNITURE = 51353
IVA = 33872
FVA = 0
SCHULDEN = 23366687
SCHULDEN_2024 = 24043569
EQUITY = 442810
EQUITY_2024 = 235774
CAP_SUBS = 16140
CUM_PNL = 211671
CUM_PNL_2024 = 4122
OTHER_EQUITY = 215000
FIN_DEBT = 22650566
FIN_DEBT_2024 = 23096573
FIN_DEBT_LT = 22064754
FIN_DEBT_ST_DUE = 585811
NEW_LOANS = 137387
AFL = 583395
ERFPACHT_SPORTHAL = 3982979.42
ERFPACHT_VERVERIJ = 9466160.83
ERFPACHT_ZWEMBAD = 7803092.14
CITY_LOAN = 812522.04
ERFPACHT_REPAY = 448227.32
CITY_LOAN_REPAY = 135167.42
ST_NONFIN = 687786
EXPL = 732062
EXPL_ONTV = 2588511
EXPL_UITG = 1856449
INVEST = -137387
INVEST_UITG = 137387
BBR_YEAR = 148667
CUM_BBR = 813277
AVAIL = 813277
AFM = 148667
AANGEWEZEN = 1847726
GECORR = -1115664
PNL = 207548
PNL_2024 = 233209
PERS = 19260
GOEDEREN = 1766099
DEPR = 525026
OMZET = 2581875
PRIJS_EXCL = 1704966.12
PRIJS_INCL = 1815144.19
CITY_STAFF = 778881.17


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
assert abs((MVA + IVA + FVA) - FIXED) < 2
assert abs((BUILDINGS + INSTALL + FURNITURE + LEASING) - MVA) < 0.02
assert abs((EQUITY + SCHULDEN) - ASSETS) < 0.02
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQUITY) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST_DUE) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 0.02
assert abs((0 - INVEST_UITG) - INVEST) < 0.02
assert abs((EXPL - AFL) - AFM) < 0.02
assert abs((AFM + (AFL - AANGEWEZEN)) - GECORR) < 0.02
assert abs((ERFPACHT_SPORTHAL + ERFPACHT_VERVERIJ + ERFPACHT_ZWEMBAD + CITY_LOAN) - FIN_DEBT_LT) < 1
assert abs((ERFPACHT_REPAY + CITY_LOAN_REPAY) - AFL) < 1
assert abs((CUM_PNL_2024 + PNL) - CUM_PNL) < 2
assert abs((CUM_BBR - 0) - AVAIL) < 0.02

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB SCO Ronse BBC jaarrekening 2025 (text PDF 97p)",
            "url": SRC_URL,
            "publisher": "AGB SCO / Stad Ronse",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1286; 6.94MB text PDF; print 21.05.2026; pub 08.06.2026; "
                "KBO 0882.840.154; assets 23.809m fin debt 22.651m leasing 21.585m "
                "prijssub 1.705m AFM +0.149m gecorr -1.116m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Stad Ronse AGB portal — AGB SCO JR2025 publicatie 08.06.2026",
            "url": SRC2_URL,
            "publisher": "Stad Ronse",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1286; Jaarrekening 2025 AGB SCO gepubliceerd 08.06.2026; "
                "sibling AGB SOB JR2025 already mined tick1194; city GE 2025 still unmined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO AGB SCO Ronse 0882.840.154",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1286; AGB since 31.07.2006; seat Leuzesesteenweg 241 9600 since 02.04.2016; "
                "1 VE; bestuurder Joris Vandenhoucke since 01.01.2013; FD jurgen.soetens@ronse.be; "
                "NACE 93.110/93.299; aanbestedende overheid; RSZ werkgever since 01.01.2022"
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
            "name_nl": "Autonoom Gemeentebedrijf Sport, Cultuur en Ontspanning Ronse (AGB SCO)",
            "name_fr": "Regie communale autonome Sport, Culture et Loisirs Renaix",
            "name_en": "AGB SCO Ronse (sport, culture and leisure)",
            "level": "local_entity",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.ronse.be/nl/autonome-gemeentebedrijven-en-eva",
            "foi_email": "jurgen.soetens@ronse.be",
            "foi_postal": "Leuzesesteenweg 241 9600 Ronse",
            "notes": (
                "tick1286 JR2025 dual residual; KBO 0882.840.154 AGB since 31.07.2006; "
                "1 VE; CC De Ververij + sporthal t Rosco + zwembad; assets 23.809m "
                "fin debt 22.651m leasing 21.585m city prijssub 1.705m equity 0.443m "
                "AFM +0.149m gecorr -1.116m; distinct AGB SOB 0842.354.433; FOI " + GAP
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbsco_assets_2025", "2025", ASSETS, "J4 assets 23.809497m vs 24.279343m"),
    ("bud_agbsco_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 24.279343m"),
    ("bud_agbsco_cash_2025", "2025", CASH, "J4 cash 0.299158m JUMP vs 0.239693m"),
    ("bud_agbsco_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 0.239693m"),
    ("bud_agbsco_mva_2025", "2025", MVA, "J4 MVA 22.246226m; leasing 21.585m; buildings 0.492m"),
    ("bud_agbsco_leasing_2025", "2025", LEASING, "J4 bedrijfsmatig leasing/erfpacht 21.585336m vs 22.033564m"),
    ("bud_agbsco_buildings_2025", "2025", BUILDINGS, "J4 terreinen en gebouwen 0.492239m"),
    ("bud_agbsco_iva_2025", "2025", IVA, "J4 IVA 0.033872m vs 0.014421m"),
    ("bud_agbsco_equity_2025", "2025", EQUITY, "J4 nettoactief 0.442810m JUMP vs 0.235774m"),
    ("bud_agbsco_equity_2024", "2024", EQUITY_2024, "J4 YE2024 nettoactief 0.235774m"),
    ("bud_agbsco_cum_pnl_2025", "2025", CUM_PNL, "T5 gecumuleerd overschot 0.211671m (was 0.004122 + PnL 0.208m)"),
    ("bud_agbsco_other_equity_2025", "2025", OTHER_EQUITY, "T5 overig nettoactief/kapitaal 0.215000m"),
    ("bud_agbsco_schulden_2025", "2025", SCHULDEN, "J4 schulden 23.366687m vs 24.043569m"),
    ("bud_agbsco_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 22.650566m vs 23.096573m"),
    ("bud_agbsco_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 23.096573m"),
    ("bud_agbsco_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin 22.064754m"),
    ("bud_agbsco_st_due_2025", "2025", FIN_DEBT_ST_DUE, "T4/J4 ST due 0.585811m"),
    ("bud_agbsco_new_loans_2025", "2025", NEW_LOANS, "T4/T2 new loans 0.137387m (T2 fin inst; doc 1740002 city)"),
    ("bud_agbsco_afl_2025", "2025", AFL, "T4/J2 periodieke aflossingen 0.583395m"),
    ("bud_agbsco_erfpacht_ververij_2025", "2025", ERFPACHT_VERVERIJ, "TB 1721100 erfpacht Ververij 9.466161m"),
    ("bud_agbsco_erfpacht_zwembad_2025", "2025", ERFPACHT_ZWEMBAD, "TB 1721200 erfpacht zwembad 7.803092m"),
    ("bud_agbsco_erfpacht_sporthal_2025", "2025", ERFPACHT_SPORTHAL, "TB 1721000 erfpacht sporthal 3.982979m"),
    ("bud_agbsco_city_loan_2025", "2025", CITY_LOAN, "TB 1740002 schulden aan de gemeente 0.812522m"),
    ("bud_agbsco_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +0.732062m"),
    ("bud_agbsco_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 2.588511m"),
    ("bud_agbsco_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 1.856449m"),
    ("bud_agbsco_invest_2025", "2025", INVEST, "J2 invest saldo -0.137387m (uitg 0.137m / ontv 0)"),
    ("bud_agbsco_bbr_2025", "2025", BBR_YEAR, "J2 budgettair resultaat boekjaar +0.148667m"),
    ("bud_agbsco_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 0.813277m (onbeschikbaar 0)"),
    ("bud_agbsco_afm_2025", "2025", AFM, "J2 AFM +0.148667m"),
    ("bud_agbsco_gecorr_2025", "2025", GECORR, "J2 gecorr AFM -1.115664m NEG (aangewezen 1.847726m)"),
    ("bud_agbsco_aangewezen_2025", "2025", AANGEWEZEN, "J2 aangewezen aflossingen 1.847726m"),
    ("bud_agbsco_pnl_2025", "2025", PNL, "J5 PnL +0.207548m vs +0.233209m retained"),
    ("bud_agbsco_pers_2025", "2025", PERS, "J5 bezoldigingen 0.019260m (conciërge+jobstudenten; VTE FOI)"),
    ("bud_agbsco_goederen_2025", "2025", GOEDEREN, "J5 goederen en diensten 1.766099m"),
    ("bud_agbsco_depr_2025", "2025", DEPR, "J5 afschrijvingen 0.525026m"),
    ("bud_agbsco_omzet_2025", "2025", OMZET, "J5 opbrengsten uit de werking 2.581875m"),
    ("bud_agbsco_prijssub_2025", "2025", PRIJS_EXCL, "Doc prijssub city 1.704966m excl / 1.815144m incl BTW"),
    ("bud_agbsco_city_staff_2025", "2025", CITY_STAFF, "TB 617 vergoeding personen ter beschikking stad 0.778881m"),
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
        "comm_agbsco_fin_debt_22_65m_2025",
        "AGB SCO YE2025 fin debt 22.651m",
        "22650566",
        "T4 22.650566m vs 23.097m; LT 22.065 + ST due 0.586; erfpacht 3 sites + city 0.813m",
        "Publish remaining 2026-2031 per erfpacht + city loan FOI",
    ),
    (
        "comm_agbsco_leasing_21_59m_2025",
        "AGB SCO YE2025 leasing/erfpacht MVA 21.585m",
        "21585336",
        "J4 leasing 21.585336m of MVA 22.246m; TB Ververij 9.466 + zwembad 7.803 + sporthal 3.983",
        "Publish lessor/canon remaining schedule FOI",
    ),
    (
        "comm_agbsco_prijssub_1_70m_2025",
        "AGB SCO 2025 city prijssubsidie 1.705m",
        "1704966",
        "Doc 1.704966m excl / 1.815144m incl; zwembad 1.269m dominates; city GE 2025 unmined",
        "Publish city dual 2026-2031 prijssub lock FOI",
    ),
    (
        "comm_agbsco_gecorr_neg_1_12m_2025",
        "AGB SCO 2025 gecorr AFM -1.116m",
        "1115664",
        "J2 AFM +0.149m but aangewezen 1.848m vs actual 0.583m → gecorr -1.116m",
        "Publish aangewezen vs erfpacht canon methodology FOI",
    ),
    (
        "comm_agbsco_city_loan_0_81m_2025",
        "AGB SCO YE2025 city loan 0.813m",
        "812522",
        "TB 1740002 0.812522m; new 0.137m (T2 fin-inst vs doc city); repay 0.135m",
        "Confirm creditor identity of 0.137m new draw FOI",
    ),
    (
        "comm_agbsco_city_staff_0_78m_2025",
        "AGB SCO 2025 city staff dual 0.779m",
        "778881",
        "AR617 0.778881m stadspersoneel vs J5 pers 0.019m; VTE unpublished",
        "Publish VTE AGB vs city + doorrekening FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "inwoners Ronse / CC De Ververij / t Rosco / zwembad",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 AGB SCO print 21.05.2026 / pub 08.06.2026",
            "decision_date": "2026-06-08",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB residual map VL JR2025 Ronse SCO",
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
        "lb_agbsco_fin_debt_22_65m_2025",
        "AGB SCO YE2025 fin debt 22.65m",
        "22650566",
        "7.0",
        "7.5",
        "Publish remaining erfpacht + city loan 2026-2031",
        "fin debt 22.651m on assets 23.809m; almost all erfpacht 3 sites + city 0.813m",
    ),
    (
        "lb_agbsco_leasing_21_59m_2025",
        "AGB SCO YE2025 leasing/erfpacht MVA 21.59m",
        "21585336",
        "6.5",
        "7.5",
        "Publish lessor/canon remaining sport-culture shell",
        "leasing 21.585m of MVA 22.246m; Ververij 9.466 + zwembad 7.803 + sporthal 3.983",
    ),
    (
        "lb_agbsco_prijssub_1_70m_2025",
        "AGB SCO 2025 city prijssub 1.70m",
        "1704966",
        "6.5",
        "6.5",
        "Publish city dual 2026-2031 prijssub lock",
        "prijssub 1.705m excl / 1.815m incl; zwembad 1.269m; city GE 2025 unmined",
    ),
    (
        "lb_agbsco_gecorr_neg_1_12m_2025",
        "AGB SCO 2025 gecorr AFM -1.12m",
        "1115664",
        "6.5",
        "6.0",
        "Publish aangewezen 1.848m vs actual 0.583m method",
        "AFM +0.149m but gecorr -1.116m; erfpacht shell",
    ),
    (
        "lb_agbsco_city_loan_0_81m_2025",
        "AGB SCO YE2025 city loan 0.81m",
        "812522",
        "5.5",
        "5.5",
        "Confirm 0.137m new draw creditor (T2 vs 1740002)",
        "city loan 0.813m; new 0.137m; repay 0.135m",
    ),
    (
        "lb_agbsco_city_staff_0_78m_2025",
        "AGB SCO 2025 city staff dual 0.78m",
        "778881",
        "5.5",
        "5.5",
        "Publish VTE AGB vs city doorrekening",
        "AR617 0.779m vs J5 pers 0.019m; 1 concierge + jobstudenten",
    ),
    (
        "lb_agbsco_thin_equity_0_44m_2025",
        "AGB SCO YE2025 thin equity 0.44m on 23.81m",
        "442810",
        "5.5",
        "5.5",
        "Keep thin equity 1.9pct of assets / lease-repay shell public",
        "EV 0.443m JUMP vs 0.236m; 1.9pct of assets; retained PnL 0.208m",
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
            "beneficiaries": "inwoners Ronse / CC De Ververij / t Rosco / zwembad",
            "stated_goal": "Local AGB residual map VL JR2025 Ronse SCO after SOB 1194 + OVERO 1062",
            "measured_outcome": (
                "assets 23.809m / equity 0.443m / fin debt 22.651m / "
                "leasing 21.585m / prijssub 1.705m / AFM +0.149m / gecorr -1.116m / PnL +0.208m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.5",
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
                "T4 remaining 2026-2031 per erfpacht (Ververij 9.466161 + zwembad 7.803092 "
                "+ sporthal 3.982979) + city loan 0.812522 + identity of new 0.137387 "
                "(T2 fin-inst vs doc 1740002 city) + VTE behind pers 0.019260 and city "
                "staff dual AR617 0.778881 + city GE dual lock of prijssub 1.704966 "
                "(city Ronse JR2025 still unmined) + aangewezen 1.847726 vs actual 0.583395"
            ),
            "why_it_matters": (
                "Unmined Ronse AGB SCO after sibling SOB 1194 and OVERO 1062. "
                "Lease/erfpacht shell 21.585m on 22.651m fin debt / 23.809m assets. "
                "City prijssub 1.705m. Gecorr AFM -1.116m. City GE 2025 still unmined."
            ),
            "priority": "8",
            "recipient_body": "AGB SCO / Stad Ronse",
            "recipient_email": "jurgen.soetens@ronse.be",
            "recipient_postal": "Leuzesesteenweg 241 9600 Ronse",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbsco_fin_debt_22_65m_2025",
            "linked_leaderboard_id": "lb_agbsco_fin_debt_22_65m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1286",
    "title": "AGB SCO Ronse JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB SCO Ronse JR2025 BBC text + KBO; "
        "KBO 0882.840.154; assets 23.809m / fin debt 22.651m / "
        "leasing 21.585m / city prijssub 1.705m / gecorr AFM -1.116m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T12:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1286 AGB SCO Ronse JR2025 dual residual; KBO 0882.840.154; "
        "assets 23.809m equity 0.443m fin debt 22.651m leasing 21.585m "
        "prijssub 1.705m AFM +0.149m gecorr -1.116m cash 0.299m PnL +0.208m; "
        "distinct AGB SOB 0842.354.433; FOI ready not sent; "
        "next rq_1287 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1287",
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
        "+ AGB SCO Ronse 1286 done; prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML "
        "(Welzijnsvereniging Zorg HH / Audio only if a fetchable JR2025 PDF appears); "
        "city+OCMW Ronse GE still unmined (HLN: GR 29.06.2026) only if a BBC PDF downloads; "
        "Steenokkerzeel city+OCMW JR2025 approved 18.06.2026 on echo raadpleegomgeving only if PDF fetches; "
        "AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; skip Motena / Trupark / "
        "Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only / Oosterzele De Kluize "
        "unless a fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; skip AGB "
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
    "notes": "spawned tick1286 after AGB SCO Ronse JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1286", rq_new, rq_spawn)
print("research_queue 1286", found, "spawned_1287", spawned)

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
            "last_unit_id": "rq_1286",
            "ticks_completed": "1286",
            "paused": "no",
            "notes": (
                "tick1286 AGB SCO Ronse JR2025 dual residual; KBO 0882.840.154; "
                "assets 23.809m fin debt 22.651m leasing 21.585m prijssub 1.705m "
                "gecorr AFM -1.116m; FOI ready; next rq_1287 residual dual L5 VL; "
                "continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = """
### Tick 1286 - 2026-08-17 - rq_1286 AGB SCO Ronse dual residual
- Unit: Autonoom Gemeentebedrijf Sport, Cultuur en Ontspanning Ronse (AGB SCO) JR2025 Entity II after sibling AGB SOB tick1194 + OVERO tick1062 (KBO **0882.840.154**; AGB since 31.07.2006; BBC text PDF on ronse.be 97p / 6.94MB; print **21.05.2026**; pub **08.06.2026**). **Distinct from** sibling AGB SOB (**0842.354.433**; mined 1194) and city+OCMW GE (city_ronse still without a mined 2025 GE package). Seat Leuzesesteenweg 241 9600. 1 VE. Voorzitter Joris Vandenhoucke / secretaris Filip Neuville / FD Jurgen Soetens. NACE 93.110 / 93.299. Sites CC De Ververij + sporthal 't Rosco + zwembad. **BBC J2 is in this file.** PATRI ST still JR2024-only; Zorgbedrijf ST TLS unexpected-EOF; Motena still Cloudflare; Bau-huis / Maaseik / Diepenbeek / Bornem still unpublished — not redone. Steenokkerzeel city GE JR2025 approved 18.06.2026 — left for a later unit. Not an every-10 tick.
- EUR strong (primary BBC text PDF): assets **23.809m** (was 24.279m); cash **0.299m** JUMP vs **0.240m**; FVA **0**; MVA **22.246m** leasing/erfpacht **21.585m** (Ververij **9.466m** + zwembad **7.803m** + sporthal **3.983m**); IVA **0.034m**; EV **0.443m** JUMP vs **0.236m** (overig **0.215m** + cum PnL **0.212m** + cap subs **0.016m**); schulden **23.367m**; fin debt **22.651m** (LT **22.065m** + ST due **0.586m**) vs **23.097m**; city loan **0.813m**; new loans **0.137m** (T2 fin-inst / doc 1740002 city); afl **0.583m** (erfpacht **0.448m** + city **0.135m**); expl **+0.732m** (ontv **2.589m** / uitg **1.856m**); invest **−0.137m**; BBR year **+0.149m** / avail **0.813m**; AFM **+0.149m** / gecorr **−1.116m** (aangewezen **1.848m**); PnL **+0.208m** (was +0.233m; retained); pers **0.019m**; city staff dual **0.779m**; city prijssub **1.705m** excl / **1.815m** incl (zwembad **1.269m**). VTE unpublished. Pension **0**.
- CSVs: sources+3/entities(new AGB SCO; city already present)/budgets+39/commitments+6/leaderboard+7 + FOI ready `gap_agbsco_fin_debt_22_65m_lease_21_59m_prijssub_1_70m_l5` (not sent); rq_1286=done; spawn rq_1287; ticks=1286. Not a *0 tick — no progress refresh.
- Next: rq_1287 residual dual L5 VL JR2025 hole_fill (prefer other unmined AGB/zorg/EVA with direct PDF; city Ronse GE or Steenokkerzeel GE only if a fetchable JR appears; skip Motena / Trupark / PATRI / Zorgbedrijf ST / Bau-huis / Maaseik / Diepenbeek unless a fetchable JR appears).

"""
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
