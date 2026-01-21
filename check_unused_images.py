import json
import os

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 画像がないプロンプトを確認
print("=" * 80)
print("画像がないプロンプト一覧（data.jsonでimage=null）")
print("=" * 80)

no_image = [(p['id'], p['title'], p['category']) for p in data if p.get('image') is None]
for pid, title, cat in no_image:
    print(f"{pid:3d}. [{cat[:6]}] {title}")

print(f"\n合計: {len(no_image)} 件")

# brainフォルダの画像を確認
brain_dir = r"C:\Users\PC_User\.gemini\antigravity\brain\44f5e7ea-58c7-4c00-ad35-eed2c22f8955"
brain_images = [f for f in os.listdir(brain_dir) if f.startswith('prompt_') and f.endswith('.png')]

print("\n" + "=" * 80)
print("brainフォルダにある画像の内容（ファイル名から推測）")
print("=" * 80)

# Parse image names to understand content
for img in sorted(brain_images):
    parts = img.replace('.png', '').split('_')
    # Extract content description
    if len(parts) >= 3:
        content = '_'.join(parts[2:-1]) if parts[-1].isdigit() else '_'.join(parts[2:])
        print(f"  {img[:50]:<50} -> {content}")
