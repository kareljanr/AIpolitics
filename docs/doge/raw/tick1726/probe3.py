import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

# companyweb BVAS / VAS
for name,url in [
 ("BVAS","https://www.companyweb.be/nl/0411100351/belgische-vereniging-van-artsensyndicaten-association-belge-des-syndicats-medicaux"),
 ("VAS","https://www.companyweb.be/nl/0422285243/vlaams-artsensyndicaat"),
 ("SVH","https://www.companyweb.be/nl/0455509822/syndicaat-van-vlaamse-huisartsen"),
 ("BosgroepIJzer","https://www.companyweb.be/nl/0816706346/bosgroep-ijzer-en-leie"),
 ("POV","https://www.companyweb.be/nl/0445224456/provinciaal-onderwijs-vlaanderen"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        print(name, "len", len(html))
        for pat in [r"Laatste balansjaar.{0,100}", r"neergelegd op.{0,60}", r"Brutomarge.{0,80}", r"2025.{0,50}", r"geen jaarrekening"]:
            m=re.search(pat, html, re.I|re.S)
            if m:
                print(" ", re.sub(r"\s+"," ", m.group(0))[:140])
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))

# AGB Hulshout / leftover city AGB pages
for name,url in [
 ("Hulshout","https://www.hulshout.be/"),
 ("AGB search","https://www.google.com/search?q=AGB+jaarrekening+2025+BBC+filetype:pdf+site:.be"),
]:
    pass

# try Dommelhof / leftover EVA
for name,url in [
 ("Dommelhof","https://www.northdata.com/?query=Dommelhof"),
 ("HVZMidwest","https://www.northdata.com/?query=Hulpverleningszone+Midwest+OR+Brandweerzone+Midwest"),
 ("HVZFluvia","https://www.northdata.com/?query=Hulpverleningszone+Fluvia"),
 ("IOEDWinAr","https://www.northdata.com/?query=WinAr+erfgoed"),
 ("IOEDErfpunt","https://www.northdata.com/?query=Erfpunt"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:4]
        print(name, "deps", deps[-6:], "links", links[:3])
    except Exception as e:
        print(name, "FAIL", type(e).__name__)
