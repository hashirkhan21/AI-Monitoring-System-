import urllib.request, json, os

API_KEY = "1"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}&pageSize=50"
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())

for m in data.get('models', []):
    name = m['name']
    display = m.get('displayName', '')
    if 'flash' in name.lower() or 'lite' in name.lower():
        print(f"{name:55s}  {display}")
