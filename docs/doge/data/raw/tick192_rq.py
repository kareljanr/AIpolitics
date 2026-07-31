from pathlib import Path
import re
p = Path("docs/doge/data/research_queue.csv")
raw = p.read_bytes()
for enc in ["utf-8", "utf-8-sig", "cp1252", "latin-1"]:
    try:
        t = raw.decode(enc)
        break
    except Exception:
        pass
m = re.search(r"^rq_187,.*$", t, re.M)
if not m:
    raise SystemExit("rq_187 missing")
new = (
    'rq_187,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Liege Airport PMV dual Antwerp register Mons BI2026 FPS taxex) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_pmv_l5_stakes,2026-07-28T13:45:00Z,2026-07-28T14:05:00Z,'
    '"tick192: PMV managed 1.941bn invested 1.332bn net 32.5m invest 393m Gigarant 695m dual SFPIM; FOI L5 ready; Port residual; spawn rq_188"'
)
seed = (
    'rq_188,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Liege Airport Antwerp register Mons BI2026 FPS taxex) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T14:05:00Z,,'
    '"Spawned tick192 after PMV; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
