# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ENT="city_steenokkerzeel"
SRC="src_stnok_jr2025_bbc"
SRC_URL="https://steenokkerzeel-echo.cipalschaubroeck.be/raadpleegomgeving/document/a0726846-bd39-4a94-8ef7-fc64cde7ffa8"
HIER="Vlaanderen>Gemeenten>Steenokkerzeel"
UTC="2026-08-17T13:20:00Z"
TICK=1298
GAP="gap_stnok_fin_debt_2_49m_igs_reval_9_51m_afm_neg_0_05m_l5"

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
    ("comm_stnok_fin_debt_2_49m_2025","Steenokkerzeel YE2025 fin debt 2.492m","2491751","T4 2.491751m (LT 1.649 + ST due 0.843) declining vs 3.530m; new loans 0.174m leasing; no new bank loans; afl 1.212m","Publish per-loan amort 2026-2031 FOI"),
    ("comm_stnok_igs_reval_9_51m_2025","Steenokkerzeel YE2025 IGS reval 9.510m","9510058","T5 IGS 18.370m vs 8.860m; herwaardering +9.510m no cash; EVA 0 on city books (AGB already 1167)","Publish per-IGS aanschaf vs herwaardering FOI"),
    ("comm_stnok_ocmw_tussen_1_19m_2025","Steenokkerzeel 2025 OCMW tussenkomst 1.195m","1194900","Tussenkomst 1.194900m (neg avail -1.189 + interne fact -0.006); J3 expl -1.168m / T5 cum PnL -1.428m NEG / equity 0.039m","Publish tussenkomst pad 2026-2031 FOI"),
    ("comm_stnok_pension_2_59m_2025","Steenokkerzeel YE2025 pension LT 2.587m","2587398","J4 LT pension 2.587m vs 6.095m; TAK26 herbelegging 1.027m; respo takeback 3.240m + pension takeback 0.535m","Publish city vs OCMW pension split FOI"),
    ("comm_stnok_avail_9_98m_afm_neg_2025","Steenokkerzeel YE2025 avail 9.977m / AFM -0.051m","9976574","avail 9.977m; BBR year -4.688m; AFM -0.051m (TAK26 1.027m); gecorr +0.878m; cash 8.647m DROP vs 12.885m","Publish uncommitted overschot vs TAK26/onbeschikbaar lock FOI"),
    ("comm_stnok_agb_werksub_0_26m_2025","Steenokkerzeel 2025 city AGB werksub 0.259m","259001","T2 city werksub aan AGB 0.259m vs AGB JR2025 prijssub 0.244m (tick 1167); dual lock; T5 EVA 0","Publish 2026-2031 beheersovereenkomst + reconciliatie FOI"),
]
n=append_rows(DATA/"commitments.csv", [{
    "commitment_id":cid,"title":title,"entity_id":ENT,"beneficiary":"Inwoners Steenokkerzeel / OCMW / AGB",
    "legal_basis":"Decreet Lokaal Bestuur; BBC JR2025 Steenokkerzeel GR 18.06.2026","decision_date":"2026-06-18",
    "start_year":"2025","end_year":"2025","total_envelope_eur":env,"cash_by_year":"","remaining_eur":"",
    "status":"open","evaluation_url":SRC_URL,"stated_goal":"Local city+OCMW dual residual map VL JR2025 Steenokkerzeel",
    "cut_option":cut,"source_id":SRC,"confidence":"strong","hierarchy_path":HIER+">jr2025_L5","notes":note+f"; tick{TICK}",
} for cid,title,env,note,cut in crows])
print("commitments", n)

lb_rows = [
    ("lb_stnok_fin_debt_2_49m_2025","Steenokkerzeel YE2025 fin debt 2.49m","2491751","6.0","6.5","Publish per-loan amort 2026-2031","fin debt 2.492m declining vs 3.530m; new loans 0.174m leasing only"),
    ("lb_stnok_igs_reval_9_51m_2025","Steenokkerzeel YE2025 IGS reval 9.51m no cash","9510058","5.5","7.5","Publish per-IGS aanschaf vs herwaardering","IGS 18.370m; reval +9.510m no cash; EVA 0 on city books"),
    ("lb_stnok_ocmw_tussen_1_19m_2025","Steenokkerzeel 2025 OCMW tussenkomst 1.19m","1194900","7.0","5.5","Publish tussenkomst pad 2026-2031","OCMW tussen 1.195m; expl -1.168m; cum -1.428m NEG; equity 0.039m"),
    ("lb_stnok_pension_2_59m_2025","Steenokkerzeel YE2025 pension LT 2.59m","2587398","6.5","6.0","Publish city vs OCMW pension split + TAK26 lock","pension 2.587m vs 6.095m; TAK26 1.027m; respo takeback 3.240m"),
    ("lb_stnok_avail_9_98m_afm_neg_2025","Steenokkerzeel YE2025 avail 9.98m / AFM -0.05m","9976574","6.0","7.0","Publish uncommitted overschot vs TAK26/onbeschikbaar","avail 9.977m; BBR -4.688m; AFM -0.051m; cash 8.647m DROP"),
    ("lb_stnok_agb_werksub_0_26m_2025","Steenokkerzeel 2025 city AGB werksub 0.26m dual","259001","6.5","5.5","Publish beheersovereenkomst + reconciliatie vs AGB 0.244m","city T2 0.259m vs AGB prijssub 0.244m tick1167; EVA 0"),
    ("lb_stnok_pers_13_32m_vte_unpub_2025","Steenokkerzeel 2025 pers 13.32m / VTE unpublished","13322470","6.0","7.0","Publish paid VTE city vs OCMW","pers 13.322m; VTE unpublished; politie 2.108m zone-naam FOI"),
]
n=append_rows(DATA/"leaderboard.csv", [{
    "item_id":iid,"name":name,"level":"L5","type":"local_budget_line","hierarchy_path":HIER+">jr2025_L5",
    "annual_cost_eur":amt,"total_cost_eur":amt,"tco_notes":tco,"confidence":"strong","source_id":SRC,
    "beneficiaries":"Inwoners Steenokkerzeel / OCMW / AGB","stated_goal":"Local city+OCMW dual residual map VL JR2025 Steenokkerzeel",
    "measured_outcome":"assets 95.073m / fin debt 2.492m / IGS reval 9.510m / AFM -0.051m / avail 9.977m / OCMW cum -1.428m NEG",
    "absurdity_score":absu,"cost_score":cost,"difficulty":"3.0","priority_index":"5.5","cut_proposal":cut,
    "status":"active","struck_reason":"","notes":f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; city GE FOI",
} for iid,name,amt,absu,cost,cut,tco in lb_rows])
print("leaderboard", n)

n=append_rows(DATA/"foi_queue.csv", [{
    "gap_id":GAP,"hierarchy_path":HIER+">jr2025_L5","entity_id":ENT,
    "what_is_missing":"T4/LT-S per-loan creditors for fin debt 2.491751m (new loans 0.173963 leasing only; no new bank loans) + IGS FVA 18.370187 inventory (reval +9.510058 no cash; EVA 0) + OCMW tussenkomst 1.194900 vs expl -1.168455 / equity 0.038505 / cum -1.428375 NEG + VTE vs pers 13.322470 + AGB dual lock city T2 0.259001 vs AGB 0.243720 + politiezone 2.108011 (name unpublished) / HVZ 1.090130 pad + AFM -0.051434 TAK26 1.027000",
    "why_it_matters":"Leftover city+OCMW Steenokkerzeel GE after AGB 1167; echo PDF now downloads. Has AGB (T5 EVA 0). Fin debt 2.492m declining; new loans 0.174m leasing. IGS reval 9.510m no cash. AFM -0.051m from TAK26. OCMW cum -1.428m NEG; tussen 1.195m. Avail 9.977m with BBR year -4.688m.",
    "priority":"8","recipient_body":"Lokaal Bestuur Steenokkerzeel (gemeente + OCMW)","recipient_email":"info@steenokkerzeel.be",
    "recipient_postal":"Orchideeenlaan 17 1820 Steenokkerzeel",
    "draft_letter_path":"docs/doge/foi/drafts/gap_stnok_fin_debt_2_49m_igs_reval_9_51m_afm_neg_0_05m_l5.md",
    "status":"ready","date_ready":"2026-08-17","date_sent":"","date_due":"","date_answered":"","response_summary":"",
    "linked_commitment_id":"comm_stnok_fin_debt_2_49m_2025","linked_leaderboard_id":"lb_stnok_fin_debt_2_49m_2025",
    "created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
}])
print("foi", n)
