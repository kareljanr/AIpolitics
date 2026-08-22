import urllib.request, ssl, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn(dep, year="2026"):
    u=f"http://cdn.staatsbladmonitor.be/{year}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0)
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__

# known deferred deposits from prior logs
for dep,label in [
 ("2026-00311716","11.11.11"),
 ("2026-00251141","CNCD"),
 ("2026-00106967","VPP already"),
 ("2026-00377886","Dijk92"),
 ("2026-00394221","NSZ"),
]:
    print(label, dep, cdn(dep))

# northdata probe candidates
for name,url in [
 ("111111","https://www.northdata.com/11.11.11,%20Koepel%20van%20de%20Vlaamse%20Noord-Zuidbeweging%20VZW,%20Brussel/KBO%200421.210.424"),
 ("AmnestyVL","https://www.northdata.com/?id=&query=Amnesty+International+Vlaanderen"),
 ("FOPEM","https://www.northdata.com/?query=FOPEM+VZW"),
 ("CLB","https://www.northdata.com/?query=Vrij+CLB+netwerk"),
 ("ASGB","https://www.northdata.com/?query=ASGB+artsen"),
 ("Cartel","https://www.northdata.com/?query=Kartel+artsensyndicaat"),
]:
    try:
        req=urllib.request.Request(url, headers={**ua,"Accept-Language":"en"})
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "deps", deps[-12:], "len", len(html))
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))
