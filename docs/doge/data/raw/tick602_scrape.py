import re
import urllib.request
from pathlib import Path

urls = [
    "https://www.iweps.be/publication/rapport-dactivite-2024/",
    "https://www.iweps.be/publication/rapport-dactivite-2023/",
    "https://www.iweps.be/",
]
for url in urls:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
        print("url", url, "len", len(html))
        pdfs = re.findall(r"https?://[^\s\"']+\.pdf", html)
        pdfs += re.findall(r"/[^\s\"']+\.pdf", html)
        for p in sorted(set(pdfs))[:25]:
            print(" PDF", p)
        for pat in ["ETP", "budget", "million", "agents", "personnel", "recettes", "dépenses"]:
            if pat.lower() in html.lower():
                print(" has", pat)
    except Exception as e:
        print("fail", url, e)

# try known pdf patterns
candidates = [
    "https://www.iweps.be/wp-content/uploads/2025/07/Rapport-activite-2024.pdf",
    "https://www.iweps.be/wp-content/uploads/2025/07/IWEPS-Rapport-dactivite-2024.pdf",
    "https://www.iweps.be/sites/default/files/2025-07/rapport_activite_2024.pdf",
    "https://www.iweps.be/wp-content/uploads/publications/rapport-dactivite-2024.pdf",
]
for u in candidates:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD")
        r = urllib.request.urlopen(req, timeout=15)
        print("HEAD", r.status, r.headers.get("Content-Type"), u)
    except Exception as e:
        print("no", u, type(e).__name__)
