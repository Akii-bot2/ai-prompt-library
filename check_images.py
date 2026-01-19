import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

prompts_without_images = [(p['id'], p['title'], p['category']) for p in data if p.get('image') is None]

print(f"Total without images: {len(prompts_without_images)}")
for p in prompts_without_images:
    print(f"{p[0]:3d}. [{p[2]}] {p[1]}")
