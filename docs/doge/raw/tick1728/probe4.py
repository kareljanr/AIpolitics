import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

# AGB Bornem - any 2025 now?
url="https://www.bornem.be/jaarrekening-gemeente-ocmw-en-agb"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
    html=resp.read().decode("utf-8","replace")
# find file titles
for m in re.finditer(r'file-info__title[^>]*>\s*<span>([^<]+)</span>', html):
    print("FILE", m.group(1))
for m in re.finditer(r'href="([^"]+\.pdf)"', html, re.I):
    print("PDF", m.group(1)[:150])

# try HVZ with official JR
for name,url in [
 ("HVZMidwest","https://www.brandweerzonemidwest.be/"),
 ("HVZFluvia","https://www.hvzfluvia.be/"),
 ("POV","https://pov.be/"),
 ("VCLB","https://www.vclb.be/"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            html=resp.read().decode("utf-8","replace")
        pdfs=re.findall(r'href="([^"]*(?:jaarverslag|jaarrekening|financ)[^"]*\.pdf)"', html, re.I)
        pdfs2=re.findall(r'href="([^"]+\.pdf)"', html, re.I)[:8]
        print(name, "finpdf", pdfs[:5], "pdfs", pdfs2[:5], "len", len(html))
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

# northdata search for unused care/WZC with 2026 deposit
for name,url in [
 ("WZCnew","https://www.northdata.com/?query=woonzorgcentrum+VZW+jaarrekening"),
 ("CLBnet","https://www.northdata.com/?query=Vrij+CLB+netwerk+OR+GO+CLB"),
 ("Leersteun","https://www.northdata.com/?query=Leersteuncentrum+VZW"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:5]
        print(name, "deps", deps[-8:], "links", links)
    except Exception as e:
        print(name, "FAIL", type(e).__name__)
