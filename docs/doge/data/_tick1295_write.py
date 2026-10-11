# -*- coding: utf-8 -*-
"""Tick 1295 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Voeren JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ROOT = DATA.parent
UTC = "2026-08-17T12:25:00Z"
TICK = 1295
SRC = "src_voeren_jr2025_bbc"
SRC2 = "src_voeren_jr2025_gr"
SRC3 = "src_kbo_voeren_0216773422"
ENT = "city_voeren"
OCMW = "ocmw_voeren"
SRC_URL = "https://www.voeren.be/upload/pdf/Rapport-jaarrekening-en-toelichting-2025.pdf"
SRC2_URL = "https://www.voeren.be/upload/pdf/Notulen-Gemeenteraad-28-mei-2026.pdf"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0216773422"
GAP = "gap_voeren_fin_debt_3_37m_pension_2_78m_ocmw_equity_neg_2_05m_l5"
HIER = "Vlaanderen>Gemeenten>Voeren"

ASSETS = 28310999
ASSETS_2024 = 26577419
CASH = 7701187
CASH_2024 = 6731669
CURRENT = 8552869
FIXED = 19758130
FVA = 4814179
IGS = 4788371
OTHER_FVA = 25809
EVA = 0
MVA = 14532925
LEASING = 490217
IVA = 411026
SCHULDEN = 8079622
EQUITY = 20231377
CAP_SUBS = 3625393
CUM_PNL = 5432607
REVAL = 208445
OTHER_EQ = 10964932
FIN_DEBT = 3366939
FIN_DEBT_LT = 3046756
FIN_DEBT_ST = 320182
FIN_DEBT_2024 = 3533150
NEW_LOANS = 145710
BANK_REMAIN = 2876721
PENSION = 2779274
PENSION_2024 = 2694949
EXPL = 2160011
EXPL_ONTV = 8454846
EXPL_UITG = 6294835
CITY_EXPL = 2620537
OCMW_EXPL = -460526
INVEST = -803636
INVEST_UITG = 1701105
BBR = 1190163
CUM_PREV = 5582065
AVAIL = 6772228
AFM = 1848089
GECORR = 1877359
AFL = 311922
PNL = 2044019
CITY_PNL = 2529273
OCMW_PNL = -485254
TUSSEN = 0
PERS = 3365389
FISCAL = 4342276
OV = 1677677
APB = 1761761
GEMFONDS = 2253918
POLITIE = 303826
HVZ = 178894
OCMW_EQUITY = -2049170
OCMW_CUM = -2320423
FLUVIUS_DIV = 53409


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
assert abs((IGS + OTHER_FVA + EVA) - FVA) < 2
assert abs((FVA + MVA + IVA) - FIXED) < 2
assert abs((EQUITY + SCHULDEN) - ASSETS) < 2
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) < 2
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) < 2
assert abs((CUM_PREV + BBR) - AVAIL) < 2
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) < 2
assert abs((CITY_PNL + OCMW_PNL) - PNL) < 2
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Voeren BBC jaarrekening 2025 (PDF 91p)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Voeren",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1295; 2.33MB BBC PDF voeren.be; GR 28.05.2026; "
                "KBO 0216.773.422 / 0216.773.521; assets 28.311m fin debt 3.367m "
                "pension 2.779m OCMW equity -2.049m NEG AFM +1.848m avail 6.772m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "Voeren GR 28.05.2026 vaststelling JR2025",
            "url": SRC2_URL,
            "publisher": "Gemeente Voeren",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1295; JR2025 vaststelling GR 28.05.2026; BBR avail 6.772m AFM 1.848m; "
                "no AGB; siblings HH 1285 / Lummen 1095 already mined"
            ),
        },
        {
            "source_id": SRC3,
            "title": "KBO Gemeente Voeren 0216.773.422",
            "url": SRC3_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1295; Stad/gemeente since 01.01.1977; seat Gemeenteplein 1 3798; 3 VE; "
                "burgemeester Joris Gaens since 01.01.2020; NACE 84.114; "
                "OCMW sibling 0216.773.521 (1 VE; voorzitter Hilde Broers since 01.01.2020); "
                "AD Kimberly Peeters / FD Hanne Muermans (BBC cover)"
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
            "name_nl": "Gemeente Voeren",
            "name_fr": "Commune de Fourons",
            "name_en": "Municipality of Voeren",
            "level": "municipality",
            "parent_id": "vlaanderen_gov",
            "community_language": "nl",
            "website": "https://www.voeren.be",
            "foi_email": "info@devoor.be",
            "foi_postal": "Gemeenteplein 1 3798 Voeren",
            "notes": (
                "tick1295 JR2025 GE residual; KBO 0216.773.422 / OCMW 0216.773.521; NIS 73109; "
                "3+1 VE; no AGB; assets 28.311m fin debt 3.367m pension 2.779m "
                "OCMW equity -2.049m NEG AFM +1.848m avail 6.772m; FOI ready"
            ),
        },
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Voeren",
            "name_fr": "CPAS Fourons",
            "name_en": "OCMW Voeren",
            "level": "ocmw",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.voeren.be",
            "foi_email": "info.ocmw@devoor.be",
            "foi_postal": "Gemeenteplein 1 3798 Voeren",
            "notes": (
                "tick1295 JR2025 dual residual; KBO 0216.773.521; J3 expl -0.461m; "
                "T5 tussenkomst 0; T5 cum PnL -2.320m NEG equity -2.049m NEG; FOI ready"
            ),
        },
    ],
)
print("entities", n)

bud_rows = [
    ("bud_voeren_assets_2025", "2025", ASSETS, "J4 assets 28.310999m vs 26.577419m"),
    ("bud_voeren_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 26.577419m"),
    ("bud_voeren_cash_2025", "2025", CASH, "J4 cash 7.701187m vs 6.731669m"),
    ("bud_voeren_cash_2024", "2024", CASH_2024, "J4 YE2024 cash 6.731669m"),
    ("bud_voeren_fva_2025", "2025", FVA, "J4/T5 FVA 4.814179m; EVA 0 + IGS 4.788371"),
    ("bud_voeren_igs_2025", "2025", IGS, "J4/T5 IGS FVA 4.788371m"),
    ("bud_voeren_mva_2025", "2025", MVA, "J4 MVA 14.532925m; leasing 0.490217m"),
    ("bud_voeren_leasing_2025", "2025", LEASING, "T5 leasing MVA 0.490217m vs 0.381631m"),
    ("bud_voeren_equity_2025", "2025", EQUITY, "J4 nettoactief 20.231377m vs 18.299509m"),
    ("bud_voeren_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 3.366939m (LT 3.047 + ST due 0.320)"),
    ("bud_voeren_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 3.533150m"),
    ("bud_voeren_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.145710m (Fluvius leasing; bank 0)"),
    ("bud_voeren_bank_remain_2025", "2025", BANK_REMAIN, "risico 6 bank credits remaining 2.876721m"),
    ("bud_voeren_pension_2025", "2025", PENSION, "J4 LT pension 2.779274m vs 2.694949m"),
    ("bud_voeren_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +2.160011m"),
    ("bud_voeren_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 8.454846m"),
    ("bud_voeren_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 6.294835m"),
    ("bud_voeren_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +2.620537m (7.914/5.293)"),
    ("bud_voeren_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -0.460526m (0.541/1.002)"),
    ("bud_voeren_invest_2025", "2025", INVEST, "J2 invest -0.803636m vs MJP -2.678m"),
    ("bud_voeren_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +1.190163m"),
    ("bud_voeren_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 6.772228m"),
    ("bud_voeren_afm_2025", "2025", AFM, "J2 AFM +1.848089m"),
    ("bud_voeren_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +1.877359m"),
    ("bud_voeren_pnl_2025", "2025", PNL, "J5 PnL +2.044019m (city +2.529 / OCMW -0.485)"),
    ("bud_voeren_tussen_2025", "2025", TUSSEN, "T5 city->OCMW tussenkomst 0"),
    ("bud_voeren_pers_2025", "2025", PERS, "J5 bezoldigingen 3.365389m / formatie 42.04"),
    ("bud_voeren_fiscal_2025", "2025", FISCAL, "J5/T2 fiscal 4.342276m"),
    ("bud_voeren_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 2.253918m"),
    ("bud_voeren_politie_2025", "2025", POLITIE, "T2 politiezone Voeren 0.303826m JUMP vs 0.172m"),
    ("bud_voeren_hvz_2025", "2025", HVZ, "T2 HVZ Oost-Limburg 0.178894m"),
    ("bud_voeren_afl_2025", "2025", AFL, "T4 periodieke aflossingen 0.311922m"),
    ("bud_voeren_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity -2.049170m NEG"),
    ("bud_voeren_ocmw_cum_2025", "2025", OCMW_CUM, "T5 OCMW cum PnL -2.320423m NEG"),
    ("bud_voeren_fluvius_div_2025", "2025", FLUVIUS_DIV, "T2/toelichting Fluvius dividend 0.053409m"),
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
        "comm_voeren_fin_debt_3_37m_2025",
        "Voeren YE2025 fin debt 3.367m",
        "3366939",
        "T4 3.366939m (LT 3.047 + ST due 0.320) declining vs 3.533m; new loans 0.146m Fluvius leasing; bank remaining 2.877m (6 credits)",
        "Publish per-loan amort 2026-2031 + Fluvius lease FOI",
    ),
    (
        "comm_voeren_pension_2_78m_2025",
        "Voeren YE2025 LT pension 2.779m",
        "2779274",
        "J4 LT pension 2.779274m vs 2.694949m; T2 pension cost 0.153m; city/OCMW split unpublished",
        "Publish pension composition + 2026-2031 pad FOI",
    ),
    (
        "comm_voeren_ocmw_equity_neg_2_05m_2025",
        "Voeren YE2025 OCMW equity -2.049m NEG",
        "2049170",
        "T5 OCMW equity -2.049170m NEG; cum PnL -2.320423m NEG; tussenkomst 0 vs J3 expl -0.461m",
        "Publish why tussenkomst 0 + 2026-2031 pad FOI",
    ),
    (
        "comm_voeren_pers_3_37m_2025",
        "Voeren 2025 personeel 3.365m",
        "3365389",
        "J5 3.365389m; formatie 42.04 (city 33.81 / OCMW 8.23); paid VTE unpublished",
        "Publish paid VTE vs formatie city/OCMW FOI",
    ),
    (
        "comm_voeren_politie_hvz_0_48m_2025",
        "Voeren 2025 politie+HVZ 0.483m",
        "482720",
        "T2 politiezone Voeren 0.304 JUMP vs 0.172 + HVZ Oost-Limburg 0.179; own-zone + 2026 VVTM associatie",
        "Publish zone split + 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_voeren_avail_6_77m_2025",
        "Voeren YE2025 avail BBR 6.772m",
        "6772228",
        "avail 6.772m; BBR year +1.190m; AFM +1.848m; cash 7.701m; invest underspend vs MJP 4.074m",
        "Publish uncommitted expl overschot vs invest carry FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Voeren / OCMW-clienten / politie-HVZ",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Voeren GR 28.05.2026",
            "decision_date": "2026-05-28",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": "",
            "status": "open",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local GE dual residual map VL JR2025 Voeren (no AGB)",
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
        "lb_voeren_fin_debt_3_37m_2025",
        "Voeren YE2025 fin debt 3.37m",
        "3366939",
        "6.0",
        "6.5",
        "Publish per-loan amort 2026-2031 + Fluvius lease",
        "fin debt 3.367m declining vs 3.533m; new loans 0.146m Fluvius leasing",
    ),
    (
        "lb_voeren_pension_2_78m_2025",
        "Voeren YE2025 LT pension 2.78m",
        "2779274",
        "6.5",
        "6.0",
        "Publish pension composition + 2026-2031 pad",
        "LT pension 2.779m vs 2.695m; T2 cost 0.153m",
    ),
    (
        "lb_voeren_ocmw_equity_neg_2_05m_2025",
        "Voeren YE2025 OCMW equity -2.05m NEG",
        "2049170",
        "8.0",
        "5.5",
        "Publish why tussenkomst 0 + 2026-2031 pad",
        "OCMW equity -2.049m NEG; cum -2.320m NEG; tussen 0 vs expl -0.461m",
    ),
    (
        "lb_voeren_pers_3_37m_2025",
        "Voeren 2025 personeel 3.37m / formatie 42 VTE",
        "3365389",
        "5.0",
        "6.0",
        "Publish paid VTE vs formatie city/OCMW",
        "pers 3.365m; formatie 42.04 (city 33.81 / OCMW 8.23)",
    ),
    (
        "lb_voeren_politie_hvz_0_48m_2025",
        "Voeren 2025 politie+HVZ 0.48m",
        "482720",
        "6.5",
        "5.0",
        "Publish zone split + 2026-2031 VVTM",
        "politiezone Voeren 0.304 JUMP vs 0.172 + HVZ Oost-Limburg 0.179",
    ),
    (
        "lb_voeren_avail_6_77m_2025",
        "Voeren YE2025 avail BBR 6.77m",
        "6772228",
        "5.5",
        "7.0",
        "Publish uncommitted expl overschot vs invest carry",
        "avail 6.772m; BBR year +1.190m; AFM +1.848m; cash 7.701m",
    ),
    (
        "lb_voeren_igs_4_79m_2025",
        "Voeren YE2025 IGS FVA 4.79m",
        "4788371",
        "5.5",
        "6.0",
        "Publish IGS inventory + Fluvius 2026 reval",
        "IGS 4.788m; Fluvius share change letter 3.04.2026 deferred to 2026; div 0.053m",
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
            "beneficiaries": "Inwoners Voeren / OCMW-clienten / politie-HVZ",
            "stated_goal": "Local GE dual residual map VL JR2025 Voeren (no AGB)",
            "measured_outcome": (
                "assets 28.311m / fin debt 3.367m / pension 2.779m / "
                "OCMW equity -2.049m NEG / AFM +1.848m / avail 6.772m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.5",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; OCMW dual FOI",
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
                "T4/LT-S per-loan creditors for fin debt 3.366939m + new loans 0.145710 "
                "(Fluvius leasing; bank remaining 2.876721) + LT pension 2.779274 composition "
                "+ OCMW tussenkomst 0 vs expl -0.460526 + OCMW equity -2.049170 NEG / "
                "cum -2.320423 NEG + 2026-2031 pad + IGS FVA 4.788371 inventory + "
                "Fluvius 3.04.2026 share-change letter deferred to 2026 + EVA 0 confirm "
                "+ paid VTE vs formatie 42.04 / pers 3.365389 + politiezone/HVZ 0.482720 "
                "2026-2031 verdeelsleutel + VVTM associatie"
            ),
            "why_it_matters": (
                "Unmined Voeren GE after residual dual hunt. No AGB. "
                "Fin debt 3.367m declining; new loans 0.146m Fluvius leasing only. "
                "OCMW dual tussen 0 vs expl -0.461m / equity -2.049m NEG. "
                "Avail 6.772m with BBR year +1.190m. Politie JUMP 0.304 vs 0.172."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Voeren (gemeente + OCMW)",
            "recipient_email": "info@devoor.be",
            "recipient_postal": "Gemeenteplein 1 3798 Voeren",
            "draft_letter_path": "docs/doge/foi/drafts/gap_voeren_fin_debt_3_37m_pension_2_78m_ocmw_equity_neg_2_05m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_voeren_fin_debt_3_37m_2025",
            "linked_leaderboard_id": "lb_voeren_fin_debt_3_37m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1295",
    "title": "Stad+OCMW Voeren JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Voeren JR2025 BBC text + KBO; "
        "KBO 0216.773.422 / 0216.773.521; assets 28.311m / fin debt 3.367m / "
        "pension 2.779m / OCMW equity -2.049m NEG / AFM +1.848m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T12:10:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1295 Stad+OCMW Voeren JR2025 GE residual; KBO 0216.773.422/0216.773.521; "
        "assets 28.311m fin debt 3.367m pension 2.779m AFM +1.848m gecorr +1.877m "
        "BBR +1.190m avail 6.772m cash 7.701m OCMW equity -2.049m NEG tussen 0 "
        "pers 3.365m formatie 42.04 politie 0.304m JUMP new loans 0.146m Fluvius; "
        "no AGB; FOI ready not sent; next rq_1296 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1296",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1295 done including Stad+OCMW Voeren 1295); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined Voeren 1295 / Heusden-Zolder 1294 / Oud-Heverlee 1293 / "
        "Huldenberg 1292 / Kapelle-op-den-Bos 1291 / Bekkevoort 1290 / Tielt-Winge 1289 / "
        "Zwaan 1288 / Houthalen-Helchteren 1285 / AGB Heist 1209 / city Heist 857; "
        "Londerzeel/Holsbeek/Merchtem/Steenokkerzeel/Pepingen/Zwalm/Wortegem-Petegem "
        "city+OCMW JR2025 only if PDF fetches; "
        "AGB Steenokkerzeel already 1167; AGB PATRI Sint-Truiden only if JR2025 downloadable; "
        "skip Motena / Trupark / Bau-huis / Maaseik / Diepenbeek / Zorgbedrijf ST / Bornem JR2024-only; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Beleko 1215; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1295 after Stad+OCMW Voeren JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1295", rq_new, rq_spawn)
print("research_queue 1295", found, "spawned_1296", spawned)

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
            "last_unit_id": "rq_1295",
            "ticks_completed": "1295",
            "paused": "no",
            "notes": (
                "tick1295 Stad+OCMW Voeren JR2025 GE residual; KBO 0216.773.422/0216.773.521; "
                "assets 28.311m fin debt 3.367m pension 2.779m OCMW equity -2.049m NEG; "
                "FOI ready; next rq_1296 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1295_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
