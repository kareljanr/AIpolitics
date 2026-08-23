import re, urllib.request
from pathlib import Path
RAW = Path("docs/doge/data/raw/tick2094")
UA = {"User-Agent": "Mozilla/5.0 (compatible; AIpolitics-DOGE/1.0; research)"}

def get(url, name):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = resp.read()
            (RAW / name).write_bytes(data)
            print(name, resp.status, len(data), resp.geturl())
            return data
    except Exception as e:
        print(name, "FAIL", e)
        return b""

# try common care-site patterns + google-ish
cands = {
    "site_wzc.html": "https://www.wzc-sintlucia.be/",
    "site_lucia2.html": "https://www.sint-lucia.be/",
    "site_lucia3.html": "https://sint-lucia.be/",
    "site_lucia4.html": "https://www.sintlucia-turnhout.be/",
    "site_lucia5.html": "https://www.zorgbedrijfturnhout.be/",
    "northdata.html": "https://www.northdata.com/Sint-Lucia+VZW,+Turnhout/0410.151.137",
    "cw_contact_probe.html": "https://www.companyweb.be/nl/0410151137/sint-lucia",
}
for n,u in cands.items():
    get(u,n)

# parse CW for email / phone / website
t = (RAW/"lucia_nl.html").read_text(encoding="utf-8", errors="replace")
emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", t))
print("cw emails", [e for e in emails if "companyweb" not in e.lower() and "sentry" not in e.lower()][:20])
phones = re.findall(r"0\d{1,2}[\s./-]?\d{2,3}[\s./-]?\d{2,3}[\s./-]?\d{2,3}", t)
print("phones sample", phones[:10])
# look for website field
plain = re.sub(r"<[^>]+>"," ",t)
plain = re.sub(r"\s+"," ",plain)
for key in ["Website", "website", "www.", "Telefoon", "E-mail", "email", "info@", "@"]:
    i = plain.lower().find(key.lower())
    if i>=0 and key!="@":
        print("CTX", key, plain[max(0,i-20):i+100])
# aanbestedende?
print("aanbestedende", "aanbestedende" in plain.lower())
