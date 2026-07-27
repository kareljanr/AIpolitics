# tick232: IDEA intercommunale 2025 outturn + HYGEA Mons waste 2026
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# IDEA RA 2025 strong
IDEA_BILAN = 441286000
IDEA_EQUITY = 279296000
IDEA_PERSONNEL = 38099000
IDEA_RESULT = 13268000
IDEA_DIVIDEND = 11392000
IDEA_FIN_PROD = 16398000
IDEA_FIN_CHARGES = 2269000
IDEA_ENG_CA = 9459000
IDEA_RESP_2026 = 3951000
IDEA_RESP_6Y = 25843000
IDEA_DDT_DIST = 23285276.09
IDEA_DIV_EXCEPT = 20000000
# HYGEA Mons 2026 strong tableau
HYGEA_MONS_TOTAL = 7760388
HYGEA_MONS_COTIS = 167374
HYGEA_MONS_APPEL = 446066
HYGEA_MONS_DEP_BEFORE = 7314322
HYGEA_MONS_REC_SACS = 2173281

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_idea_ra_2025,IDEA intercommunale rapport d activites 2025 comptes,"
    "https://www.deliberations.be/mons/decisions/23-juin-2026-17-00/gf-df-budget-idea-assemblee-generale-ordinaire-et-extraordinaire-du-24-juin-2026/publiable-annexe-i-idea-rapport-dactivites-2025/@@download/file/publiable-annexe-i-idea-rapport-dactivites-2025.pdf,"
    "IDEA AG 24 Jun 2026 annex,2026-07-29,official_report,"
    f'"Bilan 441.286m equity 279.296m personnel 38.099m result 13.268m dividend 11.392m; '
    f'responsabilisation 2026 3.951m / 6y 25.843m; DDT dist 23.285m + div except 20m; tick232"\n'
    "src_idea_note_ag_2026,IDEA AG note de synthese 24 Jun 2026 distributions DDT,"
    "https://www.deliberations.be/mons/decisions/23-juin-2026-17-00/gf-df-budget-idea-assemblee-generale-ordinaire-et-extraordinaire-du-24-juin-2026/publiable-ag-idea-note-de-synthese/@@download/file/publiable-ag-idea-note-de-synthese.pdf,"
    "IDEA AG 24 Jun 2026,2026-07-29,official_decision,"
    f'"Actif net 279.3m; distributions DDT1+2 23.285m; div exceptionnel III.C 20m; tick232"\n'
    "src_hygea_mons_2026,HYGEA waste cost-truth tableau Mons 2026,"
    "https://www.deliberations.be/mons/decisions/24-mars-2026-17-00/env-pp-gestion-des-dechets-cout-verite-previsionnel-2026/tableau-hygea/@@download/file/tableau-hygea.pdf,"
    "Ville de Mons conseil 24 Mar 2026 annex HYGEA,2026-07-29,official_budget,"
    f'"Mons total package 7.760m (dep 7.314 + appel cotisation lissage 0.446); '
    f'cotis infra 0.167; recettes sacs 2.173; tick232"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_idea_ra_2025" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_idea_bilan_2025,idea_hainaut,2025,{IDEA_BILAN},,,outturn,src_idea_ra_2025,strong,IDEA total bilan 441.286m 2025",
    f"bud_idea_equity_2025,idea_hainaut,2025,{IDEA_EQUITY},,,outturn,src_idea_ra_2025,strong,IDEA capitaux propres 279.296m 2025",
    f"bud_idea_personnel_2025,idea_hainaut,2025,{IDEA_PERSONNEL},,,outturn,src_idea_ra_2025,strong,IDEA frais personnel 38.099m 2025",
    f"bud_idea_result_2025,idea_hainaut,2025,{IDEA_RESULT},,,outturn,src_idea_ra_2025,strong,IDEA resultat global 13.268m 2025",
    f"bud_idea_dividend_2025,idea_hainaut,2025,{IDEA_DIVIDEND},,,outturn,src_idea_ra_2025,strong,IDEA dividendes distribues 11.392m 2025 (CENEO heavy)",
    f"bud_idea_fin_prod_2025,idea_hainaut,2025,{IDEA_FIN_PROD},,,outturn,src_idea_ra_2025,strong,IDEA produits financiers 16.398m 2025",
    f"bud_idea_eng_ca_2025,idea_hainaut,2025,{IDEA_ENG_CA},,,outturn,src_idea_ra_2025,strong,IDEA Engineering chiffre d affaires 9.459m 2025",
    f"bud_idea_resp_pension_2026,idea_hainaut,2026,{IDEA_RESP_2026},,,budgeted,src_idea_ra_2025,strong,IDEA cotisation responsabilisation pension 3.951m 2026 (hors bilan path)",
    f"bud_idea_ddt_dist_2026,idea_hainaut,2026,{IDEA_DDT_DIST},,,budgeted,src_idea_note_ag_2026,strong,IDEA distributions DDT1+DDT2 23.285m (cash to communes)",
    f"bud_idea_div_exceptionnel_2026,idea_hainaut,2026,{IDEA_DIV_EXCEPT},,,budgeted,src_idea_note_ag_2026,strong,IDEA dividende exceptionnel secteur III.C 20m to communes",
    f"bud_hygea_mons_total_2026,city_mons,2026,{HYGEA_MONS_TOTAL},,,budgeted,src_hygea_mons_2026,strong,Mons HYGEA waste package 7.760m 2026 (dep+appel lissage)",
    f"bud_hygea_mons_cotis_2026,city_mons,2026,{HYGEA_MONS_COTIS},,,budgeted,src_hygea_mons_2026,strong,Mons HYGEA cotisation infra/transfert 0.167m 2026",
    f"bud_hygea_mons_appel_2026,city_mons,2026,{HYGEA_MONS_APPEL},,,budgeted,src_hygea_mons_2026,strong,Mons HYGEA appel cotisation lissage 5y 0.446m 2026",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_idea_bilan_2025" not in text:
    bud.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
    print("budgets ok", len(rows))
else:
    print("budgets already")

# --- commitments ---
cmt = data / "commitments.csv"
raw = cmt.read_bytes()
if b"\x97" in raw:
    cmt.write_bytes(raw.replace(b"\x97", "\u2013".encode("utf-8")))

cmt_add = (
    "cmt_idea_2025_26,IDEA Coeur du Hainaut intercommunale multi-year path,"
    "idea_hainaut,IDEA 27 communes,RA 2025 + AG Jun 2026,"
    "2025-01-01,2025,2031,441286000,"
    '"{""bilan_2025"":441286000,""equity_2025"":279296000,""personnel_2025"":38099000,'
    '""result_2025"":13268000,""dividend_2025"":11392000,""fin_prod_2025"":16398000,'
    '""resp_pension_2026"":3951000,""resp_pension_2026_31"":25843000,'
    '""ddt_dist_class"":23285276.09,""div_exceptionnel_iiic"":20000000,'
    '""note"":""Strong RA+AG; multi-commune SOE; Mons share of DDT/dividends residual FOI; dual SPGE CENEO""}",'
    "0,active,https://www.deliberations.be/mons/decisions/23-juin-2026-17-00/gf-df-budget-idea-assemblee-generale-ordinaire-et-extraordinaire-du-24-juin-2026,"
    "Territorial development water energy intercommunale,Publish Mons commune share of dividends/DDT; open L5,"
    "src_idea_ra_2025,strong,Hainaut>IDEA,tick232\n"
    "cmt_hygea_mons_2026,Mons HYGEA waste cost package 2026,"
    "city_mons,HYGEA intercommunale,Conseil Mons annex cout-verite 2026,"
    "2025-11-12,2026,2030,7760388,"
    '"{""total_2026"":7760388,""dep_before_appel"":7314322,""appel_lissage"":446066,'
    '""cotis_infra"":167374,""recettes_sacs"":2173281,'
    '""note"":""Strong HYGEA tableau; multi-year lissage 2026-2030; dual IDEA residual""}",'
    "0,active,https://www.deliberations.be/mons/decisions/24-mars-2026-17-00/env-pp-gestion-des-dechets-cout-verite-previsionnel-2026,"
    "Municipal waste collection treatment Mons,Publish multi-year series dual HYGEA group,"
    "src_hygea_mons_2026,strong,Mons>HYGEA,tick232\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_idea_2025_26" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_idea_bilan_441m,IDEA Coeur du Hainaut bilan 441.3m 2025,Wallonia,ops,Hainaut>IDEA,{IDEA_BILAN},{IDEA_BILAN},Strong RA: bilan 441.3m equity 279.3m personnel 38.1m result 13.3m; 27 communes SOE,strong,src_idea_ra_2025,540k residents enterprises communes,Territorial water energy development intercommunale,Core local SOE not pure waste; dual SPGE CENEO; Mons share residual,3,8.5,5,6.55,Publish commune share matrix dividends DDT,seed,,tick232
lb_idea_ddt_23m,IDEA DDT distributions 23.3m class 2026,Wallonia,ops,Hainaut>IDEA>DDT,{IDEA_DDT_DIST},{IDEA_DDT_DIST},Strong AG note: DDT1+2 23.285m + div except 20m to communes; CRAC communes constrained use,strong,src_idea_note_ag_2026,Associated communes,Cable/rights cash distribution to communes,One-off distribution not pure waste; opacity on Mons share,3,7.0,4,5.5,Publish per-commune DDT table,seed,,tick232
lb_hygea_mons_7_76m,Mons HYGEA waste package 7.76m 2026,Wallonia,ops,Mons>HYGEA,{HYGEA_MONS_TOTAL},{HYGEA_MONS_TOTAL},Strong cout-verite: 7.760m total (dep 7.314 + appel 0.446); rec sacs 2.173,strong,src_hygea_mons_2026,Mons residents waste users,Municipal waste via HYGEA,Core service not pure waste; dual intercommunale,3,7.0,4,5.3,Publish multi-year path dual HYGEA group total,seed,,tick232
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_idea_bilan_441m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- entities ---
ent = data / "entities.csv"
raw = ent.read_bytes()
try:
    et = raw.decode("utf-8")
except UnicodeDecodeError:
    et = raw.decode("latin-1")
added = False
if "idea_hainaut" not in et:
    et = et.rstrip("\n") + "\n"
    et += (
        "idea_hainaut,IDEA Coeur du Hainaut,IDEA,27-commune territorial development water energy intercommunale,"
        "intercommunale,wallonie_gov,fr,https://www.idea.be,,,Bilan 441.3m 2025 equity 279.3m; tick232\n"
    )
    added = True
if "hygea" not in et:
    et = et.rstrip("\n") + "\n"
    et += (
        "hygea,HYGEA,HYGEA,Walloon Hainaut waste intercommunale (ex IDEA proprete),"
        "intercommunale,wallonie_gov,fr,,,Mons package 7.76m 2026; tick232\n"
    )
    added = True
if added:
    ent.write_text(et, encoding="utf-8")
    print("entities ok")
else:
    print("entities already")

# --- foi ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
import re

lines = ft.splitlines(keepends=True)
out = []
for line in lines:
    if "gap_mons_budget_l5" in line and line.startswith("gap_"):
        if "tick232" not in line:
            line = re.sub(
                r"tick103\+231:.*$",
                "tick103+231+232: CPAS 149.4m zone 2.60m HYGEA 7.76m IDEA group filled; full Ville BI2026 PDF + ASBL L5 + Mons IDEA dividend share still FOI ready human send",
                line.rstrip("\n\r"),
            )
            if "tick232" not in line:
                line = line.rstrip("\n\r") + "; tick232 HYGEA+IDEA partial"
            line += "\n"
            print("foi mons ok")
    out.append(line)
foi.write_text("".join(out), encoding="utf-8")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_223,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons Ville BI2026 PDF if published utilities SOE IDEA HYGEA FPS taxex other large FOI-adjacent) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:50:00Z,,'
    '"Spawned tick231 after Mons CPAS 149.4m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_223,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons Ville BI2026 PDF if published utilities SOE IDEA HYGEA FPS taxex other large FOI-adjacent) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:50:00Z,2026-07-29T03:15:00Z,'
    '"tick232: IDEA 441m bilan + DDT 23.3m + HYGEA Mons 7.76m; Ville BI2026 PDF still FOI; spawn rq_224"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_224,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons Ville BI2026 if published FPS taxex utilities SOE other large FOI-adjacent programmes) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T03:15:00Z,,'
        '"Spawned tick232 after IDEA 441m HYGEA Mons 7.76m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_223")
    print(repr(text[i : i + 280]) if i >= 0 else "missing")

# --- state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T03:15:00Z,rq_223,232,no,"
    '"Scheduler 60s. Next prio5 rq_224; rq_116 SWA deferred. FOI ready human send. '
    'tick232 IDEA 441m DDT 23.3m HYGEA Mons 7.76m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T03:15:00Z - tick 232
- Unit: **rq_223** (FOI-adjacent hole-fill - **IDEA + HYGEA Mons utilities**)
- Found (strong primary):
  - **IDEA 2025:** bilan **EUR 441.286m**; equity **279.296m**; personnel **38.099m**; result **13.268m**; dividends **11.392m**; fin products **16.398m**.
  - **IDEA 2026 path:** responsabilisation pension **3.951m** (6y **25.843m** hors bilan); DDT1+2 distributions **23.285m**; div exceptionnel III.C **20m** to communes.
  - **HYGEA Mons waste 2026 EUR 7.760m** (dep 7.314 + appel lissage 0.446; cotis infra 0.167; recettes sacs 2.173).
  - Full **Ville Mons BI2026 PDF** still not on mons.be — FOI residual ASBL L5 + Mons share of IDEA dividends.
- Wrote: sources 3; budgets 13; cmt 2; lb 3; entities 2; foi note; rq_223=done; seeded **rq_224**.
- FOI: Ville BI2026 + ASBL top20 + IDEA per-commune DDT/div still ready human send.
- Next: prio5 **rq_224**; deferred **rq_116** SWA.
"""
if "### 2026-07-29T03:15:00Z - tick 232" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick232")
