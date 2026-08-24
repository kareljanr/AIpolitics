# -*- coding: utf-8 -*-
import csv
csv.field_size_limit(10**7)
with open("docs/doge/data/entities.csv", encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
for n in [
    "sint_jozef_aarschot",
    "0413055989",
    "sint-barbara",
    "herselt",
    "de_foyer",
    "maria_s_rustoord",
    "de_linde",
    "kanunnik_triest",
    "onze_lieve_vrouw_roosdaal",
    "0421031171",
    "hydrobru",
    "vivaqua",
]:
    hits = [
        r.get("entity_id")
        for r in rows
        if n.replace("_", "") in (r.get("entity_id") or "").lower().replace("_", "")
        or n.replace("_", " ") in (r.get("name_nl") or "").lower()
        or n in (r.get("kbo") or "")
        or n in (r.get("notes") or "")
    ]
    print(n, "->", hits[:5] if hits else "MISSING")
