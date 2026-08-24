from pathlib import Path

src = Path("docs/doge/data/raw/tick2346/_src.py").read_text(encoding="utf-8")
if src.startswith("\ufeff"):
    src = src[1:]
repls = [
    ('UTC = "2026-08-28T03:40:00Z"', 'UTC = "2026-08-28T03:50:00Z"'),
    ('RQ = "rq_2345"', 'RQ = "rq_2347"'),
    ('RQ_NEXT = "rq_2346"', 'RQ_NEXT = "rq_2348"'),
    ('TICK = "2345"', 'TICK = "2346"'),
    ("raw/tick2345", "raw/tick2346"),
    ("after Blijdorp@2344", "after Staf@2345"),
    ("After Blijdorp@2344", "After Staf@2345"),
    (
        "Do NOT redo De Korenbloem/Blijdorp/Perrekes/Aurelia stack.",
        "Do NOT redo De Korenbloem/Staf/De Lier/Blijdorp/De Ark stack.",
    ),
    (
        "Do NOT redo De Korenbloem/Blijdorp/Huis Perrekes/Aurelia/Huize Eyckerheyde stack.",
        "Do NOT redo De Korenbloem/Staf/De Lier/Blijdorp/De Ark/Aurelia stack.",
    ),
]
for a, b in repls:
    src = src.replace(a, b)

inject = """# assert budgets not truncated
with open(ROOT / "budgets.csv", encoding="utf-8", newline="") as _f:
    _n = sum(1 for _ in _f) - 1
if _n < 50000:
    raise SystemExit(f"budgets truncated ({_n}); abort")

"""
marker = 'append_csv(\n    ROOT / "commitments.csv"'
if "budgets truncated" not in src:
    src = src.replace(marker, inject + marker)

out = Path("docs/doge/data/raw/tick2346/write_tick2346.py")
out.write_text(src, encoding="utf-8")
print("wrote", out, "bytes", out.stat().st_size)
for i, line in enumerate(src.splitlines(), 1):
    if any(x in line for x in ("RQ =", "RQ_NEXT", "TICK =", "UTC =", "claimable", "budgets truncated", "OK tick")):
        print(f"{i}:{line[:130]}")
