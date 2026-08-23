from pathlib import Path
import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
UA = {"User-Agent": "Mozilla/5.0"}

# try contact page
for url, name in [
    ("https://www.tenanker.be/", "tenanker_site.html"),
    ("https://www.tenanker.be/contact", "tenanker_contact.html"),
    ("https://www.tenanker.be/contacteer-ons", "tenanker_contact2.html"),
]:
    try:
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, context=ctx, timeout=30).read()
        Path(f"docs/doge/data/raw/tick2078/{name}").write_bytes(data)
        t = data.decode("utf-8", "replace")
        mails = re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", t)
        print(name, len(data), "mails", mails[:8], "title", re.findall(r"<title>(.*?)</title>", t, re.I)[:1])
    except Exception as e:
        print(name, "ERR", e)
