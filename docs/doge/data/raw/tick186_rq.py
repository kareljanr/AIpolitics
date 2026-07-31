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
m = re.search(r"^rq_181,.*$", t, re.M)
if not m:
    for line in t.splitlines():
        if "rq_181" in line:
            print(repr(line[:200]))
    raise SystemExit("rq_181 missing")
new = (
    'rq_181,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges financial authority accounts Antwerp register Mons BI2026 FPS taxex other large FOI-adjacent SOEs) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    'gap_bac_balance_sheet,2026-07-28T11:45:00Z,2026-07-28T12:05:00Z,'
    '"tick186: Brussels Airport Co rev 828m EBITDA 356m net 84m CAPEX 302m dividend 41m SFPIM 25pct; FOI BS ready; Port authority still thin; spawn rq_182"'
)
seed = (
    'rq_182,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,'
    '"Prefer public primary fills (Port Antwerp-Bruges authority accounts Charleroi BSCA dual Credendo North Sea Port Antwerp register Mons BI2026 FPS taxex) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ',2026-07-28T12:05:00Z,,'
    '"Spawned tick186 after BAC; rq_116 SWA deferred Oct-Dec 2026"'
)
t2 = t[: m.start()] + new + t[m.end() :]
if not t2.endswith("\n"):
    t2 += "\n"
t2 += seed + "\n"
p.write_bytes(t2.encode(enc))
print("rq ok")
