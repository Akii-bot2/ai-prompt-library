import json
import os

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# プロンプトIDとタイトル、現在の画像を確認
print("=" * 80)
print("音声・音楽生成カテゴリ")
print("=" * 80)

for prompt in data:
    if prompt['category'] == '音声・音楽生成':
        img = prompt.get('image') or '(なし)'
        print(f"{prompt['id']:3d}. {prompt['title']:<30} -> {img}")

print("\n" + "=" * 80)
print("動画生成カテゴリ")
print("=" * 80)

for prompt in data:
    if prompt['category'] == '動画生成':
        img = prompt.get('image') or '(なし)'
        print(f"{prompt['id']:3d}. {prompt['title']:<30} -> {img}")

# images フォルダにある画像ファイルを確認
print("\n" + "=" * 80)
print("imagesフォルダの画像ファイル")
print("=" * 80)

images_dir = 'images'
images = sorted([f for f in os.listdir(images_dir) if f.startswith('prompt_') and f.endswith('.png')])
for img in images:
    size = os.path.getsize(os.path.join(images_dir, img))
    print(f"  {img} ({size // 1024} KB)")
