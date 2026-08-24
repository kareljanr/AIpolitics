from pathlib import Path
import re


def dig(path: str) -> None:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    print("=" * 60, path)
    # strip tags for FAQ-ish
    plain = re.sub(r"<script[\s\S]*?</script>", " ", text)
    plain = re.sub(r"<style[\s\S]*?</style>", " ", plain)
    plain = re.sub(r"<[^>]+>", " ", plain)
    plain = re.sub(r"\s+", " ", plain)
    for needle in [
        "Status",
        "Closed",
        "Stopgezet",
        "Active",
        "Actief",
        "turnover",
        "omzet",
        "Gross margin",
        "brutomarge",
        "Employees",
        "NACE",
        "Main activity",
        "Hoofdactiviteit",
        "Company size",
        "filed",
        "neergelegd",
    ]:
        idx = plain.lower().find(needle.lower())
        if idx >= 0:
            print(needle, "->", plain[max(0, idx - 20) : idx + 120])
    # emails
    emails = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)))
    print("EMAILS", emails[:15])
    # publications dates
    pubs = re.findall(r"(\d{2}-\d{2}-\d{4})", text)
    print("DATES sample", pubs[:12])


for f in [
    "docs/doge/data/raw/tick2198/boskat_en.html",
    "docs/doge/data/raw/tick2198/boskat_nl.html",
    "docs/doge/data/raw/tick2198/age_en.html",
    "docs/doge/data/raw/tick2198/kbo_boskat.html",
    "docs/doge/data/raw/tick2198/kbo_age.html",
]:
    dig(f)
