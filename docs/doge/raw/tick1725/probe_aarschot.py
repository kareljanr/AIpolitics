import urllib.request, ssl, re, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# get AGB Aarschot JR2025 page
url="https://www.aarschot.be/jaarrekening-2025-agb"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
print("len", len(html))
pdfs=re.findall(r'href="([^"]+\.pdf)"', html, re.I)
print("pdfs", pdfs)
# also media/file links
for m in re.finditer(r'href="([^"]+)"[^>]*>[^<]*(jaarrekening|BBC|NBB|download)', html, re.I):
    print("LINK", m.group(1), m.group(0)[:120])
for m in re.finditer(r"/sites/default/files/[^\"]+|media/[^\"]+|documents/[^\"]+", html):
    if "jaar" in m.group(0).lower() or "agb" in m.group(0).lower() or "pdf" in m.group(0).lower():
        print("PATH", m.group(0)[:200])
