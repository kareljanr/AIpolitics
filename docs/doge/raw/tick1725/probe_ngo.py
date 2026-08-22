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

print("FOS", cdn("2026-00164086"))
print("Rikolto new", cdn("2026-00258870"))

# northdata Rikolto Belgie operational
for name,url in [
 ("FOS","https://www.northdata.com/?query=FOS+socialistische+solidariteit"),
 ("Rikolto","https://www.northdata.com/Rikolto%20Belgi%C3%AB%20VZW,%20Leuven/KBO%200420.656.336"),
 ("Willemsfonds","https://www.northdata.com/?query=Willemsfonds+VZW"),
 ("Broederlijk","https://www.northdata.com/?query=Broederlijk+Delen"),
 ("Trias","https://www.northdata.com/?query=Trias+VZW+Leuven"),
 ("PlanBE","https://www.northdata.com/?query=Plan+International+Belgie"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=25) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        links=re.findall(r'href="(/[^"]*KBO%20[0-9.]+[^"]*)"', html)[:3]
        print(name, "deps", deps[-8:], "links", links)
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))
