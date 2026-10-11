# -*- coding: utf-8 -*-
"""Tick 1303 (research_queue patched surgically — last line + spawn only).
Stad+OCMW Edegem JR2025 GE residual."""
import csv
import io
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent
sys.path.insert(0, str(DATA))
from _tick1303_hdr import *  # noqa: F401,F403


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


def patch_entity_notes(path, entity_id, new_notes):
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines(keepends=True)
    header = lines[0]
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    found = False
    for i, line in enumerate(lines[1:], start=1):
        if not line.startswith(entity_id + ","):
            continue
        row = next(csv.DictReader([header, line], fieldnames=fields))
        # DictReader with fieldnames uses first data line; rebuild
        parsed = next(csv.reader([line.strip("\n").strip("\r")]))
        row = {fields[j]: (parsed[j] if j < len(parsed) else "") for j in range(len(fields))}
        row["notes"] = new_notes
        ending = "\n" if line.endswith("\n") else ""
        lines[i] = csv_line(fields, row) + ending
        found = True
        break
    if not found:
        raise SystemExit("entity %s not found" % entity_id)
    path.write_bytes("".join(lines).encode("utf-8"))
    return True


assert abs((CURRENT + FIXED) - ASSETS) <= 1
assert abs((EVA + IGS + OCMW_VER + OTHER_FVA) - FVA) <= 2
assert abs((EQUITY + SCHULDEN) - ASSETS) <= 1
assert abs((FIN_DEBT_LT + FIN_DEBT_ST) - FIN_DEBT) <= 1
assert abs((EXPL_ONTV - EXPL_UITG) - EXPL) <= 1
assert abs((INVEST_ONTV - INVEST_UITG) - INVEST) <= 1
assert abs((CITY_EXPL + OCMW_EXPL) - EXPL) <= 2
assert abs((CUM_PREV + BBR) - (AVAIL + 186667)) <= 2
assert abs((CAP_SUBS + CUM_PNL + REVAL + OTHER_EQ) - EQUITY) <= 2
assert abs((CITY_PNL + OCMW_PNL) - PNL) <= 1
print("asserts ok")

n = append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": SRC,
            "title": "Stad+OCMW Edegem BBC jaarrekening 2025 (official PDF)",
            "url": SRC_URL,
            "publisher": "Lokaal Bestuur Edegem",
            "accessed_date": "2026-08-17",
            "source_class": "budget",
            "notes": (
                "tick1303; BBC text PDF 245p / 9.9MB edegem.be; afdruk 27.05.2026; "
                "pub 23.06.2026; GR 22.06.2026; Jnl Budg 1033453 Alg 38398; "
                "KBO 0207.537.933/0212.248.074; assets 104.029m pension 23.405m "
                "politie Hekla 4.327m PnL -3.856m"
            ),
        },
        {
            "source_id": SRC2,
            "title": "KBO Gemeente Edegem 0207.537.933",
            "url": SRC2_URL,
            "publisher": "KBO Public Search FOD Economie",
            "accessed_date": "2026-08-17",
            "source_class": "official_register",
            "notes": (
                "tick1303; city KBO 0207.537.933 / OCMW 0212.248.074; "
                "seat Gemeenteplein 1 2650; NIS 11013; AD De Vries / FD Talloen / "
                "burgemeester Koen Metsu"
            ),
        },
    ],
)
print("sources", n)

patch_entity_notes(
    DATA / "entities.csv",
    ENT,
    (
        "tick1303 JR2025 GE residual after AGB 1239 stub; KBO 0207.537.933; NIS 11013; "
        "AD Tom De Vries / FD Joost Talloen / burgemeester Koen Metsu; "
        "assets 104.029m pension 23.405m JUMP politie Hekla 4.327m PnL -3.856m; "
        "has AGB BPGE (EVA 0.100m already 1239); FOI ready"
    ),
)
print("entities city patched")

n = append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": OCMW,
            "name_nl": "OCMW Edegem",
            "name_fr": "CPAS d'Edegem",
            "name_en": "OCMW Edegem",
            "level": "municipality",
            "parent_id": ENT,
            "community_language": "nl",
            "website": "https://www.edegem.be",
            "foi_email": "lokaalbestuur@edegem.be",
            "foi_postal": "Gemeenteplein 1 2650 Edegem",
            "notes": (
                "tick1303 JR2025 GE residual; KBO 0212.248.074; J3 expl -2.472m / "
                "T5 PnL -5.483m / cum -7.092m NEG / equity 0.065m thin; "
                "tussenkomst 2.140m; FOI ready"
            ),
        },
    ],
)
print("entities ocmw", n)

bud_rows = [
    ("bud_edgm_assets_2025", "2025", ASSETS, "J4 assets 104.029251m vs 100.463991m"),
    ("bud_edgm_assets_2024", "2024", ASSETS_2024, "J4 YE2024 assets 100.463991m"),
    ("bud_edgm_cash_2025", "2025", CASH, "J4 cash+beleg 7.853245m vs 6.670618m JUMP"),
    ("bud_edgm_cash_2024", "2024", CASH_2024, "J4 YE2024 cash+beleg 6.670618m"),
    ("bud_edgm_fva_2025", "2025", FVA, "T5 FVA 17.847217m; EVA 0.100m + IGS 10.977m + OCMW-ver 6.664m + other 0.106m"),
    ("bud_edgm_eva_2025", "2025", EVA, "T5 EVA AGB BPGE kapitaal 0.100m — AGB already mined 1239"),
    ("bud_edgm_igs_2025", "2025", IGS, "T5 IGS FVA 10.977131m; reval +0.154907m"),
    ("bud_edgm_mva_2025", "2025", MVA, "J4/T5 MVA 61.422802m; leasing 4.832513m"),
    ("bud_edgm_leasing_2025", "2025", LEASING, "T5 leasing MVA 4.832513m (aankoop 0.484m)"),
    ("bud_edgm_iva_2025", "2025", IVA, "J4/T5 IVA 1.258534m"),
    ("bud_edgm_equity_2025", "2025", EQUITY, "J4 nettoactief 58.055336m vs 62.088984m DROP"),
    ("bud_edgm_cum_pnl_2025", "2025", CUM_PNL, "J4/T5 cum PnL -0.204256m NEG (city 6.888 / OCMW -7.092)"),
    ("bud_edgm_reval_2025", "2025", REVAL, "J4 herwaarderingsreserves 3.235025m (IGS +0.155m)"),
    ("bud_edgm_fin_debt_2025", "2025", FIN_DEBT, "T4 fin debt 14.053312m (LT 12.063 + ST due 1.991) vs 15.595m"),
    ("bud_edgm_fin_debt_2024", "2024", FIN_DEBT_2024, "T4 YE2024 fin debt 15.595484m"),
    ("bud_edgm_fin_debt_lt_2025", "2025", FIN_DEBT_LT, "T4/J4 LT fin debt 12.062566m"),
    ("bud_edgm_fin_debt_st_2025", "2025", FIN_DEBT_ST, "T4/J4 ST due 1.990746m"),
    ("bud_edgm_new_loans_2025", "2025", NEW_LOANS, "T4 new loans 0.483598m leasing; no new bank"),
    ("bud_edgm_pension_2025", "2025", PENSION, "J4 pension LT 23.404909m JUMP vs 15.626316m"),
    ("bud_edgm_expl_2025", "2025", EXPL, "J2 exploitatiesaldo +6.649330m"),
    ("bud_edgm_expl_ontv_2025", "2025", EXPL_ONTV, "J2 expl ontv 42.249550m"),
    ("bud_edgm_expl_uitg_2025", "2025", EXPL_UITG, "J2 expl uitg 35.600220m"),
    ("bud_edgm_city_expl_2025", "2025", CITY_EXPL, "J3 city expl +9.121073m (ontv 36.971 / uitg 27.850)"),
    ("bud_edgm_ocmw_expl_2025", "2025", OCMW_EXPL, "J3 OCMW expl -2.471743m (ontv 5.278 / uitg 7.750)"),
    ("bud_edgm_invest_2025", "2025", INVEST, "J2 invest -3.184571m vs MJP -3.953m"),
    ("bud_edgm_bbr_2025", "2025", BBR, "J2 budgettair resultaat boekjaar +1.558287m"),
    ("bud_edgm_avail_2025", "2025", AVAIL, "J2 beschikbaar BBR 10.255957m"),
    ("bud_edgm_afm_2025", "2025", AFM, "J2 AFM +5.021666m"),
    ("bud_edgm_gecorr_2025", "2025", GECORR, "J2 gecorr AFM +5.799798m"),
    ("bud_edgm_pnl_2025", "2025", PNL, "J5 PnL -3.855597m; city +1.628 / OCMW -5.483; tussen 2.140m"),
    ("bud_edgm_tussen_2025", "2025", TUSSEN, "T5 tussenkomst gemeente-OCMW 2.140328m"),
    ("bud_edgm_pers_2025", "2025", PERS, "J5/T2 bezoldigingen 14.306146m; VTE unpublished"),
    ("bud_edgm_fiscal_2025", "2025", FISCAL, "J5/T2 fiscale 22.906928m (OV 7.338 + APB 11.768)"),
    ("bud_edgm_ov_2025", "2025", OV, "T2 OV 7.338303m"),
    ("bud_edgm_apb_2025", "2025", APB, "T2 APB 11.767746m JUMP vs 9.888m"),
    ("bud_edgm_gemfonds_2025", "2025", GEMFONDS, "T2 gemeentefonds 5.404569m"),
    ("bud_edgm_politie_2025", "2025", POLITIE, "T2 PZ Hekla 4.327462m JUMP vs 4.024m"),
    ("bud_edgm_hvz_2025", "2025", HVZ, "T2 HVZ Rand werk 0.873010m"),
    ("bud_edgm_ocmw_equity_2025", "2025", OCMW_EQUITY, "T5 OCMW equity 0.064789m thin (was 3.928m)"),
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
        "comm_edgm_pension_23_40m_2025",
        "Edegem YE2025 pension LT 23.405m JUMP",
        "23404909",
        "J4 pension LT 23.404909m vs 15.626316m; trial-balance respo 16.855m + pensioen 6.550m; voorzieningen JUMP 11.545m vs 2.209m",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031 FOI",
    ),
    (
        "comm_edgm_politie_4_33m_2025",
        "Edegem 2025 PZ Hekla 4.327m",
        "4327462",
        "T2 PZ Hekla 4.327462m JUMP vs 4.024040m; HVZ Rand 0.873010m",
        "Publish 2026-2031 verdeelsleutel FOI",
    ),
    (
        "comm_edgm_tussen_2_14m_2025",
        "Edegem YE2025 OCMW tussenkomst 2.140m",
        "2140328",
        "T5 tussenkomst 2.140328m; OCMW expl -2.472m / PnL -5.483m / equity 0.065m thin / cum -7.092m NEG",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031 FOI",
    ),
    (
        "comm_edgm_igs_10_98m_2025",
        "Edegem YE2025 IGS FVA 10.977m",
        "10977131",
        "T5 IGS 10.977131m; reval +0.154907m; EVA AGB BPGE 0.100m already 1239; OCMW-ver 6.664m",
        "Publish per-IGS aanschaf vs boekwaarde FOI",
    ),
    (
        "comm_edgm_fin_debt_14_05m_2025",
        "Edegem YE2025 fin debt 14.053m",
        "14053312",
        "T4 14.053312m (LT 12.063 + ST due 1.991) vs 15.595m; new loans 0.484m leasing; afl 2.026m",
        "Publish per-contract amort 2026-2031 FOI",
    ),
    (
        "comm_edgm_pers_14_31m_2025",
        "Edegem 2025 pers 14.306m / VTE unpublished",
        "14306146",
        "pers 14.306146m; VTE unpublished; politiek 0.657 / vast 5.589 / niet-vast 5.089 / onderwijs andere ov 2.446",
        "Publish paid VTE city vs OCMW FOI",
    ),
]
n = append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": ENT,
            "beneficiary": "Inwoners Edegem / OCMW / PZ Hekla / HVZ Rand",
            "legal_basis": "Decreet Lokaal Bestuur; BBC JR2025 Stad+OCMW Edegem vastgesteld 22.06.2026",
            "decision_date": "2026-06-22",
            "start_year": "2025",
            "end_year": "2031",
            "total_envelope_eur": env,
            "cash_by_year": "",
            "remaining_eur": env,
            "status": "active",
            "evaluation_url": SRC_URL,
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Edegem",
            "cut_option": cut,
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": HIER + ">jr2025_L5",
            "notes": note + f"; tick{TICK}; primary BBC",
        }
        for cid, title, env, note, cut in crows
    ],
)
print("commitments", n)

lb_rows = [
    (
        "lb_edgm_pension_23_40m_2025",
        "Edegem YE2025 pension LT 23.40m JUMP",
        "23404909",
        "8.5",
        "8.5",
        "Publish actuarial note + respo city/OCMW split + pad 2026-2031",
        "pension LT 23.405m vs 15.626m; respo 16.855 + pensioen 6.550; voorzieningen 11.545m",
    ),
    (
        "lb_edgm_politie_4_33m_2025",
        "Edegem 2025 PZ Hekla 4.33m",
        "4327462",
        "6.5",
        "6.5",
        "Publish 2026-2031 verdeelsleutel",
        "PZ Hekla 4.327m JUMP vs 4.024m; HVZ Rand 0.873m",
    ),
    (
        "lb_edgm_tussen_2_14m_2025",
        "Edegem YE2025 OCMW tussenkomst 2.14m",
        "2140328",
        "7.0",
        "6.5",
        "Publish cash vs resultaatstoewijzing + pad 2026-2031",
        "tussenkomst 2.140m; OCMW expl -2.472m / PnL -5.483m / equity 0.065m thin",
    ),
    (
        "lb_edgm_igs_10_98m_2025",
        "Edegem YE2025 IGS FVA 10.98m",
        "10977131",
        "5.5",
        "7.0",
        "Publish per-IGS aanschaf vs boekwaarde",
        "IGS 10.977m; reval +0.155m; EVA AGB 0.100m already 1239",
    ),
    (
        "lb_edgm_fin_debt_14_05m_2025",
        "Edegem YE2025 fin debt 14.05m",
        "14053312",
        "5.5",
        "6.0",
        "Publish per-contract amort 2026-2031",
        "fin debt 14.053m vs 15.595m; new loans 0.484m leasing; afl 2.026m",
    ),
    (
        "lb_edgm_pers_14_31m_vte_unpub_2025",
        "Edegem 2025 pers 14.31m / VTE unpublished",
        "14306146",
        "6.0",
        "7.0",
        "Publish paid VTE city vs OCMW",
        "pers 14.306m; VTE unpublished; onderwijs andere ov 2.446m",
    ),
    (
        "lb_edgm_pnl_neg_3_86m_2025",
        "Edegem YE2025 PnL -3.86m NEG",
        "3855597",
        "7.5",
        "7.0",
        "Publish provision/respo jump note + OCMW recovery pad",
        "PnL -3.856m (city +1.628 / OCMW -5.483); cum -0.204m NEG; equity DROP 4.034m",
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
            "beneficiaries": "Inwoners Edegem / OCMW / PZ Hekla / HVZ Rand",
            "stated_goal": "Local city+OCMW dual residual map VL JR2025 Edegem",
            "measured_outcome": (
                "assets 104.029m / pension 23.405m / politie 4.327m / "
                "PnL -3.856m / IGS 10.977m / AFM +5.022m / avail 10.256m"
            ),
            "absurdity_score": absu,
            "cost_score": cost,
            "difficulty": "3.0",
            "priority_index": "5.5",
            "cut_proposal": cut,
            "status": "active",
            "struck_reason": "",
            "notes": f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; city GE FOI",
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
                "J4 pension LT 23.404909m JUMP vs 15.626316m city/OCMW split + "
                "respo 16.855m / pensioen 6.550m + T4 per-contract creditors for "
                "fin debt 14.053312m (new loans 0.483598 leasing) + IGS FVA "
                "10.977131m inventory (reval +0.154907; EVA AGB 0.100 already 1239) "
                "+ OCMW tussenkomst 2.140328 vs expl -2.471743 / PnL -5.483428 / "
                "equity 0.064789 thin / cum -7.092110 NEG + VTE vs pers 14.306146 "
                "+ politiezone Hekla 4.327462 / HVZ Rand 0.873010 pad"
            ),
            "why_it_matters": (
                "Unmined leftover city+OCMW Edegem GE after AGB BPGE 1239 left the "
                "city package unmined. Official BBC PDF now downloads on edegem.be. "
                "Pension LT 23.405m JUMP. PZ Hekla 4.327m. PnL -3.856m from "
                "voorzieningen 11.545m. OCMW cum -7.092m NEG; tussen 2.140m. "
                "Fin debt 14.053m declining. Avail 10.256m with BBR year +1.558m."
            ),
            "priority": "8",
            "recipient_body": "Lokaal Bestuur Edegem (gemeente + OCMW)",
            "recipient_email": "lokaalbestuur@edegem.be",
            "recipient_postal": "Gemeenteplein 1 2650 Edegem",
            "draft_letter_path": "docs/doge/foi/drafts/gap_edgm_pension_23_40m_politie_4_33m_pnl_neg_3_86m_l5.md",
            "status": "ready",
            "date_ready": "2026-08-17",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "comm_edgm_pension_23_40m_2025",
            "linked_leaderboard_id": "lb_edgm_pension_23_40m_2025",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
        }
    ],
)
print("foi", n)

rq_new = {
    "task_id": "rq_1303",
    "title": "Stad+OCMW Edegem JR2025 GE residual",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "done",
    "hierarchy_target": "L5",
    "entity_id": ENT,
    "instructions": (
        "Completed: Stad+OCMW Edegem JR2025 BBC text + KBO; "
        "KBO 0207.537.933 / 0212.248.074; assets 104.029m / pension 23.405m / "
        "politie Hekla 4.327m / PnL -3.856m NEG / IGS 10.977m / AFM +5.022m; FOI ready"
    ),
    "blocked_gap_id": GAP,
    "created_utc": "2026-08-17T13:25:00Z",
    "updated_utc": UTC,
    "notes": (
        "tick1303 Stad+OCMW Edegem JR2025 GE residual; KBO 0207.537.933/0212.248.074; "
        "assets 104.029m pension 23.405m JUMP politie Hekla 4.327m PnL -3.856m NEG "
        "IGS 10.977m AFM +5.022m gecorr +5.800m BBR +1.558m avail 10.256m cash 7.853m "
        "JUMP tussen 2.140m pers 14.306m new loans 0.484m leasing; AGB BPGE already 1239; "
        "FOI ready not sent; next rq_1304 residual dual L5 VL"
    ),
}
rq_spawn = {
    "task_id": "rq_1304",
    "title": "Continuous FOI-adjacent public hole-fill batch",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "",
    "instructions": (
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
        "(prior 1255-1303 done including Stad+OCMW Edegem 1303 / Stad+OCMW Wommelgem 1302 / "
        "Stad+OCMW Zonhoven 1301 / Stad+OCMW Kortenaken 1300 / AGB Kortenaken 1299 / "
        "Stad+OCMW Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / Stad+OCMW Diepenbeek 1297 / "
        "AGB Diepenbeek 1296 / AGB Edegem 1239); "
        "prefer other unmined AGB/zorg/EVA with direct PDF/NBB/city HTML; "
        "skip already-mined city Edegem 1303 / AGB Edegem 1239 / city Wommelgem 1302 / "
        "city Zonhoven 1301 / city Kortenaken 1300 / AGB Kortenaken 1299 / "
        "city Steenokkerzeel 1298 / AGB Steenokkerzeel 1167 / city Diepenbeek 1297 / "
        "AGB Diepenbeek 1296 / Voeren 1295 / Heusden-Zolder 1294; "
        "leftover Maarkedal/Meulebeke still unmined — take only if PDF fetches; "
        "Londerzeel/Holsbeek/Merchtem/Pepingen/Zwalm/Wortegem-Petegem city+OCMW JR2025 only if PDF fetches; "
        "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
        "skip AGSO Knokke-Heist already 1217; skip AGB Lokeren 1200; skip EVA Gezinswelzijn 1253; "
        "skip Dilbeek/Wijnegem/Rotselaar city GE already mined; skip Wingene/Genk/Brasschaat/Haacht AGB; "
        "skip Zorgbedrijf Rivierenland already 1247; skip AGB Sport Geel 1175 / AGB Deinze 941 / "
        "AGB De Kouter Poperinge 1188 / AGB Glabbeek 1224 / AGB Oostkamp 1131; "
        "skip Kuurne city already 957; skip Ternat/Lubbeek already mined; "
        "skip AGB Kapellen / Nieuwerkerken 1102 already mined; "
        "skip AGB Sport Hulshout JR2024-only; "
        "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS unexpected-EOF"
    ),
    "blocked_gap_id": "",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "spawned tick1303 after Stad+OCMW Edegem JR2025 GE residual; next residual dual L5 VL",
}
found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1303", rq_new, rq_spawn)
print("research_queue 1303", found, "spawned_1304", spawned)

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
            "last_unit_id": "rq_1303",
            "ticks_completed": "1303",
            "paused": "no",
            "notes": (
                "tick1303 Stad+OCMW Edegem JR2025 GE residual; KBO 0207.537.933/0212.248.074; "
                "assets 104.029m pension 23.405m politie Hekla 4.327m PnL -3.856m; "
                "FOI ready; next rq_1304 residual dual L5 VL; continuous hole_fill"
            ),
        }
    )
print("loop_state ok")

log = ROOT / "loop_log.md"
entry = (DATA / "_tick1303_log.md").read_text(encoding="utf-8")
if not entry.startswith("\n"):
    entry = "\n" + entry
with log.open("a", encoding="utf-8") as f:
    f.write(entry)
print("loop_log ok")
