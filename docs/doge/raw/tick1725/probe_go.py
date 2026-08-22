import urllib.request, ssl, re, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# find GO! JR PDF link from publication page JSON/HTML
url="https://www.vlaanderen.be/publicaties/jaarverslag-go-onderwijs-van-de-vlaamse-gemeenschap"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
# look for document links
for pat in [r'https:\\?/\\?/[^"\\]+\.pdf', r'href="([^"]+)"']:
    found=re.findall(pat, html)
    pdfs=[x for x in found if ".pdf" in x.lower() or "publicaties" in x.lower()]
    print("pat", pat[:20], "n", len(pdfs))
    for p in pdfs[:15]:
        print(" ", p[:200])

# also search assets.vlaanderen / publicaties CDN
for m in re.finditer(r".{0,30}(document|download|pdf|jaarverslag).{0,100}", html, re.I):
    s=re.sub(r"\s+"," ", m.group(0))
    if "http" in s or "pdf" in s.lower():
        print("CTX", s[:220])
