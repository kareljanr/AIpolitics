import re
from pathlib import Path
from pypdf import PdfReader
import ssl
import urllib.request

out = Path("docs/doge/raw/tick1752")

html = (out / "rand_contact.html").read_text(encoding="utf-8")
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)
print("CONTACT TEXT SNIPS:")
for pat in [
    r".{0,50}Brecht.{0,100}",
    r".{0,40}financi.{0,100}",
    r".{0,40}Zonehuis.{0,100}",
    r".{0,40}Overbroek.{0,100}",
    r".{0,40}Westdijk.{0,100}",
]:
    for m in re.finditer(pat, text, re.I):
        print(" ", m.group(0)[:180])

bh = (out / "rand_begroting.html").read_text(encoding="utf-8")
links = re.findall(r'href=["\']([^"\']+)["\']', bh)
print("BEGROTING LINKS:")
for l in links:
    if re.search(r"begrot|motivat|pdf|storage|download|file", l, re.I):
        print(" ", l)

kh = (out / "kbo_rand.html").read_text(encoding="utf-8")
kt = re.sub(r"<[^>]+>", " ", kh)
kt = re.sub(r"\s+", " ", kt)
idx = kt.lower().find("adres")
print("KBO around adres:", kt[idx : idx + 500] if idx >= 0 else kt[:900])

r = PdfReader(str(out / "justel_mu_2025.pdf"))
for i in [28, 29, 30, 31]:
    t = r.pages[i].extract_text() or ""
    print("==== page", i + 1, "====")
    print(t[:4500])
    print()

# Download begroting 2026 PDFs if found
ctx = ssl.create_default_context()
ua = {"User-Agent": "Mozilla/5.0"}
base = "https://www.brandweerzonerand.be"
for l in links:
    if re.search(r"begrot|motivat", l, re.I) and ("pdf" in l.lower() or "storage" in l.lower() or "download" in l.lower() or l.endswith(".pdf")):
        url = l if l.startswith("http") else base + l
        name = "rand_" + re.sub(r"[^a-zA-Z0-9]+", "_", l.split("/")[-1])[:60]
        if not name.endswith(".pdf"):
            name += ".pdf"
        try:
            req = urllib.request.Request(url, headers=ua)
            with urllib.request.urlopen(req, timeout=40, context=ctx) as resp:
                data = resp.read()
            (out / name).write_bytes(data)
            print("DL", name, len(data), data[:5])
            if data[:4] == b"%PDF":
                rr = PdfReader(str(out / name))
                print(" pages", len(rr.pages))
                print((rr.pages[0].extract_text() or "")[:1500])
        except Exception as e:
            print("DL FAIL", url, type(e).__name__, str(e)[:100])
