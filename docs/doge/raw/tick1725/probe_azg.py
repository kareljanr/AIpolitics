import urllib.request, ssl, re, os
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
# AZG / MSF Belgium
for url in [
 "https://www.northdata.com/Artsen%20Zonder%20Grenzen%20VZW,%20Elsene/KBO%200421.446.093",
 "https://www.companyweb.be/nl/0421446093/artsen-zonder-grenzen",
]:
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        html=resp.read().decode("utf-8","replace")
    deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
    print(url.split("/")[2], "deps", deps[-10:], "len", len(html))

# probe AZG CDN candidates from northdata
url="https://www.northdata.com/Artsen%20Zonder%20Grenzen%20VZW,%20Elsene/KBO%200421.446.093"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
print("AZG deps", deps)

def cdn(dep, year=None):
    y=year or dep[:4]
    u=f"http://cdn.staatsbladmonitor.be/{y}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

for d in deps[::-1][:5]:
    print(d, cdn(d))
