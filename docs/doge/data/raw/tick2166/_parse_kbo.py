import re
kbo = open("docs/doge/data/raw/tick2166/avondvrede_kbo.html", encoding="utf-8", errors="replace").read()
# strip tags loosely
text = re.sub(r"<script[\s\S]*?</script>", " ", kbo, flags=re.I)
text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text)
for needle in ["Status", "Rechtstoestand", "Rechtsvorm", "Adres", "Zetel", "NACE", "Vestiging", "aanbested", "Naam", "Actief", "NV", "SA", "0446"]:
    i = text.lower().find(needle.lower())
    if i >= 0:
        print(text[max(0,i-30):i+120])
        print("---")

en = open("docs/doge/data/raw/tick2166/avondvrede_en.html", encoding="utf-8", errors="replace").read()
idx = en.find("kernCijfers")
print("EN kern:", repr(en[idx:idx+500])[:500])
m = re.search(r"filed on [^.<]{5,40}", en, re.I)
print("filed", m.group(0) if m else None)
m = re.search(r"([0-9]+\.[0-9])\s*FTE", en)
print("FTE en", m.group(0) if m else None)

# VE count - look for vestigingseenhed
for pat in [r"([0-9]+)\s*vestiging", r"Number of establishments[^0-9]{0,20}([0-9]+)", r"I[^\w]?E[^\w]?:\s*([0-9]+)"]:
    print(pat, re.findall(pat, kbo, re.I)[:3])
