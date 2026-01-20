import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 音楽系プロンプトの画像を正しく設定
music_mapping = {
    29: 'images/prompt_29_lofi.png',       # Lo-Fi BGM -> Lo-Fi room画像
    30: 'images/prompt_30_game.png',       # ゲームBGM -> ゲーム音楽画像
    31: 'images/prompt_31_podcast.png',    # ポッドキャスト -> ポッドキャスト画像
    32: 'images/prompt_32_relax.png',      # リラクゼーション -> 瞑想画像
    33: 'images/prompt_33.png',            # 製品プロモーション動画 -> 商品+カメラ
    34: 'images/prompt_34.png',            # YouTubeイントロ -> 今回生成
    35: 'images/prompt_35.png',            # ドキュメンタリー -> 今回生成
    36: 'images/prompt_36.png',            # SNSショート -> 今回生成
}

for prompt in data:
    pid = prompt['id']
    if pid in music_mapping:
        prompt['image'] = music_mapping[pid]

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated image mappings for audio/video prompts:")
for pid, path in sorted(music_mapping.items()):
    # Find title
    title = next((p['title'] for p in data if p['id'] == pid), 'Unknown')
    print(f"  {pid}. {title:<30} -> {path}")
