import csv

# Final 12 high-quality prompts to reach 100 total
# Starting from ID 89

TEXT_TOOLS = "ChatGPT|https://chat.openai.com/;Claude|https://claude.ai/;Gemini|https://gemini.google.com/"
IMAGE_TOOLS = "Midjourney|https://www.midjourney.com/;Stable Diffusion|https://stability.ai/;Gemini|https://gemini.google.com/"
CODE_TOOLS = "GitHub Copilot|https://github.com/features/copilot;ChatGPT|https://chat.openai.com/;Gemini|https://gemini.google.com/"
AUDIO_TOOLS = "Suno AI|https://suno.com/;Udio|https://www.udio.com/"
VIDEO_TOOLS = "Runway Gen-2|https://runwayml.com/;Sora|https://openai.com/sora;Gemini|https://gemini.google.com/"

prompts = []
current_id = 89

# ===== 文章生成 2件 =====

prompts.append([current_id, "キャッチコピー作成", "",
"""【AIへの役割】
あなたは広告コピーライターです。

【目的・背景】
[例: 新商品の認知度を上げるキャッチコピー]

【商品/サービス】
名前: [例: 天然水 クリスタル]
特徴: [例: 富士山麓の湧き水、ミネラル豊富]
USP: [例: 他社より2倍のミネラル含有]

【ターゲット】
[例: 健康志向の30-50代女性]

【トーン・雰囲気】
[例: 清涼感、プレミアム感、親しみやすさ]

【期待するアウトプット】
・メインコピー（10案）
・サブコピー（各メインに対応）
・使用シーンの提案""", "文章生成", "キャッチコピー,広告,マーケティング", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "アンケート設計", "",
"""【AIへの役割】
あなたはマーケットリサーチャーです。

【目的・背景】
[例: 新サービスの需要調査]

【調査対象】
[例: 20-40代の会社員]

【調査したい内容】
[例: 利用意向、価格感度、競合比較]

【アンケート形式】
[例: Webアンケート、5分程度]

【期待するアウトプット】
・スクリーニング質問
・本調査質問（選択式、自由記述）
・回答選択肢
・質問順序の理由""", "文章生成", "アンケート,リサーチ,調査", TEXT_TOOLS])
current_id += 1

# ===== 画像生成 2件 =====

prompts.append([current_id, "Webサイトヒーロー画像", "https://placehold.co/600x400/6366f1/ffffff?text=Hero+Image",
"""【目的・背景】
Webサイトのファーストビュー用画像

【サイト種類】
[例: コーポレートサイト、ECサイト、SaaS LP]

【伝えたいイメージ】
[例: 信頼性、革新性、親しみやすさ]

【要素】
人物: [例: ビジネスパーソン、家族、なし]
背景: [例: オフィス、抽象的、グラデーション]
カラー: [例: ブランドカラー準拠]

【サンプルプロンプト】
website hero image, diverse business team collaboration, modern office environment, bright lighting, corporate blue color scheme, professional photography, space for text overlay, 16:9 aspect ratio""", "画像生成", "Webデザイン,ヒーロー,背景", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "インフォグラフィック素材", "https://placehold.co/600x400/10B981/ffffff?text=Infographic",
"""【目的・背景】
データや情報を視覚化する素材

【テーマ】
[例: ビジネス統計、プロセス図、比較]

【スタイル】
[例: フラット、アイソメトリック、手書き風]

【カラーパレット】
[例: コーポレートカラー、パステル、モノトーン]

【含める要素】
[例: グラフ、アイコン、フロー矢印]

【サンプルプロンプト】
infographic design elements, flat style icons, pie charts, bar graphs, process arrows, business theme, blue and green color palette, vector illustration, clean design""", "画像生成", "インフォグラフィック,データ,ビジネス", IMAGE_TOOLS])
current_id += 1

# ===== コーディング 2件 =====

prompts.append([current_id, "データベース設計", "",
"""【AIへの役割】
あなたはデータベースアーキテクトです。

【目的・背景】
[例: ECサイトのデータベース設計]

【システム概要】
機能: [例: ユーザー管理、商品管理、注文管理]
規模: [例: ユーザー10万人、商品1万点]

【技術要件】
DBMS: [例: PostgreSQL, MySQL]
正規化: [例: 第3正規形]

【期待するアウトプット】
・ER図（テキスト形式）
・テーブル定義
・リレーション
・インデックス戦略
・マイグレーションSQL""", "コーディング", "データベース,設計,アーキテクチャ", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "セキュリティ対策コード", "",
"""【AIへの役割】
あなたはセキュリティエンジニアです。

【目的・背景】
[例: Webアプリケーションのセキュリティ強化]

【対象脆弱性】
[例: XSS、SQLインジェクション、CSRF]

【技術スタック】
言語/FW: [例: Node.js/Express]

【期待するアウトプット】
・脆弱性の説明
・攻撃例
・対策コード
・テスト方法
・ベストプラクティス""", "コーディング", "セキュリティ,脆弱性,対策", CODE_TOOLS])
current_id += 1

# ===== 音声・音楽生成 2件 =====

prompts.append([current_id, "着信音・通知音", "https://placehold.co/600x400/3B82F6/ffffff?text=Ringtone",
"""【目的・背景】
スマートフォン、アプリの通知音

【用途】
[例: 着信音、メッセージ通知、アラーム]

【スタイル】
[例: シンプル、楽しい、洗練]

【仕様】
長さ: [例: 3-10秒]
ループ: [例: 着信音は対応]

【サンプルプロンプト】
notification sound, gentle chime, two notes ascending, modern app style, pleasant tone, short duration 2 seconds, high quality audio""", "音声・音楽生成", "着信音,通知音,アプリ", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ボーカル入り楽曲", "https://placehold.co/600x400/EC4899/ffffff?text=Vocal+Song",
"""【目的・背景】
オリジナル楽曲制作

【ジャンル】
[例: J-POP、R&B、ロック、アニソン]

【テーマ・歌詞内容】
[例: 恋愛、友情、応援歌、季節]

【ボーカルスタイル】
[例: 女性ボーカル、男性ボーカル、デュエット]

【仕様】
BPM: [例: 120-140]
キー: [例: Cメジャー]

【サンプルプロンプト】
J-pop song with female vocals, upbeat tempo 130bpm, catchy chorus, electronic instrumentation, emotional lyrics about new beginnings, radio-friendly production""", "音声・音楽生成", "楽曲,ボーカル,オリジナル", AUDIO_TOOLS])
current_id += 1

# ===== 動画生成 4件 =====

prompts.append([current_id, "ウェディング動画", "",
"""【目的・背景】
結婚式のオープニング/プロフィール動画

【スタイル】
[例: ロマンチック、ポップ、シネマティック]

【含める要素】
[例: 写真スライドショー、テキスト、BGM]

【動画仕様】
長さ: [例: 3-5分]
解像度: [例: 1080p]

【トーン】
[例: 感動的、明るい、おしゃれ]

【サンプルプロンプト】
wedding video style, romantic slow motion, soft warm color grading, lens flares, couple footage, nature backgrounds, cinematic transitions, emotional atmosphere""", "動画生成", "ウェディング,結婚式,イベント", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "教育・研修動画", "",
"""【AIへの役割】
あなたはインストラクショナルデザイナーです。

【目的・背景】
[例: 新入社員向けコンプライアンス研修]

【対象者】
[例: 新入社員、全社員]

【コンテンツ】
[例: 情報セキュリティ、ハラスメント防止]

【動画仕様】
長さ: [例: 10-15分/モジュール]
形式: [例: 講義+クイズ]

【サンプルプロンプト】
e-learning video, professional presenter, clean white background, text annotations, diagram animations, quiz overlay, corporate training style""", "動画生成", "教育,研修,Eラーニング", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "旅行・観光PR動画", "",
"""【目的・背景】
観光地、ホテル、旅行商品のPR

【対象エリア】
[例: 京都、沖縄、北海道]

【ターゲット】
[例: 国内旅行者、インバウンド]

【含める要素】
[例: 風景、食事、アクティビティ、宿泊施設]

【スタイル】
[例: シネマティック、ドローン空撮]

【サンプルプロンプト】
travel promotional video, stunning aerial drone shots, local cuisine close-ups, cultural experiences, happy travelers, cinematic color grading, inspiring music sync""", "動画生成", "旅行,観光,PR", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "ゲームトレーラー", "",
"""【目的・背景】
ゲーム発売前の告知映像

【ゲームジャンル】
[例: RPG、アクション、パズル]

【トレーラー種類】
[例: ティザー、ゲームプレイ、ストーリー]

【含める要素】
[例: カットシーン、ゲームプレイ映像、ロゴ]

【トーン】
[例: 壮大、ダーク、ポップ]

【サンプルプロンプト】
game trailer style, epic cinematic shots, dramatic lighting, action sequences, logo reveal, title card, fast-paced editing, bass-heavy music sync, release date overlay""", "動画生成", "ゲーム,トレーラー,告知", VIDEO_TOOLS])
current_id += 1

# Append to existing CSV
with open('prompts.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(prompts)

print(f"Added final {len(prompts)} high-quality prompts to prompts.csv")
print(f"Total prompts should now be exactly 100")
