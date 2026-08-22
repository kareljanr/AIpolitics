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

for name,url in [
 ("BVAS","https://www.northdata.com/Belgische%20Vereniging%20Van%20Artsensyndicaten%20-%20Association%20Belge%20des%20Syndicats%20Medicaux,%20Watermaal-Bosvoorde/KBO%200411.100.351"),
 ("VAS","https://www.northdata.com/Vlaams%20Artsensyndicaat%20VZW,%20Antwerpen/KBO%200422.285.243"),
 ("SVH","https://www.northdata.com/Syndicaat%20Van%20Vlaamse%20Huisartsen%20VZW,%20Zeebrugge/KBO%200455.509.822"),
 ("BosgroepIJzer","https://www.northdata.com/Bosgroep%20IJzer%20en%20Leie%20VZW,%20Ieper/KBO%200816.706.346"),
 ("JABS","https://www.northdata.com/Jong%20Algemeen%20Boerensyndicaat%20VZW,%20Roeselare/KBO%201008.752.785"),
]:
    try:
        req=urllib.request.Request(url, headers=ua)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            html=resp.read().decode("utf-8","replace")
        deps=sorted(set(re.findall(r"20\d{2}-\d{8}", html)))
        print(name, "deps", deps[-10:])
        for d in deps[::-1]:
            if d.startswith("2026-") or d.startswith("2025-"):
                y=d[:4]
                print(" ", d, cdn(d, y if y=="2025" else "2026"))
                if d.startswith("2026-"):
                    break
    except Exception as e:
        print(name, "FAIL", type(e).__name__, getattr(e,"code",None))
