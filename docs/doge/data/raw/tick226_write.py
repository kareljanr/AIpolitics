# tick226: Digipolis member-share omzet matrix 2026 from markup PDF
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# Member omzet 2026 (strong markup ebesluit annex)
MEMBERS_2026 = {
    "agso": ("AG Stedelijk Onderwijs", 11083813.08),
    "cia": ("AG CIA/Erfgoed", 363222.90),
    "hvz": ("Brandweerzone Antwerpen HVZ", 6994093.78),
    "inti": ("Integratie en Inburgering", 1209516.37),
    "lpa": ("Politiezone Antwerpen LPA", 69468352.01),
    "mpa": ("Mobiliteit en Parkeren MPA", 9456558.40),
    "ove": ("OVE residual member", 403081.68),
    "stad": ("Stad Antwerpen", 138020830.69),
    "vespa": ("AG VESPA", 3603271.13),
    "zba": ("Zorgbedrijf Antwerpen ZBA", 4467307.79),
}
TOTAL_2026 = 245070047.84
TOTAL_2025 = 221899608.67
MARKUP_2026 = 0.0414
MARKUP_2025 = 0.0429

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_digipolis_markup_2026,AG Digipolis mark-up omzet member matrix 2025-2026,"
    "https://ebesluit.antwerpen.be/document/69206dd5a60702536ea897cb,"
    "AG Digipolis MJP annex berekeningsfile mark up,2026-07-29,official_budget,"
    '"Member omzet 2026 sum 245.070m (stad 138.021 LPA 69.468 AGSO 11.084 MPA 9.457 HVZ 6.994 '
    'ZBA 4.467 VESPA 3.603 INTI 1.210 OVE 0.403 CIA 0.363); markup 4.14pct; 2025 sum 221.900m; tick226"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_digipolis_markup_2026" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_digipolis_member_total_2026,digipolis_antwerpen,2026,{TOTAL_2026},,,budgeted,src_digipolis_markup_2026,strong,"
    f"Digipolis member omzet sum 245.070m 2026 (markup matrix; ~AGB total 245.6m)",
    f"bud_digipolis_member_total_2025,digipolis_antwerpen,2025,{TOTAL_2025},,,budgeted,src_digipolis_markup_2026,strong,"
    f"Digipolis member omzet sum 221.900m 2025 (markup matrix)",
]
for key, (label, amt) in MEMBERS_2026.items():
    rows.append(
        f"bud_digipolis_member_{key}_2026,digipolis_antwerpen,2026,{amt},,,budgeted,src_digipolis_markup_2026,strong,"
        f"Digipolis omzet recharge {label} 2026 {amt}"
    )
# top members also as city_antwerpen-linked for stack
rows.append(
    f"bud_digipolis_stad_recharge_2026,city_antwerpen,2026,138020830.69,,,budgeted,src_digipolis_markup_2026,strong,"
    "Stad Antwerpen Digipolis omzet recharge 138.021m 2026 (full city IT via AGB; vs partial lock 38.8m)"
)
rows.append(
    f"bud_digipolis_pza_lpa_recharge_2026,city_antwerpen,2026,69468352.01,,,budgeted,src_digipolis_markup_2026,strong,"
    "PZA LPA Digipolis omzet recharge 69.468m 2026 (vs prior PZA Digipolis package 53.5m 2025 class)"
)

text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_digipolis_member_total_2026" not in text:
    bud.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
    print("budgets ok", len(rows))
else:
    print("budgets already")

# --- commitments ---
cmt = data / "commitments.csv"
raw = cmt.read_bytes()
if b"\x97" in raw:
    cmt.write_bytes(raw.replace(b"\x97", "\u2013".encode("utf-8")))

cash_json = (
    '"{""total_2026"":245070047.84,""total_2025"":221899608.67,""markup_2026_pct"":4.14,'
    '""markup_2025_pct"":4.29,'
    '""stad"":138020830.69,""lpa_pza"":69468352.01,""agso"":11083813.08,""mpa"":9456558.40,'
    '""hvz"":6994093.78,""zba"":4467307.79,""vespa"":3603271.13,""inti"":1209516.37,'
    '""ove"":403081.68,""cia"":363222.90,'
    '""note"":""Strong markup annex; omzet recharges to members fund AGB 245.6m; '
    'stad 138m is full city IT path not equal city ebesluit lock 38.8m (subset/partial timing); '
    'LPA~PZA; not double-count with AGB total as city opex""}"'
)
cmt_add = (
    "cmt_digipolis_member_matrix_2025_26,AG Digipolis member omzet share matrix,"
    "digipolis_antwerpen,10 named members cost-sharing,"
    "MJP annex berekeningsfile mark up,2025-10-08,2025,2026,245070047.84,"
    f"{cash_json},"
    "0,active,https://ebesluit.antwerpen.be/document/69206dd5a60702536ea897cb,"
    "Member IT recharge transparency matrix,Publish project L5 within member; open annual update,"
    "src_digipolis_markup_2026,strong,Antwerpen>Digipolis>members,tick226\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_digipolis_member_matrix_2025_26" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = """lb_digipolis_member_matrix_245m,Digipolis member omzet matrix 245.07m 2026,Flanders,ops,Antwerpen>Digipolis>members,245070047.84,245070047.84,Strong markup annex: 10 members sum 245.07m; stad 138.0 LPA 69.5 AGSO 11.1 MPA 9.5 HVZ 7.0; markup 4.14pct; closes member-share residual,strong,src_digipolis_markup_2026,City police fire care education staff,AGB cost-sharing recharge matrix,Core ICT ops; transparency win; double-count caution vs AGB total and city packages,4,9.0,6,7.2,Publish annual matrix update; project L5 within members,seed,,tick226
lb_digipolis_stad_138m,Stad Antwerpen Digipolis recharge 138.02m 2026,Flanders,ops,Antwerpen>Digipolis>stad,138020830.69,138020830.69,Strong markup: city omzet 138.021m vs partial ebesluit lock 38.8m; larger path includes full city IT,strong,src_digipolis_markup_2026,City staff residents digital,City full Digipolis recharge path,Core ops; reconcile lock vs omzet residual detail,4,8.5,5,6.55,Publish city package vs omzet reconciliation,seed,,tick226
lb_digipolis_lpa_69m,PZA LPA Digipolis recharge 69.47m 2026,Flanders,ops,Antwerpen>Digipolis>LPA,69468352.01,69468352.01,Strong markup: LPA/PZA 69.468m 2026 vs prior PZA Digipolis 53.5m 2025 class,strong,src_digipolis_markup_2026,Police digital services,Police zone Digipolis recharge,Core police IT; dual with PZA toelage stack,3,8.0,5,6.15,Publish PZA budget line map to LPA omzet,seed,,tick226
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_digipolis_member_matrix_245m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_218,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis member-share matrix social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:55:00Z,,'
    '"Spawned tick225 after Digipolis AGB 245.6m personnel 45.5m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_218,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis member-share matrix social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:55:00Z,2026-07-29T01:15:00Z,'
    '"tick226: Digipolis member matrix 245.07m (stad 138 LPA 69.5); Mons BI2026 still FOI; spawn rq_219"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_219,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 Antwerp social L5 ebesluit CAW ADIC large nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:15:00Z,,'
        '"Spawned tick226 after Digipolis member matrix 245m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_218")
    print(repr(text[i : i + 300]) if i >= 0 else "missing")

# --- foi ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-225: culture 16/16 14.58m + Digipolis AGB MJP 245.6m personnel 45.5m filled; "
    "residual register member-share matrix Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-226: culture 16/16 + Digipolis AGB 245.6m personnel + member matrix 245.07m filled; "
    "residual register project L5 Mons BI2026 dual VL human send"
)
if oldn in ft:
    foi.write_text(ft.replace(oldn, newn), encoding="utf-8")
    print("foi ok")
else:
    # loose
    import re

    lines = ft.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("gap_antwerp_subsidies_top20,") and "tick140" in line:
            line = (
                re.sub(
                    r"tick140.*$",
                    "tick140+204+213-226: Digipolis matrix filled; residual register project L5 Mons dual VL human send",
                    line.rstrip("\n\r"),
                )
                + ("\n" if line.endswith("\n") else "")
            )
            print("foi loose")
        out.append(line)
    foi.write_text("".join(out), encoding="utf-8")

# --- state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T01:15:00Z,rq_218,226,no,"
    '"Scheduler 60s. Next prio5 rq_219 Mons/social/CAW; rq_116 SWA deferred. '
    'FOI ready human send. tick226 Digipolis member matrix 245.07m stad 138 LPA 69.5."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = """
### 2026-07-29T01:15:00Z - tick 226
- Unit: **rq_218** (FOI-adjacent hole-fill - **Digipolis member-share omzet matrix**)
- Found (strong markup annex ebesluit PDF):
  - **Member omzet sum 2026 EUR 245.070m** (2025: 221.900m); markup **4.14%** (from 4.29%).
  - **Stad 138.021m** | **LPA/PZA 69.468m** | AGSO 11.084m | MPA 9.457m | HVZ 6.994m | ZBA 4.467m | VESPA 3.603m | INTI 1.210m | OVE 0.403m | CIA 0.363m.
  - Closes Digipolis member-share residual; aligns with AGB total 245.6m (recharges fund AGB).
  - Note: stad omzet 138m ≠ city ebesluit partial lock 38.8m (subset/timing); not double-count AGB as pure city opex.
  - Mons BI2026 still not public this tick (FOI ready).
- Wrote: sources 1; budgets 13; cmt 1; lb 3; foi note; rq_218=done; seeded **rq_219**.
- FOI: project L5 within Digipolis + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_219**; deferred **rq_116** SWA.
"""
if "tick 226" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick226")
