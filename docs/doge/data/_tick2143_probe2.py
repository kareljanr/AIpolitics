# -*- coding: utf-8 -*-
import urllib.request, re, ssl
from pathlib import Path
ctx=ssl.create_default_context()
ua={"User-Agent":"Mozilla/5.0"}
def get(url):
    req=urllib.request.Request(url, headers=ua)
    with urllib.request.urlopen(req, context=ctx, timeout=35) as r:
        return r.read().decode("utf-8","replace"), r.geturl()
text=(Path("docs/doge/data/entities.csv").read_text(encoding="utf-8",errors="replace")).lower()
# batch of plausible unused MRS / WZC / psych / disability from Walloon/Flemish lists
cands = [
("les_tilleuls_ath","https://www.companyweb.be/en/0408302145"),
("residence_val_des_roses","https://www.companyweb.be/en/0426558312"),
("home_du_parc","https://www.companyweb.be/en/0403301468"),
("les_acacias","https://www.companyweb.be/en/0439123456"),
("residence_le_manoir","https://www.companyweb.be/en/0460123456"),
# known groups leftover campuses often separate entities
("zilverlinde_olen","https://www.companyweb.be/en/0445123456"),
# try upswitch/companyweb known KBOs from public lists
("mrs_notre_dame","https://www.companyweb.be/en/0401472918"),
("residence_st_joseph_liege","https://www.companyweb.be/en/0403408287"),
("home_st_roch","https://www.companyweb.be/en/0403370142"),
("les_hirondelles_mrs","https://www.companyweb.be/en/0422614814"),
("le_clos_du_val","https://www.companyweb.be/en/0468512345"),
("residence_orpea_test","https://www.companyweb.be/en/0462123456"),
]
# Better: fetch AVIQ excel or a public directory page
for url in [
 "https://www.aviq.be/fr/liste-des-maisons-de-repos-incl-maisons-de-repos-et-de-soins-et-court-sejour-residences-services-et",
]:
  try:
    h,f=get(url)
    print("aviq", f, len(h))
    # find xlsx
    xs=re.findall(r'href=\"([^\"]+\.(?:xlsx|xls|csv))\"', h, re.I)
    print("files", xs[:5])
  except Exception as e:
    print("aviq ERR", e)

# Northdata search HTML
try:
  h,f=get("https://www.northdata.com/?q=maison+de+repos&region=Belgique")
  print("north", f[:80], len(h))
  # company links
  links=re.findall(r'href=\"(/[^\" ]+Ma[^\"]{0,80})\"', h)
  print("nlinks", links[:15])
  # also companyweb-like numbers
  nums=re.findall(r'BE\s?0\d{9}', h)
  print("BE nums", nums[:20])
except Exception as e:
  print("north ERR", e)
