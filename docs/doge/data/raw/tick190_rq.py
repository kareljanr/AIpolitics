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
m = re.search(r"^rq_185,.*$", t, re.M)
if not m:
    raise SystemExit("rq_185 missing")
new = (
    'rq_185,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_sowaer_accounts,2026-07-28T13:05:00Z,2026-07-28T13:25:00Z,'
    '"tick190: SOWAER comptes public assets 491.7m equity 366.9m ventes 47.0m net 0.30m 2025; gap major fill; Port residual; spawn rq_186"'
)
seed = (
    'rq_186,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T13:25:00Z,,'
    '"Spawned tick190 after SOWAER; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
