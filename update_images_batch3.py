import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update image paths for newly generated images
new_images = list(range(61, 73)) + list(range(81, 85))  # 61-72, 81-84

for prompt in data:
    pid = prompt['id']
    if pid in new_images:
        prompt['image'] = f"images/prompt_{pid:02d}.png"

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Updated image paths for {len(new_images)} prompts: {new_images}")

# Check remaining without images
remaining = [(p['id'], p['title']) for p in data if p.get('image') is None]
print(f"\nRemaining without custom images: {len(remaining)}")
for i, (pid, title) in enumerate(remaining):
    print(f"  {pid}. {title[:40]}")
