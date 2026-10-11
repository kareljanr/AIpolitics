# -*- coding: utf-8 -*-
"""Tick 1289 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Tielt-Winge JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T11:20:00Z"
TICK = 1289
SRC = "src_tw_jr2025_bbc"
SRC2 = "src_tw_jr2025_portal"
SRC3 = "src_kbo_tw_0216769660"
ENT = "city_tielt_winge"
OCMW = "ocmw_tielt_winge"
SRC_URL = "https://tielt-winge.meetingburger.net/Pages/HandleFile.ashx?id=256debe0-9774-402a-a334-7abcdd16e610&download=1"
SRC2_URL = "https://tielt-winge.meetingburger.net/bekendmakingen/beleid/1f087466-09c8-49d6-868f-9c5ea4d4c418"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0216769660"
GAP = "gap_tw_fin_debt_8_52m_pension_2_82m_ocmw_tussen_1_50m_l5"
HIER = "Vlaanderen>Gemeenten>Tielt-Winge"

ASSETS = 57781052
ASSETS_2024 = 55451421
CASH = 11653082
CASH_2024 = 12659178
CURRENT = 15559482
FIXED = 42221570
FVA = 6395359
IGS = 6328482
OTHER_FVA = 66877
MVA = 34691285
LEASING = 1334830
IVA = 455754
LT_RECV = 679172
SCHULDEN = 14605435
EQUITY = 43175617
CAP_SUBS = 3104506
CUM_PNL = 22153087
OTHER_EQ = 17918024
FIN_DEBT = 8522986
FIN_DEBT_LT = 7381839
FIN_DEBT_ST = 1141147
FIN_DEBT_2024 = 9611910
NEW_LOANS = 38546
PENSION = 2818873
PENSION_2024 = 2694293
ST_PROV = 1147037
EXPL = 4738194
EXPL_ONTV = 23764587
EXPL_UITG = 19026393
INVEST = -4293771
INVEST_ONTV = 506596
INVEST_UITG = 4800367
BBR = -635996
AVAIL = 13439122
CUM_PREV = 14075118
AFM = 3662037
GECORR = 4020554
PNL = 3183633
PNL_CITY = 4683463
PNL_OCMW = -1499830
TUSSEN = 1499830
PERS = 10721110
FISCAL = 10571827
OV = 3527704
APB = 6154767
GEMFONDS = 3327869
POLITIE = 967949
HVZ = 550456
HVZ_INV = 108438
IGS_SUB = 63995
WERKSUB = 9475034
GOEDEREN = 5006250
TOELAGEN = 1725192
OCMW_HULP = 1229192
CITY_EXPL = 5933003
OCMW_EXPL = -1194809


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
assert abs((FVA + MVA + IVA + LT_RECV) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((CAP_SUBS + CUM_PNL + OTHER_EQ) - EQUITY) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((PNL_CITY + PNL_OCMW) - PNL) < 2
assert abs(PNL_OCMW + TUSSEN) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Tielt-Winge BBC jaarrekening 2025 (text PDF 116p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Tielt-Winge",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1289; 2.49MB text PDF; ModDate 03.03.2026; GR+RVMW 16.04.2026; "
                "KBO 0216.769.660 / 0216.769.759; assets 57.781m fin debt 8.523m "
                "pension 2.819m OCMW tussen 1.500m AFM +3.662m avail 13.439m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Tielt-Winge meetingburger bekendmaking JR2025 gemeente en OCMW",
            "url": SRC2_URL,
            "publisher": "Gemeente Tielt-Winge",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1289; JR2025 vaststelling GR+RVMW 16.04.2026; J2 avail 13.439m AFM +3.662m; "
                "no AGB; siblings Glabbeek city 1086 / AGB 1224 already mined; not redone"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Tielt-Winge 0216.769.660",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1289; Stad/gemeente since 01.01.1977; seat Kruisstraat 2 3390; 14 VE; "
                "AD Kurt Yskout since 02.01.2025; burgemeester Katrien Houtmeyers since 02.01.2025; "
                "NACE 84.114; OCMW sibling 0216.769.759; FD Katia Valvekens (BBC cover)"
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
            "name_nl": "Gemeente Tielt-Winge",
            "name_fr": "Commune de Tielt-Winge",
            "name_en": "Municipality of Tielt-Winge",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.tielt-winge.be",
            "foi_email": "secretariaat@tielt-winge.be",
            "foi_postal": "Kruisstraat 2 3390 Tielt-Winge",
            "notes": (
                "tick1289 JR2025 GE residual; KBO 0216.769.660 / OCMW 0216.769.759; NIS 24135; "
                "14 VE; no AGB; assets 57.781m fin debt 8.523m pension 2.819m "
                "OCMW tussen 1.500m AFM +3.662m avail 13.439m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Tielt-Winge",
            "name_fr": "CPAS Tielt-Winge",
            "name_en": "OCMW Tielt-Winge",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.tielt-winge.be",
            "foi_email": "secretariaat@tielt-winge.be",
            "foi_postal": "Kruisstraat 2 3390 Tielt-Winge",
            "notes": (
                "tick1289 JR2025 dual residual; KBO 0216.769.759; J5 PnL -1.500m FULL covered "
                "by city tussenkomst 1.500m; J3 expl -1.195m; equity 3.241m; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_tw_assets_2025", "2025", ASSETS, "J4 assets 57.781052m vs 55.451421m"),
    ("bud_tw_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 55.451421m"),
    ("bud_tw_cash_2025", "2025", CASH, "J4 cash 11.653082m DROP vs 12.659178m"),
    ("bud_tw_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 12.659178m"),
    ("bud_tw_fva_2025", "2025", FVA, "J4 FVA 6.395359m; EVA 0 + IGS 6.328482"),
    ("bud_tw_igs_2025", "2025", IGS, "J4 IGS FVA 6.328482m"),
    ("bud_tw_mva_2025", "2025", MVA, "J4 MVA 34.691285m; leasing 1.334830m Fluvius"),
    ("bud_tw_leasing_2025", "2025", LEASING, "J4 leasing MVA 1.334830m vs 1.394872m"),
    ("bud_tw_equity_2025", "2025", EQUITY, "J4 nettoactief 43.175617m vs 39.782133m"),
    ("bud_tw_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 8.522986m (LT 7.382 + ST due 1.141)"),
    ("bud_tw_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 9.611910m"),
    ("bud_tw_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.038546m Fluvius leasing"),
    ("bud_tw_pension_2025", "2025", PENSION, "J4 LT pension 2.818873m vs 2.694293m"),
    ("bud_tw_st_prov_2025", "2025", ST_PROV, "J4 ST voorzieningen 1.147037m"),
    ("bud_tw_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +4.738194m"),
    ("bud_tw_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 23.764587m"),
    ("bud_tw_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 19.026393m"),
    ("bud_tw_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +5.933003m (17.846/11.913)"),
    ("bud_tw_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -1.194809m (5.918/7.113)"),
    ("bud_tw_invest_2025", "2025", INVEST, "J2 invest -4.293771m (68pct vs MJP 7.054m)"),
    ("bud_tw_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar -0.635996m"),
    ("bud_tw_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 13.439122m"),
    ("bud_tw_afm_2025", "2025", AFM, "J2 AFM +3.662037m"),
    ("bud_tw_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +4.020554m"),
    ("bud_tw_pnl_2025", "2025", PNL, "J5 PnL +3.183633m (city +4.683 / OCMW -1.500)"),
    ("bud_tw_tussen_2025", "2025", TUSSEN, "mutatiestaat city->OCMW tussenkomst 1.499830m FULL"),
    ("bud_tw_pers_2025", "2025", PERS, "T2/J5 bezoldigingen 10.721110m"),
    ("bud_tw_fiscal_2025", "2025", FISCAL, "T2 fiscal 10.571827m (OV 3.528 + APB 6.155)"),
    ("bud_tw_ov_2025", "2025", OV, "T2 opcentiemen OV 3.527704m"),
    ("bud_tw_apb_2025", "2025", APB, "T2 aanvullende PB 6.154767m"),
    ("bud_tw_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 3.327869m"),
    ("bud_tw_politie_2025", "2025", POLITIE, "T2 politiezone 0.967949m JUMP vs 0.814958m"),
    ("bud_tw_hvz_2025", "2025", HVZ, "T2 HVZ 0.550456m"),
    ("bud_tw_hvz_inv_2025", "2025", HVZ_INV, "T2 HVZ investsub 0.108438m"),
    ("bud_tw_werksub_2025", "2025", WERKSUB, "T2 werkingssubsidies 9.475034m"),
    ("bud_tw_toelagen_2025", "2025", TOELAGEN, "T2 toegestane werksub 1.725192m"),
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
        "comm_tw_fin_debt_8_52m_2025",
        "Tielt-Winge YE2025 fin debt 8.523m",
        "8522986",
        "T4 8.522986m (LT 7.382 + ST due 1.141) declining vs 9.612m; new Fluvius lease 0.039m; aangewezen 0.769m",
        "Publish per-loan creditors + 2026-2031 amort FOI",
    ),
    (
        "comm_tw_pension_2_82m_2025",
        "Tielt-Winge YE2025 pension LT 2.819m",
        "2818873",
        "J4 LT pension 2.818873m vs 2.694293m; ST prov 1.147m; responsabilisering risk in toelichting",
        "Publish city/OCMW split + 2e pijler korting FOI",
    ),
    (
        "comm_tw_ocmw_tussen_1_50m_2025",
        "Tielt-Winge 2025 OCMW tussenkomst 1.500m FULL",
        "1499830",
        "Mutatiestaat city->OCMW 1.499830m covers OCMW J5 -1.499830m; J3 OCMW expl -1.195m; city PnL +4.683m",
        "Publish cash vs book transfer + 2026-2031 pad FOI",
    ),
    (
        "comm_tw_pers_10_72m_2025",
        "Tielt-Winge 2025 personeel 10.721m",
        "10721110",
        "T2/J5 10.721110m; niet-vast 7.516 + vast 2.314 + politiek 0.440; VTE unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_tw_politie_hvz_1_63m_2025",
        "Tielt-Winge 2025 politie+HVZ 1.627m",
        "1626843",
        "T2 politie 0.967949 JUMP vs 0.815 + HVZ 0.550 + HVZ invest 0.108; IGS 0.064",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_tw_igs_fva_6_33m_2025",
        "Tielt-Winge YE2025 IGS FVA 6.328m",
        "6328482",
        "J4 IGS 6.328482m EVA 0; Fluvius lease MVA 1.335m; J3 Fluvius afl overschrijding 5.380",
        "Publish IGS inventory + Fluvius lease schedule FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Tielt-Winge / OCMW-cliënten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Tielt-Winge GR+RVMW 16.04.2026",
            "decision_date": "2026-04-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Tielt-Winge (no AGB)",
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
        "lb_tw_fin_debt_8_52m_2025",
        "Tielt-Winge YE2025 fin debt 8.52m",
        "8522986",
        "6.5",
        "7.0",
        "Publish per-loan creditors + amort 2026-2031",
        "fin debt 8.523m declining vs 9.612m; new lease 0.039m",
    ),
    (
        "lb_tw_pension_2_82m_2025",
        "Tielt-Winge YE2025 pension LT 2.82m",
        "2818873",
        "6.5",
        "6.0",
        "Publish city/OCMW split + responsabilisering",
        "pension 2.819m vs 2.694m; ST prov 1.147m",
    ),
    (
        "lb_tw_ocmw_tussen_1_50m_2025",
        "Tielt-Winge 2025 OCMW tussenkomst 1.50m FULL",
        "1499830",
        "7.0",
        "6.5",
        "Publish cash vs book transfer + 2026-2031 pad",
        "tussen 1.500m covers OCMW PnL -1.500m; J3 expl -1.195m",
    ),
    (
        "lb_tw_pers_10_72m_2025",
        "Tielt-Winge 2025 personeel 10.72m",
        "10721110",
        "5.5",
        "7.0",
        "Publish paid VTE vs formatie",
        "pers 10.721m; VTE unpublished; city expl +5.933m",
    ),
    (
        "lb_tw_politie_hvz_1_63m_2025",
        "Tielt-Winge 2025 politie+HVZ 1.63m",
        "1626843",
        "6.0",
        "6.0",
        "Publish zone split + 2026-2031",
        "politie 0.968 JUMP + HVZ 0.550 + HVZ invest 0.108",
    ),
    (
        "lb_tw_igs_fva_6_33m_2025",
        "Tielt-Winge YE2025 IGS FVA 6.33m",
        "6328482",
        "5.5",
        "6.5",
        "Publish IGS inventory + Fluvius lease",
        "IGS 6.328m EVA 0; Fluvius lease 1.335m",
    ),
    (
        "lb_tw_avail_13_44m_2025",
        "Tielt-Winge YE2025 avail BBR 13.44m",
        "13439122",
        "5.0",
        "7.5",
        "Publish 1.4m uncommitted expl overschot vs 2.2m invest carry",
        "avail 13.439m; BBR year -0.636m; AFM +3.662m; cash 11.653m DROP",
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
            "beneficiaries": "Inwoners Tielt-Winge / OCMW-cliënten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Tielt-Winge (no AGB)",
            "measured_outcome": (
                "assets 57.781m / fin debt 8.523m / pension 2.819m / "
                "OCMW tussen 1.500m / AFM +3.662m / avail 13.439m"
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
                "T4 per-loan creditors for fin debt 8.522986m + Fluvius lease 0.038546m "
                "+ pension LT 2.818873 city/OCMW split + responsabilisering "
                "+ OCMW tussenkomst 1.499830m cash vs book + 2026-2031 pad "
                "+ paid VTE behind pers 10.721110m + politiezone/HVZ 1.626843m zone split "
                "+ IGS FVA 6.328482 inventory + Fluvius lease schedule"
            ),
            "why_it_matters": (
                "Unmined Tielt-Winge GE after residual dual hunt. No AGB. "
                "Fin debt 8.523m declining. OCMW dual 1.500m FULL cover. "
                "Pension 2.819m. Avail 13.439m with BBR year -0.636m. VTE unpublished."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Tielt-Winge (gemeente + OCMW)",
            "recipient_email": "secretariaat@tielt-winge.be",
            "recipient_postal": "Kruisstraat 2 3390 Tielt-Winge",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_tw_fin_debt_8_52m_2025",
            "linked_leaderboard_id": "lb_tw_fin_debt_8_52m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1289",
    "title": "Stad+OCMW Tielt-Winge JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Tielt-Winge JR2025 BBC text + KBO; "
        "KBO 0216.769.660 / 0216.769.759; assets 57.781m / fin debt 8.523m / "
        "pension 2.819m / OCMW tussen 1.500m / AFM +3.662m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T14:10:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1289 Stad+OCMW Tielt-Winge JR2025 GE residual; KBO 0216.769.660/0216.769.759; "
        "assets 57.781m fin debt 8.523m pension 2.819m AFM +3.662m gecorr +4.021m "
        "BBR -0.636m avail 13.439m cash 11.653m DROP OCMW tussen 1.500m FULL "
        "pers 10.721m politie 0.968m JUMP; no AGB; FOI ready not sent; "
        "next rq_1290 residual dual L5 VL + every-10"
    ),
}
rq_spawn = {
    "task_id": "rq_1290",
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
        "+ AGB SCO Ronse 1286 + Stad+OCMW Ronse 1287 + De Zilveren Zwaan 1288 "
        "+ Stad+OCMW Tielt-Winge 1289 done; "
        "tick 1290 is every-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md "
        "THEN one residual dual unit; "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Tielt-Winge 1289 / Zwaan 1288 / AGB Heist 1209 / city Heist 857; "
        "Steenokkerzeel city+OCMW JR2025 listed on city site only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden (0635.564.190) only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only / "
        "Oosterzele De Kluize unless a fetchable JR2025 PDF appears; skip AGSO Knokke-Heist already 1217; "
        "skip AGB Lokeren 1200; WAGSO already mined tick1199; skip Mobil-O/AG EOS inactive; "
        "skip Woonzorgnetwerk Edegem / Zorgbedrijf Brasschaat unpublished; "
        "skip Dilbeek/Wijnegem city GE already mined; skip Wingene/Genk/Brasschaat AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Cultuur Geel 1252; "
        "skip AGB Deinze 941 / AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224; "
        "ebesluit TLS + Leuven besluitvorming TLS + Roeselare.be Cloudflare + "
        "zorgbedrijfsinttruiden.be TLS unexpected-EOF — prefer org sites / NBB / "
        "city HTML; Brugge SAS / Blauwe Lelie / SPOOR / WOK only if they have a "
        "separate downloadable JR"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1289 after Stad+OCMW Tielt-Winge JR2025 GE residual; next residual dual L5 VL + every-10",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1289", rq_new, rq_spawn)
print("research_queue 1289", found, "spawned_1290", spawned)

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
            "last_unit_id": "rq_1289",
            "ticks_completed": "1289",
            "paused": "no",
            "notes": (
                "tick1289 Stad+OCMW Tielt-Winge JR2025 GE residual; KBO 0216.769.660/0216.769.759; "
                "assets 57.781m fin debt 8.523m pension 2.819m OCMW tussen 1.500m; "
                "FOI ready; next rq_1290 residual dual L5 VL + every-10; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1289_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
