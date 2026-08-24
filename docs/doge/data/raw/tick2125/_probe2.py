# -*- coding: utf-8 -*-
import re
import ssl
import urllib.request

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

CANDS = [
    "0412210456",
    "0425123789",
    "0438687654",
    "0440123456",
    "0443249616",
    "0453380125",
    "0464822341",
    "0466266429",
    "0475123890",
    "0480566704",
    "0598966387",
    "0685516024",
]


def main():
    for kbo in CANDS:
        url = f"https://www.companyweb.be/en/{kbo}"
        try:
            req = urllib.request.Request(url, headers=UA)
            html = urllib.request.urlopen(req, timeout=30, context=ctx).read().decode("utf-8", "replace")
            open(f"cand_{kbo}_en.html", "w", encoding="utf-8").write(html)
            last = re.search(r"Last balance sheet year[^0-9]*(\d{4})", html)
            title = re.search(r"<title>([^<]+)", html)
            # also check if 2025 appears as first year column
            fin = ""
            idx = html.find("Financial data")
            if idx > 0:
                text = re.sub(r"<[^>]+>", " ", html[idx : idx + 4500])
                fin = re.sub(r"\s+", " ", text)[:420]
            print(kbo, "last", last.group(1) if last else "?", "|", (title.group(1)[:75] if title else ""))
            print(" ", fin)
            print("---")
        except Exception as e:
            print(kbo, "ERR", e)


if __name__ == "__main__":
    main()
