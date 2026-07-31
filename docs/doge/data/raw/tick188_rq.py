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
else:
    raise SystemExit("decode fail")
m = re.search(r"^rq_183,.*$", t, re.M)
if not m:
    raise SystemExit("rq_183 missing")
new = (
    'rq_183,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Credendo export credit Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_credendo_l5_claims,2026-07-28T12:25:00Z,2026-07-28T12:45:00Z,'
    '"tick188: Credendo assets 3.921bn equity 3.302bn GWP 481m comprehensive 257m cover 33bn class; FOI L5 claims ready; Port residual; spawn rq_184"'
)
seed = (
    'rq_184,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T12:45:00Z,,'
    '"Spawned tick188 after Credendo; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
