document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const cardGrid = document.getElementById('card-grid');
    const categoryFiltersContainer = document.getElementById('category-filters');
    const tagFiltersContainer = document.getElementById('tag-filters');
    const searchInput = document.getElementById('search-input');

    // Category Default Images
    const categoryImages = {
        '文章生成': 'images/category_text.png',
        '画像生成': 'images/category_image.png',
        'コーディング': 'images/category_coding.png',
        '音声・音楽生成': 'images/category_audio.png',
        '動画生成': 'images/category_video.png'
    };

    // State
    let allPrompts = [];
    let activeCategory = 'all';
    let activeTag = null; // null means all tags in valid scope
    let activeKeyword = '';

    // 1. Fetch Data
    fetch('data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load data');
            }
            return response.json();
        })
        .then(data => {
            allPrompts = data;
            init(data);
        })
        .catch(error => {
            console.error('Error:', error);
            cardGrid.innerHTML = `<div class="loading">プロンプトの読み込みに失敗しました。後でもう一度試してください。</div>`;
        });

    // 2. Initialization
    function init(data) {
        renderCategoryFilters(data);
        renderTagFilters(data); // Initial: render all tags or relevant tags
        renderCards(data);

        // Search Listener
        searchInput.addEventListener('input', (e) => {
            activeKeyword = e.target.value.toLowerCase().trim();
            filterAndRenderCards();
        });
    }

    // 3. Render Category Filters
    function renderCategoryFilters(data) {
        // Extract unique categories
        const categories = new Set();
        data.forEach(item => {
            if (item.category) {
                categories.add(item.category);
            }
        });

        // Clear existing (except "All" handled by overwrite or logic, here simplified)
        categoryFiltersContainer.innerHTML = '';

        // "All" button
        const allBtn = document.createElement('button');
        allBtn.className = 'category-btn active'; // Default active
        allBtn.textContent = 'すべて';
        allBtn.dataset.category = 'all';
        allBtn.onclick = () => handleCategoryFilter('all', allBtn);
        categoryFiltersContainer.appendChild(allBtn);

        // Category buttons
        Array.from(categories).sort().forEach(cat => {
            const btn = document.createElement('button');
            btn.className = 'category-btn';
            btn.textContent = cat;
            btn.dataset.category = cat;
            btn.onclick = () => handleCategoryFilter(cat, btn);
            categoryFiltersContainer.appendChild(btn);
        });
    }

    // 4. Render Tag Filters based on current Category
    function renderTagFilters(data) {
        tagFiltersContainer.innerHTML = '';

        // Filter data based on activeCategory first to see what tags are available
        let relevantData = data;
        if (activeCategory !== 'all') {
            relevantData = data.filter(item => item.category === activeCategory);
        }

        const tags = new Set();
        relevantData.forEach(item => {
            item.tags.forEach(t => tags.add(t));
        });
        const sortedTags = Array.from(tags).sort();

        // If no tags available for this category (unlikely), valid but empty
        if (sortedTags.length === 0) return;

        // Create tag buttons
        sortedTags.forEach(tag => {
            const btn = document.createElement('button');
            btn.className = 'tag-btn';
            if (activeTag === tag) {
                btn.classList.add('active');
            }
            btn.textContent = tag;
            btn.dataset.tag = tag;
            btn.onclick = () => handleTagFilter(tag, btn);
            tagFiltersContainer.appendChild(btn);
        });
    }

    // 5. Handle Category Filter Click
    function handleCategoryFilter(category, clickedBtn) {
        if (activeCategory === category) return; // No change

        activeCategory = category;
        activeTag = null; // Reset tag selection when category changes

        // Update Category UI
        const catButtons = categoryFiltersContainer.querySelectorAll('.category-btn');
        catButtons.forEach(btn => btn.classList.remove('active'));
        clickedBtn.classList.add('active');

        // Re-render tags applicable to this new category
        renderTagFilters(allPrompts);

        // Filter cards
        filterAndRenderCards();
    }

    // 6. Handle Tag Filter Click
    function handleTagFilter(tag, clickedBtn) {
        // Toggle logic: if clicking active tag, deselect it
        if (activeTag === tag) {
            activeTag = null;
            clickedBtn.classList.remove('active');
        } else {
            activeTag = tag;
            // Update Tag UI
            const tagButtons = tagFiltersContainer.querySelectorAll('.tag-btn');
            tagButtons.forEach(btn => btn.classList.remove('active'));
            clickedBtn.classList.add('active');
        }

        filterAndRenderCards();
    }

    // 7. Filter and Render Cards logic
    function filterAndRenderCards() {
        let filtered = allPrompts;

        // Apply Category Filter
        if (activeCategory !== 'all') {
            filtered = filtered.filter(item => item.category === activeCategory);
        }

        // Apply Tag Filter
        if (activeTag) {
            filtered = filtered.filter(item => item.tags.includes(activeTag));
        }

        // Apply Keyword Search Filter
        if (activeKeyword) {
            filtered = filtered.filter(item => {
                const searchTarget = `
                    ${item.title} 
                    ${item.prompt} 
                    ${item.tags.join(' ')} 
                    ${item.category}
                `.toLowerCase();
                return searchTarget.includes(activeKeyword);
            });
        }

        renderCards(filtered);
    }

    // 8. Render Cards Implementation
    function renderCards(prompts) {
        cardGrid.innerHTML = '';

        if (prompts.length === 0) {
            cardGrid.innerHTML = '<div class="loading">条件に一致するプロンプトが見つかりませんでした。</div>';
            return;
        }

        const fragment = document.createDocumentFragment();

        prompts.forEach(item => {
            const card = document.createElement('div');
            card.className = 'card';

            // Image handling
            let imageHtml = '';
            if (item.image) {
                imageHtml = `<img src="${item.image}" alt="${item.title}" class="card-image" loading="lazy">`;
            } else if (categoryImages[item.category]) {
                imageHtml = `<img src="${categoryImages[item.category]}" alt="${item.category}" class="card-image" loading="lazy">`;
            } else {
                imageHtml = `
                    <div class="card-placeholder">
                        <i class="fa-solid fa-wand-magic-sparkles"></i>
                    </div>
                `;
            }

            // Tags HTML
            const tagsHtml = item.tags.map(tag => `<span class="tag">#${tag}</span>`).join('');

            // Tools HTML
            let toolsHtml = '';
            if (item.tools && item.tools.length > 0) {
                const toolsLinks = item.tools.map(tool => `
                    <a href="${tool.url}" target="_blank" rel="noopener noreferrer" class="tool-link">
                        <i class="fa-solid fa-arrow-up-right-from-square"></i> ${tool.name}
                    </a>
                `).join('');

                toolsHtml = `
                    <div class="card-tools">
                        <div class="tool-label">推奨ツール:</div>
                        <div class="tools-container">
                            ${toolsLinks}
                        </div>
                    </div>
                `;
            }

            // Category Badge
            const categoryBadge = item.category ? `<div class="category-badge">${item.category}</div>` : '';

            card.innerHTML = `
                <div class="card-image-container">
                    ${imageHtml}
                    ${categoryBadge}
                </div>
                <div class="card-content">
                    <div class="card-header">
                        <h2 class="card-title">${item.title}</h2>
                        <button class="copy-btn" aria-label="Copy prompt" onclick="copyPrompt('${item.id}', this)">
                            <i class="fa-regular fa-copy"></i>
                        </button>
                    </div>
                    <div class="prompt-text-container">
                        <code class="prompt-text" id="prompt-${item.id}">${item.prompt}</code>
                    </div>
                    <div class="card-tags">
                        ${tagsHtml}
                    </div>
                    ${toolsHtml}
                </div>
            `;
            fragment.appendChild(card);
        });

        cardGrid.appendChild(fragment);
    }

    // 9. Copy Functionality with Ad Toast
    // Ad data mapping by category
    const adData = {
        '画像生成': {
            hint: '💡 画像生成にはRTX搭載PCが必須！32GBメモリで快適に',
            cta: '👉 RTX搭載ノートPC ¥219,800〜',
            url: 'https://rpx.a8.net/svt/ejp?a8mat=4AV8S8+E97O8I+2HOM+BWGDT&rakuten=y&a8ejpredirect=https%3A%2F%2Fhb.afl.rakuten.co.jp%2Fhgc%2Fg00pw5s4.2bo11b4c.g00pw5s4.2bo12a23%2Fa26011868606_4AV8S8_E97O8I_2HOM_BWGDT%3Fpc%3Dhttps%253A%252F%252Fitem.rakuten.co.jp%252Fmousecomputer%252Fm-k7-h-ma%252F'
        },
        'コーディング': {
            hint: '💡 Python環境構築済み！開発・テスト環境に最適',
            cta: '👉 ConoHa VPSで快適開発',
            url: 'https://px.a8.net/svt/ejp?a8mat=4AV8S9+1DEZZM+50+4YQJIQ'
        },
        '文章生成': {
            hint: '💡 Office付きで文章作成もAIも快適',
            cta: '👉 高コスパノートPC ¥123,800〜',
            url: 'https://rpx.a8.net/svt/ejp?a8mat=4AV8S8+E97O8I+2HOM+BWGDT&rakuten=y&a8ejpredirect=https%3A%2F%2Fhb.afl.rakuten.co.jp%2Fhgc%2Fg00pw5s4.2bo11b4c.g00pw5s4.2bo12a23%2Fa26011868606_4AV8S8_E97O8I_2HOM_BWGDT%3Fpc%3Dhttps%253A%252F%252Fitem.rakuten.co.jp%252Fmousecomputer%252Fm-a5a5a01s%252F'
        },
        '音声・音楽生成': {
            hint: '💡 音楽AIはCPU/GPU性能が重要！RTX搭載で快適',
            cta: '👉 RTX搭載ノートPC ¥219,800〜',
            url: 'https://rpx.a8.net/svt/ejp?a8mat=4AV8S8+E97O8I+2HOM+BWGDT&rakuten=y&a8ejpredirect=https%3A%2F%2Fhb.afl.rakuten.co.jp%2Fhgc%2Fg00pw5s4.2bo11b4c.g00pw5s4.2bo12a23%2Fa26011868606_4AV8S8_E97O8I_2HOM_BWGDT%3Fpc%3Dhttps%253A%252F%252Fitem.rakuten.co.jp%252Fmousecomputer%252Fm-k7-h-ma%252F'
        },
        '動画生成': {
            hint: '💡 動画生成にはRTX搭載・32GBメモリが必須',
            cta: '👉 動画編集向けノートPC ¥219,800〜',
            url: 'https://rpx.a8.net/svt/ejp?a8mat=4AV8S8+E97O8I+2HOM+BWGDT&rakuten=y&a8ejpredirect=https%3A%2F%2Fhb.afl.rakuten.co.jp%2Fhgc%2Fg00pw5s4.2bo11b4c.g00pw5s4.2bo12a23%2Fa26011868606_4AV8S8_E97O8I_2HOM_BWGDT%3Fpc%3Dhttps%253A%252F%252Fitem.rakuten.co.jp%252Fmousecomputer%252Fm-k7-h-ma%252F'
        },
        'default': {
            hint: '💡 AI活用に最適なPCをチェック',
            cta: '👉 高コスパノートPC ¥123,800〜',
            url: 'https://rpx.a8.net/svt/ejp?a8mat=4AV8S8+E97O8I+2HOM+BWGDT&rakuten=y&a8ejpredirect=https%3A%2F%2Fhb.afl.rakuten.co.jp%2Fhgc%2Fg00pw5s4.2bo11b4c.g00pw5s4.2bo12a23%2Fa26011868606_4AV8S8_E97O8I_2HOM_BWGDT%3Fpc%3Dhttps%253A%252F%252Fitem.rakuten.co.jp%252Fmousecomputer%252Fm-a5a5a01s%252F'
        }
    };

    // Show ad toast with frequency cap
    function showAdToast(category) {
        // Frequency cap: max 3 toasts per session
        const toastCount = parseInt(sessionStorage.getItem('adToastCount') || '0');
        if (toastCount >= 3) return;

        const ad = adData[category] || adData['default'];

        // Create custom toast element
        const toastNode = document.createElement('div');
        toastNode.innerHTML = `
            <div style="line-height: 1.6;">
                <div style="font-weight: bold; margin-bottom: 4px;">✅ プロンプトをコピーしました！</div>
                <div style="font-size: 0.9em; opacity: 0.9;">${ad.hint}</div>
                <div style="margin-top: 8px; font-weight: 500; color: #60a5fa;">${ad.cta}</div>
            </div>
        `;

        Toastify({
            node: toastNode,
            duration: 6000,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            className: "ad-toast",
            style: {
                background: "linear-gradient(135deg, #1e293b 0%, #334155 100%)",
                borderRadius: "12px",
                padding: "16px 20px",
                maxWidth: "320px",
                boxShadow: "0 10px 25px rgba(0,0,0,0.3)",
                border: "1px solid #475569",
                cursor: "pointer"
            },
            onClick: function () {
                window.open(ad.url, '_blank');
            }
        }).showToast();

        sessionStorage.setItem('adToastCount', String(toastCount + 1));
    }

    window.copyPrompt = function (id, btnElement) {
        const textToCopy = document.getElementById(`prompt-${id}`).textContent;

        // Get the category from the card
        const card = btnElement.closest('.card');
        const categoryBadge = card.querySelector('.category-badge');
        const category = categoryBadge ? categoryBadge.textContent : 'default';

        navigator.clipboard.writeText(textToCopy).then(() => {
            const icon = btnElement.querySelector('i');
            btnElement.classList.add('copied');
            icon.classList.remove('fa-copy');
            icon.classList.add('fa-check');

            // Show ad toast
            showAdToast(category);

            setTimeout(() => {
                btnElement.classList.remove('copied');
                icon.classList.remove('fa-check');
                icon.classList.add('fa-copy');
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy text: ', err);
            alert('Failed to copy to clipboard');
        });
    }

    // ===== Problem Solver Feature =====
    const problemInput = document.getElementById('problem-input');
    const solveBtn = document.getElementById('solve-btn');
    const recommendationsContainer = document.getElementById('recommendations');

    // Keyword mapping for problem-to-solution matching
    const keywordMapping = {
        // Text/Writing related
        'メール': ['メール文面', 'ビジネス', '文章生成'],
        'mail': ['メール文面', 'ビジネス', '文章生成'],
        '文章': ['文章生成', 'ブログ', 'コンテンツ'],
        '書く': ['文章生成', 'ライティング'],
        '作文': ['文章生成', 'ライティング'],
        'ブログ': ['ブログ', 'SEO', 'コンテンツ'],
        '記事': ['ブログ', 'ニュース', 'SEO'],
        '翻訳': ['翻訳', 'ローカライズ'],
        'プレゼン': ['プレゼン', '資料作成', '提案'],
        '資料': ['資料作成', 'プレゼン', '報告書'],
        '報告書': ['報告書', '分析', 'ビジネス'],
        '議事録': ['議事録', '会議', 'ビジネス'],
        'マニュアル': ['マニュアル作成', '手順書', 'ガイド'],
        '求人': ['求人票', '採用', 'HR'],
        'SNS': ['SNS', 'マーケティング', '投稿'],
        'ツイート': ['SNS', 'マーケティング', 'X'],
        'インスタ': ['SNS', 'マーケティング', 'Instagram'],
        '広告': ['広告', 'マーケティング', 'キャッチコピー'],
        'キャッチコピー': ['キャッチコピー', '広告', 'マーケティング'],
        'スピーチ': ['スピーチ', '原稿', 'イベント'],
        '小説': ['小説', 'ストーリー', 'クリエイティブ'],
        'FAQ': ['FAQ', 'サポート', 'ヘルプ'],
        'レビュー': ['レビュー', 'カスタマーサポート', '返信'],
        '契約書': ['契約書', '法務', 'ビジネス'],
        'アンケート': ['アンケート', 'リサーチ', '調査'],

        // Image related
        '画像': ['画像生成', 'イラスト', 'デザイン'],
        'イラスト': ['イラスト', '画像生成', 'キャラクター'],
        '絵': ['画像生成', 'イラスト', 'アート'],
        'デザイン': ['デザイン', 'ロゴ', 'UI'],
        'ロゴ': ['ロゴ', 'ブランディング', 'デザイン'],
        'アイコン': ['アイコン', 'UI', 'Webデザイン'],
        'キャラクター': ['キャラクター', 'イラスト', 'ゲーム'],
        'マスコット': ['マスコット', 'キャラクター', 'ブランディング'],
        '写真': ['写真', 'ポートレート', '撮影'],
        '商品': ['商品', '撮影', 'EC'],
        '建築': ['建築', 'CG', '不動産'],
        'インテリア': ['インテリア', '建築', 'デザイン'],
        '食べ物': ['食品', 'フード', '料理'],
        '料理': ['食品', 'フード', '料理'],
        'バナー': ['バナー', '広告', 'マーケティング'],
        'サムネイル': ['サムネイル', 'YouTube', 'SNS'],
        'コンセプトアート': ['コンセプトアート', 'ゲーム', 'ファンタジー'],
        'ファンタジー': ['ファンタジー', 'コンセプトアート', 'キャラクター'],
        'SF': ['SF', 'コンセプトアート', '未来'],
        'テクスチャ': ['テクスチャ', 'パターン', '素材'],

        // Coding related
        'コード': ['コーディング', 'プログラミング'],
        'プログラム': ['コーディング', 'プログラミング'],
        'スクリプト': ['Python', '自動化', 'コーディング'],
        '自動化': ['自動化', 'Python', 'バッチ'],
        'API': ['API', 'バックエンド', 'JavaScript'],
        'Web': ['Webサイト', 'HTML', 'フロントエンド'],
        'ホームページ': ['Webサイト', 'HTML', 'CSS'],
        'アプリ': ['React', 'フロントエンド', 'UI'],
        'Python': ['Python', 'データ分析', '自動化'],
        'JavaScript': ['JavaScript', 'フロントエンド', 'API'],
        'React': ['React', 'フロントエンド', 'UI'],
        'SQL': ['SQL', 'データベース', '分析'],
        'データベース': ['データベース', 'SQL', '設計'],
        'テスト': ['テスト', 'ユニットテスト', 'QA'],
        'Docker': ['Docker', 'DevOps', '環境構築'],
        'GitHub': ['GitHub Actions', 'CI/CD', 'DevOps'],
        'セキュリティ': ['セキュリティ', '脆弱性', '対策'],
        '正規表現': ['正規表現', 'パターン', 'テキスト処理'],
        'アルゴリズム': ['アルゴリズム', 'データ構造', '学習'],
        'CSS': ['CSS', 'アニメーション', 'UI'],
        'アニメーション': ['アニメーション', 'CSS', 'UI'],

        // Audio related
        '音楽': ['音声・音楽生成', 'BGM', '作曲'],
        'BGM': ['BGM', '音声・音楽生成', 'ゲーム'],
        '曲': ['音声・音楽生成', 'BGM', '楽曲'],
        '作曲': ['音声・音楽生成', 'BGM'],
        'ゲーム音楽': ['ゲーム', 'BGM', 'バトル'],
        'リラックス': ['リラックス', 'リラクゼーション', '瞑想'],
        '環境音': ['ASMR', '環境音', 'リラクゼーション'],
        'ジングル': ['ジングル', 'ポッドキャスト', '短尺'],
        '着信音': ['着信音', '通知音', 'アプリ'],
        'EDM': ['EDM', 'ダンス', 'クラブ'],
        'ジャズ': ['ジャズ', 'ラウンジ', 'BGM'],
        'オーケストラ': ['オーケストラ', '映画', '壮大'],

        // Video related
        '動画': ['動画生成', '映像', 'YouTube'],
        '映像': ['動画生成', '映像', 'シネマティック'],
        'YouTube': ['YouTube', '動画', 'オープニング'],
        'ショート': ['SNS', 'ショート', 'TikTok'],
        'TikTok': ['SNS', 'ショート', 'TikTok'],
        'プロモーション': ['プロモーション', '広告', 'SNS'],
        'CM': ['プロモーション', '広告', '製品'],
        'トレーラー': ['トレーラー', 'ゲーム', '告知'],
        'インタビュー': ['インタビュー', '企業', '人物'],
        '結婚式': ['ウェディング', '結婚式', 'イベント'],
        '研修': ['教育', '研修', 'Eラーニング'],
        '旅行': ['旅行', '観光', 'PR'],
        '不動産': ['不動産', '物件', '紹介'],
    };

    // Score calculation function
    function calculateRelevanceScore(prompt, userProblem) {
        let score = 0;
        const problemLower = userProblem.toLowerCase();
        const promptText = `${prompt.title} ${prompt.category} ${prompt.tags.join(' ')} ${prompt.prompt}`.toLowerCase();

        // Direct text match
        const problemWords = problemLower.split(/[\s,、。]+/).filter(w => w.length > 1);
        problemWords.forEach(word => {
            if (promptText.includes(word)) {
                score += 10;
            }
        });

        // Keyword mapping match
        Object.keys(keywordMapping).forEach(keyword => {
            if (problemLower.includes(keyword.toLowerCase())) {
                const relatedTags = keywordMapping[keyword];
                relatedTags.forEach(tag => {
                    if (prompt.tags.includes(tag) || prompt.category.includes(tag)) {
                        score += 15;
                    }
                    if (promptText.includes(tag.toLowerCase())) {
                        score += 5;
                    }
                });
            }
        });

        return score;
    }

    // Get top 3 recommendations
    function getRecommendations(userProblem) {
        if (!userProblem.trim()) return [];

        const scoredPrompts = allPrompts.map(prompt => ({
            ...prompt,
            score: calculateRelevanceScore(prompt, userProblem)
        }));

        return scoredPrompts
            .filter(p => p.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 3);
    }

    // Render recommendations
    function renderRecommendations(recommendations) {
        if (recommendations.length === 0) {
            recommendationsContainer.innerHTML = `
                <div class="recommendations-title">
                    <i class="fa-solid fa-circle-info"></i>
                    おすすめが見つかりませんでした
                </div>
                <p style="color: var(--text-muted);">別のキーワードで試してみてください。例: 「メール」「画像」「自動化」など</p>
            `;
            recommendationsContainer.style.display = 'block';
            return;
        }

        const listHtml = recommendations.map((rec, index) => `
            <div class="recommendation-item" onclick="scrollToCard(${rec.id})">
                <div class="recommendation-info">
                    <div class="recommendation-title">${index + 1}. ${rec.title}</div>
                    <div class="recommendation-category">${rec.category}</div>
                </div>
                <span class="recommendation-score">マッチ度: ${Math.min(100, rec.score)}%</span>
                <i class="fa-solid fa-chevron-right recommendation-arrow"></i>
            </div>
        `).join('');

        recommendationsContainer.innerHTML = `
            <div class="recommendations-title">
                <i class="fa-solid fa-check-circle"></i>
                おすすめのプロンプト
            </div>
            <div class="recommendation-list">
                ${listHtml}
            </div>
        `;
        recommendationsContainer.style.display = 'block';
    }

    // Scroll to card and highlight
    window.scrollToCard = function (promptId) {
        // Reset filters to show all
        activeCategory = 'all';
        activeTag = null;
        activeKeyword = '';
        searchInput.value = '';

        // Re-render with all prompts
        const catButtons = categoryFiltersContainer.querySelectorAll('.category-btn');
        catButtons.forEach(btn => btn.classList.remove('active'));
        categoryFiltersContainer.querySelector('[data-category="all"]').classList.add('active');
        renderTagFilters(allPrompts);
        renderCards(allPrompts);

        // Find and scroll to the card
        setTimeout(() => {
            const targetCard = document.querySelector(`#prompt-${promptId}`);
            if (targetCard) {
                const card = targetCard.closest('.card');
                card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                card.style.boxShadow = '0 0 0 3px var(--accent-color)';
                setTimeout(() => {
                    card.style.boxShadow = '';
                }, 3000);
            }
        }, 100);
    }

    // Event listener for solve button
    if (solveBtn) {
        solveBtn.addEventListener('click', () => {
            const problem = problemInput.value;
            const recommendations = getRecommendations(problem);
            renderRecommendations(recommendations);
        });

        // Also trigger on Enter key
        problemInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                solveBtn.click();
            }
        });
    }
});
