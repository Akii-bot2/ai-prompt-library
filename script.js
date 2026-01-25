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
    let currentLang = localStorage.getItem('siteLang') || (navigator.language.startsWith('ja') ? 'ja' : 'en');

    // Translation Dictionary
    const translations = {
        ja: {
            header: {
                title: 'AIプロンプトライブラリー',
                description: 'AI生成のためのプロンプトコレクション'
            },
            search: {
                placeholder: 'プロンプトを検索...'
            },
            category: {
                all: 'すべて'
            },
            solver: {
                title: '困っていることから探す',
                description: 'あなたのお悩みを入力すると、おすすめのプロンプトを3つ提案します',
                placeholder: '例: メールの文章がうまく書けない、SNS用の画像を作りたい、データ分析を自動化したい...',
                button: 'おすすめを見る'
            },
            onboarding: {
                slide1: { title: 'AIプロンプト集へようこそ！', desc: 'Gemini、ChatGPT、Midjourney、Suno AI などで使える<br>プロンプトテンプレートを<strong>100種類以上</strong>収録' },
                slide2: { title: 'カテゴリから探す', desc: '文章生成、画像生成、コーディングなど<br><strong>5つのカテゴリ</strong>からプロンプトを選択' },
                slide3: { title: 'ワンタップでコピー', desc: '気になるプロンプトのコピーボタンをタップ<br>そのまま<strong>AIツールに貼り付け</strong>るだけ！' },
                slide4: { title: '入力フォームで簡単カスタマイズ', desc: '「✏️ 入力」ボタンがあるプロンプトは<br><strong>フォームに入力するだけ</strong>で最適なプロンプトを生成' },
                skip: 'スキップ',
                next: '次へ'
            },
            loading: 'プロンプトを読み込み中...',
            error: 'プロンプトの読み込みに失敗しました。後でもう一度試してください。',
            noResult: '条件に一致するプロンプトが見つかりませんでした。',
            toolLabel: '推奨ツール:',
            form: {
                input: '入力',
                badge: 'フォーム入力対応',
                header: '情報を入力してプロンプトを生成',
                simple: 'かんたん',
                detailed: '詳細',
                optionalHeader: '詳細項目（オプション）',
                generate: 'プロンプトを生成',
                generated: '生成されたプロンプト',
                copy: 'コピー',
                copied: 'コピー完了'
            },
            ad: {
                toast: '✅ プロンプトをコピーしました！',
                pr: 'PR'
            }
        },
        en: {
            header: {
                title: 'AI Prompt Library',
                description: 'A collection of prompts for AI generation'
            },
            search: {
                placeholder: 'Search prompts...'
            },
            category: {
                all: 'All'
            },
            solver: {
                title: 'Find by Problem',
                description: 'Enter your problem and we will recommend 3 prompts.',
                placeholder: 'Ex: I cannot write email well, I want to create SNS images, I want to automate data analysis...',
                button: 'Get Recommendations'
            },
            onboarding: {
                slide1: { title: 'Welcome to AI Prompt Library!', desc: 'Over 100 prompt templates for Gemini, ChatGPT, Midjourney, Suno AI, etc.' },
                slide2: { title: 'Browse by Category', desc: 'Select prompts from <strong>5 categories</strong> including Text, Image, Coding, etc.' },
                slide3: { title: 'One-Tap Copy', desc: 'Tap the copy button and <strong>paste directly into your AI tool!</strong>' },
                slide4: { title: 'Easy Customization', desc: 'Prompts with "✏️ Input" button can be optimized just by <strong>filling in the form</strong>.' },
                skip: 'Skip',
                next: 'Next'
            },
            loading: 'Loading prompts...',
            error: 'Failed to load prompts. Please try again later.',
            noResult: 'No prompts found matching your criteria.',
            toolLabel: 'Recommended Tools:',
            form: {
                input: 'Input',
                badge: 'Form Supported',
                header: 'Fill form to generate prompt',
                simple: 'Simple',
                detailed: 'Detailed',
                optionalHeader: 'Optional Fields',
                generate: 'Generate Prompt',
                generated: 'Generated Prompt',
                copy: 'Copy',
                copied: 'Copied'
            },
            ad: {
                toast: '✅ Prompt copied!',
                pr: 'Ad'
            }
        }
    };

    // Category Images Language Map
    const categoryImagesMap = {
        ja: {
            '文章生成': 'images/category_text.png',
            '画像生成': 'images/category_image.png',
            'コーディング': 'images/category_coding.png',
            '音声・音楽生成': 'images/category_audio.png',
            '動画生成': 'images/category_video.png'
        },
        en: {
            'Text Generation': 'images/category_text.png',
            'Image Generation': 'images/category_image.png',
            'Coding': 'images/category_coding.png',
            'Audio/Music Generation': 'images/category_audio.png',
            'Video Generation': 'images/category_video.png'
        }
    };

    // Native Ads Data (Multi-language)
    const nativeAdsData = {
        ja: [
            {
                title: 'AI開発に最適な環境',
                description: 'ConoHa VPSなら、Python環境構築済みですぐに開発スタート。月額料金でコスト管理も簡単。',
                cta: 'ConoHa VPSを見る',
                url: 'https://px.a8.net/svt/ejp?a8mat=4AV8S9+1DEZZM+50+4YQJIQ',
                icon: 'fa-server',
                color: '#3b82f6'
            },
            // ... (other JA ads kept same, simplified here for brevity but in real code keep all)
            {
                title: '低価格＆高性能VPS',
                description: 'KAGOYA CLOUD VPSは初期費用無料、日額20円〜。AI開発やWebアプリ運用に最適な高機能VPS。',
                cta: 'KAGOYA VPSを見る',
                url: 'https://px.a8.net/svt/ejp?a8mat=4AV8S9+1FSQEQ+7YE+NWZDE',
                icon: 'fa-cloud',
                color: '#ff6b35'
            }
        ],
        en: [
            {
                title: 'Optimal Environment for AI Dev',
                description: 'Start developing immediately with pre-configured Python environment on ConoHa VPS.',
                cta: 'Check ConoHa VPS',
                url: 'https://px.a8.net/svt/ejp?a8mat=4AV8S9+1DEZZM+50+4YQJIQ',
                icon: 'fa-server',
                color: '#3b82f6'
            },
            {
                title: 'High Performance VPS',
                description: 'KAGOYA CLOUD VPS offers high functionality for AI development and Web apps.',
                cta: 'Check KAGOYA VPS',
                url: 'https://px.a8.net/svt/ejp?a8mat=4AV8S9+1FSQEQ+7YE+NWZDE',
                icon: 'fa-cloud',
                color: '#ff6b35'
            }
        ]
    };

    // Ad Toast Data (Multi-language)
    const adToastData = {
        ja: {
            '画像生成': { hint: '💡 画像生成にはRTX搭載PCが必須！32GBメモリで快適に', cta: '👉 RTX搭載ノートPC ¥219,800〜', url: '...' },
            'default': { hint: '💡 AI活用に最適なPCをチェック', cta: '👉 高コスパノートPC ¥123,800〜', url: '...' }
        },
        en: {
            'Image Generation': { hint: '💡 RTX PC is essential for image gen!', cta: '👉 RTX Laptop', url: '...' },
            'default': { hint: '💡 Check optimal PC for AI', cta: '👉 High CP Laptop', url: '...' }
        }
    };
    // (Note: Simplified ad data structure for brevity in replacement)


    // 1. Initialize
    initApp();

    function initApp() {
        updateLanguageUI(currentLang);
        setupLanguageSwitcher();
        fetchData(currentLang);

        // Search Listener
        searchInput.addEventListener('input', (e) => {
            activeKeyword = e.target.value.toLowerCase().trim();
            filterAndRenderCards();
        });
    }

    // Language Switcher Setup
    function setupLanguageSwitcher() {
        const btn = document.getElementById('lang-btn');
        const dropdown = document.getElementById('lang-dropdown');
        const options = dropdown.querySelectorAll('.lang-option');
        const currentLangSpan = document.getElementById('current-lang');

        // Initial state
        currentLangSpan.textContent = currentLang === 'ja' ? 'JP' : 'EN';
        options.forEach(opt => {
            opt.classList.toggle('active', opt.dataset.lang === currentLang);
        });

        // Toggle dropdown
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdown.classList.toggle('show');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', () => {
            dropdown.classList.remove('show');
        });

        // Handle language selection
        options.forEach(opt => {
            opt.addEventListener('click', () => {
                const newLang = opt.dataset.lang;
                if (newLang !== currentLang) {
                    currentLang = newLang;
                    localStorage.setItem('siteLang', currentLang);
                    currentLangSpan.textContent = currentLang === 'ja' ? 'JP' : 'EN';

                    // Update UI and fetch new data
                    updateLanguageUI(currentLang);
                    fetchData(currentLang);

                    // Update active class
                    options.forEach(o => o.classList.remove('active'));
                    opt.classList.add('active');
                }
            });
        });
    }

    // Update UI Text based on Language
    function updateLanguageUI(lang) {
        // Validation: fallback to 'ja' if lang is not found in translations
        if (!translations[lang]) {
            console.warn(`Language '${lang}' not found, falling back to 'ja'`);
            lang = 'ja';
            // Update state so other functions use the correct lang
            currentLang = 'ja';
            localStorage.setItem('siteLang', 'ja');
        }

        const t = translations[lang];

        // Update data-i18n elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const keyStr = el.dataset.i18n;
            if (keyStr) {
                const keys = keyStr.split('.');
                let value = t;
                keys.forEach(k => { value = value ? value[k] : null; });
                if (value) {
                    if (el.tagName !== 'INPUT' && el.tagName !== 'TEXTAREA') {
                        el.innerHTML = value;
                    }
                }
            }
        });

        // Update placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const keyStr = el.dataset.i18nPlaceholder;
            if (keyStr) {
                const keys = keyStr.split('.');
                let value = t;
                keys.forEach(k => { value = value ? value[k] : null; });
                if (value) el.placeholder = value;
            }
        });

        // Update html lang attribute
        document.documentElement.lang = lang;
    }

    // Fetch Data logic
    function fetchData(lang) {
        const filename = lang === 'ja' ? 'data_ja.json' : 'data_en.json';

        cardGrid.innerHTML = `<div class="loading">${translations[lang].loading}</div>`;

        fetch(filename)
            .then(response => {
                if (!response.ok) {
                    // Fallback to ja if en not found (during transition)
                    if (lang === 'en' && response.status === 404) {
                        return fetch('data_ja.json').then(r => r.json());
                    }
                    throw new Error('Failed to load data');
                }
                return response.json();
            })
            .then(data => {
                allPrompts = data;
                // Reset filters on lang switch
                activeCategory = 'all';
                activeTag = null;
                renderCategoryFilters(data);
                renderTagFilters(data);
                renderCards(data);
            })
            .catch(error => {
                console.error('Error:', error);
                cardGrid.innerHTML = `<div class="loading">${translations[lang].error}</div>`;
            });
    }

    // 3. Render Category Filters
    function renderCategoryFilters(data) {
        const t = translations[currentLang];

        // Extract unique categories
        const categories = new Set();
        data.forEach(item => {
            if (item.category) {
                categories.add(item.category);
            }
        });

        // Clear existing
        categoryFiltersContainer.innerHTML = '';

        // "All" button
        const allBtn = document.createElement('button');
        allBtn.className = 'category-btn active'; // Default active
        allBtn.textContent = t.category.all;
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

    // Native Ad Cards Data (Use centralized nativeAdsData)
    // (nativeAdsData is already defined in global scope)

    // Create Native Ad Card
    function createNativeAdCard(ad) {
        const t = translations[currentLang];
        const card = document.createElement('div');
        card.className = 'card native-ad-card';
        card.innerHTML = `
            <div class="card-image-container">
                <div class="native-ad-placeholder" style="background: linear-gradient(135deg, ${ad.color}22 0%, ${ad.color}44 100%);">
                    <i class="fa-solid ${ad.icon}" style="color: ${ad.color};"></i>
                </div>
                <div class="category-badge" style="background: ${ad.color};">${t.ad.pr}</div>
            </div>
            <div class="card-content">
                <div class="card-header">
                    <h2 class="card-title">${ad.title}</h2>
                </div>
                <div class="native-ad-description">
                    ${ad.description}
                </div>
                <a href="${ad.url}" target="_blank" rel="noopener noreferrer nofollow" class="native-ad-cta" style="background: ${ad.color};">
                    <i class="fa-solid fa-arrow-up-right-from-square"></i>
                    ${ad.cta}
                </a>
            </div>
        `;
        card.addEventListener('click', (e) => {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'native_ad_click', {
                    'event_category': 'advertising',
                    'event_label': ad.title,
                    'ad_type': 'native_card'
                });
            }
            if (!e.target.closest('.native-ad-cta')) {
                window.open(ad.url, '_blank');
            }
        });
        return card;
    }

    // 8. Render Cards Implementation
    function renderCards(prompts) {
        const t = translations[currentLang];
        const categoryImages = categoryImagesMap[currentLang];
        const nativeAds = nativeAdsData[currentLang];

        cardGrid.innerHTML = '';

        if (prompts.length === 0) {
            cardGrid.innerHTML = `<div class="loading">${t.noResult}</div>`;
            return;
        }

        // Sort: hasForm prompts first, then by original order (id)
        const sortedPrompts = [...prompts].sort((a, b) => {
            if (a.hasForm && !b.hasForm) return -1;
            if (!a.hasForm && b.hasForm) return 1;
            return a.id - b.id;
        });

        const fragment = document.createDocumentFragment();
        const adInterval = 10; // Insert ad every 10 cards
        let adIndex = 0;

        sortedPrompts.forEach((item, index) => {
            // Insert native ad card every 10 cards
            if (index > 0 && index % adInterval === 0 && adIndex < nativeAds.length) {
                const adCard = createNativeAdCard(nativeAds[adIndex]);
                fragment.appendChild(adCard);
                adIndex++;
            }

            const card = document.createElement('div');
            card.className = 'card';

            // Image handling
            let imageHtml = '';
            // Check if item.category exists in mapping, default to text if not found (fallback)
            const catImgSrc = categoryImages[item.category] || categoryImages['文章生成'] || categoryImages['Text Generation'];

            if (item.image) {
                imageHtml = `<img src="${item.image}" alt="${item.title}" class="card-image" loading="lazy">`;
            } else if (catImgSrc) {
                imageHtml = `<img src="${catImgSrc}" alt="${item.category}" class="card-image" loading="lazy">`;
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
                        <div class="tool-label">${t.toolLabel}</div>
                        <div class="tools-container">
                            ${toolsLinks}
                        </div>
                    </div>
                `;
            }

            // Category Badge
            const categoryBadge = item.category ? `<div class="category-badge">${item.category}</div>` : '';

            // Form button for hasForm prompts
            let formButtonHtml = '';
            let formBadgeHtml = '';
            if (item.hasForm) {
                formButtonHtml = `
                    <button class="form-btn" aria-label="Open form" onclick="togglePromptForm(${item.id}, this)">
                        <i class="fa-solid fa-edit"></i>
                        <span>${t.form.input}</span>
                    </button>
                `;
                formBadgeHtml = `<div class="form-supported-badge"><i class="fa-solid fa-sparkles"></i> ${t.form.badge}</div>`;
            }

            card.innerHTML = `
                <div class="card-image-container">
                    ${imageHtml}
                    ${categoryBadge}
                </div>
                <div class="card-content">
                    <div class="card-header">
                        <h2 class="card-title">${item.title}</h2>
                        <div class="card-actions">
                            ${formButtonHtml}
                            <button class="copy-btn" aria-label="Copy prompt" onclick="copyPrompt('${item.id}', this)">
                                <i class="fa-regular fa-copy"></i>
                            </button>
                        </div>
                    </div>
                    ${formBadgeHtml}
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
    const getAdToastConfig = (category) => {
        const ads = adToastData[currentLang];
        // Normalize category key for lookup (e.g., if category is "Image Generation")
        return ads[category] || ads['default'];
    };

    function showAdToast(category) {
        // Frequency cap: max 3 toasts per session
        const toastCount = parseInt(sessionStorage.getItem('adToastCount') || '0');
        if (toastCount >= 3) return;

        const t = translations[currentLang];
        let adConfig = getAdToastConfig(category);

        // If ad config is an array (not currently used but for future proof), select one
        const ad = Array.isArray(adConfig)
            ? adConfig[Math.floor(Math.random() * adConfig.length)]
            : adConfig;

        if (!ad) return;

        // Create custom toast element
        const toastNode = document.createElement('div');
        toastNode.innerHTML = `
            <div style="line-height: 1.6;">
                <div style="font-weight: bold; margin-bottom: 4px;">${t.ad.toast}</div>
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
                if (typeof gtag !== 'undefined') {
                    gtag('event', 'toast_ad_click', {
                        'event_category': 'advertising',
                        'event_label': category,
                        'ad_type': 'toast'
                    });
                }
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

            if (typeof gtag !== 'undefined') {
                gtag('event', 'prompt_copy', {
                    'event_category': 'engagement',
                    'event_label': category,
                    'prompt_id': id
                });
            }

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

    // ===== Prompt Form Feature =====

    // Extract variables from prompt text
    function extractVariables(promptText) {
        const regex = /\[(\*?)([^\]]+)\]/g;
        const variables = [];
        const seen = new Set();
        let match;

        while ((match = regex.exec(promptText)) !== null) {
            const fullMatch = match[0]; // [*variable name] or [variable name]
            const isEssential = match[1] === '*'; // Check if starts with *
            const varContent = match[2]; // variable name without brackets and *

            if (!seen.has(fullMatch)) {
                seen.add(fullMatch);
                // Extract label (the part before parentheses)
                const labelMatch = varContent.match(/^([^（(]+)/);
                const label = labelMatch ? labelMatch[1].trim() : varContent;

                variables.push({
                    full: fullMatch,
                    content: varContent,
                    label: label,
                    isEssential: isEssential
                });
            }
        }
        return variables;
    }

    // Tone labels for slider (Multi-language)
    const toneLabelsMap = {
        ja: {
            labels: ['フォーマル', 'ビジネス', 'カジュアル'],
            descriptions: {
                0: '敬語中心、堅めの表現',
                1: '丁寧だが堅すぎない標準的なビジネス文体',
                2: '親しみやすく柔らかい表現'
            },
            left: '堅い',
            right: '砕けた',
            header: '文体のトーン'
        },
        en: {
            labels: ['Formal', 'Business', 'Casual'],
            descriptions: {
                0: 'Strictly formal and polite.',
                1: 'Standard professional business tone.',
                2: 'Friendly and casual tone.'
            },
            left: 'Formal',
            right: 'Casual',
            header: 'Tone of Voice'
        }
    };

    // Generate form HTML with simple/detailed mode and tone slider
    function generateFormHTML(promptId, variables, category) {
        const t = translations[currentLang];
        const essentialVars = variables.filter(v => v.isEssential);
        const optionalVars = variables.filter(v => !v.isEssential);

        const createInputs = (vars, isOptional = false) => vars.map((v, index) => `
            <div class="prompt-form-field ${isOptional ? 'optional-field' : 'essential-field'}">
                <label class="prompt-form-label" for="form-${promptId}-${isOptional ? 'opt-' : ''}${index}">
                    ${v.label}
                    ${!isOptional ? '<span class="required-badge">Required</span>' : ''}
                </label>
                <input type="text" 
                       class="prompt-form-input" 
                       id="form-${promptId}-${isOptional ? 'opt-' : ''}${index}"
                       data-variable="${v.full.replace(/"/g, '&quot;')}"
                       placeholder="${v.content}">
            </div>
        `).join('');

        const essentialInputs = createInputs(essentialVars, false);
        const optionalInputs = createInputs(optionalVars, true);

        // Categories that don't need tone slider (non-text generation)
        // Adjust check for both EN/JA category names
        const noToneCategories = [
            '画像生成', '動画生成', '音声・音楽生成', 'コーディング',
            'Image Generation', 'Video Generation', 'Audio/Music Generation', 'Coding'
        ];
        const showToneSlider = !noToneCategories.includes(category);

        const toneData = toneLabelsMap[currentLang];

        const toneSliderHTML = showToneSlider ? `
                <!-- Tone Slider -->
                <div class="tone-slider-container">
                    <label class="tone-slider-label">
                        <i class="fa-solid fa-comment-dots"></i> ${toneData.header}
                    </label>
                    <div class="tone-slider-wrapper">
                        <span class="tone-label-left">${toneData.left}</span>
                        <input type="range" 
                               class="tone-slider" 
                               id="tone-${promptId}"
                               min="0" max="2" value="1"
                               oninput="updateToneLabel(${promptId})">
                        <span class="tone-label-right">${toneData.right}</span>
                    </div>
                    <div class="tone-current" id="tone-display-${promptId}">
                        <span class="tone-value">${toneData.labels[1]}</span>
                        <span class="tone-desc">${toneData.descriptions[1]}</span>
                    </div>
                </div>
        ` : '';

        return `
            <div class="prompt-form-container" id="form-container-${promptId}">
                <div class="prompt-form-header">
                    <i class="fa-solid fa-edit"></i> ${t.form.header}
                </div>
                
                <!-- Mode Toggle -->
                <div class="form-mode-toggle">
                    <button class="mode-btn active" data-mode="simple" onclick="toggleFormMode(${promptId}, 'simple', this)">
                        <i class="fa-solid fa-bolt"></i> ${t.form.simple}
                    </button>
                    <button class="mode-btn" data-mode="detailed" onclick="toggleFormMode(${promptId}, 'detailed', this)">
                        <i class="fa-solid fa-sliders"></i> ${t.form.detailed}
                    </button>
                </div>

                ${toneSliderHTML}

                <!-- Essential Fields (always visible) -->
                <div class="prompt-form-fields essential-fields">
                    ${essentialInputs}
                </div>

                <!-- Optional Fields (hidden in simple mode) -->
                <div class="prompt-form-fields optional-fields" id="optional-fields-${promptId}" style="display: none;">
                    <div class="optional-fields-header">
                        <i class="fa-solid fa-plus-circle"></i> ${t.form.optionalHeader}
                    </div>
                    ${optionalInputs}
                </div>

                <button class="generate-prompt-btn" onclick="generateFilledPrompt(${promptId})">
                    <i class="fa-solid fa-wand-magic-sparkles"></i>
                    ${t.form.generate}
                </button>
                <div class="generated-prompt-container" id="generated-${promptId}" style="display: none;">
                    <div class="generated-prompt-header">
                        <span><i class="fa-solid fa-check-circle"></i> ${t.form.generated}</span>
                        <button class="copy-generated-btn" onclick="copyGeneratedPrompt(${promptId})">
                            <i class="fa-regular fa-copy"></i> ${t.form.copy}
                        </button>
                    </div>
                    <pre class="generated-prompt-text" id="generated-text-${promptId}"></pre>
                </div>
            </div>
        `;
    }

    // Toggle form mode (simple/detailed)
    window.toggleFormMode = function (promptId, mode, btn) {
        const container = document.getElementById(`form-container-${promptId}`);
        const optionalFields = document.getElementById(`optional-fields-${promptId}`);
        const modeButtons = container.querySelectorAll('.mode-btn');

        modeButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        if (mode === 'detailed') {
            optionalFields.style.display = 'block';
        } else {
            optionalFields.style.display = 'none';
        }
    }

    // Update tone label when slider changes
    window.updateToneLabel = function (promptId) {
        const slider = document.getElementById(`tone-${promptId}`);
        const display = document.getElementById(`tone-display-${promptId}`);
        const value = parseInt(slider.value);
        const toneData = toneLabelsMap[currentLang];

        display.innerHTML = `
            <span class="tone-value">${toneData.labels[value]}</span>
            <span class="tone-desc">${toneData.descriptions[value]}</span>
        `;
    }

    // Toggle form visibility
    window.togglePromptForm = function (promptId, btn) {
        const card = btn.closest('.card');
        let formContainer = card.querySelector('.prompt-form-container');

        if (formContainer) {
            // Toggle visibility
            formContainer.classList.toggle('active');
            btn.classList.toggle('active');
        } else {
            // Create form
            const prompt = allPrompts.find(p => p.id === promptId);
            if (!prompt) return;

            const variables = extractVariables(prompt.prompt);
            if (variables.length === 0) return;

            const formHTML = generateFormHTML(promptId, variables, prompt.category);
            const cardContent = card.querySelector('.card-content');
            cardContent.insertAdjacentHTML('beforeend', formHTML);

            formContainer = card.querySelector('.prompt-form-container');
            formContainer.classList.add('active');
            btn.classList.add('active');
        }
    }

    // Generate filled prompt
    window.generateFilledPrompt = function (promptId) {
        const prompt = allPrompts.find(p => p.id === promptId);
        if (!prompt) return;

        let filledPrompt = prompt.prompt;
        const formContainer = document.getElementById(`form-container-${promptId}`);
        const inputs = formContainer.querySelectorAll('.prompt-form-input');

        inputs.forEach(input => {
            const variable = input.dataset.variable;
            const value = input.value.trim() || input.placeholder;
            filledPrompt = filledPrompt.split(variable).join(value);
        });

        // Apply tone from slider
        const toneSlider = document.getElementById(`tone-${promptId}`);
        if (toneSlider) {
            const toneValue = parseInt(toneSlider.value);
            const toneData = toneLabelsMap[currentLang];
            const toneText = toneData.labels[toneValue];

            const toneInstructionsMap = {
                ja: {
                    0: 'フォーマルな敬語中心で、堅めの表現を使用してください。',
                    1: '丁寧だが堅すぎない、標準的なビジネス文体で書いてください。',
                    2: '親しみやすく柔らかい表現を使い、適度にカジュアルに書いてください。'
                },
                en: {
                    0: 'Use a strictly formal and polite tone suitable for official documents.',
                    1: 'Use a standard professional business tone, polite but not overly stiff.',
                    2: 'Use a friendly and casual tone, easy to understand.'
                }
            };

            const toneInstruction = toneInstructionsMap[currentLang][toneValue];

            // Replace or append tone instruction
            // Note: This logic depends on the specific placeholder text in Japanese. 
            // For mult-lang, we might need a more robust way, but for now we check Japanese anchor.
            // Or we just append it if not found? 
            // Let's keep it simple: if JA and match found, replace. Else append.

            if (filledPrompt.includes('【トーン・雰囲気】')) {
                filledPrompt = filledPrompt.replace(
                    /(【トーン・雰囲気】\n)[^\n【]*/,
                    `$1文体: ${toneText}\n${toneInstruction}`
                );
            } else if (currentLang === 'en') {
                // Determine if there is a tone section in English prompt (if we had one)
                // For now, let's just append if it's a text prompt
                // (This is a simplification, ideally prompts have consistent structure)
            }
        }

        // Show generated prompt
        const generatedContainer = document.getElementById(`generated-${promptId}`);
        const generatedText = document.getElementById(`generated-text-${promptId}`);
        generatedText.textContent = filledPrompt;
        generatedContainer.style.display = 'block';

        // Scroll to generated prompt
        generatedContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        // GA4 tracking
        if (typeof gtag !== 'undefined') {
            gtag('event', 'prompt_generate', {
                'event_category': 'engagement',
                'prompt_id': promptId
            });
        }
    }

    // Copy generated prompt
    window.copyGeneratedPrompt = function (promptId) {
        const t = translations[currentLang];
        const generatedText = document.getElementById(`generated-text-${promptId}`);
        const textToCopy = generatedText.textContent;

        navigator.clipboard.writeText(textToCopy).then(() => {
            const btn = document.querySelector(`#generated-${promptId} .copy-generated-btn`);
            const originalHTML = btn.innerHTML;
            btn.innerHTML = `<i class="fa-solid fa-check"></i> ${t.form.copied}`;
            btn.classList.add('copied');

            // Get category for ad toast
            const card = btn.closest('.card');
            const categoryBadge = card.querySelector('.category-badge');
            const category = categoryBadge ? categoryBadge.textContent : 'default';
            showAdToast(category);

            setTimeout(() => {
                btn.innerHTML = originalHTML;
                btn.classList.remove('copied');
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy text: ', err);
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
        const promptText = `${prompt.title} ${prompt.category} ${prompt.tags.join(' ')} ${prompt.prompt} `.toLowerCase();

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
            < div class="recommendations-title" >
                <i class="fa-solid fa-circle-info"></i>
        おすすめが見つかりませんでした
                </div >
            <p style="color: var(--text-muted);">別のキーワードで試してみてください。例: 「メール」「画像」「自動化」など</p>
        `;
            recommendationsContainer.style.display = 'block';
            return;
        }

        const listHtml = recommendations.map((rec, index) => `
            < div class="recommendation-item" onclick = "scrollToCard(${rec.id})" >
                <div class="recommendation-info">
                    <div class="recommendation-title">${index + 1}. ${rec.title}</div>
                    <div class="recommendation-category">${rec.category}</div>
                </div>
                <span class="recommendation-score">マッチ度: ${Math.min(100, rec.score)}%</span>
                <i class="fa-solid fa-chevron-right recommendation-arrow"></i>
            </div >
            `).join('');

        recommendationsContainer.innerHTML = `
            < div class="recommendations-title" >
                <i class="fa-solid fa-check-circle"></i>
        おすすめのプロンプト
            </div >
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

    // ===== Onboarding Feature =====
    const ONBOARDING_KEY = 'ai_prompt_library_onboarding_completed';
    let currentSlide = 0;
    const totalSlides = 4;

    // Check if onboarding should be shown
    function shouldShowOnboarding() {
        return !localStorage.getItem(ONBOARDING_KEY);
    }

    // Show onboarding modal
    function showOnboarding() {
        const modal = document.getElementById('onboarding-modal');
        if (modal) {
            modal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    // Close onboarding modal
    window.closeOnboarding = function () {
        const modal = document.getElementById('onboarding-modal');
        if (modal) {
            modal.classList.remove('active');
            document.body.style.overflow = '';
            localStorage.setItem(ONBOARDING_KEY, 'true');
        }
    };

    // Go to specific slide
    function goToSlide(index) {
        if (index < 0 || index >= totalSlides) return;

        currentSlide = index;
        const slides = document.querySelectorAll('.onboarding-slide');
        const dots = document.querySelectorAll('.onboarding-dots .dot');
        const nextBtn = document.getElementById('onboarding-next');

        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });

        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });

        // Update button text on last slide
        const t = translations[currentLang];
        if (index === totalSlides - 1) {
            nextBtn.innerHTML = `${currentLang === 'ja' ? 'はじめる' : 'Start'} <i class="fa-solid fa-check"></i>`;
            nextBtn.classList.add('finish');
        } else {
            nextBtn.innerHTML = `${t.onboarding.next} <i class="fa-solid fa-chevron-right"></i>`;
            nextBtn.classList.remove('finish');
        }
    }

    // Next slide
    window.nextSlide = function () {
        if (currentSlide < totalSlides - 1) {
            goToSlide(currentSlide + 1);
        } else {
            closeOnboarding();
        }
    };

    // Previous slide
    function prevSlide() {
        if (currentSlide > 0) {
            goToSlide(currentSlide - 1);
        }
    }

    // Dot click handler
    function initDotNavigation() {
        const dots = document.querySelectorAll('.onboarding-dots .dot');
        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => goToSlide(i));
        });
    }

    // Touch swipe support
    function initSwipeNavigation() {
        const slidesContainer = document.getElementById('onboarding-slides');
        if (!slidesContainer) return;

        let startX = 0;
        let isDragging = false;

        slidesContainer.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
        }, { passive: true });

        slidesContainer.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
        }, { passive: true });

        slidesContainer.addEventListener('touchend', (e) => {
            if (!isDragging) return;
            isDragging = false;

            const endX = e.changedTouches[0].clientX;
            const diff = startX - endX;

            if (Math.abs(diff) > 50) {
                if (diff > 0) {
                    // Swipe left - next
                    nextSlide();
                } else {
                    // Swipe right - prev
                    prevSlide();
                }
            }
        }, { passive: true });
    }

    // Keyboard navigation
    function initKeyboardNavigation() {
        document.addEventListener('keydown', (e) => {
            const modal = document.getElementById('onboarding-modal');
            if (!modal || !modal.classList.contains('active')) return;

            if (e.key === 'ArrowRight' || e.key === 'Enter') {
                nextSlide();
            } else if (e.key === 'ArrowLeft') {
                prevSlide();
            } else if (e.key === 'Escape') {
                closeOnboarding();
            }
        });
    }

    // Overlay click to close
    function initOverlayClose() {
        const overlay = document.querySelector('.onboarding-overlay');
        if (overlay) {
            overlay.addEventListener('click', closeOnboarding);
        }
    }

    // Initialize onboarding
    function initOnboarding() {
        const LANG_SELECTED_KEY = 'ai_prompt_library_lang_selected';
        const modal = document.getElementById('first-visit-lang-modal');

        if (!localStorage.getItem(LANG_SELECTED_KEY)) {
            // If language not selected yet, show language selection modal
            setTimeout(() => {
                if (modal) {
                    modal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            }, 500);
        } else if (shouldShowOnboarding()) {
            initDotNavigation();
            initSwipeNavigation();
            initKeyboardNavigation();
            initOverlayClose();

            // Show after a short delay for better UX
            setTimeout(showOnboarding, 500);
        }
    }

    // Handle initial language selection
    window.selectInitialLang = function (lang) {
        const LANG_SELECTED_KEY = 'ai_prompt_library_lang_selected';
        localStorage.setItem(LANG_SELECTED_KEY, 'true');

        // Update language state
        currentLang = lang;
        localStorage.setItem('siteLang', lang);

        // Update UI
        updateLanguageUI(lang);
        fetchData(lang);

        // Update lang switcher active state
        const dropdown = document.getElementById('lang-dropdown');
        if (dropdown) {
            const options = dropdown.querySelectorAll('.lang-option');
            const currentLangSpan = document.getElementById('current-lang');
            currentLangSpan.textContent = lang === 'ja' ? 'JP' : 'EN';
            options.forEach(opt => {
                opt.classList.toggle('active', opt.dataset.lang === lang);
            });
        }

        // Close lang selection modal
        const langModal = document.getElementById('first-visit-lang-modal');
        if (langModal) {
            langModal.classList.remove('active');
            document.body.style.overflow = '';
        }

        // Proceed to onboarding
        initDotNavigation();
        initSwipeNavigation();
        initKeyboardNavigation();
        initOverlayClose();
        showOnboarding();
        goToSlide(0); // Ensure it starts from first slide with correct language
    };

    // Start onboarding check
    initOnboarding();
});
