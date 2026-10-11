# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ENT="city_diepenbeek"
SRC="src_diepbk_jr2025_bbc"
SRC_URL="https://www.diepenbeek.be/file_uploads/42819.pdf?sc=F808981DD9F273563DAD49F3E75B762A"
HIER="Vlaanderen>Gemeenten>Diepenbeek"
UTC="2026-08-17T12:50:00Z"
TICK=1297
GAP="gap_diepbk_fin_debt_13_59m_igs_reval_19_43m_ocmw_equity_neg_0_71m_l5"

def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing = {row.get(fields[0]) for row in reader}
    added=0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(fields[0]) in existing:
                continue
            w.writerow({k: row.get(k,"") for k in fields})
            added += 1
    return added

crows = [
    ("comm_diepbk_fin_debt_13_59m_2025","Diepenbeek YE2025 fin debt 13.592m","13592179","T4 13.592179m (LT 11.712 + ST due 1.850 + ST 0.030) declining vs 14.916m; new loans 0.577m leasing; no new bank loans; afl 1.931m","Publish per-loan amort 2026-2031 FOI"),
    ("comm_diepbk_igs_reval_19_43m_2025","Diepenbeek YE2025 IGS reval 19.425m","19425066","T5 IGS 45.774m vs 26.349m; herwaardering +19.425m no cash; EVA AGBD 7.010m frozen","Publish per-IGS aanschaf vs herwaardering FOI"),
    ("comm_diepbk_ocmw_equity_neg_0_71m_2025","Diepenbeek YE2025 OCMW equity -0.708m NEG","708459","T5 OCMW equity -0.708m NEG / cum PnL -7.385m NEG; J3 expl -1.554m; tussenkomst 0","Publish tussenkomst pad 2026-2031 FOI"),
    ("comm_diepbk_pension_3_09m_2025","Diepenbeek YE2025 pension LT 3.093m","3093433","J4 LT pension 3.093m declining vs 3.293m; T2 pensioenkost 0.197m","Publish city vs OCMW pension split FOI"),
    ("comm_diepbk_avail_21_86m_2025","Diepenbeek YE2025 avail BBR 21.858m","21858004","avail 21.858m; BBR year +0.364m; AFM +5.047m; cash 25.047m; onbeschikbaar 3.359m (2e pijler + Boost BOA)","Publish uncommitted overschot vs onbeschikbaar lock FOI"),
    ("comm_diepbk_agb_werksub_0_70m_2025","Diepenbeek 2025 city AGB werksub 0.699m","698706","T2 city werksub aan AGB 0.699m vs AGBD JR2025 algemene 0.385m (tick 1296); dual lock","Publish 2026-2031 beheersovereenkomst + reconciliatie FOI"),
]
n=append_rows(DATA/"commitments.csv", [{
    "commitment_id":cid,"title":title,"entity_id":ENT,"beneficiary":"Inwoners Diepenbeek / OCMW / AGBD",
    "legal_basis":"Decreet Lokaal Bestuur; BBC JR2025 Diepenbeek GR 22.06.2026","decision_date":"2026-06-22",
    "start_year":"2025","end_year":"2025","total_envelope_eur":env,"cash_by_year":"","remaining_eur":"",
    "status":"open","evaluation_url":SRC_URL,"stated_goal":"Local city+OCMW dual residual map VL JR2025 Diepenbeek",
    "cut_option":cut,"source_id":SRC,"confidence":"strong","hierarchy_path":HIER+">jr2025_L5","notes":note+f"; tick{TICK}",
} for cid,title,env,note,cut in crows])
print("commitments", n)

lb_rows = [
    ("lb_diepbk_fin_debt_13_59m_2025","Diepenbeek YE2025 fin debt 13.59m","13592179","6.0","7.0","Publish per-loan amort 2026-2031","fin debt 13.592m declining vs 14.916m; new loans 0.577m leasing only"),
    ("lb_diepbk_igs_reval_19_43m_2025","Diepenbeek YE2025 IGS reval 19.43m no cash","19425066","5.5","7.5","Publish per-IGS aanschaf vs herwaardering","IGS 45.774m; reval +19.425m no cash; EVA AGBD 7.010m frozen"),
    ("lb_diepbk_ocmw_equity_neg_0_71m_2025","Diepenbeek YE2025 OCMW equity -0.71m NEG","708459","7.0","5.5","Publish tussenkomst pad 2026-2031","OCMW equity -0.708m NEG / cum -7.385m; expl -1.554m; tussen 0"),
    ("lb_diepbk_pension_3_09m_2025","Diepenbeek YE2025 pension LT 3.09m","3093433","6.0","6.0","Publish city vs OCMW pension split","pension 3.093m declining vs 3.293m; T2 kost 0.197m"),
    ("lb_diepbk_avail_21_86m_2025","Diepenbeek YE2025 avail BBR 21.86m","21858004","5.0","7.5","Publish uncommitted overschot vs 2e pijler/BOA lock","avail 21.858m; BBR +0.364m; AFM +5.047m; cash 25.047m"),
    ("lb_diepbk_agb_werksub_0_70m_2025","Diepenbeek 2025 city AGB werksub 0.70m dual","698706","6.5","5.5","Publish beheersovereenkomst + reconciliatie vs AGBD 0.385m","city T2 0.699m vs AGBD algemene 0.385m tick1296"),
    ("lb_diepbk_pers_24_85m_vte_unpub_2025","Diepenbeek 2025 pers 24.85m / VTE unpublished","24853856","6.0","7.0","Publish paid VTE city vs OCMW","pers 24.854m; VTE unpublished; onderwijs andere ov 2.505m"),
]
n=append_rows(DATA/"leaderboard.csv", [{
    "item_id":iid,"name":name,"level":"L5","type":"local_budget_line","hierarchy_path":HIER+">jr2025_L5",
    "annual_cost_eur":amt,"total_cost_eur":amt,"tco_notes":tco,"confidence":"strong","source_id":SRC,
    "beneficiaries":"Inwoners Diepenbeek / OCMW / AGBD","stated_goal":"Local city+OCMW dual residual map VL JR2025 Diepenbeek",
    "measured_outcome":"assets 190.496m / fin debt 13.592m / IGS reval 19.425m / OCMW equity -0.708m NEG / AFM +5.047m / avail 21.858m",
    "absurdity_score":absu,"cost_score":cost,"difficulty":"3.0","priority_index":"5.5","cut_proposal":cut,
    "status":"active","struck_reason":"","notes":f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; city GE FOI",
} for iid,name,amt,absu,cost,cut,tco in lb_rows])
print("leaderboard", n)

n=append_rows(DATA/"foi_queue.csv", [{
    "gap_id":GAP,"hierarchy_path":HIER+">jr2025_L5","entity_id":ENT,
    "what_is_missing":"T4/LT-S per-loan creditors for fin debt 13.592179m (new loans 0.576680 leasing only; no new bank loans) + IGS FVA 45.774081 inventory (reval +19.425066 no cash) + OCMW tussenkomst 0 vs expl -1.554171 / equity -0.708459 NEG / cum -7.385064 + VTE vs pers 24.853856 + AGB dual lock city T2 0.698706 vs AGBD 0.384720 + politiezone LRH 2.765711 / HVZ 0.952387 pad",
    "why_it_matters":"Unmined city+OCMW Diepenbeek GE after AGB 1296 left this live PDF. Has AGB (EVA 7.010m). Fin debt 13.592m declining; new loans 0.577m leasing. IGS reval 19.425m no cash. OCMW equity -0.708m NEG; tussen 0. Avail 21.858m with BBR year +0.364m.",
    "priority":"8","recipient_body":"Lokaal Bestuur Diepenbeek (gemeente + OCMW)","recipient_email":"info@diepenbeek.be",
    "recipient_postal":"Dorpsstraat 14 3590 Diepenbeek",
    "draft_letter_path":"docs/doge/foi/drafts/gap_diepbk_fin_debt_13_59m_igs_reval_19_43m_ocmw_equity_neg_0_71m_l5.md",
    "status":"ready","date_ready":"2026-08-17","date_sent":"","date_due":"","date_answered":"","response_summary":"",
    "linked_commitment_id":"comm_diepbk_fin_debt_13_59m_2025","linked_leaderboard_id":"lb_diepbk_fin_debt_13_59m_2025",
    "created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
}])
print("foi", n)
