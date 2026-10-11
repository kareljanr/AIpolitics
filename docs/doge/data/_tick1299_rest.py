# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ENT="agb_kortenaken"
SRC="src_agbktn_jr2025_bbc"
SRC_URL="https://www.kortenaken.be/sites/default/files/2026-05/20260528_VASTSTELLING-BBC-JAARREKENING-AGB.pdf"
HIER="Vlaanderen>Gemeenten>Kortenaken>AGB"
UTC="2026-08-17T13:50:00Z"
TICK=1299
GAP="gap_agbktn_fin_debt_3_28m_lease_3_22m_prijssub_0_16m_l5"

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
    ("comm_agbktn_fin_debt_3_28m_2025","AGB Kortenaken YE2025 fin debt 3.281m","3280771","T4 3.280771m (LT 3.233 + ST due 0.047) declining vs 3.311m; new loans 0.017m city interest-free; leasing MVA 3.216m","Publish per-contract amort 2026-2035 leasing vs city loans FOI"),
    ("comm_agbktn_lease_3_22m_2025","AGB Kortenaken YE2025 leasing MVA 3.216m","3216363","T5 leasing 3.216363m (sporthal De Vruen); canon 0.036550m; DBFM Sport Vlaanderen since 08.05.2012","Publish remaining DBFM/erfpacht schedule FOI"),
    ("comm_agbktn_prijssub_0_16m_2025","AGB Kortenaken 2025 city prijssub 0.157m","157062","D2/T2 prijssub Kortenaken 0.156547 + Bekkevoort 0.000515; factor 7 since 01.01.2025; city GE live unmined","Publish 2026-2031 beheersovereenkomst pad FOI"),
    ("comm_agbktn_gecorr_neg_0_21m_2025","AGB Kortenaken YE2025 gecorr AFM -0.209m","209080","J2 gecorr AFM -0.209080m; aangewezen 0.264871 vs actual 0.046621; AFM +0.009171","Publish aangewezen vs actual amort pad FOI"),
    ("comm_agbktn_avail_0_09m_2025","AGB Kortenaken YE2025 avail BBR 0.095m","94988","avail 0.094988m; BBR year +0.009171m; cash 0.104m JUMP; dividend 0.010m","Publish uncommitted overschot vs dividend lock FOI"),
    ("comm_agbktn_maint_0_07m_2025","AGB Kortenaken 2025 Sport Vlaanderen onderhoud 0.067m","67229","D2 onderhoud 0.067229m; index 20pct loon / 80pct materiaal since 08.05.2012; daklek residual unpublished","Publish DBFM index + daklek residual euro FOI"),
]
n=append_rows(DATA/"commitments.csv", [{
    "commitment_id":cid,"title":title,"entity_id":ENT,"beneficiary":"Inwoners Kortenaken / Sporthal De Vruen",
    "legal_basis":"Decreet Lokaal Bestuur; BBC JR2025 AGB Kortenaken RVB 28.05.2026","decision_date":"2026-05-28",
    "start_year":"2025","end_year":"2025","total_envelope_eur":env,"cash_by_year":"","remaining_eur":"",
    "status":"open","evaluation_url":SRC_URL,"stated_goal":"Local AGB dual residual map VL JR2025 Kortenaken",
    "cut_option":cut,"source_id":SRC,"confidence":"strong","hierarchy_path":HIER+">jr2025_L5","notes":note+f"; tick{TICK}",
} for cid,title,env,note,cut in crows])
print("commitments", n)

lb_rows = [
    ("lb_agbktn_fin_debt_3_28m_2025","AGB Kortenaken YE2025 fin debt 3.28m","3280771","6.0","6.5","Publish per-contract amort 2026-2035 leasing vs city loans","fin debt 3.281m declining vs 3.311m; new loans 0.017m city interest-free"),
    ("lb_agbktn_lease_3_22m_2025","AGB Kortenaken YE2025 leasing 3.22m De Vruen","3216363","6.5","7.0","Publish remaining DBFM/erfpacht schedule","leasing MVA 3.216m; canon 0.037m; Sport Vlaanderen DBFM 2012"),
    ("lb_agbktn_prijssub_0_16m_2025","AGB Kortenaken 2025 city prijssub 0.16m","157062","6.5","5.5","Publish 2026-2031 factor-7 prijssub pad","city 0.157m + Bekkevoort 0.001m; klant only 0.022m; city GE unmined"),
    ("lb_agbktn_gecorr_neg_0_21m_2025","AGB Kortenaken YE2025 gecorr AFM -0.21m","209080","7.0","5.5","Publish aangewezen vs actual amort pad","gecorr -0.209m; aangewezen 0.265m vs actual 0.047m; AFM +0.009m"),
    ("lb_agbktn_avail_0_09m_2025","AGB Kortenaken YE2025 avail BBR 0.09m","94988","5.0","5.0","Publish uncommitted overschot vs dividend 0.010m","avail 0.095m; BBR +0.009m; cash 0.104m JUMP; dividend 0.010m"),
    ("lb_agbktn_maint_0_07m_2025","AGB Kortenaken 2025 Sport Vlaanderen onderhoud 0.07m","67229","6.0","5.0","Publish DBFM index + daklek residual euro","onderhoud 0.067m; index 20/80 since 2012; daklek unpublished"),
    ("lb_agbktn_pers_0_city_dual_2025","AGB Kortenaken 2025 pers 0 / city staff dual unpublished","0","6.5","4.5","Publish VTE AGB vs city staff De Vruen","J5 no bezoldigingen; city dual staff unpublished"),
]
n=append_rows(DATA/"leaderboard.csv", [{
    "item_id":iid,"name":name,"level":"L5","type":"local_budget_line","hierarchy_path":HIER+">jr2025_L5",
    "annual_cost_eur":amt,"total_cost_eur":amt,"tco_notes":tco,"confidence":"strong","source_id":SRC,
    "beneficiaries":"Inwoners Kortenaken / Sporthal De Vruen","stated_goal":"Local AGB dual residual map VL JR2025 Kortenaken",
    "measured_outcome":"assets 3.479m / fin debt 3.281m / leasing 3.216m / city prijssub 0.157m / gecorr AFM -0.209m / avail 0.095m",
    "absurdity_score":absu,"cost_score":cost,"difficulty":"3.0","priority_index":"5.5","cut_proposal":cut,
    "status":"active","struck_reason":"","notes":f"tick{TICK}; primary BBC JR2025 PDF; not TE-additive of 348bn; AGB dual FOI",
} for iid,name,amt,absu,cost,cut,tco in lb_rows])
print("leaderboard", n)

n=append_rows(DATA/"foi_queue.csv", [{
    "gap_id":GAP,"hierarchy_path":HIER+">jr2025_L5","entity_id":ENT,
    "what_is_missing":"T4/LT-S per-contract creditors for fin debt 3.280771m (leasing MVA 3.216363; new loans 0.016500 city interest-free to 31.12.2035; canon 0.036550 + city afl 0.010071) + city prijssub 0.156547 factor-7 2026-2031 pad + Bekkevoort 0.000515 + VTE vs pers 0 / city staff dual + gecorr AFM -0.209080 (aangewezen 0.264871) + Sport Vlaanderen DBFM 0.067229 / daklek residual + city GE dual lock (JR2025 now live unmined)",
    "why_it_matters":"Unmined AGB Kortenaken after residual dual hunt. Official BBC PDF now downloads. FVA 0. Fin debt 3.281m almost all leasing 3.216m; new loans 0.017m city interest-free. City prijssub 0.157m (klant only 0.022m). Gecorr AFM -0.209m. Avail 0.095m with BBR year +0.009m. City GE PDF now live, left unmined.",
    "priority":"8","recipient_body":"AGB Kortenaken / Gemeente Kortenaken","recipient_email":"financien@kortenaken.be",
    "recipient_postal":"Dorpsplein 35 3470 Kortenaken",
    "draft_letter_path":"docs/doge/foi/drafts/gap_agbktn_fin_debt_3_28m_lease_3_22m_prijssub_0_16m_l5.md",
    "status":"ready","date_ready":"2026-08-17","date_sent":"","date_due":"","date_answered":"","response_summary":"",
    "linked_commitment_id":"comm_agbktn_fin_debt_3_28m_2025","linked_leaderboard_id":"lb_agbktn_fin_debt_3_28m_2025",
    "created_utc":UTC,"updated_utc":UTC,"notes":f"tick{TICK}; ready not sent; do not send without human OK; primary BBC euros",
}])
print("foi", n)
