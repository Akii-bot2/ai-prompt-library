import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total: {len(data)} prompts\n")
for p in data:
    print(f"{p['id']}|{p['title']}|{p['category']}")
