# -*- coding: utf-8 -*-
from pathlib import Path

src_path = Path("docs/doge/scripts/_tick2330_alma.py")
t = src_path.read_text(encoding="utf-8")
repls = [
    ('TICK="2330"', 'TICK="2332"'),
    ('RQ="rq_2330"', 'RQ="rq_2332"'),
    ('NEXT_RQ="rq_2331"', 'NEXT_RQ="rq_2333"'),
    ("tick2330", "tick2332"),
    ('UTC="2026-08-28T00:55:00Z"', 'UTC="2026-08-28T01:25:00Z"'),
    ("if ticks < 2329:", "if ticks < 2331:"),
    ('NEW_TICKS="2330"', 'NEW_TICKS="2332"'),
    ("EVERY-10 + leftover dual", "leftover dual"),
    ("tick{TICK} EVERY-10", "tick{TICK}"),
    ("after Tandem@2329", "after Mivalti@2331"),
    ("Tandem@2329", "Mivalti@2331"),
    ("src_alma_site_foi_2330", "src_alma_site_foi_2332"),
    ("EVERY-10 leftover dual Alma", "leftover dual Alma"),
    ("**EVERY-10 @ 2330** (next **2340**)", "NOT every-10 (last 2330; next **2340**)"),
    ("spawned after tick{TICK} Alma EVERY-10", "spawned after tick{TICK} Alma"),
    ("print(\"EVERY-10 refreshed\")", "print(\"NOT every-10 skip progress\")"),
]
for a, b in repls:
    t = t.replace(a, b)
t = t.replace(
    '(DATA/"progress_every_10_ticks.md").write_text(f',
    'if False: (DATA/"progress_every_10_ticks.md").write_text(f',
)
t = t.replace(
    '(DATA/"doge_waste_top10_current.md").write_text(f',
    'if False: (DATA/"doge_waste_top10_current.md").write_text(f',
)
Path("docs/doge/scripts/_tick2332_alma.py").write_text(t, encoding="utf-8")
print("wrote _tick2332_alma.py")
