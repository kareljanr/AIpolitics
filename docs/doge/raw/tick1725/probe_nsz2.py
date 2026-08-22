import urllib.request, ssl, re, json
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

# northdata page for PDF / deposit details
url="https://www.northdata.com/Neutraal%20Syndicaat%20voor%20Zelfstandigen%20VZW,%20Brussel/KBO%200410.357.609"
req=urllib.request.Request(url, headers=ua)
with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
    html=resp.read().decode("utf-8","replace")
# look for deposit / pdf / cbso links around 2026-00394221
idx=html.find("2026-00394221")
print("idx", idx)
print(html[max(0,idx-500):idx+800])
print("---")
# all pdf-like
for m in re.finditer(r".{0,80}(pdf|deposit|cbso|consult|staatsblad|2026-00394221).{0,120}", html, re.I):
    s=re.sub(r"\s+"," ", m.group(0))
    if "2026-00394221" in s or "pdf" in s.lower() or "cdn" in s.lower():
        print("CTX", s[:250])

# try alternate CDN hosts
dep="2026-00394221"
alts=[
 f"https://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf",
 f"http://cdn.staatsbladmonitor.be/2026pdf/{dep}.pdf",
 f"https://www.staatsbladmonitor.be/pdf/{dep}.pdf",
 f"https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/{dep}",
]
for u in alts:
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            print("OK", resp.status, resp.getheader("Content-Length"), u)
    except Exception as e:
        print("FAIL", getattr(e,"code",None), type(e).__name__, u)
