# -*- coding: utf-8 -*-
"""Tick 1299 (research_queue patched surgically — last line + spawn only).
AGB Kortenaken JR2025 Entity II residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T13:50:00Z"
TICK = 1299
SRC = "src_agbktn_jr2025_bbc"
SRC2 = "src_agbktn_jr2025_rvb"
SRC3 = "src_kbo_agbktn_0535811469"
ENT = "agb_kortenaken"
CITY = "city_kortenaken"
SRC_URL = "https://www.kortenaken.be/sites/default/files/2026-05/20260528_VASTSTELLING-BBC-JAARREKENING-AGB.pdf"
SRC2_URL = "https://www.kortenaken.be/sites/default/files/2026-05/20260528_VASTSTELLING-BBC-JAARREKENING-AGB_RVB.pdf"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0535811469"
GAP = "gap_agbktn_fin_debt_3_28m_lease_3_22m_prijssub_0_16m_l5"
HIER = "Vlaanderen>Gemeenten>Kortenaken>AGB"

ASSETS = 3479256
ASSETS_2024 = 3503923
CASH = 103630
CASH_2024 = 69293
CURRENT = 190289
FIXED = 3288967
FVA = 0
EVA = 0
IGS = 0
MVA = 3287804
LEASING = 3216363
IVA = 1163
SCHULDEN = 3376072
EQUITY = 103184
CAP_SUBS = 0
CUM_PNL = 78184
OTHER_EQ = 25000
FIN_DEBT = 3280771
FIN_DEBT_LT = 3233422
FIN_DEBT_ST = 47348
FIN_DEBT_2024 = 3310891
NEW_LOANS = 16500
PENSION = 0
EXPL = 55792
EXPL_ONTV = 193795
EXPL_UITG = 138003
INVEST = -16500
BBR = 9171
CUM_PREV = 85817
AVAIL = 94988
AFM = 9171
GECORR = -209080
AANGEWEZEN = 264871
AFL = 46621
PNL = 15431
DIVIDEND = 10000
RETAINED = 5431
PERS = 0
PRIJSSUB = 157062
PRIJSSUB_CITY = 156547
PRIJSSUB_BEKK = 515
WERKING = 190398
CLIENT = 22410
CANON = 36550
CITY_LOAN_AFL = 10071
MAINT = 67229


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
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
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
assert abs((FVA + MVA + IVA) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQ) - EQUITY) < 2
assert abs((DIVIDEND + RETAINED) - PNL) < 2
assert abs((PRIJSSUB_CITY + PRIJSSUB_BEKK) - PRIJSSUB) < 2
assert abs((CANON + CITY_LOAN_AFL) - AFL) < 2
assert abs((AFM + (AFL - AANGEWEZEN)) - GECORR) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB Kortenaken BBC jaarrekening 2025 (PDF 71p)",
            "url": SRC_URL,
            "publisher": "Autonoom Gemeentebedrijf Kortenaken",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1299; 2.83MB BBC PDF kortenaken.be 20260528_VASTSTELLING-BBC-JAARREKENING-AGB; "
                "RVB 28.05.2026 pub 29.05.2026; KBO 0535.811.469; assets 3.479m fin debt 3.281m "
                "leasing 3.216m city prijssub 0.157m gecorr AFM -0.209m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGB Kortenaken RVB 28.05.2026 vaststelling JR2025",
            "url": SRC2_URL,
            "publisher": "Raad van bestuur AGB Kortenaken",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1299; JR2025 vaststelling RVB 28.05.2026 pub 29.05.2026; "
                "AFM 9171 / BBR 9171 / avail 94988 / PnL 15431 / winstuitkering 10000; "
                "voorzitter Niels Willems; city GE JR2025 also live left for later unit"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Autonoom Gemeentebedrijf Kortenaken 0535.811.469",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1299; AGB KBO 0535.811.469; seat Dorpsplein 35 3470; 1 VE; "
                "voorzitter Niels Willems / AD Dominique Hayen / FD Eddy Jacobs; "
                "city sibling 0207.520.711 / OCMW 0212.189.379 (kortenaken.be contact)"
            ),
        },
    ],
)
print("sources", n)

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": CITY,
            "name_nl": "Gemeente Kortenaken",
            "name_fr": "Commune de Kortenaken",
            "name_en": "Municipality of Kortenaken",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.kortenaken.be",
            "foi_email": "financien@kortenaken.be",
            "foi_postal": "Dorpsplein 35 3470 Kortenaken",
            "notes": (
                "tick1299 parent stub for AGB; KBO 0207.520.711 / OCMW 0212.189.379 "
                "(kortenaken.be contact); NIS 24054; city+OCMW JR2025 BBC now published "
                "22.06.2026 — left unmined for later GE unit"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Autonoom Gemeentebedrijf Kortenaken",
            "name_fr": "Regie communale autonome Kortenaken",
            "name_en": "Autonomous municipal company Kortenaken",
            "level": "municipal_agency",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.kortenaken.be/bestuur-organisatie/beleidsdocumenten/jaarrekening/agb",
            "foi_email": "financien@kortenaken.be",
            "foi_postal": "Dorpsplein 35 3470 Kortenaken",
            "notes": (
                "tick1299 JR2025 Entity II residual; KBO 0535.811.469; 1 VE; no FVA; "
                "assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m "
                "gecorr AFM -0.209m avail 0.095m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbktn_assets_2025", "2025", ASSETS, "J4 assets 3.479256m vs 3.503923m"),
    ("bud_agbktn_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 3.503923m"),
    ("bud_agbktn_cash_2025", "2025", CASH, "J4 cash+beleg 0.103630m JUMP vs 0.069293m"),
    ("bud_agbktn_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 0.069293m"),
    ("bud_agbktn_fva_2025", "2025", FVA, "T5 FVA 0; EVA 0 + IGS 0"),
    ("bud_agbktn_mva_2025", "2025", MVA, "J4/T5 MVA 3.287804m; leasing 3.216363m"),
    ("bud_agbktn_leasing_2025", "2025", LEASING, "T5 leasing MVA 3.216363m (sporthal De Vruen)"),
    ("bud_agbktn_iva_2025", "2025", IVA, "J4/T5 IVA 0.001163m"),
    ("bud_agbktn_equity_2025", "2025", EQUITY, "J4 nettoactief 0.103184m vs 0.097754m"),
    ("bud_agbktn_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL 0.078184m (year retained 0.005431m)"),
    ("bud_agbktn_other_eq_2025", "2025", OTHER_EQ, "J4 overig nettoactief 0.025000m"),
    ("bud_agbktn_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 3.280771m (LT 3.233 + ST due 0.047)"),
    ("bud_agbktn_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 3.310891m"),
    ("bud_agbktn_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 3.233422m"),
    ("bud_agbktn_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 0.047348m; ST fin 0"),
    ("bud_agbktn_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.016500m renteloze stadslening; no bank"),
    ("bud_agbktn_pension_2025", "2025", PENSION, "J4 no pension voorziening; 0"),
    ("bud_agbktn_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +0.055792m"),
    ("bud_agbktn_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 0.193795m"),
    ("bud_agbktn_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 0.138003m"),
    ("bud_agbktn_invest_2025", "2025", INVEST, "J2 invest -0.016500m (spinningfietsen)"),
    ("bud_agbktn_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +0.009171m"),
    ("bud_agbktn_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 0.094988m"),
    ("bud_agbktn_afm_2025", "2025", AFM, "J2 AFM +0.009171m"),
    ("bud_agbktn_gecorr_2025", "2025", GECORR, "J2 gecorr AFM -0.209080m (aangewezen 0.264871m)"),
    ("bud_agbktn_pnl_2025", "2025", PNL, "J5 PnL +0.015431m; dividend 0.010m / retained 0.005431m"),
    ("bud_agbktn_pers_2025", "2025", PERS, "J5 no bezoldigingen; pers 0 on AGB books"),
    ("bud_agbktn_prijssub_2025", "2025", PRIJSSUB, "T2/D2 prijssub 0.157062m (city 0.156547 + Bekkevoort 0.000515)"),
    ("bud_agbktn_werking_2025", "2025", WERKING, "J5/T2 ontvangsten uit de werking 0.190398m"),
    ("bud_agbktn_client_2025", "2025", CLIENT, "D2 klantentarieven 0.022410m excl btw"),
    ("bud_agbktn_afl_2025", "2025", AFL, "T4/J2 periodieke aflossingen 0.046621m (canon 0.036550 + city 0.010071)"),
    ("bud_agbktn_dividend_2025", "2025", DIVIDEND, "J5/RVB winstuitkering gemeente 0.010000m"),
    ("bud_agbktn_maint_2025", "2025", MAINT, "D2 Sport Vlaanderen onderhoud 0.067229m"),
    ("bud_agbktn_schulden_2025", "2025", SCHULDEN, "J4 schulden total 3.376072m"),
    ("bud_agbktn_aangewezen_2025", "2025", AANGEWEZEN, "J2 aangewezen aflossingen 0.264871m vs actual 0.046621m"),
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
        "comm_agbktn_fin_debt_3_28m_2025",
        "AGB Kortenaken YE2025 fin debt 3.281m",
        "3280771",
        "T4 3.280771m (LT 3.233 + ST due 0.047) declining vs 3.311m; new loans 0.017m city interest-free; leasing MVA 3.216m",
        "Publish per-contract amort 2026-2035 leasing vs city loans FOI",
    ),
    (
        "comm_agbktn_lease_3_22m_2025",
        "AGB Kortenaken YE2025 leasing MVA 3.216m",
        "3216363",
        "T5 leasing 3.216363m (sporthal De Vruen); canon 0.036550m; DBFM Sport Vlaanderen since 08.05.2012",
        "Publish remaining DBFM/erfpacht schedule FOI",
    ),
    (
        "comm_agbktn_prijssub_0_16m_2025",
        "AGB Kortenaken 2025 city prijssub 0.157m",
        "157062",
        "D2/T2 prijssub Kortenaken 0.156547 + Bekkevoort 0.000515; factor 7 since 01.01.2025; city GE live unmined",
        "Publish 2026-2031 beheersovereenkomst pad FOI",
    ),
    (
        "comm_agbktn_gecorr_neg_0_21m_2025",
        "AGB Kortenaken YE2025 gecorr AFM -0.209m",
        "209080",
        "J2 gecorr AFM -0.209080m; aangewezen 0.264871 vs actual 0.046621; AFM +0.009171",
        "Publish aangewezen vs actual amort pad FOI",
    ),
    (
        "comm_agbktn_avail_0_09m_2025",
        "AGB Kortenaken YE2025 avail BBR 0.095m",
        "94988",
        "avail 0.094988m; BBR year +0.009171m; cash 0.104m JUMP; dividend 0.010m",
        "Publish uncommitted overschot vs dividend lock FOI",
    ),
    (
        "comm_agbktn_maint_0_07m_2025",
        "AGB Kortenaken 2025 Sport Vlaanderen onderhoud 0.067m",
        "67229",
        "D2 onderhoud 0.067229m; index 20pct loon / 80pct materiaal since 08.05.2012; daklek residual unpublished",
        "Publish DBFM index + daklek residual euro FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Kortenaken / Sporthal De Vruen",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 AGB Kortenaken RVB 28.05.2026",
            "decision_date": "2026-05-28",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB dual residual map VL JR2025 Kortenaken",
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
        "lb_agbktn_fin_debt_3_28m_2025",
        "AGB Kortenaken YE2025 fin debt 3.28m",
        "3280771",
        "6.0",
        "6.5",
        "Publish per-contract amort 2026-2035 leasing vs city loans",
        "fin debt 3.281m declining vs 3.311m; new loans 0.017m city interest-free",
    ),
    (
        "lb_agbktn_lease_3_22m_2025",
        "AGB Kortenaken YE2025 leasing 3.22m De Vruen",
        "3216363",
        "6.5",
        "7.0",
        "Publish remaining DBFM/erfpacht schedule",
        "leasing MVA 3.216m; canon 0.037m; Sport Vlaanderen DBFM 2012",
    ),
    (
        "lb_agbktn_prijssub_0_16m_2025",
        "AGB Kortenaken 2025 city prijssub 0.16m",
        "157062",
        "6.5",
        "5.5",
        "Publish 2026-2031 factor-7 prijssub pad",
        "city 0.157m + Bekkevoort 0.001m; klant only 0.022m; city GE unmined",
    ),
    (
        "lb_agbktn_gecorr_neg_0_21m_2025",
        "AGB Kortenaken YE2025 gecorr AFM -0.21m",
        "209080",
        "7.0",
        "5.5",
        "Publish aangewezen vs actual amort pad",
        "gecorr -0.209m; aangewezen 0.265m vs actual 0.047m; AFM +0.009m",
    ),
    (
        "lb_agbktn_avail_0_09m_2025",
        "AGB Kortenaken YE2025 avail BBR 0.09m",
        "94988",
        "5.0",
        "5.0",
        "Publish uncommitted overschot vs dividend 0.010m",
        "avail 0.095m; BBR +0.009m; cash 0.104m JUMP; dividend 0.010m",
    ),
    (
        "lb_agbktn_maint_0_07m_2025",
        "AGB Kortenaken 2025 Sport Vlaanderen onderhoud 0.07m",
        "67229",
        "6.0",
        "5.0",
        "Publish DBFM index + daklek residual euro",
        "onderhoud 0.067m; index 20/80 since 2012; daklek unpublished",
    ),
    (
        "lb_agbktn_pers_0_city_dual_2025",
        "AGB Kortenaken 2025 pers 0 / city staff dual unpublished",
        "0",
        "6.5",
        "4.5",
        "Publish VTE AGB vs city staff De Vruen",
        "J5 no bezoldigingen; city dual staff unpublished",
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
            "beneficiaries": "Inwoners Kortenaken / Sporthal De Vruen",
            "stated_goal": "Local AGB dual residual map VL JR2025 Kortenaken",
            "measured_outcome": (
                "assets 3.479m / fin debt 3.281m / leasing 3.216m / "
                "city prijssub 0.157m / gecorr AFM -0.209m / avail 0.095m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.5",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; AGB dual FOI",
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
                "T4/LT-S per-contract creditors for fin debt 3.280771m (leasing MVA 3.216363; "
                "new loans 0.016500 city interest-free to 31.12.2035; canon 0.036550 + city afl 0.010071) "
                "+ city prijssub 0.156547 factor-7 2026-2031 pad + Bekkevoort 0.000515 + "
                "VTE vs pers 0 / city staff dual + gecorr AFM -0.209080 (aangewezen 0.264871) + "
                "Sport Vlaanderen DBFM 0.067229 / daklek residual + city GE dual lock (JR2025 now live unmined)"
            ),
            "why_it_matters": (
                "Unmined AGB Kortenaken after residual dual hunt. Official BBC PDF now downloads. "
                "FVA 0. Fin debt 3.281m almost all leasing 3.216m; new loans 0.017m city interest-free. "
                "City prijssub 0.157m (klant only 0.022m). Gecorr AFM -0.209m. "
                "Avail 0.095m with BBR year +0.009m. City GE PDF now live, left unmined."
            ),
            "priority": "8",
            "recipient_body": "AGB Kortenaken / Gemeente Kortenaken",
            "recipient_email": "financien@kortenaken.be",
            "recipient_postal": "Dorpsplein 35 3470 Kortenaken",
            "draft_letter_path": "docs/doge/foi/drafts/gap_agbktn_fin_debt_3_28m_lease_3_22m_prijssub_0_16m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbktn_fin_debt_3_28m_2025",
            "linked_leaderboard_id": "lb_agbktn_fin_debt_3_28m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1299",
    "title": "AGB Kortenaken JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Kortenaken JR2025 BBC text + KBO; "
        "KBO 0535.811.469; assets 3.479m / fin debt 3.281m / "
        "leasing 3.216m / city prijssub 0.157m / gecorr AFM -0.209m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:20:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1299 AGB Kortenaken JR2025 Entity II residual; KBO 0535.811.469; "
        "assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m "
        "AFM +0.009m gecorr -0.209m BBR +0.009m avail 0.095m cash 0.104m JUMP "
        "new loans 0.017m city interest-free dividend 0.010m; city GE JR2025 live left unmined; "
        "FOI ready not sent; next rq_1300 residual dual L5 VL + every-10 progress"
    ),
}
rq_spawn = {
    "task_id": "rq_1300",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1299 done including AGB Kortenaken 1299 / Stad+OCMW Steenokkerzeel 1298 / "
        "AGB Steenokkerzeel 1167 / Stad+OCMW Diepenbeek 1297 / AGB Diepenbeek 1296); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "city Kortenaken GE JR2025 now fetchable on kortenaken.be — take as GE unit; "
        "skip already-mined AGB Kortenaken 1299 / city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / "
        "city Diepenbeek 1297 / AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / "
        "Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / "
        "Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem city+OCMW JR2025 only if PDF fetches; "
        "AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF; "
        "tick 1300 is every-10: also refresh progress_every_10_ticks.md + doge_waste_top10_current.md"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1299 after AGB Kortenaken JR2025 Entity II residual; next residual dual L5 VL + every-10 progress@1300",
}
path = DATA / "research_queue.csv"
before = path.stat().st_size
found, spawned = patch_last_rq_and_spawn(path, "rq_1299", rq_new, rq_spawn)
after = path.stat().st_size
print("research_queue 1299", found, "spawned_1300", spawned, "size", before, "->", after)

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
            "last_unit_id": "rq_1299",
            "ticks_completed": "1299",
            "paused": "no",
            "notes": (
                "tick1299 AGB Kortenaken JR2025 Entity II residual; KBO 0535.811.469; "
                "assets 3.479m fin debt 3.281m leasing 3.216m city prijssub 0.157m gecorr AFM -0.209m; "
                "FOI ready; next rq_1300 residual dual L5 VL + every-10; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1299_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
