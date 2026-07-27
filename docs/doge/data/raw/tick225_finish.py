# tick225 finish after partial write
from pathlib import Path

data = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
root = Path(r"C:\Users\karel\dev\AIpolitics")

# entities
ent = data / "entities.csv"
raw = ent.read_bytes()
try:
    t = raw.decode("utf-8")
except UnicodeDecodeError:
    t = raw.decode("latin-1")
    ent.write_text(t, encoding="utf-8")
    t = ent.read_text(encoding="utf-8")
    print("entities reencoded")

lines = t.splitlines()
out = []
for line in lines:
    if line.startswith("digipolis_antwerpen,") and "245.6m" not in line:
        if ",,," in line:
            head, _notes = line.rsplit(",,,", 1)
            line = (
                head
                + ",,,AGB MJP 2026 total 245.6m personnel 45.5m; city lock 38.8m partial; "
                "2025 city~75.2m+PZA~53.5m; tick225"
            )
            print("entity updated")
        else:
            print("entity no notes field")
    out.append(line)
ent.write_text("\n".join(out) + "\n", encoding="utf-8")

# research queue
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
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
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_217")
    print(repr(text[i : i + 300]) if i >= 0 else "missing")

# foi
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-224: AGB packages + culture sample 16/16 houses 14.58m complete; "
    "residual register Digipolis 2026 personnel Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-225: culture 16/16 14.58m + Digipolis AGB MJP 245.6m personnel 45.5m filled; "
    "residual register member-share matrix Mons BI2026 dual VL human send"
)
if oldn in ft:
    foi.write_text(ft.replace(oldn, newn), encoding="utf-8")
    print("foi ok")
else:
    print("foi miss")

# state
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:55:00Z,rq_217,225,no,"
    '"Scheduler 60s. Next prio5 rq_218 Mons/member-share/social; rq_116 SWA deferred. '
    'FOI ready human send. tick225 Digipolis AGB 245.6m personnel 45.46m."\n',
    encoding="utf-8",
)
print("state ok")

# log
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
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
if "tick 225" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE finish")
