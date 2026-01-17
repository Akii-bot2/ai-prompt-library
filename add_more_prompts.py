import csv

# Additional high-quality prompts with structured placeholders
# Starting from ID 37 (continuing from existing 36 prompts)

TEXT_TOOLS = "ChatGPT|https://chat.openai.com/;Claude|https://claude.ai/;Gemini|https://gemini.google.com/"
IMAGE_TOOLS = "Midjourney|https://www.midjourney.com/;Stable Diffusion|https://stability.ai/;Gemini|https://gemini.google.com/"
CODE_TOOLS = "GitHub Copilot|https://github.com/features/copilot;ChatGPT|https://chat.openai.com/;Gemini|https://gemini.google.com/"
AUDIO_TOOLS = "Suno AI|https://suno.com/;Udio|https://www.udio.com/"
VIDEO_TOOLS = "Runway Gen-2|https://runwayml.com/;Sora|https://openai.com/sora;Gemini|https://gemini.google.com/"

prompts = []
current_id = 37

# ===== 文章生成 追加 (12件) =====

prompts.append([current_id, "議事録作成", "",
"""【AIへの役割】
あなたは会議ファシリテーターです。

【目的・背景】
[例: 部門ミーティングの議事録を作成する]

【参加者】
[例: マーケティング部 5名]

【トーン・雰囲気】
簡潔で正確、要点を押さえた

【期待するアウトプット】
・日時、場所、参加者
・議題一覧
・各議題の議論要約
・決定事項
・アクションアイテム（担当者、期限）""", "文章生成", "議事録,ビジネス,会議", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "製品説明文", "",
"""【AIへの役割】
あなたはコピーライターです。

【目的・背景】
[例: ECサイトの商品ページ用説明文を作成]

【製品情報】
名前: [例: ワイヤレスイヤホン XYZ]
特徴: [例: ノイズキャンセリング、30時間再生]

【ターゲット】
[例: 20-40代の音楽好き]

【トーン・雰囲気】
魅力的で購買意欲を刺激する

【期待するアウトプット】
・キャッチコピー
・製品概要（100文字）
・詳細説明（300-500文字）
・スペック表""", "文章生成", "製品説明,EC,マーケティング", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "プレスリリース作成", "",
"""【AIへの役割】
あなたは広報担当者です。

【目的・背景】
[例: 新サービスのローンチを発表する]

【発表内容】
[例: AIチャットボットサービス開始]

【ターゲット】
[例: IT系メディア、業界記者]

【トーン・雰囲気】
公式、信頼性がある、ニュース価値を伝える

【期待するアウトプット】
・タイトル
・リード文（5W1H）
・本文（背景、詳細、今後の展望）
・会社概要
・問い合わせ先""", "文章生成", "プレスリリース,広報,メディア", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "FAQ作成", "",
"""【AIへの役割】
あなたはカスタマーサポートの専門家です。

【目的・背景】
[例: 自社サービスのヘルプページ用FAQ]

【サービス/製品】
[例: サブスクリプション型動画配信サービス]

【想定される質問カテゴリ】
[例: 料金、使い方、解約、トラブル]

【トーン・雰囲気】
親切で分かりやすい

【期待するアウトプット】
・カテゴリ別Q&A（各5-10件）
・回答は簡潔に（100文字以内）""", "文章生成", "FAQ,サポート,ヘルプ", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "求人票作成", "",
"""【AIへの役割】
あなたは採用担当者です。

【目的・背景】
[例: エンジニア採用の求人票を作成]

【ポジション詳細】
職種: [例: フロントエンドエンジニア]
雇用形態: [例: 正社員]
必須スキル: [例: React, TypeScript 3年以上]

【企業の魅力】
[例: フルリモート、フレックス制度]

【トーン・雰囲気】
魅力的で候補者を惹きつける

【期待するアウトプット】
・職種タイトル
・仕事内容
・応募条件
・福利厚生
・選考フロー""", "文章生成", "求人票,採用,HR", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "自己紹介文", "",
"""【AIへの役割】
あなたはパーソナルブランディングの専門家です。

【目的・背景】
[例: LinkedInプロフィール用の自己紹介]

【基本情報】
職業: [例: マーケティングマネージャー]
経験年数: [例: 10年]
強み: [例: データドリブンな戦略立案]

【ターゲット】
[例: 転職エージェント、採用担当者]

【トーン・雰囲気】
プロフェッショナルかつ人間味のある

【期待するアウトプット】
・キャッチフレーズ
・経歴要約
・実績ハイライト
・価値観・目標""", "文章生成", "自己紹介,キャリア,プロフィール", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "レビュー返信", "",
"""【AIへの役割】
あなたはカスタマーサクセス担当です。

【目的・背景】
[例: 低評価レビューに誠実に返信する]

【レビュー内容】
[例: 配送が遅れた、商品に傷があった]

【対象プラットフォーム】
[例: Amazon、Googleマップ]

【トーン・雰囲気】
誠実、謝罪と感謝、建設的

【期待するアウトプット】
・お礼
・問題への謝罪
・改善策の提示
・継続利用のお願い""", "文章生成", "レビュー,カスタマーサポート,返信", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "契約書ドラフト", "",
"""【AIへの役割】
あなたは法務アドバイザーです。

【目的・背景】
[例: フリーランス向け業務委託契約書のドラフト]

【契約種類】
[例: 業務委託契約、秘密保持契約、売買契約]

【主要条件】
[例: 期間、報酬、成果物の定義]

【トーン・雰囲気】
法的に正確、明確

【期待するアウトプット】
・契約書タイトル
・当事者情報
・目的条項
・権利義務
・期間・解除条項
・署名欄

※法的助言ではありません。専門家に確認してください。""", "文章生成", "契約書,法務,ビジネス", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "スピーチ原稿", "",
"""【AIへの役割】
あなたはスピーチライターです。

【目的・背景】
[例: 結婚式の友人代表スピーチ]

【シチュエーション】
場面: [例: 結婚式、入社式、卒業式]
時間: [例: 5分程度]

【話者情報】
[例: 新郎の大学時代の友人]

【トーン・雰囲気】
感動的、ユーモア、心温まる

【期待するアウトプット】
・冒頭（自己紹介、関係性）
・エピソード
・メッセージ
・締めの言葉""", "文章生成", "スピーチ,原稿,イベント", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "小説・ストーリー", "",
"""【AIへの役割】
あなたは小説家です。

【目的・背景】
[例: 短編小説のプロット作成]

【ジャンル】
[例: ミステリー、恋愛、SF、ファンタジー]

【設定】
舞台: [例: 近未来の東京]
主人公: [例: 記憶を失った探偵]

【トーン・雰囲気】
[例: ダーク、コミカル、感動的]

【期待するアウトプット】
・あらすじ（200文字）
・主要キャラクター紹介
・起承転結の構成
・冒頭シーン（500文字）""", "文章生成", "小説,ストーリー,クリエイティブ", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "ニュースレター", "",
"""【AIへの役割】
あなたはコンテンツマーケターです。

【目的・背景】
[例: 月次の顧客向けニュースレター]

【配信対象】
[例: 既存顧客500名]

【含めるコンテンツ】
[例: 新機能紹介、イベント告知、業界ニュース]

【トーン・雰囲気】
親しみやすく、価値を提供

【期待するアウトプット】
・件名（開封率を意識）
・挨拶
・各セクション（見出し+本文）
・CTA
・フッター""", "文章生成", "ニュースレター,メール,マーケティング", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "翻訳・ローカライズ", "",
"""【AIへの役割】
あなたはプロの翻訳者です。

【目的・背景】
[例: 日本語のWebサイトを英語にローカライズ]

【原文】
[翻訳したいテキストを貼り付け]

【翻訳方向】
[例: 日→英、英→日]

【トーン・雰囲気】
[例: フォーマル、カジュアル、技術的]

【ターゲット】
[例: アメリカ市場向け]

【期待するアウトプット】
・翻訳文
・文化的に適切な表現への調整
・意訳が必要な箇所の注釈""", "文章生成", "翻訳,ローカライズ,多言語", TEXT_TOOLS])
current_id += 1

# ===== 画像生成 追加 (12件) =====

prompts.append([current_id, "ポートレート写真風", "https://placehold.co/600x400/8B4513/ffffff?text=Portrait",
"""【目的・背景】
プロフィール写真、広告素材

【被写体】
性別/年齢: [例: 30代女性]
表情: [例: 自信に満ちた笑顔]
服装: [例: ビジネスカジュアル]

【撮影スタイル】
ライティング: [例: レンブラントライティング、自然光]
背景: [例: スタジオグレー、屋外ボケ]
構図: [例: バストアップ、3/4アングル]

【サンプルプロンプト】
professional headshot portrait, asian businesswoman, confident smile, soft studio lighting, blurred office background, 85mm lens, shallow depth of field, 8k""", "画像生成", "ポートレート,写真,プロフィール", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "商品撮影風", "https://placehold.co/600x400/ffffff/333333?text=Product",
"""【目的・背景】
EC、広告用の商品ビジュアル

【商品】
種類: [例: 化粧品、電子機器、アパレル]
特徴: [例: 高級感、ミニマル]

【撮影スタイル】
背景: [例: 白背景、グラデーション、生活シーン]
ライティング: [例: ソフトボックス、リムライト]
アングル: [例: 正面、45度、俯瞰]

【サンプルプロンプト】
product photography, luxury perfume bottle, minimalist white background, studio lighting, reflections, glass material, commercial quality, 8k""", "画像生成", "商品,撮影,EC", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "建物・建築CG", "https://placehold.co/600x400/87CEEB/333333?text=Architecture",
"""【目的・背景】
建築ビジュアライゼーション、不動産広告

【建築物】
種類: [例: モダン住宅、オフィスビル、商業施設]
スタイル: [例: ミニマリスト、和風、未来的]

【表現】
時間帯: [例: 昼、夕暮れ、夜景]
アングル: [例: 外観パース、インテリア、鳥瞰]
環境: [例: 緑化、都市環境]

【サンプルプロンプト】
architectural visualization, modern japanese house, minimalist design, large windows, wooden exterior, garden, sunset lighting, photorealistic render, 8k""", "画像生成", "建築,CG,不動産", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "抽象アート", "https://placehold.co/600x400/FF6B6B/ffffff?text=Abstract",
"""【目的・背景】
壁紙、アート作品、装飾

【コンセプト】
テーマ: [例: 感情、自然、音楽]
カラーパレット: [例: 暖色系、モノクロ、パステル]

【スタイル】
参考: [例: 抽象表現主義、幾何学的、流体アート]
テクスチャ: [例: 油絵の質感、デジタルスムース]

【サンプルプロンプト】
abstract art, fluid paint strokes, vibrant colors, blue and gold, emotional expression, modern art gallery style, high resolution, artistic""", "画像生成", "アート,抽象,装飾", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "イラスト（絵本風）", "https://placehold.co/600x400/FFD700/333333?text=Storybook",
"""【目的・背景】
絵本、児童向けコンテンツ

【シーン】
場面: [例: 森の動物たちのパーティー]
キャラクター: [例: うさぎ、くま、小鳥]

【スタイル】
塗り: [例: 水彩、パステル、クレヨン風]
タッチ: [例: 優しい、ほのぼの]

【サンプルプロンプト】
children's book illustration, cute forest animals having picnic, soft watercolor style, warm colors, whimsical, storybook art, gentle lighting""", "画像生成", "絵本,イラスト,児童", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "テクスチャ・パターン", "https://placehold.co/600x400/8FBC8F/ffffff?text=Texture",
"""【目的・背景】
デザイン素材、背景、3Dテクスチャ

【テクスチャ種類】
素材: [例: 木目、大理石、布地、金属]
パターン: [例: 幾何学、花柄、和風]

【仕様】
シームレス: [例: はい/いいえ]
解像度: [例: 4K]

【サンプルプロンプト】
seamless wood texture, light oak grain, natural pattern, high resolution, tileable, 4k, PBR material ready""", "画像生成", "テクスチャ,パターン,素材", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "モックアップ用画像", "https://placehold.co/600x400/4169E1/ffffff?text=Mockup",
"""【目的・背景】
デザイン提案、プレゼン用素材

【モックアップ種類】
デバイス: [例: iPhone、MacBook、ポスター]
シーン: [例: デスク上、手持ち、壁掛け]

【スタイル】
環境: [例: オフィス、カフェ、ミニマル]
アングル: [例: 正面、斜め、俯瞰]

【サンプルプロンプト】
mockup scene, iphone on wooden desk, minimal office environment, natural lighting, shallow depth of field, professional photography, 4k""", "画像生成", "モックアップ,デザイン,プレゼン", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "バナー・広告素材", "https://placehold.co/600x400/FF4500/ffffff?text=Banner",
"""【目的・背景】
Web広告、SNS広告のビジュアル

【広告内容】
商品/サービス: [例: フィットネスアプリ]
メッセージ: [例: 30日間無料トライアル]

【デザイン仕様】
サイズ: [例: 1200x628（Facebook）]
スタイル: [例: モダン、ポップ、高級感]

【サンプルプロンプト】
advertising banner design, fitness app promotion, energetic person exercising, bold typography space, vibrant orange gradient, modern design, eye-catching""", "画像生成", "バナー,広告,マーケティング", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "マスコットキャラクター", "https://placehold.co/600x400/32CD32/ffffff?text=Mascot",
"""【目的・背景】
企業/サービスのマスコット

【キャラクター設定】
モチーフ: [例: 動物、ロボット、食べ物]
性格: [例: 元気、優しい、知的]
ブランドイメージ: [例: テック系、エコ、子供向け]

【スタイル】
デザイン: [例: シンプル、ディテール多め]
用途: [例: 印刷物、アニメーション対応]

【サンプルプロンプト】
mascot character design, friendly robot, rounded shapes, blue and white colors, simple design, multiple expressions sheet, vector style, brand mascot""", "画像生成", "マスコット,キャラクター,ブランディング", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "SNS投稿用グラフィック", "https://placehold.co/600x400/E91E63/ffffff?text=Social",
"""【目的・背景】
Instagram、X等のフィード投稿

【コンテンツ】
種類: [例: 名言、お知らせ、Tips]
ブランド: [例: ロゴ、カラー指定]

【デザイン仕様】
サイズ: [例: 1080x1080（Instagram正方形）]
スタイル: [例: ミニマル、カラフル、エレガント]

【サンプルプロンプト】
social media post design, inspirational quote card, minimalist layout, soft pastel background, modern typography, instagram aesthetic, clean design""", "画像生成", "SNS,グラフィック,デザイン", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "コンセプトアート（SF）", "https://placehold.co/600x400/1a1a2e/00FF7F?text=Sci-Fi",
"""【目的・背景】
ゲーム、映画、小説のビジュアル開発

【シーン設定】
舞台: [例: 宇宙ステーション、火星コロニー]
時代: [例: 2150年]
テーマ: [例: 人類の宇宙進出]

【スタイル】
参考作品: [例: Blade Runner、Mass Effect]
雰囲気: [例: ユートピア、ディストピア]

【サンプルプロンプト】
sci-fi concept art, futuristic space station interior, holographic displays, sleek design, ambient blue lighting, astronauts in background, cinematic composition, matte painting style, 8k""", "画像生成", "コンセプトアート,SF,ゲーム", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "コンセプトアート（ファンタジー）", "https://placehold.co/600x400/4B0082/FFD700?text=Fantasy",
"""【目的・背景】
ゲーム、TRPG、小説のビジュアル

【シーン設定】
舞台: [例: 魔法の王国、ダンジョン]
要素: [例: ドラゴン、魔法使い、古代遺跡]

【スタイル】
参考: [例: ダークファンタジー、ハイファンタジー]
アーティスト風: [例: Frank Frazetta風]

【サンプルプロンプト】
fantasy concept art, ancient dragon's lair, treasure hoard, dramatic lighting, volumetric fog, epic scale, digital painting, artstation trending, 8k""", "画像生成", "コンセプトアート,ファンタジー,ゲーム", IMAGE_TOOLS])
current_id += 1

# ===== コーディング 追加 (12件) =====

prompts.append([current_id, "Python: 自動化スクリプト（ファイル操作）", "",
"""【AIへの役割】
あなたはPythonエンジニアです。

【目的・背景】
[例: フォルダ内のファイルを日付別に整理したい]

【入力】
対象: [例: ~/Downloads内のファイル]
条件: [例: 拡張子、作成日]

【処理内容】
[例: 年月フォルダを作成し移動]

【期待するアウトプット】
・コード（コメント付き）
・エラーハンドリング
・ログ出力
・ドライラン機能""", "コーディング", "Python,自動化,ファイル操作", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "Python: API連携", "",
"""【AIへの役割】
あなたはバックエンドエンジニアです。

【目的・背景】
[例: OpenWeather APIから天気情報を取得]

【API情報】
サービス: [例: OpenWeather]
認証: [例: APIキー]

【処理内容】
[例: 指定都市の天気を取得してJSON保存]

【期待するアウトプット】
・リクエスト処理
・レスポンスパース
・エラーハンドリング
・レート制限考慮""", "コーディング", "Python,API,外部連携", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "JavaScript: DOM操作", "",
"""【AIへの役割】
あなたはフロントエンドエンジニアです。

【目的・背景】
[例: フォームの入力バリデーションを実装]

【要件】
対象要素: [例: メールアドレス、電話番号]
バリデーション: [例: 必須、形式チェック]

【UI要件】
エラー表示: [例: 入力欄下に赤文字]
リアルタイム: [例: 入力中にチェック]

【期待するアウトプット】
・バニラJS実装
・HTML/CSS
・アクセシビリティ対応""", "コーディング", "JavaScript,DOM,フロントエンド", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "React: カスタムフック", "",
"""【AIへの役割】
あなたはReact専門家です。

【目的・背景】
[例: API呼び出しを共通化するカスタムフック]

【フック名】
[例: useFetch, useLocalStorage]

【機能要件】
[例: ローディング状態、エラーハンドリング、キャッシュ]

【期待するアウトプット】
・TypeScript対応フック
・使用例
・テストコード
・ドキュメント""", "コーディング", "React,フック,フロントエンド", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "CSS: アニメーション", "",
"""【AIへの役割】
あなたはCSSアニメーション専門家です。

【目的・背景】
[例: ボタンホバー時のエフェクト]

【アニメーション種類】
[例: フェード、スライド、バウンス、モーフィング]

【仕様】
トリガー: [例: ホバー、クリック、スクロール]
速度: [例: 0.3秒]
イージング: [例: ease-out]

【期待するアウトプット】
・CSS（@keyframes）
・HTML構造
・パフォーマンス考慮""", "コーディング", "CSS,アニメーション,UI", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "Node.js: バッチ処理", "",
"""【AIへの役割】
あなたはバックエンドエンジニアです。

【目的・背景】
[例: 毎日深夜にデータベースのバックアップ]

【処理内容】
[例: DBダンプ、圧縮、S3アップロード]

【スケジュール】
[例: cron形式で指定]

【期待するアウトプット】
・スクリプト
・ログ出力
・エラー通知（Slack等）
・リトライ処理""", "コーディング", "Node.js,バッチ,バックエンド", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "SQL: データ移行", "",
"""【AIへの役割】
あなたはDBAです。

【目的・背景】
[例: 旧テーブルから新テーブルへのデータ移行]

【テーブル構造】
移行元: [例: users_old (id, name, email)]
移行先: [例: users (id, first_name, last_name, email)]

【変換ルール】
[例: nameをfirst_nameとlast_nameに分割]

【期待するアウトプット】
・移行SQL
・データ検証クエリ
・ロールバック手順""", "コーディング", "SQL,データ移行,DBA", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "Docker: 開発環境構築", "",
"""【AIへの役割】
あなたはDevOpsエンジニアです。

【目的・背景】
[例: Node.js + PostgreSQL + Redisの開発環境]

【技術スタック】
言語/FW: [例: Node.js 20]
DB: [例: PostgreSQL 15]
その他: [例: Redis, Nginx]

【期待するアウトプット】
・Dockerfile
・docker-compose.yml
・.env.example
・README（起動手順）""", "コーディング", "Docker,DevOps,環境構築", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "テスト: ユニットテスト", "",
"""【AIへの役割】
あなたはQAエンジニアです。

【目的・背景】
[例: ユーティリティ関数のテストを作成]

【テスト対象】
関数/クラス: [例: formatDate, validateEmail]
言語: [例: JavaScript/TypeScript]

【フレームワーク】
[例: Jest, Vitest, pytest]

【期待するアウトプット】
・正常系テスト
・異常系テスト
・エッジケース
・モック/スタブ使用例""", "コーディング", "テスト,ユニットテスト,QA", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "GitHub Actions: CI/CD", "",
"""【AIへの役割】
あなたはDevOpsエンジニアです。

【目的・背景】
[例: PRマージ時に自動テスト＆デプロイ]

【パイプライン】
トリガー: [例: push, pull_request]
ステップ: [例: lint, test, build, deploy]

【デプロイ先】
[例: Vercel, AWS, GCP]

【期待するアウトプット】
・.github/workflows/ci.yml
・シークレット設定手順
・バッジ埋め込みコード""", "コーディング", "GitHub Actions,CI/CD,DevOps", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "正規表現: パターン作成", "",
"""【AIへの役割】
あなたは正規表現の専門家です。

【目的・背景】
[例: 電話番号を抽出したい]

【マッチ対象】
形式: [例: 090-1234-5678, 0901234567]
言語: [例: JavaScript, Python]

【期待するアウトプット】
・正規表現パターン
・使用例コード
・マッチ/非マッチ例
・解説""", "コーディング", "正規表現,パターン,テキスト処理", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "アルゴリズム: 実装", "",
"""【AIへの役割】
あなたはアルゴリズムの専門家です。

【目的・背景】
[例: 面接対策でソートアルゴリズムを理解したい]

【アルゴリズム】
[例: クイックソート、二分探索、ダイクストラ]

【言語】
[例: Python, JavaScript]

【期待するアウトプット】
・実装コード
・計算量（時間・空間）
・動作原理の解説
・使用場面""", "コーディング", "アルゴリズム,データ構造,学習", CODE_TOOLS])
current_id += 1

# ===== 音声・音楽生成 追加 (8件) =====

prompts.append([current_id, "ゲームBGM（フィールド）", "https://placehold.co/600x400/228B22/ffffff?text=Field+BGM",
"""【目的・背景】
RPG等のフィールドマップBGM

【シーン】
場所: [例: 草原、雪山、砂漠]
雰囲気: [例: 冒険的、神秘的、穏やか]

【楽器構成】
[例: オーケストラ、民族楽器、シンセ]

【仕様】
BPM: [例: 80-120]
ループ: [例: 対応必須]

【サンプルプロンプト】
adventure RPG field music, orchestral, light percussion, hopeful melody, moderate tempo 100bpm, fantasy adventure theme, seamless loop""", "音声・音楽生成", "ゲーム,フィールド,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ゲームBGM（メニュー）", "https://placehold.co/600x400/4a4a4a/ffffff?text=Menu+BGM",
"""【目的・背景】
ゲームのタイトル画面、メニュー画面

【雰囲気】
[例: 荘厳、期待感、ノスタルジック]

【楽器構成】
[例: ピアノ、ストリングス、アンビエント]

【仕様】
BPM: [例: 60-80]
ループ: [例: 対応]

【サンプルプロンプト】
game menu music, ambient piano, soft strings, peaceful atmosphere, slow tempo 70bpm, title screen theme, ethereal, loop ready""", "音声・音楽生成", "ゲーム,メニュー,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "効果音（UI）", "https://placehold.co/600x400/6366f1/ffffff?text=UI+SFX",
"""【目的・背景】
アプリ、ゲームのUI操作音

【効果音種類】
[例: ボタンクリック、通知、成功、エラー]

【スタイル】
[例: ミニマル、ゲーム風、高級感]

【仕様】
長さ: [例: 0.1-0.5秒]
フォーマット: [例: WAV, MP3]

【サンプルプロンプト】
UI click sound effect, soft click, modern app style, short crisp sound, satisfying feedback, high quality audio""", "音声・音楽生成", "効果音,UI,アプリ", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "YouTube BGM（チュートリアル）", "https://placehold.co/600x400/FF0000/ffffff?text=Tutorial+BGM",
"""【目的・背景】
解説動画、ハウツー動画のバックBGM

【雰囲気】
[例: 集中できる、邪魔にならない、軽快]

【楽器構成】
[例: ピアノ、アコースティックギター]

【仕様】
BPM: [例: 90-110]
長さ: [例: 3-5分ループ]

【サンプルプロンプト】
background music for tutorial video, light acoustic guitar, subtle piano, not distracting, moderate tempo 100bpm, corporate friendly, royalty free style""", "音声・音楽生成", "YouTube,チュートリアル,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ASMR・環境音", "https://placehold.co/600x400/2F4F4F/90EE90?text=Ambient",
"""【目的・背景】
睡眠導入、作業用環境音

【サウンドスケープ】
[例: 雨音、焚き火、カフェ、森]

【追加要素】
[例: 雷、鳥の声、人の話し声（遠く）]

【仕様】
長さ: [例: 30分-1時間]
ループ対応: [例: シームレス]

【サンプルプロンプト】
rain ambience, gentle rain on window, distant thunder, cozy indoor atmosphere, ASMR quality, seamless loop, 1 hour""", "音声・音楽生成", "ASMR,環境音,リラクゼーション", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "EDM・ダンストラック", "https://placehold.co/600x400/FF1493/ffffff?text=EDM",
"""【目的・背景】
クラブ、フェス、動画用

【サブジャンル】
[例: House, Trance, Dubstep, Future Bass]

【雰囲気】
[例: アップリフティング、ダーク、ハード]

【仕様】
BPM: [例: 128-145]
長さ: [例: 3-5分]

【サンプルプロンプト】
future bass EDM track, energetic synth drops, powerful bass, uplifting melody, 140bpm, festival anthem style, high quality production""", "音声・音楽生成", "EDM,ダンス,クラブ", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ジャズ・ラウンジ", "https://placehold.co/600x400/D2691E/ffffff?text=Jazz",
"""【目的・背景】
バー、レストラン、ラウンジBGM

【スタイル】
[例: スムースジャズ、ボサノバ、スウィング]

【楽器構成】
[例: ピアノトリオ、サックス、ウッドベース]

【雰囲気】
[例: 洗練、リラックス、ロマンチック]

【サンプルプロンプト】
smooth jazz lounge music, saxophone melody, piano accompaniment, upright bass, brushed drums, relaxed tempo 90bpm, sophisticated atmosphere""", "音声・音楽生成", "ジャズ,ラウンジ,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "オーケストラ・映画音楽", "https://placehold.co/600x400/FFD700/333333?text=Orchestral",
"""【目的・背景】
映画、トレーラー、壮大なシーン

【シーン】
[例: 戦闘、感動、サスペンス、勝利]

【楽器構成】
フルオーケストラ、合唱

【仕様】
BPM: [例: シーンによる]
長さ: [例: 2-4分]

【サンプルプロンプト】
epic orchestral cinematic music, full orchestra, choir, dramatic build-up, triumphant climax, movie trailer style, emotional, hans zimmer inspired""", "音声・音楽生成", "オーケストラ,映画,壮大", AUDIO_TOOLS])
current_id += 1

# ===== 動画生成 追加 (8件) =====

prompts.append([current_id, "製品デモ動画", "",
"""【AIへの役割】
あなたは動画ディレクターです。

【目的・背景】
[例: SaaSツールの機能紹介動画]

【製品】
[例: プロジェクト管理ツール]

【ターゲット】
[例: IT企業の意思決定者]

【動画仕様】
長さ: [例: 2分]
スタイル: [例: 画面録画+アニメーション]

【シーン構成】
・問題提起
・ソリューション紹介
・主要機能デモ
・ユーザーの声
・CTA

【サンプルプロンプト】
product demo video, clean UI animation, screen recording style, professional voiceover text overlay, modern transitions""", "動画生成", "デモ,製品,SaaS", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "インタビュー動画", "",
"""【目的・背景】
社員紹介、顧客インタビュー

【インタビュイー】
[例: CEO、顧客、社員]

【トーン】
[例: 誠実、親しみやすい、プロフェッショナル]

【撮影スタイル】
構図: [例: バストアップ、Bロール挿入]
ライティング: [例: 3点照明]
背景: [例: オフィス、白バック]

【サンプルプロンプト】
interview video style, talking head shot, professional lighting, blurred office background, confident speaker, b-roll cutaways""", "動画生成", "インタビュー,企業,人物", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "説明動画（アニメーション）", "",
"""【目的・背景】
サービス説明、コンセプト紹介

【内容】
[例: 保険商品の仕組み説明]

【アニメーションスタイル】
[例: 2Dイラスト、モーショングラフィックス、ホワイトボード]

【ナレーション】
[例: 日本語、男性、落ち着いた声]

【動画仕様】
長さ: [例: 90秒]

【サンプルプロンプト】
explainer video animation, 2D flat design, smooth motion graphics, icon animations, character illustration, corporate color scheme""", "動画生成", "説明動画,アニメーション,マーケティング", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "イベント・ハイライト", "",
"""【目的・背景】
カンファレンス、セミナーのダイジェスト

【イベント内容】
[例: 年次カンファレンス、展示会]

【含める要素】
[例: 基調講演、ブース、参加者インタビュー]

【編集スタイル】
テンポ: [例: 速いカット]
音楽: [例: アップビート]
長さ: [例: 2-3分]

【サンプルプロンプト】
event highlight video, dynamic cuts, energetic music sync, crowd shots, speaker presentations, booth interactions, time-lapse, drone shots""", "動画生成", "イベント,ハイライト,ダイジェスト", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "料理・レシピ動画", "",
"""【目的・背景】
YouTube、SNS用のレシピ紹介

【料理】
[例: パスタ、スイーツ、和食]

【撮影スタイル】
アングル: [例: 俯瞰、横から]
テンポ: [例: 早送り、リアルタイム]

【編集】
テキスト: [例: 分量、手順のテロップ]
BGM: [例: 軽快、落ち着いた]

【サンプルプロンプト】
cooking video, overhead shot, hands preparing food, ingredient close-ups, satisfying cutting sounds, text overlays with measurements, warm lighting""", "動画生成", "料理,レシピ,フード", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "トランジション・エフェクト", "",
"""【目的・背景】
動画編集用のトランジション素材

【種類】
[例: ワイプ、ズーム、グリッチ、液体]

【用途】
[例: YouTube、Vlog、企業動画]

【仕様】
解像度: [例: 4K]
フレームレート: [例: 60fps]
背景: [例: 透過、カラー]

【サンプルプロンプト】
video transition effect, liquid morphing, smooth animation, vibrant colors, 4K resolution, 60fps, alpha channel""", "動画生成", "トランジション,エフェクト,素材", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "ミュージックビデオ風", "",
"""【目的・背景】
楽曲のビジュアル化

【楽曲ジャンル】
[例: ポップ、ロック、ヒップホップ、EDM]

【ビジュアルスタイル】
[例: パフォーマンス、ストーリー、抽象]

【演出】
[例: ダンス、風景カット、VFX]

【サンプルプロンプト】
music video style, artist performance, dramatic lighting, slow motion shots, dynamic camera movement, visual effects, beat-synced editing""", "動画生成", "MV,ミュージックビデオ,音楽", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "不動産・物件紹介", "",
"""【目的・背景】
賃貸・売買物件の紹介動画

【物件】
種類: [例: マンション、一戸建て、オフィス]
特徴: [例: 駅近、新築、眺望]

【撮影スタイル】
[例: ジンバル移動、ドローン空撮]

【編集】
テキスト: [例: 間取り、価格表示]
音楽: [例: 落ち着いた、高級感]

【サンプルプロンプト】
real estate video tour, smooth gimbal walk-through, bright natural lighting, modern interior, room transitions, drone exterior shot, text overlays with specs""", "動画生成", "不動産,物件,紹介", VIDEO_TOOLS])
current_id += 1

# Append to existing CSV
with open('prompts.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(prompts)

print(f"Added {len(prompts)} additional high-quality prompts to prompts.csv")
print(f"Total prompts should now be approximately {36 + len(prompts)}")
