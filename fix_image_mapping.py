import json
import shutil
import os

# Load data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create a mapping of what image matches what prompt based on title keywords
image_content_map = {
    # 生成した画像の内容 -> 対象プロンプトのID
    'prompt_22.png': 22,  # Web Scraping -> Python: Webスクレイピング ✓
    'prompt_23.png': 23,  # REST API -> JavaScript: REST API実装 ✓
    'prompt_24.png': 24,  # React -> React: UIコンポーネント ✓
    'prompt_25.png': 25,  # SQL Database -> SQL: 複雑なクエリ作成 ✓
    'prompt_26.png': None,  # Unit Test (緑のテスト) -> マッチなし（コーディング用カテゴリ画像使用）
    'prompt_27.png': None,  # Docker -> マッチなし
    'prompt_28.png': 28,  # Git branching -> Git: ワークフロー設計 ✓
    'prompt_29.png': None,  # Security shield -> マッチなし
    'prompt_30.png': None,  # CI/CD -> マッチなし
    'prompt_31.png': None,  # BGM film -> 音楽系に使用可能
    'prompt_32.png': None,  # Jingle mic -> 音楽系に使用可能
    'prompt_33.png': None,  # Podcast -> 音楽系に使用可能
    'prompt_34.png': 29,  # Lo-Fi room -> Lo-Fi BGM（作業用） ✓
    'prompt_35.png': 30,  # Game music -> ゲームBGM（バトル） ✓
    'prompt_36.png': 32,  # Meditation lotus -> リラクゼーション音楽 ✓
    'prompt_37.png': None,  # EDM DJ -> 音楽系だがマッチなし
    'prompt_38.png': None,  # Jazz -> 音楽系だがマッチなし
    'prompt_39.png': None,  # Orchestral -> 音楽系だがマッチなし
    'prompt_40.png': None,  # Voiceover -> マッチなし
    'prompt_41.png': 33,  # Product promo video -> 製品プロモーション動画 ✓
}

# Better approach: Use category-based default images for mismatched ones
# and only assign images where we have clear matches

# Clear all images first for 22-41
for prompt in data:
    if 22 <= prompt['id'] <= 41:
        prompt['image'] = None

# Assign matched images
matches = {
    22: 'images/prompt_22.png',  # Web Scraping
    23: 'images/prompt_23.png',  # REST API
    24: 'images/prompt_24.png',  # React
    25: 'images/prompt_25.png',  # SQL
    28: 'images/prompt_28.png',  # Git
    29: 'images/prompt_34.png',  # Lo-Fi BGM -> 使用 34の画像（Lo-Fi room）
    30: 'images/prompt_35.png',  # ゲームBGM -> 使用 35の画像（Game music）
    32: 'images/prompt_36.png',  # リラクゼーション音楽 -> 使用 36の画像（Meditation）
    33: 'images/prompt_41.png',  # 製品プロモーション動画 -> 使用 41の画像
}

# Rename files in images folder to correct mapping
images_dir = 'images'

# First, backup the current state by copying with _old suffix
print("Renaming images to match prompts...")

# Create the new mappings by renaming
rename_map = {
    'prompt_34.png': 'prompt_29_new.png',  # Lo-Fi image -> prompt 29
    'prompt_35.png': 'prompt_30_new.png',  # Game music -> prompt 30
    'prompt_36.png': 'prompt_32_new.png',  # Meditation -> prompt 32
    'prompt_41.png': 'prompt_33_new.png',  # Product video -> prompt 33
}

# Execute renames with temp names first
for old_name, new_name in rename_map.items():
    old_path = os.path.join(images_dir, old_name)
    new_path = os.path.join(images_dir, new_name)
    if os.path.exists(old_path):
        shutil.copy(old_path, new_path)
        print(f"Copied {old_name} -> {new_name}")

# Now rename to final names
final_renames = {
    'prompt_29_new.png': 'prompt_29.png',
    'prompt_30_new.png': 'prompt_30.png',
    'prompt_32_new.png': 'prompt_32.png',
    'prompt_33_new.png': 'prompt_33.png',
}

for old_name, new_name in final_renames.items():
    old_path = os.path.join(images_dir, old_name)
    new_path = os.path.join(images_dir, new_name)
    if os.path.exists(old_path):
        # Remove existing if exists
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

# Update data.json with matched images
for prompt in data:
    pid = prompt['id']
    if pid in matches:
        # Get the correct image path
        prompt['image'] = matches[pid]
    elif 22 <= pid <= 41:
        # Keep images that are correctly matched (22-25, 28)
        if pid in [22, 23, 24, 25, 28]:
            prompt['image'] = f"images/prompt_{pid:02d}.png"
        else:
            # Use null for unmatched - will fall back to category image
            prompt['image'] = None

# Save updated data
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nUpdated data.json with corrected image mappings")

# Show the result
print("\n=== 最終的なマッピング ===")
for prompt in data:
    if 22 <= prompt['id'] <= 41:
        img = prompt.get('image') or 'カテゴリデフォルト'
        print(f"{prompt['id']:3d}. {prompt['title'][:30]:<30} -> {img}")
