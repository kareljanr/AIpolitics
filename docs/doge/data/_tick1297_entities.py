# -*- coding: utf-8 -*-
import csv, io, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent

def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()

def patch_id_line(path, id_value, new_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    payload = csv_line(fields, new_row).encode("utf-8")
    raw = path.read_bytes()
    needle = b"\n" + id_value.encode("utf-8") + b","
    idx = raw.find(needle)
    if idx == -1:
        raise SystemExit("id line not found: %s" % id_value)
    start = idx + 1
    end = raw.find(b"\n", start)
    if end == -1:
        end = len(raw)
    ending = b"\n"
    new = raw[:start] + payload + ending + raw[end + 1 :]
    path.write_bytes(new)

def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing = {row.get(fields[0]) for row in reader}
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(fields[0]) in existing:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added

city_row = {
    "entity_id": "city_diepenbeek",
    "name_nl": "Gemeente Diepenbeek",
    "name_fr": "Commune de Diepenbeek",
    "name_en": "Municipality of Diepenbeek",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.diepenbeek.be",
    "foi_email": "info@diepenbeek.be",
    "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
    "notes": "tick1297 JR2025 GE residual (updated from tick1296 stub); KBO 0207.465.974; NIS 71011; 14 VE; AD Jan Dreesen / FD Monique Aerts / burgemeester Rik Kriekels; assets 190.496m fin debt 13.592m IGS reval 19.425m OCMW equity -0.708m NEG; AGB sibling agb_diepenbeek 0885.640.088 already 1296; FOI ready",
}
before = (DATA/"entities.csv").stat().st_size
patch_id_line(DATA/"entities.csv", "city_diepenbeek", city_row)
after = (DATA/"entities.csv").stat().st_size
print("city patched", before, "->", after)
n = append_rows(DATA/"entities.csv", [{
    "entity_id": "ocmw_diepenbeek",
    "name_nl": "OCMW Diepenbeek",
    "name_fr": "CPAS de Diepenbeek",
    "name_en": "OCMW Diepenbeek",
    "level": "municipality",
    "parent_id": "city_diepenbeek",
    "community_language": "nl",
    "website": "https://www.diepenbeek.be",
    "foi_email": "info@diepenbeek.be",
    "foi_postal": "Dorpsstraat 14 3590 Diepenbeek",
    "notes": "tick1297 JR2025 GE residual; KBO 0212.246.787; 4 VE; voorzitter Rik Kriekels; J3 expl -1.554m / T5 cum PnL -7.385m NEG / equity -0.708m NEG; tussenkomst 0; FOI ready",
}])
print("ocmw", n)
