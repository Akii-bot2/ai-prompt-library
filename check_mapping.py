import json
import os

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 現在の状況を確認
print("=" * 70)
print("現在のID 22-50のマッピング状況")
print("=" * 70)

for prompt in data:
    if 22 <= prompt['id'] <= 50:
        img = prompt.get('image') or '(カテゴリデフォルト)'
        print(f"{prompt['id']:3d}. [{prompt['category'][:6]}] {prompt['title'][:25]:<25} -> {img}")

# images フォルダの内容
print("\n" + "=" * 70)
print("imagesフォルダの画像ファイル (prompt_XX.png)")
print("=" * 70)

images_dir = 'images'
images = sorted([f for f in os.listdir(images_dir) if f.startswith('prompt_') and f.endswith('.png')])
for img in images:
    size = os.path.getsize(os.path.join(images_dir, img))
    print(f"  {img} ({size // 1024} KB)")
