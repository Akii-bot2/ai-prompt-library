import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 生成した画像の内容と対象プロンプトの正しいマッピング
# 実際に生成した画像の内容:
# prompt_22.png: Web Scraping (Python spider web)
# prompt_23.png: REST API (HTTP methods)
# prompt_24.png: React components (React logo)
# prompt_25.png: SQL Database (tables)
# prompt_26.png: Unit Test (green checkmarks) - NOT used (no matching prompt)
# prompt_27.png: Docker (whale containers) - NOT used
# prompt_28.png: Git branching (orange/purple)
# prompt_29.png: Security (shield lock) - SHOULD be Lo-Fi room now
# prompt_30.png: CI/CD (infinity loop) - SHOULD be game music now
# prompt_31.png: BGM (film reel music) 
# prompt_32.png: Jingle (microphone) - SHOULD be meditation now
# prompt_33.png: Podcast (headphones mic) - SHOULD be product video now
# prompt_34.png: Lo-Fi room (cat, vinyl)
# prompt_35.png: Game music (8-bit controller)
# prompt_36.png: Meditation (lotus zen)
# prompt_37.png: EDM (DJ turntables)
# prompt_38.png: Jazz (saxophone piano)
# prompt_39.png: Orchestral (violins, clapperboard)
# prompt_40.png: Voiceover (human silhouette, mic)
# prompt_41.png: Product promo (camera filming product)

# data.json のプロンプトIDとタイトル:
# 22: Python: Webスクレイピング -> prompt_22 ✓
# 23: JavaScript: REST API実装 -> prompt_23 ✓
# 24: React: UIコンポーネント -> prompt_24 ✓
# 25: SQL: 複雑なクエリ作成 -> prompt_25 ✓
# 26: HTML/CSS: レスポンシブレイアウト -> null (カテゴリデフォルト)
# 27: TypeScript: 型定義設計 -> null
# 28: Git: ワークフロー設計 -> prompt_28 ✓
# 29: Lo-Fi BGM -> prompt_34 (Lo-Fi room)
# 30: ゲームBGM（バトル） -> prompt_35 (Game music)
# 31: ポッドキャスト用ジングル -> prompt_33 (Podcast headphones)
# 32: リラクゼーション音楽 -> prompt_36 (Meditation lotus)
# 33: 製品プロモーション動画 -> prompt_41 (Product promo)
# 34: YouTube動画オープニング -> null
# 35: ドキュメンタリー風映像 -> null
# 36: SNS用ショート動画 -> null
# 37-41: 文章生成系 -> null

correct_mapping = {
    22: 'images/prompt_22.png',  # Web Scraping
    23: 'images/prompt_23.png',  # REST API
    24: 'images/prompt_24.png',  # React
    25: 'images/prompt_25.png',  # SQL
    26: None,  # HTML/CSS - カテゴリデフォルト
    27: None,  # TypeScript - カテゴリデフォルト
    28: 'images/prompt_28.png',  # Git
    29: 'images/prompt_34.png',  # Lo-Fi BGM -> Lo-Fi room画像
    30: 'images/prompt_35.png',  # ゲームBGM -> Game music画像
    31: 'images/prompt_33.png',  # ポッドキャスト -> Podcast画像
    32: 'images/prompt_36.png',  # リラクゼーション -> Meditation画像
    33: 'images/prompt_41.png',  # 製品プロモ -> Product promo画像
    34: None,  # YouTube opning - カテゴリデフォルト
    35: None,  # ドキュメンタリー - カテゴリデフォルト
    36: None,  # SNSショート - カテゴリデフォルト
    37: None,  # 議事録 - カテゴリデフォルト
    38: None,  # 製品説明文 - カテゴリデフォルト
    39: None,  # プレスリリース - カテゴリデフォルト
    40: None,  # FAQ - カテゴリデフォルト
    41: None,  # 求人票 - カテゴリデフォルト
}

# Update data.json
for prompt in data:
    pid = prompt['id']
    if pid in correct_mapping:
        prompt['image'] = correct_mapping[pid]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated image mappings:")
print()
for prompt in data:
    if 22 <= prompt['id'] <= 45:
        img = prompt.get('image') or '(カテゴリデフォルト)'
        cat = prompt['category'][:6]
        print(f"{prompt['id']:3d}. [{cat}] {prompt['title'][:28]:<28} -> {img}")
