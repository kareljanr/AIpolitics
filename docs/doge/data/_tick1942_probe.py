from pathlib import Path
import re

raw = Path(__file__).resolve().parent / "raw"

ar = (raw / "tick1942_synatom_ar.html").read_text(encoding="utf-8", errors="replace")
text = re.sub(r"<script[^>]*>.*?</script>", " ", ar, flags=re.I | re.S)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)
print("AR", text[:2500])
print("---links---")
for m in re.finditer(r'href=["\']([^"\']+)["\']', ar):
    h = m.group(1)
    if any(x in h.lower() for x in ["pdf", "2025", "2024", "report", "account", "jaar"]):
        print(h)

k = (raw / "tick1942_synatom_kbo.html").read_text(encoding="utf-8", errors="replace")
kt = re.sub(r"<[^>]+>", " ", k)
kt = re.sub(r"\s+", " ", kt)
print("KBO", kt[:2500])

cw = (raw / "tick1942_synatom_cw.html").read_text(encoding="utf-8", errors="replace")
for pat in [
    r"neergelegd op [^.<]{5,40}",
    r"Laatste balansjaar[^<]{0,40}",
    r"Personeel[^€]{0,80}",
]:
    for m in re.finditer(pat, cw, flags=re.I):
        print("HIT", m.group(0)[:120])

# FAQ omzet exact
m = re.search(r"omzet van € ([0-9.]+)", cw)
print("FAQ omzet", m.group(1) if m else None)
# check for assets keywords in CW
cwt = re.sub(r"<[^>]+>", " ", cw)
cwt = re.sub(r"\s+", " ", cwt)
for label in ["Balanstotaal", "Totale activa", "EBITDA", "kapitaal", "aanbestedende"]:
    i = cwt.lower().find(label.lower())
    if i >= 0:
        print(label, "->", cwt[i : i + 160])
