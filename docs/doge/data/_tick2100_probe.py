import csv
csv.field_size_limit(10**7)
with open('docs/doge/data/leaderboard.csv', encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))

def pi(r):
    try:
        return float(r.get('priority_index') or 0)
    except Exception:
        return 0

filtered = []
for r in rows:
    p = pi(r)
    name = (r.get('name') or '') + (r.get('notes') or '') + (r.get('tco_notes') or '')
    if p > 10:
        continue
    if 'Metro3' in name or 'snowball' in name.lower():
        continue
    if (r.get('status') or '') == 'struck':
        continue
    filtered.append(r)
filtered.sort(key=pi, reverse=True)
print('rows', len(rows), 'filtered', len(filtered))
for r in filtered[:12]:
    print(f"{pi(r):.2f}|{(r.get('item_id') or '')[:42]}|{(r.get('name') or '')[:65]}|{(r.get('annual_cost_eur') or '')[:16]}|{r.get('confidence')}")

# check Always Home / Comnexio in entities
with open('docs/doge/data/entities.csv', encoding='utf-8-sig') as f:
    ents = list(csv.DictReader(f))
for e in ents:
    blob = ' '.join((e.get(k) or '') for k in e).lower()
    if 'always' in blob or 'comnexio' in blob or e.get('entity_id') == 'nv_slg_operaties_vlaanderen':
        print('ENT', e.get('entity_id'), (e.get('notes') or '')[:100])
