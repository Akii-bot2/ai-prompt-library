import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update image paths for generated images (22-41)
for prompt in data:
    prompt_id = prompt['id']
    if 22 <= prompt_id <= 41:
        prompt['image'] = f"images/prompt_{prompt_id:02d}.png"

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated image paths for prompts 22-41")

# Check remaining without images
remaining = [(p['id'], p['title']) for p in data if p.get('image') is None]
print(f"Remaining without images: {len(remaining)}")
for p in remaining[:10]:
    print(f"  {p[0]}. {p[1]}")
