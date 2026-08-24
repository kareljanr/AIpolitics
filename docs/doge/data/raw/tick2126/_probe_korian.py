# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

PATHS = [
    "https://www.pappers.be/fr/recherche?q=Cheveux+d%27Argent",
    "https://www.pappers.be/fr/recherche?q=Le+Chenoy",
    "https://www.pappers.be/fr/recherche?q=Golden+Morgen",
    "https://www.pappers.be/fr/recherche?q=Le+Colvert",
    "https://www.pappers.be/fr/recherche?q=Heris+Soignies",
    "https://www.pappers.be/fr/recherche?q=Bellevue+Forest",
    "https://www.pappers.be/fr/recherche?q=Jardins+d+Astrid+Maurage",
    "https://www.companyweb.be/en/les-cheveux-dargent",
    "https://www.companyweb.be/en/le-chenoy",
    "https://www.companyweb.be/en/golden-morgen",
    "https://www.companyweb.be/en/le-colvert",
    "https://www.companyweb.be/en/le-heris",
]


def main():
    for path in PATHS:
        try:
            req = urllib.request.Request(path, headers=UA)
            html = urllib.request.urlopen(req, timeout=20, context=ctx).read().decode("utf-8", "replace")
            title = re.search(r"<title>([^<]+)", html)
            links = re.findall(r'href="(/fr/company/[^"]+)"', html)
            nums = re.findall(r"0\d{3}\.\d{3}\.\d{3}", html[:40000])
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            print(
                path.split("q=")[-1][:45] if "q=" in path else path.split("/")[-1],
                "len",
                len(html),
                "last",
                last.group(1) if last else "-",
                "title",
                (title.group(1)[:55] if title else ""),
                "links",
                links[:4],
                "nums",
                list(dict.fromkeys(nums))[:6],
            )
        except Exception as e:
            print(path[-50:], type(e).__name__, e)


if __name__ == "__main__":
    main()
