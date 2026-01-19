import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# List all prompts with images
print("=" * 80)
print("プロンプト一覧（ID, タイトル, カテゴリ, 画像パス）")
print("=" * 80)

for prompt in data:
    if prompt.get('image'):
        print(f"{prompt['id']:3d}. [{prompt['category']}] {prompt['title']}")
        print(f"     画像: {prompt['image']}")
        print()
