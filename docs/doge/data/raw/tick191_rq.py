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
m = re.search(r"^rq_186,.*$", t, re.M)
if not m:
    raise SystemExit("rq_186 missing")
new = (
    'rq_186,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T13:25:00Z,2026-07-28T13:45:00Z,'
    '"tick191: SOFICO RA2024 op rev 495.1m net 100.7m invest 265m PKPL 347m infra 2.58bn dual VL roads; Port residual; spawn rq_187"'
)
seed = (
    'rq_187,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Liege Airport PMV dual Antwerp register Mons BI2026 FPS taxex) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T13:45:00Z,,'
    '"Spawned tick191 after SOFICO; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
