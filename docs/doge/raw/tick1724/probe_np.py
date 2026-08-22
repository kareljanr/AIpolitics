import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
req=urllib.request.Request("https://www.natuurpunt.be/dit-is-natuurpunt/jaarverslag", headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
links=re.findall(r'href="([^"]+\.pdf)"', html, re.I)
print("PDF links:", links[:30])
links2=re.findall(r"https?://[^\s\"']+\.pdf", html, re.I)
print("abs:", links2[:20])
for m in re.finditer(r".{0,60}(jaarverslag|Jaarverslag Natuurpunt).{0,160}", html):
    print("CTX:", re.sub(r"\s+"," ", m.group(0))[:250])
