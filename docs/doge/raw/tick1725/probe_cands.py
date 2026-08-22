import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def head(u):
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

# candidates with known or guessed deposits / KBOs from recent notes
cands = [
 # Algemeen Boerensyndicaat ABS
 ("ABS northdata","https://www.northdata.com/A.B.S.%20VZW,%20Roeselare/KBO%200414.798.130"),
 ("BVAS search","https://www.northdata.com/BVAS"),
]
# probe companyweb/northdata for ABS
for name,url in [
 ("ABS", "https://www.northdata.com/Algemeen%20Boerensyndicaat%20VZW,%20Roeselare/KBO%200414.798.130"),
 ("ABS2", "https://www.companyweb.be/nl/0414798130/algemeen-boerensyndicaat"),
 ("BVAS", "https://www.companyweb.be/nl/search?q=BVAS+artsensyndicaat"),
 ("POV", "https://www.companyweb.be/nl/0445224456/provinciaal-onderwijs-vlaanderen"),
 ("GO", "https://www.companyweb.be/nl/search?q=GO+onderwijs+vlaamse"),
 ("APEFE", "https://www.companyweb.be/nl/search?q=APEFE"),
 ("VLOR", "https://www.companyweb.be/nl/search?q=Vlaamse+Onderwijsraad"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "len", len(html), "deps", deps[-10:])
        # financial year hints
        for m in re.finditer(r"Laatste balansjaar.{0,80}|Last balance sheet year.{0,80}|neergelegd op.{0,40}", html, re.I|re.S):
            print(" ", re.sub(r"\s+"," ", m.group(0))[:120])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))
