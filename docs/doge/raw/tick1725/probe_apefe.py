import urllib.request, ssl, os, re
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}

def cdn_head(dep, year="2026"):
    u=f"http://cdn.staatsbladmonitor.be/{year}pdf/{dep}.pdf"
    try:
        req=urllib.request.Request(u, method="HEAD", headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, int(resp.getheader("Content-Length") or 0), u
    except Exception as e:
        return getattr(e,"code",None), type(e).__name__, u

print("APEFE", cdn_head("2026-00375176"))
print("APEFE old", cdn_head("2025-00336948", "2025"))

# get ASGB and FARO deposits from northdata company pages
for name,url in [
 ("ASGB","https://www.northdata.com/Algemeen%20Syndicaat%20Van%20Geneeskundigen%20Van%20Belgi%C3%AB%20VZW,%20Kontich/KBO%200429.331.205"),
 ("FARO","https://www.northdata.com/Faro%C2%B7Vlaams%20Steunpunt%20Voor%20Cultureel%20Erfgoed%20VZW,%20Bruxelles/KBO%200893.863.017"),
 ("APEFE","https://www.northdata.com/Association%20Pour%20la%20Promotion%20de%20l'%20Education%20et%20de%20la%20Formation%20%C3%A0%20l'%20Etranger/KBO%200467.325.808"),
]:
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        html=resp.read().decode("utf-8","replace")
    deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
    print(name, "deps", deps[-10:])
    # probe latest 2026
    for d in deps[::-1]:
        if d.startswith("2026-"):
            print(" ", d, cdn_head(d))
            break
