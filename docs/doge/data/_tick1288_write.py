# -*- coding: utf-8 -*-
"""Tick 1288 (research_queue patched surgically — last line + spawn only).
Welzijnsvereniging De Zilveren Zwaan JR2025 dual residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T14:10:00Z"
TICK = 1288
SRC = "src_zwaan_jr2025_bbc"
SRC2 = "src_zwaan_jr2025_portal"
SRC3 = "src_kbo_zwaan_0781430812"
ENT = "zorg_zilveren_zwaan"
CITY = "city_heist_op_den_berg"
SRC_URL = "https://www.heist-op-den-berg.be/file/download/b708863d-fa78-449c-9cfd-a20e54f52b6b/NQF3wek5KW6keYOY3z9BLd6Cez97eOTqJzBcUSrwbF43d.pdf"
SRC2_URL = "https://www.heist-op-den-berg.be/jaarrekening"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0781430812"
GAP = "gap_zwaan_ocmw_sub_1_81m_pers_7_77m_equity_thin_0_04m_l5"
HIER = "Vlaanderen>Gemeenten>Heist-op-den-Berg>De Zilveren Zwaan"

ASSETS = 2539583
ASSETS_2024 = 2352152
CASH = 737515
CASH_2024 = 533593
CURRENT = 2121371
FIXED = 418212
FVA = 27142
IGS = 1250
OTHER_FVA = 25892
MVA = 391069
SCHULDEN = 2500632
EQUITY = 38951
CAP_SUBS = 287629
CUM_PNL = -636847
OTHER_EQUITY = 388169
ST_PROV = 391124
FIN_DEBT = 0
EXPL = 6207
EXPL_ONTV = 11111973
EXPL_UITG = 11105766
INVEST = 0
INVEST_ONTV = 148574
INVEST_UITG = 148574
BBR = 6207
AVAIL = 11863
CUM_BBR_PREV = 5656
AFM = 6207
GECORR = 6207
PNL = -112534
PNL_2024 = -111204
PERS = 7767330
PERS_NIETVAST = 7490510
PERS_OTHER = 276820
GOEDEREN = 3337305
WERKING = 7321353
WERKSUB = 3759267
ALG_SUB = 1810543
OCMW_SUB = 1809678
OCMW_SUB_2024 = 2060797
VL_ALG = 865
SPEC_SUB = 1948724
FED_SPEC = 233338
VL_SPEC = 1715176
OCMW_INV = 148574
VTE_Q4 = "122.13"

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
assert abs((IGS + OTHER_FVA) - FVA) < 2
assert abs((FVA + MVA) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQUITY) - EQUITY) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 2
assert abs((EXPL + INVEST) - BBR) < 2
assert abs((CUM_BBR_PREV + BBR) - AVAIL) < 2
assert AFM == EXPL == GECORR == BBR
assert abs((PERS_NIETVAST + PERS_OTHER) - PERS) < 2
assert abs((VL_ALG + OCMW_SUB) - ALG_SUB) < 2
assert abs((FED_SPEC + VL_SPEC + 210) - SPEC_SUB) < 2
assert abs((ALG_SUB + SPEC_SUB) - WERKSUB) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Welzijnsvereniging De Zilveren Zwaan BBC jaarrekening 2025 (text PDF 63p)",
            "url": SRC_URL,
            "publisher": "Welzijnsvereniging De Zilveren Zwaan / Lokaal Bestuur Heist-op-den-Berg",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1288; 2.43MB text PDF; ModDate 25.03.2026; AV 12.05.2026; pub 13.05.2026; "
                "KBO 0781.430.812; assets 2.540m OCMW sub 1.810m pers 7.767m equity 0.039m thin; "
                "fin debt 0; AFM +6.207; PnL -0.113m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Heist-op-den-Berg jaarrekening portal — WV De Zilveren Zwaan JR2025",
            "url": SRC2_URL,
            "publisher": "Gemeente Heist-op-den-Berg",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1288; JR2025 WV vaststelling 12.05.2026 bekendmaking 13.05.2026; "
                "siblings city GE tick857 + AGB Heist tick1209 already mined; not redone"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO De Zilveren Zwaan 0781.430.812",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1288; Vereniging van OCMWs since 28.01.2022; seat Stationsstraat 2 2220; "
                "2 VE (WZC Berkenhof 2.163.071.492 + Zwaan 2.338.099.876); "
                "AD Annelies Van den Eynde since 01.02.2024; bestuurder Kelly Van Tendeloo since 21.01.2025; "
                "NACE 87.101 RVT / 86.995 voeding; RSZ werkgever since 01.01.2023"
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
            "name_nl": "De Zilveren Zwaan - uw welzijn, onze zorg",
            "name_fr": "De Zilveren Zwaan (association de CPAS Heist-op-den-Berg)",
            "name_en": "De Zilveren Zwaan (Heist-op-den-Berg OCMW care association)",
            "level": "ocmw_association",
            "parent_id": CITY,
            "community_language": "nl",
            "website": "https://www.zilverenzwaan.be",
            "foi_email": "info@zilverenzwaan.be",
            "foi_postal": "Stationsstraat 2 2220 Heist-op-den-Berg",
            "notes": (
                "tick1288 JR2025 dual residual after city GE 857 + AGB Heist 1209; "
                "KBO 0781.430.812; 2 VE WZC Berkenhof + thuiszorg; "
                "assets 2.540m equity 0.039m thin cum PnL -0.637m; OCMW werksub 1.810m; "
                "pers 7.767m VTE Q4 122.13 sickness 18.45pct; fin debt 0; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_zwaan_assets_2025", "2025", ASSETS, "J4 assets 2.539583m vs 2.352152m"),
    ("bud_zwaan_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 2.352152m"),
    ("bud_zwaan_cash_2025", "2025", CASH, "J4 cash 0.737515m JUMP vs 0.533593m"),
    ("bud_zwaan_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 0.533593m"),
    ("bud_zwaan_fva_2025", "2025", FVA, "J4 FVA 0.027142m; IGS 0.001250 + other 0.025892"),
    ("bud_zwaan_mva_2025", "2025", MVA, "J4 MVA 0.391069m; leasing 0; WZC buildings mostly off-book"),
    ("bud_zwaan_equity_2025", "2025", EQUITY, "J4 nettoactief 0.038951m THIN vs 0.048646m"),
    ("bud_zwaan_cap_subs_2025", "2025", CAP_SUBS, "J4 kapitaalssubsidies 0.287629m vs 0.184790m"),
    ("bud_zwaan_cum_pnl_2025", "2025", CUM_PNL, "J4 gecumuleerd tekort -0.636847m vs -0.524312m"),
    ("bud_zwaan_other_eq_2025", "2025", OTHER_EQUITY, "J4 overig nettoactief 0.388169m (inbreng)"),
    ("bud_zwaan_schulden_2025", "2025", SCHULDEN, "J4 schulden 2.500632m all ST vs 2.303506m"),
    ("bud_zwaan_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 0.391124m vs 0.364183m"),
    ("bud_zwaan_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 0 (no bank/lease loans)"),
    ("bud_zwaan_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +6.207"),
    ("bud_zwaan_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 11.111973m"),
    ("bud_zwaan_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 11.105766m"),
    ("bud_zwaan_invest_2025", "2025", INVEST, "J2 invest saldo 0 (ontv=uitg 0.148574m OCMW-funded)"),
    ("bud_zwaan_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +6.207"),
    ("bud_zwaan_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 0.011863m"),
    ("bud_zwaan_afm_2025", "2025", AFM, "J2 AFM +6.207 (no aflossingen)"),
    ("bud_zwaan_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +6.207"),
    ("bud_zwaan_pnl_2025", "2025", PNL, "J5 PnL -0.112534m vs -0.111204m"),
    ("bud_zwaan_pers_2025", "2025", PERS, "T2/J5 bezoldigingen 7.767330m (niet-vast 7.491m)"),
    ("bud_zwaan_goederen_2025", "2025", GOEDEREN, "T2/J5 goederen en diensten 3.337305m"),
    ("bud_zwaan_werking_2025", "2025", WERKING, "T2 ontvangsten uit de werking 7.321353m"),
    ("bud_zwaan_werksub_2025", "2025", WERKSUB, "T2 werkingssubsidies 3.759267m"),
    ("bud_zwaan_ocmw_sub_2025", "2025", OCMW_SUB, "T2 OCMW algemene werksub 1.809678m DROP vs 2.060797m"),
    ("bud_zwaan_ocmw_sub_2024", "2024", OCMW_SUB_2024, "T2 YE2024 OCMW werksub 2.060797m"),
    ("bud_zwaan_ocmw_inv_2025", "2025", OCMW_INV, "T2 OCMW investeringssubsidies 0.148574m"),
    ("bud_zwaan_vl_spec_2025", "2025", VL_SPEC, "T2 VL specifieke werksub 1.715176m"),
    ("bud_zwaan_fed_spec_2025", "2025", FED_SPEC, "T2 federale specifieke werksub 0.233338m"),
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
        "comm_zwaan_ocmw_sub_1_81m_2025",
        "Zwaan 2025 OCMW werksub 1.810m",
        "1809678",
        "T2 OCMW algemene werksub 1.809678m DROP vs 2.060797m; plus OCMW invest 0.148574m; VL spec 1.715m + fed 0.233m",
        "Publish 2026-2031 OCMW toelage lock + why DROP 0.251m FOI",
    ),
    (
        "comm_zwaan_pers_7_77m_2025",
        "Zwaan 2025 personeel 7.767m / VTE 122.13",
        "7767330",
        "T2/J5 7.767330m; niet-vast 7.490510 + other 0.276820; Q4 VTE 122.13 / 183 heads; sickness 18.45pct",
        "Publish paid VTE vs formatie + sickness cost FOI",
    ),
    (
        "comm_zwaan_equity_thin_0_04m_2025",
        "Zwaan YE2025 equity 0.039m thin / cum PnL -0.637m",
        "38951",
        "J4 nettoactief 0.038951m; cap subs 0.288m + other 0.388m + cum -0.637m; PnL -0.113m vs BBR +6.207",
        "Publish why accounting loss vs cash BBR + WZC building ownership FOI",
    ),
    (
        "comm_zwaan_werking_7_32m_2025",
        "Zwaan 2025 werking ontvangsten 7.321m",
        "7321353",
        "T2 ontvangsten uit de werking 7.321353m (WZC Berkenhof + thuiszorg); goederen 3.337m",
        "Publish WZC vs thuiszorg split + occupancy VAZG FOI",
    ),
    (
        "comm_zwaan_vl_fed_spec_1_95m_2025",
        "Zwaan 2025 VL+fed specifieke werksub 1.949m",
        "1948724",
        "T2 VL 1.715176 + fed 0.233338 + other 210; total werksub 3.759m",
        "Publish VSB/RIZIV line split FOI",
    ),
    (
        "comm_zwaan_st_prov_0_39m_2025",
        "Zwaan YE2025 ST voorzieningen 0.391m",
        "391124",
        "J4 ST voorzieningen 0.391124m vs 0.364183m; fin debt 0; all schulden ST 2.501m",
        "Publish provision composition (leave/pension/other) FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "WZC Berkenhof bewoners / thuiszorgklanten Heist-op-den-Berg / OCMW Heist",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 WV De Zilveren Zwaan AV 12.05.2026 / pub 13.05.2026",
            "decision_date": "2026-05-12",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local zorg dual residual map VL JR2025 De Zilveren Zwaan after city 857 + AGB 1209",
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
        "lb_zwaan_ocmw_sub_1_81m_2025",
        "Zwaan 2025 OCMW werksub 1.81m",
        "1809678",
        "6.5",
        "6.0",
        "Publish 2026-2031 OCMW toelage + DROP 0.25m",
        "OCMW werksub 1.810m DROP vs 2.061m; invest sub 0.149m",
    ),
    (
        "lb_zwaan_pers_7_77m_2025",
        "Zwaan 2025 personeel 7.77m / VTE 122.13",
        "7767330",
        "6.0",
        "6.5",
        "Publish paid VTE vs sickness 18.45pct",
        "pers 7.767m; Q4 VTE 122.13 / 183 heads; sickness 18.45pct",
    ),
    (
        "lb_zwaan_equity_thin_0_04m_2025",
        "Zwaan YE2025 equity 0.04m thin / cum -0.64m",
        "38951",
        "6.5",
        "5.5",
        "Publish PnL -0.113m vs BBR +6k + building ownership",
        "equity 0.039m; cum PnL -0.637m; cap subs 0.288m",
    ),
    (
        "lb_zwaan_werking_7_32m_2025",
        "Zwaan 2025 werking 7.32m (WZC+thuiszorg)",
        "7321353",
        "5.5",
        "6.5",
        "Publish WZC vs thuiszorg + VAZG occupancy",
        "werking 7.321m; goederen 3.337m; expl +6.207 on 11.1m",
    ),
    (
        "lb_zwaan_vl_fed_spec_1_95m_2025",
        "Zwaan 2025 VL+fed specifieke werksub 1.95m",
        "1948724",
        "5.5",
        "6.0",
        "Publish VSB/RIZIV line split",
        "VL 1.715 + fed 0.233; total werksub 3.759m",
    ),
    (
        "lb_zwaan_st_prov_0_39m_2025",
        "Zwaan YE2025 ST voorzieningen 0.39m",
        "391124",
        "5.5",
        "5.5",
        "Publish provision composition; fin debt is 0",
        "ST prov 0.391m; schulden all ST 2.501m; fin debt 0",
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
            "beneficiaries": "WZC Berkenhof bewoners / thuiszorgklanten Heist-op-den-Berg / OCMW Heist",
            "stated_goal": "Local zorg dual residual map VL JR2025 De Zilveren Zwaan after city 857 + AGB 1209",
            "measured_outcome": (
                "assets 2.540m / equity 0.039m thin / OCMW sub 1.810m / "
                "pers 7.767m / AFM +6.207 / PnL -0.113m / fin debt 0"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 text PDF; not TE-additive of 348bn; OCMW dual FOI",
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
                "OCMW werksub 1.809678m DROP vs 2.060797m + invest 0.148574m pad 2026-2031 "
                "+ why PnL -112534 vs BBR +6207 + equity thin 38951 / cum -636847 "
                "+ ST voorzieningen 391124 composition + WZC Berkenhof building ownership "
                "+ WZC vs thuiszorg split of werking 7.321353m + VAZG occupancy "
                "+ paid VTE vs Q4 122.13 / sickness 18.45pct behind pers 7.767330m "
                "+ VL/fed specific 1.948724m VSB/RIZIV lines"
            ),
            "why_it_matters": (
                "Unmined Heist zorg sibling after city GE 857 + AGB 1209. "
                "OCMW dual 1.810m werksub + 0.149m invest. Equity 0.039m thin. "
                "Pers 7.767m / 122 VTE with 18.45pct sickness. Fin debt 0."
            ),
            "priority": "8",
            "recipient_body": "Welzijnsvereniging De Zilveren Zwaan / OCMW Heist-op-den-Berg",
            "recipient_email": "info@zilverenzwaan.be",
            "recipient_postal": "Stationsstraat 2 2220 Heist-op-den-Berg",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_zwaan_ocmw_sub_1_81m_2025",
            "linked_leaderboard_id": "lb_zwaan_ocmw_sub_1_81m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1288",
    "title": "De Zilveren Zwaan JR2025 dual residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: WV De Zilveren Zwaan JR2025 BBC text + KBO; "
        "KBO 0781.430.812; assets 2.540m / OCMW sub 1.810m / pers 7.767m / "
        "equity 0.039m thin / fin debt 0; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:20:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1288 WV De Zilveren Zwaan JR2025 dual residual; KBO 0781.430.812; "
        "assets 2.540m cash 0.738m JUMP equity 0.039m thin cum -0.637m "
        "OCMW sub 1.810m DROP pers 7.767m VTE 122.13 sickness 18.45pct "
        "AFM +6.207 PnL -0.113m fin debt 0; FOI ready not sent; "
        "next rq_1289 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1289",
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
        "+ AGB SCO Ronse 1286 + Stad+OCMW Ronse 1287 + De Zilveren Zwaan 1288 done; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined AGB Heist 1209 / city Heist 857 / Zwaan 1288; "
        "Steenokkerzeel city+OCMW JR2025 listed on city site only if PDF fetches; "
        "AGB Steenokkerzeel NBB 2025 only if a primary PDF downloads; "
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
    "notes": "spawned tick1288 after De Zilveren Zwaan JR2025 dual residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1288", rq_new, rq_spawn)
print("research_queue 1288", found, "spawned_1289", spawned)

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
            "last_unit_id": "rq_1288",
            "ticks_completed": "1288",
            "paused": "no",
            "notes": (
                "tick1288 WV De Zilveren Zwaan JR2025 dual residual; KBO 0781.430.812; "
                "assets 2.540m OCMW sub 1.810m pers 7.767m equity 0.039m thin; "
                "FOI ready; next rq_1289 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1288_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
