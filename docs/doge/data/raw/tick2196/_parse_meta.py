from pathlib import Path
import re
import html as H

kbo = Path("docs/doge/data/raw/tick2196/kbo.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", kbo)))
for key in [
    "Adres",
    "Rechtsvorm",
    "Aard van de entiteit",
    "Nace",
    "NACE",
    "Vestigingseenheid",
    "Functies",
    "Afkorting",
    "Status",
    "E-mail",
    "Telefoon",
]:
    i = text.find(key)
    if i >= 0:
        print("---", key, "---")
        print(text[i : i + 400])

print("VE markers", len(re.findall(r"Vestigingseenheidnummer", text)))
# list addresses
for m in re.finditer(r"Adres van de zetel(.{0,200})", text):
    print("ZETEL", m.group(1)[:200])

contact = Path("docs/doge/data/raw/tick2196/contact.html").read_text(
    encoding="utf-8", errors="replace"
)
ct = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", contact)))
emails = re.findall(r"[\w.+-]+@[\w.-]+\.\w+", ct)
print("emails", emails[:15])
print("CONTACT", ct[:1000])

en = Path("docs/doge/data/raw/tick2196/en.html").read_text(encoding="utf-8", errors="replace")
# FTE history if any
for pat in [
    r'amountOfEmployees\s*=\s*"([^"]+)"',
    r"employeesByYear\s*=\s*(\[[^\]]{0,400}\])",
    r"numberOfEmployees[^\n]{0,200}",
]:
    m = re.search(pat, en)
    print("PAT", pat[:30], "->", (m.group(0)[:180] if m else None))

# YoY from page labels
et = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", en)))
for lab in ["Turnover", "Gross margin", "Profit/Loss", "Equity", "Employees"]:
    m = re.search(lab + r".{0,120}?([+\-]?\d[\d.,]*)\s*%", et)
    if m:
        print(lab, "delta%", m.group(1))

# check used entities
import csv

csv.field_size_limit(10**7)
used = False
for name in ["entities.csv", "leaderboard.csv", "commitments.csv"]:
    with open(f"docs/doge/data/{name}", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            blob = "|".join(row.values())
            if "0407657148" in blob.replace(".", "") or "vzw_bwz" in blob or "BWZ" in blob and "Zottegem" in blob:
                print("USED in", name, list(row.values())[0][:80])
                used = True
print("used_flag", used)

# verify loop state + rq_2196
with open("docs/doge/data/loop_state.csv", encoding="utf-8") as f:
    print("STATE", f.read().strip())
with open("docs/doge/data/research_queue.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        if row.get("task_id") in ("rq_2195", "rq_2196"):
            print(row["task_id"], row["status"], row["title"][:90])
