# -*- coding: utf-8 -*-
"""Tick 1296 (research_queue patched surgically — last line + spawn only).
AGB Diepenbeek JR2025 Entity II residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T12:45:00Z"
TICK = 1296
SRC = "src_agbd_jr2025_bbc"
SRC2 = "src_agbd_jr2025_rvb"
SRC3 = "src_kbo_agbd_0885640088"
ENT = "agb_diepenbeek"
CITY = "city_diepenbeek"
SRC_URL = "https://www.diepenbeek.be/file_uploads/42825.pdf?sc=E2527E18F2018B1606A8B07F83BA56D0"
SRC2_URL = "https://www.diepenbeek.be/file_uploads/42823.pdf?sc=C45439FC20A6ECC257B5E4E7D4AB4465"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0885640088"
GAP = "gap_agbd_fin_debt_3_03m_city_werksub_0_38m_cum_neg_0_91m_l5"
HIER = "Vlaanderen>Gemeenten>Diepenbeek>AGB"

ASSETS = 12012548
ASSETS_2024 = 12264288
CASH = 920957
CASH_2024 = 744009
CURRENT = 1768492
FIXED = 10244055
FVA = 0
EVA = 0
IGS = 0
MVA = 10244055
LEASING = 0
SCHULDEN = 3443569
EQUITY = 8568979
CAP_SUBS = 2471720
CUM_PNL = -912741
OTHER_EQ = 7010000
FIN_DEBT = 3026093
FIN_DEBT_LT = 2667854
FIN_DEBT_ST = 358239
FIN_DEBT_2024 = 3373396
NEW_LOANS = 0
PENSION = 0
EXPL = 523967
EXPL_ONTV = 971689
EXPL_UITG = 447722
INVEST = -88384
INVEST_UITG = 96384
INVEST_ONTV = 8000
BBR = 88281
CUM_PREV = 1266250
AVAIL = 1354531
AFM = 176665
GECORR = 254095
AFL = 347302
PNL = 97060
PERS = 0
WERKSUB = 384720
WERKING = 572349
RENTE = 93208
BELEG = 400000
BELEG_YLD = 8036


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
assert abs((FVA + MVA) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQ) - EQUITY) < 2
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "AGB Diepenbeek BBC jaarrekening 2025 (PDF 74p)",
            "url": SRC_URL,
            "publisher": "Autonoom Gemeentebedrijf Diepenbeek",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1296; 7.57MB BBC PDF diepenbeek.be file_uploads/42825; RVB 22.06.2026; "
                "KBO 0885.640.088; assets 12.013m fin debt 3.026m city werksub 0.385m "
                "cum PnL -0.913m NEG AFM +0.177m avail 1.355m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "AGBD RVB 22.06.2026 vaststelling JR2025",
            "url": SRC2_URL,
            "publisher": "Raad van bestuur AGB Diepenbeek",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1296; JR2025 vaststelling RVB 22.06.2026 2026_AGBrvb_00010; pub 24.06.2026; "
                "voorzitter Rik Kriekels; city GE JR2025 also live left for later unit"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Autonoom Gemeentebedrijf Diepenbeek 0885.640.088",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1296; AGB since 03.10.2006; seat Dorpsstraat 14 3590; 2 VE; "
                "voorzitter Rik Kriekels since 18.02.2019; AD Jan Dreesen / FD Monique Aerts "
                "gedelegeerd bestuurder; NACE 68.203; email info@diepenbeek.be; "
                "city sibling 0207.465.974 (diepenbeek.be contact)"
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
            "name_nl": "Gemeente Diepenbeek",
            "name_fr": "Commune de Diepenbeek",
            "name_en": "Municipality of Diepenbeek",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.diepenbeek.be",
            "foi_email": "info@diepenbeek.be",
            "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
            "notes": (
                "tick1296 parent stub for AGBD; KBO 0207.465.974 (diepenbeek.be contact); NIS 71011; "
                "city+OCMW JR2025 BBC now published 22.06.2026/24.06.2026 — left unmined for later GE unit"
            ),
        },
        {
            "entity_id": ENT,
            "name_nl": "Autonoom Gemeentebedrijf Diepenbeek (AGBD)",
            "name_fr": "Regie communale autonome Diepenbeek",
            "name_en": "Autonomous municipal company Diepenbeek",
            "level": "municipal_agency",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.diepenbeek.be/agbd",
            "foi_email": "info@diepenbeek.be",
            "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
            "notes": (
                "tick1296 JR2025 Entity II residual; KBO 0885.640.088; 2 VE; no FVA; "
                "assets 12.013m fin debt 3.026m city werksub 0.385m cum PnL -0.913m NEG "
                "AFM +0.177m avail 1.355m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_agbd_assets_2025", "2025", ASSETS, "J4 assets 12.012548m vs 12.264288m"),
    ("bud_agbd_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 12.264288m"),
    ("bud_agbd_cash_2025", "2025", CASH, "J4 cash+beleg 0.920957m JUMP vs 0.744009m"),
    ("bud_agbd_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 0.744009m"),
    ("bud_agbd_fva_2025", "2025", FVA, "T5 FVA 0; EVA 0 + IGS 0"),
    ("bud_agbd_mva_2025", "2025", MVA, "J4/T5 MVA 10.244055m; leasing 0"),
    ("bud_agbd_leasing_2025", "2025", LEASING, "T5 leasing MVA 0"),
    ("bud_agbd_equity_2025", "2025", EQUITY, "J4 nettoactief 8.568979m vs 8.543473m"),
    ("bud_agbd_cap_subs_2025", "2025", CAP_SUBS, "J4/T5 cap subs 2.471720m vs 2.543274m"),
    ("bud_agbd_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL -0.912741m NEG vs -1.009801m"),
    ("bud_agbd_other_eq_2025", "2025", OTHER_EQ, "J4 overig nettoactief/kapitaal 7.010000m"),
    ("bud_agbd_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 3.026093m (LT 2.668 + ST due 0.358)"),
    ("bud_agbd_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 3.373396m"),
    ("bud_agbd_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 2.667854m"),
    ("bud_agbd_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 0.358239m"),
    ("bud_agbd_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0"),
    ("bud_agbd_pension_2025", "2025", PENSION, "J4 no pension voorziening; 0"),
    ("bud_agbd_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +0.523967m"),
    ("bud_agbd_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 0.971689m"),
    ("bud_agbd_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 0.447722m"),
    ("bud_agbd_invest_2025", "2025", INVEST, "J2 invest -0.088384m vs MJP -0.481m"),
    ("bud_agbd_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +0.088281m"),
    ("bud_agbd_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 1.354531m"),
    ("bud_agbd_afm_2025", "2025", AFM, "J2 AFM +0.176665m"),
    ("bud_agbd_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +0.254095m"),
    ("bud_agbd_pnl_2025", "2025", PNL, "J5 PnL +0.097060m (was +0.086414m)"),
    ("bud_agbd_pers_2025", "2025", PERS, "J5 no bezoldigingen; pers 0 on AGB books"),
    ("bud_agbd_werksub_2025", "2025", WERKSUB, "T2/J5 city algemene werksub 0.384720m"),
    ("bud_agbd_werking_2025", "2025", WERKING, "J5/T2 ontvangsten uit de werking 0.572349m"),
    ("bud_agbd_rente_2025", "2025", RENTE, "T2/J5 rente aan andere entiteiten 0.093208m"),
    ("bud_agbd_afl_2025", "2025", AFL, "T4/J2 periodieke aflossingen 0.347302m"),
    ("bud_agbd_beleg_2025", "2025", BELEG, "risico tak-26 Federale Verzekering 0.400000m inside cash+beleg"),
    ("bud_agbd_beleg_yld_2025", "2025", BELEG_YLD, "risico tak-26 yield 8036.24"),
    ("bud_agbd_invest_uitg_2025", "2025", INVEST_UITG, "J2/T2 invest uitg 0.096384m"),
    ("bud_agbd_schulden_2025", "2025", SCHULDEN, "J4 schulden total 3.443569m"),
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
        "comm_agbd_fin_debt_3_03m_2025",
        "AGBD YE2025 fin debt 3.026m",
        "3026093",
        "T4 3.026093m (LT 2.668 + ST due 0.358) declining vs 3.373m; new loans 0; 4 doorgeefleningen gemeente ING/Argenta/Belfius x2",
        "Publish per-loan amort 2026-2031 FOI",
    ),
    (
        "comm_agbd_city_werksub_0_38m_2025",
        "AGBD 2025 city werksub 0.385m",
        "384720",
        "T2/J5 algemene werksub van de gemeente 0.384720m; city GE JR2025 live unmined",
        "Publish 2026-2031 beheersovereenkomst pad FOI",
    ),
    (
        "comm_agbd_cum_neg_0_91m_2025",
        "AGBD YE2025 cum PnL -0.913m NEG",
        "912741",
        "T5 cum PnL -0.912741m NEG vs -1.009801m; year PnL +0.097060m; kapitaal 7.010m frozen",
        "Publish resorption pad 2026-2031 FOI",
    ),
    (
        "comm_agbd_mva_10_24m_2025",
        "AGBD YE2025 MVA 10.244m patrimonium",
        "10244055",
        "J4 MVA 10.244m (gemeenschap 5.823 + bedrijfsmatig 4.421); leasing 0; GC De Plak + Demerstrand",
        "Publish site split + 2026-2031 invest carry FOI",
    ),
    (
        "comm_agbd_avail_1_35m_2025",
        "AGBD YE2025 avail BBR 1.355m",
        "1354531",
        "avail 1.354531m; BBR year +0.088m; AFM +0.177m; cash 0.921m incl tak-26 0.400m",
        "Publish uncommitted expl overschot vs belegging lock FOI",
    ),
    (
        "comm_agbd_rente_0_09m_2025",
        "AGBD 2025 rente 0.093m",
        "93208",
        "T2/J5 rente aan andere entiteiten 0.093208m (doorgeef path); afl 0.347m",
        "Publish rate per of 4 doorgeefleningen FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Diepenbeek / GC De Plak / Demerstrand",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 AGB Diepenbeek RVB 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local AGB dual residual map VL JR2025 Diepenbeek",
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
        "lb_agbd_fin_debt_3_03m_2025",
        "AGBD YE2025 fin debt 3.03m",
        "3026093",
        "6.0",
        "6.5",
        "Publish per-loan amort 2026-2031 4 doorgeefleningen",
        "fin debt 3.026m declining vs 3.373m; new loans 0; ING/Argenta/Belfius x2",
    ),
    (
        "lb_agbd_city_werksub_0_38m_2025",
        "AGBD 2025 city werksub 0.38m",
        "384720",
        "6.5",
        "5.5",
        "Publish 2026-2031 beheersovereenkomst pad",
        "city algemene werksub 0.385m; city GE JR2025 live unmined",
    ),
    (
        "lb_agbd_cum_neg_0_91m_2025",
        "AGBD YE2025 cum PnL -0.91m NEG",
        "912741",
        "7.0",
        "5.5",
        "Publish resorption pad 2026-2031",
        "cum -0.913m NEG after year +0.097m; kapitaal 7.010m frozen",
    ),
    (
        "lb_agbd_mva_10_24m_2025",
        "AGBD YE2025 MVA 10.24m patrimonium shell",
        "10244055",
        "5.5",
        "7.0",
        "Publish site split De Plak/Demerstrand + invest carry",
        "MVA 10.244m leasing 0; FVA 0; GC De Plak + Demerstrand",
    ),
    (
        "lb_agbd_avail_1_35m_2025",
        "AGBD YE2025 avail BBR 1.35m",
        "1354531",
        "5.0",
        "6.0",
        "Publish uncommitted overschot vs tak-26 lock",
        "avail 1.355m; BBR +0.088m; AFM +0.177m; cash 0.921m incl 0.400m tak-26",
    ),
    (
        "lb_agbd_rente_0_09m_2025",
        "AGBD 2025 rente 0.09m doorgeef",
        "93208",
        "6.0",
        "5.0",
        "Publish rate per of 4 doorgeefleningen",
        "rente 0.093m aan andere entiteiten; afl 0.347m; new loans 0",
    ),
    (
        "lb_agbd_pers_0_city_dual_2025",
        "AGBD 2025 pers 0 / city staff dual unpublished",
        "0",
        "6.5",
        "4.5",
        "Publish VTE AGB vs city staff De Plak/Demerstrand",
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
            "beneficiaries": "Inwoners Diepenbeek / GC De Plak / Demerstrand",
            "stated_goal": "Local AGB dual residual map VL JR2025 Diepenbeek",
            "measured_outcome": (
                "assets 12.013m / fin debt 3.026m / city werksub 0.385m / "
                "cum PnL -0.913m NEG / AFM +0.177m / avail 1.355m"
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
                "T4/LT-S per-loan creditors for fin debt 3.026093m (4 doorgeefleningen "
                "gemeente ING/Argenta/Belfius x2; new loans 0) + city werksub 0.384720 "
                "2026-2031 pad + city GE dual lock (JR2025 now live unmined) + "
                "VTE vs pers 0 / city staff dual + cum PnL -0.912741 NEG resorption + "
                "tak-26 0.400000 availability inside cash 0.920957"
            ),
            "why_it_matters": (
                "Unmined AGB Diepenbeek after residual dual hunt. FVA 0 / leasing 0. "
                "Fin debt 3.026m declining via doorgeef path; new loans 0. "
                "City werksub 0.385m; cum PnL still -0.913m NEG. "
                "Avail 1.355m with BBR year +0.088m. City GE PDF now live, left unmined."
            ),
            "priority": "8",
            "recipient_body": "AGB Diepenbeek / Gemeente Diepenbeek",
            "recipient_email": "info@diepenbeek.be",
            "recipient_postal": "Dorpsstraat 14 3590 Diepenbeek",
            "draft_letter_path": "docs/doge/foi/drafts/gap_agbd_fin_debt_3_03m_city_werksub_0_38m_cum_neg_0_91m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_agbd_fin_debt_3_03m_2025",
            "linked_leaderboard_id": "lb_agbd_fin_debt_3_03m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1296",
    "title": "AGB Diepenbeek JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: AGB Diepenbeek JR2025 BBC text + KBO; "
        "KBO 0885.640.088; assets 12.013m / fin debt 3.026m / "
        "city werksub 0.385m / cum PnL -0.913m NEG / AFM +0.177m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T12:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1296 AGB Diepenbeek JR2025 Entity II residual; KBO 0885.640.088; "
        "assets 12.013m fin debt 3.026m city werksub 0.385m AFM +0.177m gecorr +0.254m "
        "BBR +0.088m avail 1.355m cash 0.921m cum PnL -0.913m NEG new loans 0 "
        "4 doorgeefleningen; city GE JR2025 live left unmined; FOI ready not sent; "
        "next rq_1297 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1297",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1296 done including AGB Diepenbeek 1296); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "city Diepenbeek GE JR2025 now fetchable on diepenbeek.be — take as GE unit; "
        "skip already-mined AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294 / "
        "Oud-Heverlee 1293 / Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / "
        "Tielt-Winge 1289 / Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen/Zwalm/Wortegem-Petegem "
        "city+OCMW JR2025 only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215 / AGB Oostkamp 1131; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1296 after AGB Diepenbeek JR2025 Entity II residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1296", rq_new, rq_spawn)
print("research_queue 1296", found, "spawned_1297", spawned)

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
            "last_unit_id": "rq_1296",
            "ticks_completed": "1296",
            "paused": "no",
            "notes": (
                "tick1296 AGB Diepenbeek JR2025 Entity II residual; KBO 0885.640.088; "
                "assets 12.013m fin debt 3.026m city werksub 0.385m cum PnL -0.913m NEG; "
                "FOI ready; next rq_1297 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1296_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
