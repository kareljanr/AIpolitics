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
m = re.search(r"^rq_184,.*$", t, re.M)
if not m:
    raise SystemExit("rq_184 missing")
new = (
    'rq_184,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_skeyes_bs_2025,2026-07-28T12:45:00Z,2026-07-28T13:05:00Z,'
    '"tick189: skeyes ANS omzet 335.2m profit 15.4m equity ~308m COVID loan 110m correction 195m dual airports; FOI 2025 BS ready; Port residual; spawn rq_185"'
)
seed = (
    'rq_185,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority North Sea Port Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T13:05:00Z,,'
    '"Spawned tick189 after skeyes; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
