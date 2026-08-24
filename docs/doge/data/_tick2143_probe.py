# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, re, ssl, csv
from pathlib import Path
csv.field_size_limit(10**7)
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
def get(url):
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
        return r.read().decode("utf-8","replace")
text=(Path("docs/doge/data/entities.csv").read_text(encoding="utf-8",errors="replace")+Path("docs/doge/data/leaderboard.csv").read_text(encoding="utf-8",errors="replace")).lower()
# DDG
q='site:companyweb.be/en "nursing homes" "Last balance sheet year 2025"'
page=get("https://html.duckduckgo.com/html/?q="+urllib.parse.quote(q))
links=[]
for l in re.findall(r"uddg=([^&\"]+)", page):
    u=urllib.parse.unquote(l)
    if "companyweb.be" in u and "/en/" in u:
        links.append(u.split("&")[0])
print("ddg links", len(links))
for u in links[:20]:
    print(" ", u[:140])
# also try companyweb search
try:
    s=get("https://www.companyweb.be/en/search?q=maison+de+repos")
    print("cw search len", len(s), "title", re.search(r"<title>([^<]+)", s).group(1)[:80] if re.search(r"<title>", s) else None)
    hrefs=re.findall(r'href="(/en/\d{10}/[^"]+)"', s)
    print("hrefs", len(hrefs), hrefs[:10])
except Exception as e:
    print("cw search ERR", e)
# REW probe alternate
for name,url in [
 ("rew1","https://www.companyweb.be/en/0200931936"),
 ("rew2","https://www.companyweb.be/en/0200.931.936".replace(".","")),
 ("rew3","https://www.companyweb.be/fr/0200931936"),
]:
    try:
        h=get(url)
        years=re.findall(r"\n(202[0-9])\s*:", h)
        m=re.search(r"Last balance sheet year[^0-9]*([0-9]{4})", h, re.I)
        print(name, "years", years[:5], "last", m.group(1) if m else None, re.search(r"<title>([^<]+)", h).group(1)[:70])
    except Exception as e:
        print(name, "ERR", type(e).__name__, e)
