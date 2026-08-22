import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# AGB Bornem page - any 2025?
url="https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
pdfs=re.findall(r'href="([^"]+\.pdf)"', html, re.I)
print("pdfs", pdfs)
for m in re.finditer(r".{0,40}(2025|AGB|jaarrekening).{0,80}", html, re.I):
    s=re.sub(r"\s+"," ", m.group(0))
    if "2025" in s or "agb" in s.lower():
        print(s[:180])

# ASGB companyweb
url="https://www.companyweb.be/nl/0429331205/algemeen-syndicaat-van-geneeskundigen-van-belgie"
try:
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        html=resp.read().decode("utf-8","replace")
    print("ASGB len", len(html))
    for m in re.finditer(r"Laatste balansjaar.{0,120}|neergelegd op.{0,80}|Brutomarge.{0,80}|2025.{0,40}", html, re.I|re.S):
        print(re.sub(r"\s+"," ", m.group(0))[:150])
except Exception as e:
    print("ASGB FAIL", e)
