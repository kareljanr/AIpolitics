import re, html, pathlib, json

out = pathlib.Path("docs/doge/data/raw/tick2212")

def strip_html(t: str) -> list[str]:
    t = re.sub(r"<script[\s\S]*?</script>", " ", t)
    t = re.sub(r"<style[\s\S]*?</style>", " ", t)
    t = re.sub(r"<[^>]+>", "\n", t)
    t = html.unescape(t)
    lines = [re.sub(r"\s+", " ", l).strip() for l in t.splitlines()]
    return [l for l in lines if l]

def parse_fin_table(lines: list[str]) -> dict:
    # Find header years row containing 2025 then metric rows
    data = {}
    for i, l in enumerate(lines):
        if l == "2025" and i + 1 < len(lines) and lines[i + 1] in ("",) or True:
            # look back for metric name within 5 lines
            pass
    # Better: scan for metric labels and capture following euro amounts
    metrics = [
        "Winst/Verlies",
        "Omzet",
        "Eigen vermogen",
        "Brutomarge",
        "Personeel",
        "Profit/Loss",
        "Turnover",
        "Equity",
        "Gross margin",
        "Employees",
        "Bénéfices/pertes",
        "Chiffre d'affaires",
        "Capitaux propres",
        "Marge brute",
        "Personnel",
    ]
    for i, l in enumerate(lines):
        if l in metrics:
            vals = []
            for j in range(i + 1, min(i + 20, len(lines))):
                s = lines[j]
                if s in metrics or s.startswith("Publicat"):
                    break
                # euro amounts like € 11.339.072 or €11,339,072 or percentages skip
                if re.search(r"[€$]|^\d", s) and "%" not in s:
                    # clean
                    nums = re.findall(r"[-−]?\s*[\d.,]+", s)
                    if nums:
                        vals.append(s.strip())
                elif re.fullmatch(r"[-−]?\d+[.,]?\d*", s):
                    vals.append(s)
            data[l] = vals[:4]
    return data

for name in ["odas_nl.html", "odas_en.html", "odas_fr.html"]:
    t = (out / name).read_text(encoding="utf-8", errors="replace")
    lines = strip_html(t)
    print("==", name)
    # key identity
    for key in [
        "Status",
        "Ondernemingsnummer",
        "Btw-plicht",
        "Oprichting",
        "Laatste balansjaar",
        "Bedrijfsgrootte",
        "Hoofdactiviteit",
        "Last balance sheet year",
        "Company size",
        "Main activity",
        "Dernier bilan",
        "Taille d'entreprise",
        "Activité principale",
    ]:
        for i, l in enumerate(lines):
            if l == key and i + 1 < len(lines):
                print(key, "=>", lines[i + 1])
                break
    # address
    for i, l in enumerate(lines):
        if "Pathoeke" in l or "8000" in l and "Brugge" in l:
            print("addr", l)
            break
    # neerlegging FAQ
    for i, l in enumerate(lines):
        if "neergelegd" in l.lower() or "filed on" in l.lower() or "déposés le" in l.lower() or "deposes le" in l.lower():
            print("neer-line", l)
            if i + 1 < len(lines):
                print("neer-next", lines[i + 1])
    fin = parse_fin_table(lines)
    print("FIN", json.dumps(fin, ensure_ascii=False, indent=2))
    # NACE / VE
    for i, l in enumerate(lines):
        if "NACE" in l or "nace" in l or "vestiging" in l.lower() or "establishment" in l.lower() or "unité" in l.lower():
            if len(l) < 120:
                print("meta", l, "|", lines[i + 1] if i + 1 < len(lines) else "")
    print()
