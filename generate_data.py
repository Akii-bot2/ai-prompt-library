import csv
import random

# Fixed starting ID (current max is 6)
START_ID = 7

# Templates and Lists for Mass Generation (Japanese Localization)

# 1. Image Generation (Prompts english for tools, Title/Tags Japanese)
image_subjects = ["猫", "犬", "戦士", "城", "宇宙船", "森", "山", "サイバーパンクな通り", "魔法使い", "ドラゴン", "ロボット", "花", "海", "夕日", "都市のスカイライン", "古代遺跡", "図書館", "カフェ", "スチームパンクの歯車", "異星の惑星"]
image_subjects_en = ["cat", "dog", "warrior", "castle", "spaceship", "forest", "mountain", "cyberpunk street", "wizard", "dragon", "robot", "flower", "ocean", "sunset", "city skyline", "ancient ruins", "library", "coffee shop", "steampunk gear", "alien planet"]
image_styles = ["油絵風", "水彩画風", "デジタルアート", "写真リアル", "アニメスタイル", "浮世絵風", "ピクセルアート", "3Dレンダリング", "シネマティックライティング", "ジブリ風", "ゴッホ風", "鉛筆画", "ノワール", "ヴェイパーウェイヴ", "ローポリ", "アイソメトリック", "コンセプトアート", "マットペインティング", "ポップアート", "シュルレアリスム"]
image_styles_en = ["oil painting", "watercolor", "digital art", "photorealistic", "anime style", "ukiyo-e", "pixel art", "3d render", "cinematic lighting", "studio ghibli style", "van gogh style", "pencil sketch", "noir", "vaporwave", "low poly", "isometric", "concept art", "matte painting", "pop art", "surrealism"]
image_tools = "Midjourney|https://www.midjourney.com/;Stable Diffusion|https://stability.ai/;Gemini|https://gemini.google.com/"

# 2. Text Generation (All Japanese)
text_topics = ["マーケティングメール", "ブログ記事", "SNSのキャプション", "プレスリリース", "詩", "ショートストーリー", "議事録", "求人票", "カバーレター", "レシピ", "旅行日程表", "製品説明", "レビューへの返信", "スピーチ", "エッセイ", "ニュース記事", "FAQセクション", "チュートリアル", "ニュースレター", "スローガン"]
text_contexts = ["プロフェッショナルなトーン", "親しみやすいトーン", "説得力のある", "ユーモラスな", "簡潔な", "詳細な", "SEO最適化された", "子供向けの", "専門家向けの", "緊急の"]
text_tools = "ChatGPT|https://chat.openai.com/;Claude|https://claude.ai/;Gemini|https://gemini.google.com/"

# 3. Coding (All Japanese)
coding_langs = ["Python", "JavaScript", "HTML/CSS", "SQL", "React", "Rust", "Go", "TypeScript", "Bash", "Java"]
coding_tasks = ["リストをソートする", "REST APIを作成する", "ウェブサイトをスクレイピングする", "シンプルなゲームを作る", "メールアドレスの正規表現バリデーション", "データベースに接続する", "divを中央揃えにする", "非同期fetchを行う", "ユニットテストを書く", "データを可視化する"]
coding_tools = "GitHub Copilot|https://github.com/features/copilot;ChatGPT|https://chat.openai.com/;Gemini|https://gemini.google.com/"

# 4. Audio (Prompts English for tools, Metadata Japanese)
audio_moods = ["楽しい", "悲しい", "メランコリック", "エネルギッシュ", "リラックス", "不気味", "ロマンチック", "壮大", "ジャズ風", "ローファイ"]
audio_moods_en = ["upbeat", "sad", "melancholic", "energetic", "relaxing", "spooky", "romantic", "epic", "jazzy", "lo-fi"]
audio_instruments = ["ピアノ", "ギター", "シンセサイザー", "オーケストラ", "ドラム", "フルート", "バイオリン", "電子音", "ベース", "ボーカル"]
audio_instruments_en = ["piano", "guitar", "synth", "orchestra", "drums", "flute", "violin", "electronic", "bass", "vocals"]
audio_tools = "Suno AI|https://suno.com/;Udio|https://www.udio.com/"

# 5. Video (Prompts English for tools, Metadata Japanese)
video_scenes = ["ビーチのドローン撮影", "スローモーションのランニング", "都市のタイムラプス", "カフェでの会話", "カーチェイス", "打ち上げ花火", "料理のチュートリアル", "ジャンプする猫", "窓に当たる雨", "山からの日の出"]
video_scenes_en = ["drone shot of a beach", "slow motion running", "time lapse of city", "conversation in a cafe", "car chase", "exploding fireworks", "cooking tutorial", "cat jumping", "rain falling on window", "sunrise over mountains"]
video_styles = ["シネマティック", "手持ちカメラ風", "アニメスタイル", "白黒", "ビンテージフィルム", "4Kリアル", "カートゥーン", "ストップモーション", "GoPro映像", "ドローン視点"]
video_styles_en = ["cinematic", "handheld camera", "anime style", "black and white", "vintage film", "4k realistic", "cartoon", "stop motion", "gopro footage", "drone view"]
video_tools = "Runway Gen-2|https://runwayml.com/;Sora|https://openai.com/sora;Gemini|https://gemini.google.com/"

new_rows = []
current_id = START_ID

# Generate Image Prompts (20)
for _ in range(20):
    idx_subj = random.randrange(len(image_subjects))
    idx_style = random.randrange(len(image_styles))
    
    subj_jp = image_subjects[idx_subj]
    style_jp = image_styles[idx_style]
    subj_en = image_subjects_en[idx_subj]
    style_en = image_styles_en[idx_style]

    prompt = f"{subj_en}, {style_en}, highly detailed, 8k, masterpiece, trending on artstation"
    title = f"{style_jp}の{subj_jp}"
    tags = f"画像生成,{style_jp},{subj_jp},アート"
    
    new_rows.append([current_id, title, "", prompt, "画像生成", tags, image_tools])
    current_id += 1

# Generate Text Prompts (20)
for _ in range(20):
    topic = random.choice(text_topics)
    context = random.choice(text_contexts)
    prompt = f"「[トピック]」に関する{topic}を書いてください。{context}で、読者を引き込む内容にしてください。"
    title = f"{context} {topic}"
    tags = f"文章生成,{topic},{context}"
    
    new_rows.append([current_id, title, "", prompt, "文章生成", tags, text_tools])
    current_id += 1

# Generate Coding Prompts (20)
for _ in range(20):
    lang = random.choice(coding_langs)
    task = random.choice(coding_tasks)
    prompt = f"{lang}を使って、{task}ためのスクリプトを作成してください。コードの各部分には分かりやすい日本語のコメントを含めてください。"
    title = f"{lang}: {task}"
    tags = f"コーディング,{lang},プログラミング"
    
    new_rows.append([current_id, title, "", prompt, "コーディング", tags, coding_tools])
    current_id += 1

# Generate Audio Prompts (20)
for _ in range(20):
    idx_mood = random.randrange(len(audio_moods))
    idx_inst = random.randrange(len(audio_instruments))
    
    mood_jp = audio_moods[idx_mood]
    inst_jp = audio_instruments[idx_inst]
    mood_en = audio_moods_en[idx_mood]
    inst_en = audio_instruments_en[idx_inst]

    prompt = f"A {mood_en} track featuring {inst_en}, high quality audio, studio recording"
    title = f"{mood_jp}な{inst_jp}"
    tags = f"音声・音楽生成,{mood_jp},BGM"
    
    new_rows.append([current_id, title, "https://placehold.co/600x400/4B0082/ffffff?text=Audio", prompt, "音声・音楽生成", tags, audio_tools])
    current_id += 1

# Generate Video Prompts (20)
for _ in range(20):
    idx_scene = random.randrange(len(video_scenes))
    idx_style = random.randrange(len(video_styles))
    
    scene_jp = video_scenes[idx_scene]
    style_jp = video_styles[idx_style]
    scene_en = video_scenes_en[idx_scene]
    style_en = video_styles_en[idx_style]

    prompt = f"{scene_en}, {style_en}, high resolution, 60fps"
    title = f"{style_jp} {scene_jp}"
    tags = f"動画生成,{style_jp},動画"
    
    new_rows.append([current_id, title, "", prompt, "動画生成", tags, video_tools])
    current_id += 1

# Append to prompts.csv
with open('prompts.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(new_rows)

print(f"Added {len(new_rows)} new Japanese prompts to prompts.csv")
