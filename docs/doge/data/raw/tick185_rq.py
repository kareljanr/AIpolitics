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
m = re.search(r"^rq_180,.*$", t, re.M)
if not m:
    for line in t.splitlines():
        if "rq_180" in line:
            print(repr(line[:200]))
    raise SystemExit("rq_180 missing")
new = (
    'rq_180,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Antwerp register Mons BI2026 FPS taxex Port Antwerp-Bruges other large FOI-adjacent SOEs) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_bio_l5_portfolio,2026-07-28T11:25:00Z,2026-07-28T11:45:00Z,'
    '"tick185: BIO AR2025 assets 1.196bn equity 1.176bn net 9.0m dividend 4.5m approvals 235m cost of risk 20.1m dual Enabel; FOI L5 ready; Port financials thin public; spawn rq_181"'
)
seed = (
    'rq_181,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges financial authority accounts Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent SOEs) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T11:45:00Z,,'
    '"Spawned tick185 after BIO; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
