import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# GO! jaarverslag page
for url in [
 "https://www.vlaanderen.be/publicaties/jaarverslag-go-onderwijs-van-de-vlaamse-gemeenschap",
 "https://pro.g-o.be/",
 "https://www.g-o.be/over-go/organisatie/",
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        pdfs=re.findall(r'href="([^"]+\.pdf)"', html, re.I)
        print(url, "pdfs", pdfs[:10], "len", len(html))
        for m in re.finditer(r".{0,40}(jaarverslag|financ|begroting|budget).{0,80}", html, re.I):
            s=re.sub(r"\s+"," ", m.group(0))
            if "pdf" in s.lower() or "2024" in s or "2025" in s:
                print(" CTX", s[:180])
    except Exception as e:
        print(url, "FAIL", type(e).__name__, getattr(e,"code",None))

# Bosgroep residual - find unused with CDN
for name,url in [
 ("BosgroepOVL","https://www.northdata.com/?query=Bosgroep+Oost-Vlaanderen"),
 ("BosgroepLimburg","https://www.northdata.com/?query=Bosgroep+Limburg"),
 ("BosgroepKoepel","https://www.northdata.com/?query=Bosgroepen+Vlaanderen"),
 ("HVZMidwest","https://www.northdata.com/?query=Hulpverleningszone+Midwest"),
 ("HVZFluvia","https://www.northdata.com/?query=Hulpverleningszone+Fluvia"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:4]
        print(name, "deps", deps[-6:], "links", links)
    except Exception as e:
        print(name, "FAIL", type(e).__name__)
