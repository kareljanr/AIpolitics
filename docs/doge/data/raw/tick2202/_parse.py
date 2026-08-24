from pathlib import Path
import re
import csv
import time

# claim queue
p = Path("docs/doge/data/research_queue.csv")
csv.field_size_limit(10**7)
for attempt in range(5):
    try:
        with p.open(newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            cols = r.fieldnames
            rows = list(r)
        for row in rows:
            if row["task_id"] == "rq_2202":
                print("rq_2202 status", row["status"])
                if row["status"] in ("open", "in_progress"):
                    row["status"] = "in_progress"
                    row["updated_utc"] = "2026-08-26T13:20:00Z"
        with p.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print("claim ok")
        break
    except OSError as e:
        print("retry", e)
        time.sleep(1)

ent = Path("docs/doge/data/entities.csv").read_text(encoding="utf-8").lower()
for n in ["0407.201.941", "0407201941", "kaliber", "0454.426.489", "kromme"]:
    print(n, "ENT" if n.lower() in ent else "FREE")


def parse(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    print("====", path)
    m = re.search(r"filed on ([0-9-]+)", text)
    print("filed", m.group(1) if m else None)
    m = re.search(r"total turnover of .([0-9.,]+)", text)
    print("faq", m.group(1) if m else None)
    print("empty", bool(re.search(r"did not publish any turnover", text, re.I)))
    parts = re.split(r'title="Section [^"]+"', text)
    for part in parts[1:8]:
        lab = re.search(r">\s*([A-Za-z /]+)<", part[:500])
        euros = re.findall(r"<span>€\s*</span>\s*<span>\s*([0-9.,\s-]+)</span>", part)
        plain = re.findall(r"<span>([0-9]+(?:[.,][0-9]+)?)</span>", part)
        pct = re.findall(r"<span>([+-]?[0-9]+,[0-9]+%)</span>", part)
        print(lab.group(1).strip() if lab else "?", euros[:4], plain[:4], pct[:3])


parse("docs/doge/data/raw/tick2202/kaliber.html")
parse("docs/doge/data/raw/tick2202/kromme.html")
