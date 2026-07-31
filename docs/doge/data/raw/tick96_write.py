from pathlib import Path
from datetime import datetime, timezone

root = Path("docs/doge/data")
now = "2026-07-22T16:19:00Z"

# foi_queue append
foi = root / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
if "gap_hainaut_asbl_list_2026" not in ft:
    if not ft.endswith("\n"):
        ft += "\n"
    ft += (
        "gap_hainaut_asbl_list_2026,"
        "Hainaut>subsidies>ASBL_entities_ge_50k,"
        "prov_hainaut,"
        "Annex budget 2026 listing 199 entities with provincial aids >=50k/yr with amounts and motivation,"
        "CoA confirms annex exists and flags missing motivation; amounts not in public CoA PDF; L5 opacity on largest Walloon province,"
        "8,"
        "Province de Hainaut publicite de l administration,"
        ","  # email unknown - human confirm
        "Hotel de la Province Place de la Louve 1 7000 Mons,"
        "docs/doge/foi/drafts/gap_hainaut_asbl_list_2026.md,"
        "ready,"
        "2026-07-22,"
        ",,,,,"  # sent due answered summary
        "cmt_hainaut_asbl_opacity_2026,"
        "lb_hainaut_asbl_opacity,"
        f"{now},{now},"
        "rq_096 draft ready human send only; FR letter\n"
    )
    foi.write_text(ft, encoding="utf-8")
    print("foi_queue ok")
else:
    print("foi exists")

# research queue
rq = root / "research_queue.csv"
rt = rq.read_text(encoding="utf-8")
rt = rt.replace(
    'rq_096,Hainaut full named ASBL EUR list FOI or secondary,continuous,3,open,L5,prov_hainaut,"If public annex of 199 entities with EUR appears: extract top 20; else open FOI for annex list with amounts.",,2026-07-22T16:04:00Z,2026-07-22T16:04:00Z,"CoA notes annex exists but amounts not in published CoA PDF"',
    'rq_096,Hainaut full named ASBL EUR list FOI or secondary,continuous,3,blocked_foi,L5,prov_hainaut,"If public annex of 199 entities with EUR appears: extract top 20; else open FOI for annex list with amounts.",gap_hainaut_asbl_list_2026,2026-07-22T16:04:00Z,2026-07-22T16:19:00Z,"Public search negative; FOI draft ready gap_hainaut_asbl_list_2026; human send"',
)
if "rq_097," not in rt:
    if not rt.endswith("\n"):
        rt += "\n"
    rt += 'rq_097,Namur or Brabant wallon province L5 named sample,continuous,2,open,L5,prov_namur,"Extract 3+ named ASBL/subsidy lines from CoA Namur or BW province budget 2026 if public.",,2026-07-22T16:19:00Z,2026-07-22T16:19:00Z,"Parallel Hainaut/Liege L5; complete Walloon province L5 map"\n'
rq.write_text(rt, encoding="utf-8")
print("queue ok")

# sources
src = root / "sources.csv"
st = src.read_text(encoding="utf-8")
if "src_tick96_hainaut_asbl_search_negative" not in st:
    if not st.endswith("\n"):
        st += "\n"
    st += (
        "src_tick96_hainaut_asbl_search_negative,"
        "Tick96 search for public Hainaut 199-entity ASBL EUR annex negative,"
        "docs/doge/data/raw/hainaut_prov_ccrek_budget_2026.pdf,"
        "DOGE loop research,2026-07-22,secondary,"
        '"Web/portal search found no public named EUR list; CoA PDF remains best public evidence of annex existence"\n'
    )
    src.write_text(st, encoding="utf-8")
print("sources ok")

# leaderboard note update
lb = root / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
lt2 = lt.replace(
    "Publish full named EUR list + justifications,seed,,tick95",
    "FOI draft gap_hainaut_asbl_list_2026 ready tick96; human send,seed,,tick96",
)
if lt2 != lt:
    lb.write_text(lt2, encoding="utf-8")
    print("lb ok")

# commitments notes
cmt = root / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
if "gap_hainaut_asbl_list_2026" not in ct and "cmt_hainaut_asbl_opacity_2026" in ct:
    ct = ct.replace(
        "Publish named EUR list,src_ccrek_hainaut_prov_budget_2026,strong,Province_Hainaut>ASBL_list,CoA flags unmotivated subsidisation of 199 entities",
        "FOI gap_hainaut_asbl_list_2026 ready,src_ccrek_hainaut_prov_budget_2026,strong,Province_Hainaut>ASBL_list,CoA flags unmotivated subsidisation of 199 entities; FOI draft tick96",
    )
    cmt.write_text(ct, encoding="utf-8")
    print("cmt ok")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    'main,continuous,continuous,2026-07-22T16:19:00Z,rq_096,96,no,"Hainaut ASBL FOI draft ready (tick96). Next: rq_097 Namur/BW L5 or rq_089 SWA; human may send FOI."\n',
    encoding="utf-8",
)
print("state ok")

log = Path("docs/doge/loop_log.md")
entry = """
### 2026-07-22T16:19:00Z -- tick 96
- Unit: rq_096 (Hainaut full named ASBL EUR list — public search + FOI)
- Found (strong process; **public list still missing**): Re-checked CoA Hainaut budget 2026 PDF and web/portal search for a published annex of the **199 entities** with provincial aids >= EUR 50k/yr. **No machine-readable or PDF named EUR list** found on public portals this tick. CoA remains best primary evidence that the annex **exists** administratively and that **motivation for extraprovincialisation is missing**. Action: **FOI draft** `gap_hainaut_asbl_list_2026` (FR, publicite de l'administration) status **ready** — **human send only**.
- Wrote: foi draft + foi_queue ready; sources note; rq_096=blocked_foi; lb/cmt notes; seeded rq_097 Namur/BW L5; ticks=96
- FOI: **gap_hainaut_asbl_list_2026** ready (not sent)
- Next: **rq_097** Namur/Brabant wallon L5 (prio 2) or **rq_089** SWA Q4 (prio 1); human may send Hainaut FOI

""".encode("utf-8")
raw = log.read_bytes()
if b"tick 96" not in raw:
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + entry)
    print("log ok")
else:
    print("log exists")
