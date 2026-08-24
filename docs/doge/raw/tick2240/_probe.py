import csv,re
from pathlib import Path
csv.field_size_limit(10_000_000)
raw=Path('docs/doge/raw/tick2240')
kbo=(raw/'kbo.html').read_text(encoding='utf-8',errors='replace')
for pat in [r'Status</td>\s*<td[^>]*><span[^>]*>([^<]+)', r'Actief', r'eenheid', r'Nacebel', r'88\.993', r'aanbested', r'@', r'telefoon']:
    print('pat',pat, bool(re.search(pat,kbo,re.I)))
# extract emails from contact
c=(raw/'contact.html').read_text(encoding='utf-8',errors='replace')
emails=sorted(set(re.findall(r'[\w.+-]+@[\w.-]+\.\w+', c)))
print('emails', emails[:20])
phones=sorted(set(re.findall(r'\+32[\d\s./-]{8,}|\d{2,3}[\s./-]\d{2,3}[\s./-]\d{2,3}', c)))
print('phones', phones[:10])
# check entity unused
with open('docs/doge/data/entities.csv',encoding='utf-8') as f:
    text=f.read()
print('axedis in entities', 'axedis' in text.lower())
print('0465786674 in entities', '0465786674' in text or '0465.786.674' in text)
# top10
with open('docs/doge/data/leaderboard.csv', encoding='utf-8') as f:
    rows=list(csv.DictReader(f))

def fnum(x):
    try: return float(str(x).replace(',','').replace(' ',''))
    except: return None

cands=[]
for r in rows:
    pi=fnum(r.get('priority_index'))
    if pi is None or pi>10: continue
    annual=fnum(r.get('annual_cost_eur')) or 0
    name=(r.get('name') or '')
    iid=r.get('item_id') or ''
    low=name.lower()+' '+iid.lower()
    if any(k in low for k in ['snowball','metro3','hedera','mog ii','hermreg','safe loan','debt stock']):
        continue
    cands.append((pi, annual, r))
cands.sort(key=lambda t: (-t[0], -t[1]))
for i,(pi,ann,r) in enumerate(cands[:10],1):
    print(i, r['item_id'], round(pi,3), ann, r['name'][:60])
print('lb rows', len(rows))
