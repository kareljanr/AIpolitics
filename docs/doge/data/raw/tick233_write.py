# tick233: Mons Ville budget 2026 after MB1 — full ord/extra totals
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# Source: deliberations 23 Jun 2026 1er amendement (vote recorded; page may still say projet)
ORD_REC_PROPRE = 242204040.98
ORD_DEP_PROPRE = 241834209.04
ORD_BONI_PROPRE = 369831.94
ORD_REC_GLOB = 245129149.82
ORD_DEP_GLOB = 243264254.04
ORD_BONI_GLOB = 1864895.78
EXTRA_REC_PROPRE = 60823062.67
EXTRA_DEP_PROPRE = 63197706.84
EXTRA_MALI_PROPRE = -2374644.17
EXTRA_REC_GLOB = 165215294.26
EXTRA_DEP_GLOB = 163011883.88
EXTRA_BONI_GLOB = 2203410.38
DOT_CPAS = 26944775.57
DOT_FE_CATH = 1014436.23
DOT_FE_PROT = 58778.52
DOT_POLICE = 27335195.99
DOT_SECOURS = 2604469.70
BUDGET_PARTICIPATIF = 107742.00
# city cash-out class ord+extra dep propre same-year
CITY_CASH_PROPRE = ORD_DEP_PROPRE + EXTRA_DEP_PROPRE  # 305031915.88

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_mons_ville_mb1_2026,Mons Ville 1er amendement budget general 2026 recap,"
    "https://www.deliberations.be/mons/decisions/23-juin-2026-17-00/gf-df-budget-1er-amendement-au-budget-general-des-recettes-et-des-depenses-de-lexercice-2026,"
    "Ville de Mons conseil communal 23 Jun 2026,2026-07-29,official_decision,"
    f'"Ord dep propre {ORD_DEP_PROPRE:.2f} rec {ORD_REC_PROPRE:.2f}; extra dep propre {EXTRA_DEP_PROPRE:.2f}; '
    f'police zone {DOT_POLICE:.2f} CPAS {DOT_CPAS:.2f} secours {DOT_SECOURS:.2f}; '
    f'note: page labelled projet but vote results recorded; tick233"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_mons_ville_mb1_2026" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_mons_ville_ord_dep_propre_2026,city_mons,2026,{ORD_DEP_PROPRE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville ordinaire depenses exercice propre 241.834m after MB1 2026",
    f"bud_mons_ville_ord_rec_propre_2026,city_mons,2026,{ORD_REC_PROPRE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville ordinaire recettes exercice propre 242.204m after MB1 2026",
    f"bud_mons_ville_ord_dep_global_2026,city_mons,2026,{ORD_DEP_GLOB},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville ordinaire depenses globales 243.264m after MB1 2026",
    f"bud_mons_ville_extra_dep_propre_2026,city_mons,2026,{EXTRA_DEP_PROPRE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville extraordinaire depenses exercice propre 63.198m after MB1 2026",
    f"bud_mons_ville_extra_rec_propre_2026,city_mons,2026,{EXTRA_REC_PROPRE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville extraordinaire recettes exercice propre 60.823m after MB1 2026",
    f"bud_mons_ville_cash_propre_2026,city_mons,2026,{CITY_CASH_PROPRE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville ord+extra dep propre same-year class 305.032m after MB1 2026",
    f"bud_mons_zone_police_2026,city_mons,2026,{DOT_POLICE},,,budgeted,src_mons_ville_mb1_2026,strong,Mons Ville dotation Zone de Police 27.335m 2026 (MB1 recap)",
    f"bud_mons_fabriques_catholiques_2026,city_mons,2026,{DOT_FE_CATH},,,budgeted,src_mons_ville_mb1_2026,strong,Mons fabriques eglise catholiques 1.014m 2026",
    f"bud_mons_fabriques_protestants_2026,city_mons,2026,{DOT_FE_PROT},,,budgeted,src_mons_ville_mb1_2026,strong,Mons fabriques eglise protestants 58.8k 2026",
    f"bud_mons_budget_participatif_2026,city_mons,2026,{BUDGET_PARTICIPATIF},,,budgeted,src_mons_ville_mb1_2026,strong,Mons budget participatif 107.7k 2026",
    f"bud_mons_cpas_dotation_tutelle_2026,city_mons,2026,{DOT_CPAS},,,budgeted,src_mons_ville_mb1_2026,strong,Mons CPAS dotation tutelle-approved 26.945m in MB1 recap (vs interv 27.918m prior)",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_mons_ville_ord_dep_propre_2026" not in text:
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
    "cmt_mons_ville_budget_2026,Mons Ville budget 2026 after MB1 full ord+extra,"
    "city_mons,Ville de Mons,Conseil 23 Jun 2026 1er amendement,"
    "2026-05-28,2026,2026,305031915.88,"
    '"{""ord_dep_propre"":241834209.04,""ord_rec_propre"":242204040.98,""ord_boni_propre"":369831.94,'
    '""ord_dep_global"":243264254.04,""ord_rec_global"":245129149.82,'
    '""extra_dep_propre"":63197706.84,""extra_rec_propre"":60823062.67,'
    '""extra_dep_global"":163011883.88,""extra_rec_global"":165215294.26,'
    '""cash_propre_ord_extra"":305031915.88,'
    '""dot_police"":27335195.99,""dot_cpas_tutelle"":26944775.57,""dot_secours"":2604469.70,'
    '""fabriques_cath"":1014436.23,""fabriques_prot"":58778.52,""budget_participatif"":107742,'
    '""note"":""Strong deliberations with vote; page may still say projet; full ASBL L5 annex residual FOI; closes gap_mons totals""}",'
    "0,active,https://www.deliberations.be/mons/decisions/23-juin-2026-17-00/gf-df-budget-1er-amendement-au-budget-general-des-recettes-et-des-depenses-de-lexercice-2026,"
    "City Mons full 2026 budget totals after MB1,Publish ASBL top20 annex; dual Oxygene residual,"
    "src_mons_ville_mb1_2026,strong,Mons>Ville,tick233\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_mons_ville_budget_2026" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_mons_ville_242m,Mons Ville ordinaire dep 241.8m 2026 MB1,Wallonia,ops,Mons>Ville,{ORD_DEP_PROPRE},{ORD_DEP_PROPRE},Strong MB1: ord dep propre 241.8m rec 242.2m boni 0.37m; extra dep 63.2m; cash propre class 305m,strong,src_mons_ville_mb1_2026,Mons residents services,City ordinary budget after first amendment,Core local government; ASBL L5 residual FOI; dual Oxygene,3,8.5,5,6.55,Publish ASBL top20 full PDF annex,seed,,tick233
lb_mons_zone_police_27m,Mons Zone de Police city dotation 27.3m 2026,Wallonia,ops,Mons>ZonePolice,{DOT_POLICE},{DOT_POLICE},Strong MB1 recap: 27.335m police zone; dual federal residual,strong,src_mons_ville_mb1_2026,Residents safety,Municipal police zone financing,Core safety not pure waste; dual federal,3,7.5,4,5.7,Publish zone multi-year dual federal share,seed,,tick233
lb_mons_cash_propre_305m,Mons Ville ord+extra dep propre ~305m 2026,Wallonia,ops,Mons>Ville_cash,{CITY_CASH_PROPRE},{CITY_CASH_PROPRE},Strong: ord 241.8 + extra 63.2 = 305.0m same-year propre class; not full global with prior years,strong,src_mons_ville_mb1_2026,Mons residents,City same-year cash-out class,Core local; double-count caution with CPAS/police dots inside,3,8.5,5,6.55,Publish L5 ASBL matrix,seed,,tick233
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_mons_ville_242m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- foi: update gap_mons status notes - material totals filled ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
import re

lines = ft.splitlines(keepends=True)
out = []
for line in lines:
    if line.startswith("gap_mons_budget_l5,") or (
        "gap_mons_budget_l5" in line[:40] if line.startswith("gap_") else False
    ):
        # update what_is_missing and notes - keep ready for ASBL L5
        # replace notes end
        line = re.sub(
            r"tick103\+231\+232:.*$",
            "tick103+231-233: Ville MB1 ord 241.8m extra 63.2m police 27.3m CPAS/HYGEA/IDEA filled; residual ASBL third-party L5 annex FOI ready human send",
            line.rstrip("\n\r"),
        )
        if "tick233" not in line:
            line = line.rstrip("\n\r") + "; tick233 Ville totals filled residual ASBL L5"
        if not line.endswith("\n"):
            line += "\n"
        print("foi mons updated")
    out.append(line)
foi.write_text("".join(out), encoding="utf-8")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_224,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons Ville BI2026 if published FPS taxex utilities SOE other large FOI-adjacent programmes) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T03:15:00Z,,'
    '"Spawned tick232 after IDEA 441m HYGEA Mons 7.76m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_224,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons Ville BI2026 if published FPS taxex utilities SOE other large FOI-adjacent programmes) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T03:15:00Z,2026-07-29T03:40:00Z,'
    '"tick233: Mons Ville MB1 ord 241.8m extra 63.2m police 27.3m; ASBL L5 residual FOI; spawn rq_225"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_225,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(FPS taxex utilities SOE other large FOI-adjacent programmes; Mons ASBL L5 if public) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T03:40:00Z,,'
        '"Spawned tick233 after Mons Ville MB1 241.8m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_224")
    print(repr(text[i : i + 280]) if i >= 0 else "missing")

# --- state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T03:40:00Z,rq_224,233,no,"
    '"Scheduler 60s. Next prio5 rq_225; rq_116 SWA deferred. FOI ready human send. '
    'tick233 Mons Ville MB1 ord 241.8m extra 63.2m police 27.3m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T03:40:00Z - tick 233
- Unit: **rq_224** (FOI-adjacent hole-fill - **Mons Ville budget 2026 MB1 totals**)
- Found (strong deliberations 23 Jun 2026 1er amendement; vote recorded):
  - **Ordinaire dep propre EUR 241.834m** / rec **242.204m** (boni 0.370m); global dep **243.264m**.
  - **Extraordinaire dep propre EUR 63.198m** / rec **60.823m**; global dep **163.012m** (incl. prior years).
  - **Same-year cash-propre class EUR 305.032m** (ord+extra dep propre).
  - Dotations: **Zone Police 27.335m**; CPAS tutelle **26.945m**; Zone Secours **2.604m**; fabriques cath **1.014m** + prot **59k**; budget participatif **108k**.
  - Residual: machine-readable **ASBL third-party L5** annex still FOI (totals gap largely closed).
- Wrote: sources 1; budgets 11; cmt 1; lb 3; foi note; rq_224=done; seeded **rq_225**.
- FOI: ASBL top20 L5 still ready human send.
- Next: prio5 **rq_225**; deferred **rq_116** SWA.
"""
if "### 2026-07-29T03:40:00Z - tick 233" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick233")
