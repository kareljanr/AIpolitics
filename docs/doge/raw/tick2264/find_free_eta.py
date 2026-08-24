import re
from pathlib import Path

html = Path(__file__).with_name("leseta_annuaire.html").read_text("utf-8", "ignore")
slugs = sorted(set(re.findall(r"/annuaire-eta/([a-z0-9\-]+)/", html)))
print("slugs", len(slugs))
for s in slugs:
    print(s)

mined = """
lorraine eupen ajr alteria erables geer nekto belair corelap cambier gaillettes
hunelle dauphins saupont serviplast delcour travco pilifs jardiniers lumiere apam
gielen perron atelier axedis beauraing manufast metalgroup entranam enghien entra
tertre rucher rekreatief travie vleugels kiemkracht oever vites kringwinkel manus
reset azalee kemphaan mirto blankedale werkmmaat ate ensival jean-delcour
jean-gielen le-perron l-atelier eta-123 les-erables val-du-geer les-dauphins
moulin-de-la-hunelle les-gaillettes atelier-cambier la-lumiere jeunes-jardiniers
ferme-nos-pilifs bw-eupen atelier-jean-regniers
""".split()
print("--- FREE? ---")
for s in slugs:
    if not any(m in s for m in mined):
        print("FREE?", s)
