from pathlib import Path

src = Path("docs/doge/data/raw/tick2351/write_tick2351_talander.py").read_text(encoding="utf-8")
repls = [
    ('TICK = "2351"', 'TICK = "2352"'),
    ('RQ, NEXT = "rq_2351", "rq_2352"', 'RQ, NEXT = "rq_2352", "rq_2353"'),
    ("src_talander_kbo_2351", "src_talander_kbo_2352"),
    ("src_talander_site_contact_2351", "src_talander_site_contact_2352"),
    ("tick2351", "tick2352"),
    ("after Leieborg@2350", "after De Korenbloem@2351"),
    ("Leieborg/Helan", "Korenbloem/Leieborg/Helan"),
    ("04:15:00Z", "04:25:00Z"),
    ("rq_2351 missing", "rq_2352 missing"),
]
for a, b in repls:
    src = src.replace(a, b)
out = Path("docs/doge/data/raw/tick2352/write_tick2352_talander.py")
out.write_text(src, encoding="utf-8")
print("patched", out)
