import csv

# High-quality prompts with structured placeholders
# Format: id, title, image, prompt, category, tags, tools

TEXT_TOOLS = "ChatGPT|https://chat.openai.com/;Claude|https://claude.ai/;Gemini|https://gemini.google.com/"
IMAGE_TOOLS = "Midjourney|https://www.midjourney.com/;Stable Diffusion|https://stability.ai/;Gemini|https://gemini.google.com/"
CODE_TOOLS = "GitHub Copilot|https://github.com/features/copilot;ChatGPT|https://chat.openai.com/;Gemini|https://gemini.google.com/"
AUDIO_TOOLS = "Suno AI|https://suno.com/;Udio|https://www.udio.com/"
VIDEO_TOOLS = "Runway Gen-2|https://runwayml.com/;Sora|https://openai.com/sora;Gemini|https://gemini.google.com/"

prompts = []
current_id = 1

# ===== 文章生成カテゴリ (20件) =====

# メール文面
prompts.append([current_id, "ビジネスメール作成（謝罪）", "", 
"""【AIへの役割】
あなたはビジネスコミュニケーションのプロフェッショナルです。

【目的・背景】
[例: 納期遅延について取引先に謝罪する]

【ターゲット】
[例: 長年の取引先の担当者]

【トーン・雰囲気】
誠実で丁寧、かつプロフェッショナル

【期待するアウトプット】
・件名
・本文（挨拶、謝罪、原因説明、対策、締め）
・署名""", "文章生成", "メール文面,ビジネス,謝罪", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "ビジネスメール作成（依頼）", "", 
"""【AIへの役割】
あなたはビジネスメールの専門家です。

【目的・背景】
[例: 新規プロジェクトへの協力を依頼する]

【ターゲット】
[例: 他部署のマネージャー]

【トーン・雰囲気】
丁寧かつ説得力のある

【期待するアウトプット】
・件名
・本文（背景説明、依頼内容、メリット提示、締め切り）""", "文章生成", "メール文面,ビジネス,依頼", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "お礼メール作成", "", 
"""【AIへの役割】
あなたは心のこもったコミュニケーションの専門家です。

【目的・背景】
[例: 面接後のお礼を伝える]

【ターゲット】
[例: 採用担当者]

【トーン・雰囲気】
温かみがあり、誠実

【期待するアウトプット】
・件名
・本文（感謝、印象に残った点、意欲表明）""", "文章生成", "メール文面,お礼", TEXT_TOOLS])
current_id += 1

# マニュアル作成
prompts.append([current_id, "業務マニュアル作成", "", 
"""【AIへの役割】
あなたは業務プロセス設計の専門家です。

【目的・背景】
[例: 新入社員向けの経費精算手順書を作成する]

【ターゲット】
[例: 入社1ヶ月目の新入社員]

【トーン・雰囲気】
分かりやすく、ステップバイステップ

【期待するアウトプット】
・目次
・各ステップの詳細手順（スクリーンショット挿入箇所の指示含む）
・よくある質問（FAQ）
・注意点""", "文章生成", "マニュアル作成,業務,手順書", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "製品操作マニュアル", "", 
"""【AIへの役割】
あなたはテクニカルライターです。

【目的・背景】
[例: 家電製品の初期設定ガイドを作成する]

【ターゲット】
[例: テクノロジーに詳しくない高齢者]

【トーン・雰囲気】
簡潔で親切、専門用語を避ける

【期待するアウトプット】
・箱を開けてから使えるまでの手順
・図解の挿入箇所指示
・トラブルシューティング""", "文章生成", "マニュアル作成,製品,ガイド", TEXT_TOOLS])
current_id += 1

# 資料作成
prompts.append([current_id, "プレゼン資料構成案", "", 
"""【AIへの役割】
あなたはプレゼンテーションデザインの専門家です。

【目的・背景】
[例: 新規事業の提案を役員会で発表する]

【ターゲット】
[例: 経営層（意思決定者）]

【トーン・雰囲気】
論理的、説得力があり、データドリブン

【期待するアウトプット】
・スライド構成（10枚程度）
・各スライドの見出しとキーメッセージ
・ビジュアル候補の提案""", "文章生成", "資料作成,プレゼン,提案", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "企画書テンプレート", "", 
"""【AIへの役割】
あなたは企画立案のプロフェッショナルです。

【目的・背景】
[例: 社内イベントの企画を上司に提案する]

【ターゲット】
[例: 部門長]

【トーン・雰囲気】
説得力があり、具体的で実行可能

【期待するアウトプット】
・企画概要
・目的と期待効果
・スケジュール案
・予算概算
・リスクと対策""", "文章生成", "資料作成,企画書,提案", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "報告書作成", "", 
"""【AIへの役割】
あなたはビジネスレポートの専門家です。

【目的・背景】
[例: 四半期の営業成績を報告する]

【ターゲット】
[例: 経営陣]

【トーン・雰囲気】
客観的、簡潔、データに基づく

【期待するアウトプット】
・エグゼクティブサマリー
・主要KPIの分析
・課題と改善策
・次期の展望""", "文章生成", "資料作成,報告書,分析", TEXT_TOOLS])
current_id += 1

# ブログ・コンテンツ
prompts.append([current_id, "SEOブログ記事", "", 
"""【AIへの役割】
あなたはSEOとコンテンツマーケティングの専門家です。

【目的・背景】
[例: 「在宅ワーク 効率化」で検索上位を狙う]

【ターゲット】
[例: 在宅勤務を始めたばかりの会社員]

【トーン・雰囲気】
親しみやすく、実用的

【期待するアウトプット】
・SEO最適化されたタイトル（H1）
・メタディスクリプション
・見出し構成（H2, H3）
・本文（2000-3000文字）
・CTAの提案""", "文章生成", "ブログ,SEO,コンテンツ", TEXT_TOOLS])
current_id += 1

prompts.append([current_id, "SNS投稿文作成", "", 
"""【AIへの役割】
あなたはソーシャルメディアマーケターです。

【目的・背景】
[例: 新製品の認知度を上げたい]

【ターゲット】
[例: 20-30代の女性]

【トーン・雰囲気】
カジュアルで親しみやすい、絵文字適度に使用

【期待するアウトプット】
・Instagram用（画像キャプション、ハッシュタグ）
・X(Twitter)用（140字以内）
・投稿最適時間の提案""", "文章生成", "SNS,マーケティング,投稿", TEXT_TOOLS])
current_id += 1

# ===== 画像生成カテゴリ (20件) =====

prompts.append([current_id, "キャラクターデザイン（ファンタジー）", "https://placehold.co/600x400/2e1a1a/e9b645?text=Fantasy+Character", 
"""【目的・背景】
ゲームやイラスト用のオリジナルキャラクター

【キャラクター設定】
種族: [例: エルフ、人間、獣人]
職業: [例: 魔法使い、戦士、盗賊]
性別・年齢: [例: 女性、20代]
性格: [例: 勇敢、神秘的、陽気]

【ビジュアルスタイル】
[例: アニメスタイル、写実的、セルシェード]

【構図・ポーズ】
[例: 全身立ち絵、バストアップ、アクションポーズ]

【サンプルプロンプト】
female elf mage, long silver hair, glowing blue eyes, ornate robe, holding magical staff, forest background, fantasy art style, highly detailed, 8k""", "画像生成", "キャラクター,ファンタジー,ゲーム", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "キャラクターデザイン（現代）", "https://placehold.co/600x400/1a1a2e/e94560?text=Modern+Character", 
"""【目的・背景】
現代設定のキャラクターイラスト

【キャラクター設定】
職業: [例: 学生、会社員、アーティスト]
性別・年齢: [例: 男性、30代]
ファッション: [例: カジュアル、ストリート、フォーマル]

【ビジュアルスタイル】
[例: リアル調、イラスト調、漫画風]

【構図・ポーズ】
[例: 日常シーン、ポートレート]

【サンプルプロンプト】
young japanese businessman, modern suit, confident smile, city background, professional photograph style, cinematic lighting""", "画像生成", "キャラクター,現代,リアル", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "風景イラスト（自然）", "https://placehold.co/600x400/228B22/ffffff?text=Nature+Landscape", 
"""【目的・背景】
背景素材、壁紙、コンセプトアート用

【シーン設定】
場所: [例: 山、海、森、草原]
時間帯: [例: 朝焼け、昼、夕暮れ、夜]
季節: [例: 春、夏、秋、冬]
天気: [例: 晴れ、曇り、雨、雪]

【ビジュアルスタイル】
[例: 写真リアル、油絵風、ジブリ風、印象派]

【サンプルプロンプト】
breathtaking mountain landscape, sunset, golden hour lighting, snow-capped peaks, pine forest, lake reflection, oil painting style, 8k resolution""", "画像生成", "風景,自然,背景", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "風景イラスト（都市）", "https://placehold.co/600x400/1a1a2e/e94560?text=Urban+Landscape", 
"""【目的・背景】
都市景観のコンセプトアート

【シーン設定】
都市タイプ: [例: 近未来、現代東京、レトロ欧州]
時間帯: [例: 夜景、雨の日、霧]
視点: [例: 俯瞰、ストリートレベル、屋上から]

【ビジュアルスタイル】
[例: サイバーパンク、写実的、アニメ背景]

【サンプルプロンプト】
futuristic tokyo cityscape, neon lights, rain, reflections on wet streets, cyberpunk aesthetic, flying cars, holographic advertisements, cinematic lighting, 8k""", "画像生成", "風景,都市,SF", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "3Dオブジェクトデザイン", "https://placehold.co/600x400/4a4a4a/ffffff?text=3D+Object", 
"""【目的・背景】
ゲームアセット、プロダクトビジュアライゼーション

【オブジェクト】
種類: [例: 武器、家具、乗り物、食品]
詳細: [例: 中世の剣、モダンなソファ]

【ビジュアルスタイル】
[例: フォトリアル3D、ローポリ、スタイライズド]

【ライティング・背景】
[例: スタジオ照明、透明背景、環境光]

【サンプルプロンプト】
medieval fantasy sword, intricate gold handle design, glowing blue runes, 3D render, studio lighting, transparent background, octane render, highly detailed""", "画像生成", "3D,オブジェクト,ゲーム", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "ロゴデザイン", "https://placehold.co/600x400/000000/ffffff?text=Logo+Design", 
"""【目的・背景】
企業・サービス・イベント用のロゴ

【ブランド情報】
名前: [例: TechNova]
業種: [例: ITスタートアップ]
ブランドイメージ: [例: 革新的、信頼性、親しみやすい]

【デザイン希望】
タイプ: [例: シンボルマーク、ロゴタイプ、コンビネーション]
カラー: [例: 青系、モノクロ、グラデーション]
スタイル: [例: ミニマル、幾何学的、手書き風]

【サンプルプロンプト】
minimalist tech company logo, abstract geometric shape, blue gradient, modern typography, clean lines, vector style, white background""", "画像生成", "ロゴ,デザイン,ブランディング", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "アイコンセット", "https://placehold.co/600x400/6366f1/ffffff?text=Icon+Set", 
"""【目的・背景】
アプリ、Webサイト、プレゼン用のアイコン

【アイコン内容】
テーマ: [例: ビジネス、ヘルスケア、教育]
必要なアイコン: [例: ホーム、設定、ユーザー、検索]

【デザインスタイル】
線の太さ: [例: 細い線、太い線、塗りつぶし]
角: [例: 丸角、直角]
カラー: [例: 単色、グラデーション、アクセントカラー]

【サンプルプロンプト】
flat design icon set, business theme, home settings user search icons, thin line style, rounded corners, blue color scheme, consistent style, vector""", "画像生成", "アイコン,UI,Webデザイン", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "食品・料理写真風", "https://placehold.co/600x400/8B4513/ffffff?text=Food+Photo", 
"""【目的・背景】
メニュー、広告、SNS投稿用の料理ビジュアル

【料理情報】
料理名: [例: パスタ、寿司、ケーキ]
スタイル: [例: 和食、洋食、デザート]

【撮影スタイル】
アングル: [例: 真上(フラットレイ)、45度、接写]
ライティング: [例: 自然光、バックライト、ムーディ]
背景・小物: [例: 木のテーブル、白皿、ハーブ添え]

【サンプルプロンプト】
professional food photography, fresh sushi platter, wooden board, chopsticks, natural lighting, shallow depth of field, magazine quality, 8k""", "画像生成", "食品,写真,広告", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "インテリアデザイン", "https://placehold.co/600x400/DEB887/333333?text=Interior", 
"""【目的・背景】
住宅、オフィス、店舗のインテリア提案

【空間情報】
部屋タイプ: [例: リビング、寝室、オフィス]
スタイル: [例: モダン、北欧、和モダン]
広さ: [例: 20畳、コンパクト]

【要素】
家具: [例: ソファ、デスク、ベッド]
カラーパレット: [例: ナチュラル、モノトーン、アクセントカラー]
素材: [例: 木、コンクリート、ファブリック]

【サンプルプロンプト】
modern japanese living room interior, minimalist design, natural wood furniture, large windows, indoor plants, warm lighting, architectural photography, 8k""", "画像生成", "インテリア,建築,デザイン", IMAGE_TOOLS])
current_id += 1

prompts.append([current_id, "アニメ風イラスト", "https://placehold.co/600x400/FF69B4/ffffff?text=Anime+Style", 
"""【目的・背景】
同人誌、グッズ、アイコン用イラスト

【キャラクター】
タイプ: [例: 美少女、少年、デフォルメ]
表情: [例: 笑顔、クール、照れ]
服装: [例: 制服、ファンタジー衣装、私服]

【スタイル・作画】
参考作風: [例: 京アニ風、ufotable風、萌え系]
塗り: [例: アニメ塗り、厚塗り、水彩]

【サンプルプロンプト】
anime girl illustration, long pink hair, school uniform, cherry blossom background, cute smile, soft lighting, nijijourney style, high quality, detailed""", "画像生成", "アニメ,イラスト,キャラクター", IMAGE_TOOLS])
current_id += 1

# ===== コーディングカテゴリ (20件) =====

prompts.append([current_id, "Python: データ分析スクリプト", "", 
"""【AIへの役割】
あなたは経験豊富なPythonエンジニアです。

【目的・背景】
[例: CSVファイルの売上データを分析し、月次レポートを自動生成したい]

【開発環境】
Python: [例: 3.11]
使用ライブラリ: [例: pandas, matplotlib]

【入力データ】
[例: sales.csv - 日付、商品名、売上金額、個数のカラムを含む]

【期待するアウトプット】
・コード全体（コメント付き）
・月別売上集計
・グラフ出力（棒グラフ、折れ線グラフ）
・エラーハンドリング""", "コーディング", "Python,データ分析,自動化", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "Python: Webスクレイピング", "", 
"""【AIへの役割】
あなたはWebスクレイピングの専門家です。

【目的・背景】
[例: ニュースサイトから最新記事のタイトルとURLを取得したい]

【対象サイト】
[例: 一般的なニュースサイト（robots.txtを遵守）]

【技術要件】
ライブラリ: [例: requests, BeautifulSoup]
注意点: [例: レート制限、User-Agent設定]

【期待するアウトプット】
・スクレイピングコード
・データ保存（CSV/JSON）
・エラー処理
・法的注意事項のコメント""", "コーディング", "Python,スクレイピング,自動化", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "JavaScript: REST API実装", "", 
"""【AIへの役割】
あなたはNode.js/Express開発者です。

【目的・背景】
[例: ユーザー管理のCRUD APIを構築したい]

【技術スタック】
フレームワーク: [例: Express.js]
データベース: [例: MongoDB, PostgreSQL]

【エンドポイント】
[例: GET /users, POST /users, PUT /users/:id, DELETE /users/:id]

【期待するアウトプット】
・ルーティング設定
・コントローラー
・バリデーション
・エラーハンドリング
・Swagger/OpenAPIドキュメント""", "コーディング", "JavaScript,API,バックエンド", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "React: UIコンポーネント", "", 
"""【AIへの役割】
あなたはReactのフロントエンド専門家です。

【目的・背景】
[例: 再利用可能なモーダルコンポーネントを作成したい]

【技術スタック】
React: [例: 18.x]
スタイリング: [例: CSS Modules, Tailwind]
状態管理: [例: useState, Zustand]

【コンポーネント要件】
props: [例: isOpen, onClose, title, children]
機能: [例: ESCキーで閉じる、外側クリックで閉じる]

【期待するアウトプット】
・TypeScript対応のコンポーネント
・スタイル
・使用例（ストーリー）
・アクセシビリティ対応""", "コーディング", "React,フロントエンド,UI", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "SQL: 複雑なクエリ作成", "", 
"""【AIへの役割】
あなたはデータベースエンジニアです。

【目的・背景】
[例: 顧客の購買履歴から優良顧客を抽出したい]

【データベース】
種類: [例: PostgreSQL, MySQL]
テーブル構造: [例: customers, orders, products]

【要件】
抽出条件: [例: 過去1年で10万円以上購入した顧客]
並び順: [例: 購入金額の降順]

【期待するアウトプット】
・SQLクエリ
・インデックス推奨
・実行計画の解説
・パフォーマンス最適化のヒント""", "コーディング", "SQL,データベース,分析", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "HTML/CSS: レスポンシブレイアウト", "", 
"""【AIへの役割】
あなたはCSS設計の専門家です。

【目的・背景】
[例: モバイルファーストのランディングページを作成したい]

【レイアウト要件】
構成: [例: ヘッダー、ヒーロー、特徴セクション、フッター]
ブレイクポイント: [例: 768px, 1024px]

【デザイン仕様】
カラー: [例: プライマリ #3B82F6]
フォント: [例: Noto Sans JP]

【期待するアウトプット】
・セマンティックHTML
・モダンCSS（Flexbox/Grid）
・レスポンシブ対応
・アクセシビリティ考慮""", "コーディング", "HTML,CSS,Webサイト", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "TypeScript: 型定義設計", "", 
"""【AIへの役割】
あなたはTypeScriptの型システム専門家です。

【目的・背景】
[例: ECサイトのドメインモデルの型を設計したい]

【ドメイン】
エンティティ: [例: User, Product, Order, Cart]
関係性: [例: UserはOrdersを持つ、OrderはProductsを含む]

【要件】
ユーティリティ型: [例: Partial, Pick, Omit の活用]
ジェネリクス: [例: APIレスポンス型]

【期待するアウトプット】
・interface/type定義
・型ガード関数
・Zodスキーマ（オプション）
・使用例""", "コーディング", "TypeScript,型定義,設計", CODE_TOOLS])
current_id += 1

prompts.append([current_id, "Git: ワークフロー設計", "", 
"""【AIへの役割】
あなたはDevOpsエンジニアです。

【目的・背景】
[例: チーム開発のブランチ戦略を確立したい]

【チーム規模】
人数: [例: 5名]
リリース頻度: [例: 週1回]

【要件】
ブランチモデル: [例: Git Flow, GitHub Flow]
CI/CD: [例: GitHub Actions連携]

【期待するアウトプット】
・ブランチ命名規則
・マージ戦略
・コミットメッセージ規約
・プルリクエストテンプレート""", "コーディング", "Git,DevOps,チーム開発", CODE_TOOLS])
current_id += 1

# ===== 音声・音楽生成カテゴリ (10件) =====

prompts.append([current_id, "Lo-Fi BGM（作業用）", "https://placehold.co/600x400/4B0082/ffffff?text=Lo-Fi", 
"""【目的・背景】
作業・勉強に集中するためのBGM

【ムード・雰囲気】
[例: 穏やか、ノスタルジック、雨の日]

【楽器・サウンド】
メイン: [例: ピアノ、ギター]
サブ: [例: ソフトなドラム、環境音]

【テンポ・長さ】
BPM: [例: 70-85]
長さ: [例: 3分]

【サンプルプロンプト】
lo-fi hip hop, chill piano melody, soft vinyl crackle, rain ambience, slow tempo 75bpm, study focus, warm atmosphere""", "音声・音楽生成", "Lo-Fi,作業用,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ゲームBGM（バトル）", "https://placehold.co/600x400/8B0000/ffffff?text=Battle+BGM", 
"""【目的・背景】
ゲームのボス戦・バトルシーン用

【ムード・雰囲気】
[例: 激しい、緊迫感、壮大]

【楽器・サウンド】
メイン: [例: オーケストラ、エレキギター]
パーカッション: [例: 激しいドラム、ティンパニ]

【テンポ・長さ】
BPM: [例: 140-180]
ループ対応: [例: はい]

【サンプルプロンプト】
epic orchestral battle music, intense percussion, brass fanfare, electric guitar riffs, fast tempo 160bpm, boss fight theme, loop ready""", "音声・音楽生成", "ゲーム,バトル,BGM", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "ポッドキャスト用ジングル", "https://placehold.co/600x400/32CD32/ffffff?text=Podcast", 
"""【目的・背景】
番組のオープニング/エンディング用

【ムード・雰囲気】
[例: 明るい、プロフェッショナル、カジュアル]

【番組ジャンル】
[例: ビジネス、エンタメ、教育]

【テンポ・長さ】
長さ: [例: 5-10秒]
BPM: [例: 110-130]

【サンプルプロンプト】
upbeat podcast intro jingle, modern synth melody, corporate feel, professional, 8 seconds, catchy hook, fade out ready""", "音声・音楽生成", "ポッドキャスト,ジングル,短尺", AUDIO_TOOLS])
current_id += 1

prompts.append([current_id, "リラクゼーション音楽", "https://placehold.co/600x400/2F4F4F/F0FFF0?text=Relaxing", 
"""【目的・背景】
瞑想、ヨガ、睡眠導入用

【ムード・雰囲気】
[例: 穏やか、神秘的、自然]

【楽器・サウンド】
メイン: [例: シンセパッド、ピアノ]
環境音: [例: 波の音、鳥の声、風]

【テンポ・長さ】
BPM: [例: 50-70]
長さ: [例: 10分]

【サンプルプロンプト】
ambient meditation music, soft synthesizer pads, gentle piano, nature sounds, very slow tempo 55bpm, calming, healing frequencies, 432hz""", "音声・音楽生成", "リラクゼーション,瞑想,睡眠", AUDIO_TOOLS])
current_id += 1

# ===== 動画生成カテゴリ (10件) =====

prompts.append([current_id, "製品プロモーション動画", "", 
"""【AIへの役割】
あなたは動画プロデューサーです。

【目的・背景】
[例: 新発売のスマートウォッチのSNS広告動画]

【ターゲット】
[例: 20-30代の健康志向ビジネスパーソン]

【動画仕様】
長さ: [例: 30秒]
アスペクト比: [例: 9:16（縦動画）]
スタイル: [例: クリーン、ミニマル、ダイナミック]

【シーン構成】
イントロ: [例: 問題提起、日常シーン]
本編: [例: 製品登場、機能紹介]
アウトロ: [例: ロゴ、CTA]

【サンプルプロンプト（シーン別）】
Scene 1: close-up of smartwatch on wrist, morning sunlight, person checking health stats
Scene 2: dynamic transition, product features appearing, sleek animation""", "動画生成", "プロモーション,広告,SNS", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "YouTube動画オープニング", "", 
"""【目的・背景】
チャンネルのブランディング用イントロ

【チャンネルジャンル】
[例: テック系、Vlog、ゲーム実況]

【トーン・雰囲気】
[例: クール、ポップ、プロフェッショナル]

【動画仕様】
長さ: [例: 5秒]
ロゴ/チャンネル名: [例: TechReview]

【要素】
モーション: [例: ロゴアニメーション、パーティクル]
カラー: [例: ブランドカラー使用]
サウンド: [例: ジングル連動]

【サンプルプロンプト】
dynamic youtube intro animation, logo reveal, particle effects, tech style, blue neon glow, fast paced, 5 seconds, 4k""", "動画生成", "YouTube,オープニング,ブランディング", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "ドキュメンタリー風映像", "", 
"""【目的・背景】
ストーリーテリング、インタビュー素材

【テーマ】
[例: 職人の仕事、地域の歴史、自然環境]

【ビジュアルスタイル】
トーン: [例: シネマティック、ノスタルジック]
カラーグレード: [例: フィルム風、ナチュラル]

【カメラワーク】
[例: ゆっくりしたパン、クローズアップ、インタビューショット]

【サンプルプロンプト】
documentary style footage, craftsman hands working, warm color grading, shallow depth of field, slow cinematic movements, natural lighting, film grain""", "動画生成", "ドキュメンタリー,撮影,映像", VIDEO_TOOLS])
current_id += 1

prompts.append([current_id, "SNS用ショート動画", "", 
"""【目的・背景】
TikTok/Reels/Shorts用のエンゲージメント獲得

【コンテンツタイプ】
[例: ハウツー、Before/After、トレンド]

【ターゲット】
[例: Z世代]

【動画仕様】
長さ: [例: 15-60秒]
アスペクト比: 9:16

【要素】
フック: [例: 最初の3秒で興味を引く]
テンポ: [例: 速いカット]
テキスト: [例: 字幕オーバーレイ]

【サンプルプロンプト】
vertical video, fast cuts, trendy transitions, bright colorful aesthetic, gen-z style, dynamic camera movement, text overlays, engaging hook""", "動画生成", "SNS,ショート,TikTok", VIDEO_TOOLS])
current_id += 1

# Write to CSV
with open('prompts.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'title', 'image', 'prompt', 'category', 'tags', 'tools'])
    writer.writerows(prompts)

print(f"Created refined prompts.csv with {len(prompts)} high-quality prompts")
