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
    "entity_id": "city_steenokkerzeel",
    "name_nl": "Gemeente Steenokkerzeel",
    "name_fr": "Commune de Steenokkerzeel",
    "name_en": "Municipality of Steenokkerzeel",
    "level": "municipality",
    "parent_id": "vlaanderen_gov",
    "community_language": "nl",
    "website": "https://www.steenokkerzeel.be",
    "foi_email": "info@steenokkerzeel.be",
    "foi_postal": "Orchideeenlaan 17 1820 Steenokkerzeel",
    "notes": "tick1298 JR2025 GE residual (updated from tick1167 stub); KBO 0206.561.993; NIS 23094; 7 VE; AD Heidi Abeloos / FD Luk Vandeuren / burgemeester Kurt Ryon; assets 95.073m fin debt 2.492m IGS reval 9.510m AFM -0.051m OCMW equity 0.039m / cum -1.428m NEG; AGB sibling agb_steenokkerzeel already 1167 (T5 EVA 0); FOI ready",
}
before = (DATA/"entities.csv").stat().st_size
patch_id_line(DATA/"entities.csv", "city_steenokkerzeel", city_row)
after = (DATA/"entities.csv").stat().st_size
print("city patched", before, "->", after)
n = append_rows(DATA/"entities.csv", [{
    "entity_id": "ocmw_steenokkerzeel",
    "name_nl": "OCMW Steenokkerzeel",
    "name_fr": "CPAS de Steenokkerzeel",
    "name_en": "OCMW Steenokkerzeel",
    "level": "municipality",
    "parent_id": "city_steenokkerzeel",
    "community_language": "nl",
    "website": "https://www.steenokkerzeel.be",
    "foi_email": "info@steenokkerzeel.be",
    "foi_postal": "Orchideeenlaan 17 1820 Steenokkerzeel",
    "notes": "tick1298 JR2025 GE residual; KBO 0212.173.345; 2 VE; voorzitter Kurt Ryon; J3 expl -1.168m / T5 cum PnL -1.428m NEG / equity 0.039m; tussenkomst 1.195m; FOI ready",
}])
print("ocmw", n)
