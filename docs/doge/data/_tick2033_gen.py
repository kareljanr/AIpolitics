from pathlib import Path

src = Path("docs/doge/data/_tick2032_write.py").read_text(encoding="utf-8")
out = src
out = out.replace("rq_2033", "rq_2034")
out = out.replace('ticks_completed"] = "2032"', 'ticks_completed"] = "2033"')
out = out.replace("ticks=2032", "ticks=2033")
out = out.replace("tick2032", "tick2033")
out = out.replace("Tick 2032", "Tick 2033")
out = out.replace("**tick:** 2032", "**tick:** 2033")
out = out.replace("rq_2032", "rq_2033")
out = out.replace(
    "after **rq_2031 WZC St Vincentius Antwerpen/Ekeren**",
    "after **rq_2032 WZC OLV Lourdes Kortenberg**",
)
out = out.replace(
    "after WZC St Vincentius Antwerpen/Ekeren",
    "after WZC OLV Lourdes Kortenberg",
)
out = out.replace(
    "Do not redo Vincentius Antwerpen/Rillaar",
    "Do not redo Lourdes/Vincentius Antwerpen/Rillaar",
)
out = out.replace(
    "Do NOT redo Cassiers WZC, WZC St Vincentius",
    "Do NOT redo Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius",
)
out = out.replace('UTC = "2026-08-24T12:45:00Z"', 'UTC = "2026-08-24T12:55:00Z"')
out = out.replace(
    "leftover dual hole-fill after WZC St Vincentius Antwerpen/Ekeren — Cassiers WZC YE2025 Medium",
    "leftover dual hole-fill after WZC OLV Lourdes Kortenberg — Cassiers WZC YE2025 Medium",
)
out = out.replace(
    "Lourdes Kortenberg YE2025 / OLVA Antwerpen YE2025",
    "OLVA Antwerpen YE2025",
)
out = out.replace(
    "Bernardus Assenede / OLV Roosdaal / Lourdes / OLVA / Triest",
    "Bernardus Assenede / OLV Roosdaal / OLVA / Triest",
)
out = out.replace(
    "Bernardus Assenede-OLV Roosdaal-Lourdes-OLVA-Triest",
    "Bernardus Assenede-OLV Roosdaal-OLVA-Triest",
)
Path("docs/doge/data/_tick2033_write.py").write_text(out, encoding="utf-8")
assert 'ticks_completed"] = "2033"' in out
assert "rq_2033" in out and "rq_2034" in out
print("ok", len(out))
