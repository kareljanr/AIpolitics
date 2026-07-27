# tick225: Digipolis AGB MJP 2026 personnel + full institutional totals
from pathlib import Path
import re

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# --- sources ---
src_path = data / "sources.csv"
src_add = (
    "src_digipolis_mjp_2026,AG Digipolis Antwerpen MJP 2026-2031 full AGB budget,"
    "https://ebesluit.antwerpen.be/document/69206dd6a60702536ea897d0,"
    "AG Digipolis / Stad Antwerpen MJP 2026-2031,2026-07-29,official_budget,"
    '"Total uitg 245.610m 2026 (exp 244.879 + inv 0.731); personnel 45.458m '
    '(vast 0.152 + contract 43.715 + other 1.591); goederen 198.878m; debt 15.063m; '
    'treasury advance city 22m 2026; VTE max 329 + internalise 7.3m; tick225"\n'
)
text = src_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_digipolis_mjp_2026" not in text:
    src_path.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud_path = data / "budgets.csv"
bud_add = """bud_digipolis_agb_total_2026,digipolis_antwerpen,2026,245610183,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis full MJP total uitgaven 245.610m 2026 (cost-sharing entity not city-only)
bud_digipolis_agb_exp_2026,digipolis_antwerpen,2026,244878864,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis exploitatie-uitgaven 244.879m 2026
bud_digipolis_agb_invest_2026,digipolis_antwerpen,2026,731319,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis immateriele invest 0.731m 2026
bud_digipolis_personnel_2026,digipolis_antwerpen,2026,45457636,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis personnel (bezoldigingen) 45.458m 2026 residual filled
bud_digipolis_personnel_contract_2026,digipolis_antwerpen,2026,43715012,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis contract personnel 43.715m of 45.458m 2026
bud_digipolis_goods_services_2026,digipolis_antwerpen,2026,198877840,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis goederen en diensten 198.878m 2026
bud_digipolis_debt_stock_2026,digipolis_antwerpen,2026,15062689,,,budgeted,src_digipolis_mjp_2026,strong,AG Digipolis financial debt stock 15.063m EOY2026 class (member treasury)
"""
text = bud_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_digipolis_agb_total_2026" not in text:
    bud_path.write_text(text + bud_add, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets already")

# --- commitments ---
cmt_path = data / "commitments.csv"
# fix encoding if needed
raw = cmt_path.read_bytes()
if b"\x97" in raw:
    cmt_path.write_bytes(raw.replace(b"\x97", "\u2013".encode("utf-8")))
cmt_add = (
    "cmt_digipolis_agb_mjp_2026_31,AG Digipolis Antwerpen full institutional MJP multi-year,"
    "digipolis_antwerpen,AG Digipolis Antwerpen,AGB kostendelende vereniging MJP 2026-2031,"
    "2025-12-15,2026,2031,245610183,"
    '"{""2026_total"":245610183,""2026_exp"":244878864,""2026_invest"":731319,'
    '""2026_personnel"":45457636,""2026_goods_services"":198877840,'
    '""2027_total"":257670957,""2028_total"":217780761,""2029_total"":219664932,'
    '""2030_total"":226593798,""2031_total"":229313643,'
    '""personnel_path"":[45457636,48321430,49847064,50502038,51664739,52748886],'
    '""debt_2026"":15062689,""city_treasury_advance_2026"":22000000,'
    '""vte_max_prior"":329,""internalise_savings_legislatuur"":7300000,'
    '""note"":""Strong AGB MJP; total is multi-member cost-sharing not additive with city lock 38.8m alone; '
    'city+PZA+BZA+other members fund via recharges; personnel residual closed""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69206dd6a60702536ea897d0,"
    "Municipal ICT AGB full cost base,Publish member-share matrix L5; open project portfolio,"
    "src_digipolis_mjp_2026,strong,Antwerpen>Digipolis>AGB,tick225\n"
    "cmt_digipolis_personnel_2026_31,AG Digipolis personnel multi-year path,"
    "digipolis_antwerpen,AG Digipolis staff,MJP Schema T2 bezoldigingen,"
    "2025-12-15,2026,2031,45457636,"
    '"{""2026"":45457636,""2027"":48321430,""2028"":49847064,""2029"":50502038,'
    '""2030"":51664739,""2031"":52748886,""2026_contract"":43715012,""2026_vast"":151986,'
    '""2026_other"":1590637,""note"":""Strong T2; closes 2026 personnel residual vs city-side 38.8m lock""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69206dd6a60702536ea897d0,"
    "AGB IT staff cost path,Publish FTE path vs 329 max; internalise 7.3m realisation,"
    "src_digipolis_mjp_2026,strong,Antwerpen>Digipolis>personnel,tick225\n"
)
text = cmt_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_digipolis_agb_mjp_2026_31" not in text:
    cmt_path.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb_path = data / "leaderboard.csv"
lb_add = """lb_digipolis_agb_246m,AG Digipolis Antwerpen full AGB ~245.6m 2026,Flanders,ops,Antwerpen>Digipolis>AGB,245610183,245610183,Strong MJP: total uitg 245.6m (exp 244.9 + inv 0.7); multi-member cost-sharing; city lock 38.8m is city share only,strong,src_digipolis_mjp_2026,City PZA BZA members digital services,Municipal ICT AGB full institutional budget,Core digital ops not pure waste; large vs city opex; dual with prior city/PZA packages; member matrix residual,4,9.0,5,6.9,Publish member-share L5 matrix; open project portfolio,seed,,tick225
lb_digipolis_personnel_45m,AG Digipolis personnel 45.46m 2026,Flanders,ops,Antwerpen>Digipolis>personnel,45457636,52748886,Strong MJP T2: 45.46m 2026 path to 52.75m 2031; contract 43.7m; closes prior personnel residual,strong,src_digipolis_mjp_2026,IT staff serving group Antwerpen,AGB ICT workforce cost,Core ops; internalise consultants path 7.3m savings claim; VTE max 329,3,7.5,5,5.85,Publish FTE realisation vs 329; unit cost KPIs,seed,,tick225
"""
text = lb_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_digipolis_agb_246m" not in text:
    lb_path.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- entities update ---
ent_path = data / "entities.csv"
text = ent_path.read_text(encoding="utf-8")
old_ent = (
    "digipolis_antwerpen,AG Digipolis Antwerpen,Digipolis Anvers,Antwerp municipal ICT AGB cost-sharing,"
    "parastatal,city_antwerpen,nl,https://www.digipolis.be,,,City IT AGB; 2025 city package class ~75.2m + PZA ~53.5m dual; 2024 city 57.6m; tick213"
)
new_ent = (
    "digipolis_antwerpen,AG Digipolis Antwerpen,Digipolis Anvers,Antwerp municipal ICT AGB cost-sharing,"
    "parastatal,city_antwerpen,nl,https://www.digipolis.be,,,AGB MJP 2026 total 245.6m personnel 45.5m; "
    "city lock 38.8m partial; 2025 city~75.2m+PZA~53.5m; tick225"
)
if old_ent in text:
    ent_path.write_text(text.replace(old_ent, new_ent), encoding="utf-8")
    print("entity ok")
elif "digipolis_antwerpen" in text and "245.6m" not in text:
    # loose replace notes field end
    text2 = re.sub(
        r"(digipolis_antwerpen,.*?,,,).*",
        r"\1AGB MJP 2026 total 245.6m personnel 45.5m; city lock 38.8m partial; tick225",
        text,
        count=1,
    )
    if text2 != text:
        ent_path.write_text(text2, encoding="utf-8")
        print("entity loose ok")
    else:
        print("entity skip")
else:
    print("entity already or missing")

# --- research_queue ---
rq_path = data / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    'rq_217,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis 2026 personnel social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:35:00Z,,'
    '"Spawned tick224 after culture 16/16 complete 14.58m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_217,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis 2026 personnel social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:35:00Z,2026-07-29T00:55:00Z,'
    '"tick225: Digipolis AGB MJP total 245.6m personnel 45.46m residual closed; Mons BI2026 still FOI; spawn rq_218"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_218,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 Antwerp Digipolis member-share matrix social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:55:00Z,,'
        '"Spawned tick225 after Digipolis AGB 245.6m personnel 45.5m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq_path.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq not matched")
    idx = text.find("rq_217")
    print(repr(text[idx : idx + 350]) if idx >= 0 else "no rq_217")

# --- foi note ---
foi_path = data / "foi_queue.csv"
text = foi_path.read_text(encoding="utf-8")
old_note = (
    "tick140+204+213-224: AGB packages + culture sample 16/16 houses 14.58m complete; "
    "residual register Digipolis 2026 personnel Mons BI2026 dual VL human send"
)
new_note = (
    "tick140+204+213-225: culture 16/16 14.58m + Digipolis AGB MJP 245.6m personnel 45.5m filled; "
    "residual register member-share matrix Mons BI2026 dual VL human send"
)
if old_note in text:
    foi_path.write_text(text.replace(old_note, new_note), encoding="utf-8")
    print("foi ok")
else:
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("gap_antwerp_subsidies_top20,") and "tick140" in line:
            line = re.sub(
                r"tick140.*$",
                "tick140+204+213-225: Digipolis AGB 245.6m personnel filled; residual register member matrix Mons dual VL human send",
                line.rstrip("\n\r"),
            ) + ("\n" if line.endswith("\n") else "")
            print("foi loose")
        out.append(line)
    foi_path.write_text("".join(out), encoding="utf-8")

# --- loop_state ---
state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:55:00Z,rq_217,225,no,"
    '"Scheduler 60s. Next prio5 rq_218 Mons/member-share/social; rq_116 SWA deferred. '
    'FOI ready human send. tick225 Digipolis AGB 245.6m personnel 45.46m."\n'
)
(data / "loop_state.csv").write_text(state, encoding="utf-8")
print("state ok")

# --- loop_log append (safe) ---
log_path = root / "docs/doge/loop_log.md"
raw = log_path.read_bytes()
# minimal fix lone 0x97 only if present
if b"\x97" in raw:
    out = bytearray()
    i = 0
    while i < len(raw):
        b = raw[i]
        if b < 0x80:
            out.append(b)
            i += 1
        elif 0xC2 <= b <= 0xDF and i + 1 < len(raw) and 0x80 <= raw[i + 1] <= 0xBF:
            out.extend(raw[i : i + 2])
            i += 2
        elif 0xE0 <= b <= 0xEF and i + 2 < len(raw) and all(0x80 <= raw[i + j] <= 0xBF for j in (1, 2)):
            out.extend(raw[i : i + 3])
            i += 3
        elif 0xF0 <= b <= 0xF4 and i + 3 < len(raw) and all(0x80 <= raw[i + j] <= 0xBF for j in (1, 2, 3)):
            out.extend(raw[i : i + 4])
            i += 4
        elif b == 0x97 or b == 0x96:
            out.extend("\u2013".encode())
            i += 1
        else:
            out.append(b if b < 0x80 else ord("?"))
            i += 1
    try:
        text = bytes(out).decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")
else:
    text = raw.decode("utf-8", errors="replace")

entry = """
### 2026-07-29T00:55:00Z - tick 225
- Unit: **rq_217** (FOI-adjacent hole-fill - **AG Digipolis MJP 2026 personnel residual**)
- Found (strong Digipolis MJP 2026-2031 ebesluit PDF):
  - **AG Digipolis total uitgaven 2026 EUR 245.610m** (exp **244.879m** + invest **0.731m**).
  - **Personnel residual closed: EUR 45.458m** 2026 (contract 43.715 + vast 0.152 + other 1.591); path to **52.749m** 2031.
  - Goederen/diensten **198.878m**; debt stock **15.063m**; city treasury advance **22m** 2026 (from 25m 2025).
  - VTE max kader 329; internalisation savings path **7.3m** legislatuur (claim in MJP).
  - Note: city ebesluit lock **38.8m** is city-share only; AGB 245.6m is multi-member cost-sharing (not pure additive city opex).
  - Mons BI2026 public PDF still not found this tick (FOI remains ready).
- Wrote: sources 1; budgets 7; cmt 2; lb 2; entity note; foi note; rq_217=done; seeded **rq_218**.
- FOI: Digipolis member-share matrix + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_218**; deferred **rq_116** SWA.
"""
if "tick 225" not in text:
    log_path.write_text(text.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick225")
