import json

# Load data.json
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update image paths for prompts 1-21
for prompt in data:
    prompt_id = prompt['id']
    if 1 <= prompt_id <= 21:
        prompt['image'] = f'images/prompt_{prompt_id:02d}.png'

# Save updated data.json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated {len([p for p in data if p['image'] and p['image'].startswith('images/prompt_')])} prompts with new images")
