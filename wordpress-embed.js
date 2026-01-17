/**
 * AI Prompt Library - WordPress Embed Version
 * GitHub: https://github.com/Akii-bot2/ai-prompt-library
 * 
 * このファイルをWordPressの固定ページに埋め込んで使用します
 */

(function () {
    'use strict';

    // Configuration
    const CONFIG = {
        dataUrl: 'https://akii-bot2.github.io/ai-prompt-library/data.json',
        containerId: 'prompt-library-app',
        itemsPerPage: 12
    };

    // State
    let allPrompts = [];
    let currentCategory = 'all';
    let currentPage = 1;

    // Initialize
    document.addEventListener('DOMContentLoaded', init);

    async function init() {
        const container = document.getElementById(CONFIG.containerId);
        if (!container) {
            console.error('Prompt Library: Container not found');
            return;
        }

        // Inject styles
        injectStyles();

        // Show loading
        container.innerHTML = '<div class="pl-loading">プロンプトを読み込み中...</div>';

        try {
            const response = await fetch(CONFIG.dataUrl);
            if (!response.ok) throw new Error('Failed to fetch data');
            allPrompts = await response.json();
            render(container);
        } catch (error) {
            console.error('Prompt Library Error:', error);
            container.innerHTML = '<div class="pl-error">データの読み込みに失敗しました。</div>';
        }
    }

    function render(container) {
        const categories = [...new Set(allPrompts.map(p => p.category))];

        container.innerHTML = `
            <div class="pl-header">
                <h2 class="pl-title">🪄 AIプロンプトライブラリー</h2>
                <p class="pl-subtitle">100種類の高品質プロンプト集</p>
            </div>
            
            <div class="pl-filters">
                <button class="pl-category-btn active" data-category="all">すべて</button>
                ${categories.map(cat => `<button class="pl-category-btn" data-category="${cat}">${cat}</button>`).join('')}
            </div>
            
            <div class="pl-grid" id="pl-grid"></div>
            
            <div class="pl-load-more" id="pl-load-more">
                <button class="pl-more-btn" id="pl-more-btn">もっと見る</button>
            </div>
        `;

        // Event listeners
        container.querySelectorAll('.pl-category-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                container.querySelectorAll('.pl-category-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentCategory = btn.dataset.category;
                currentPage = 1;
                renderCards();
            });
        });

        document.getElementById('pl-more-btn').addEventListener('click', () => {
            currentPage++;
            renderCards(true);
        });

        renderCards();
    }

    function renderCards(append = false) {
        const grid = document.getElementById('pl-grid');
        const loadMore = document.getElementById('pl-load-more');

        let filtered = allPrompts;
        if (currentCategory !== 'all') {
            filtered = allPrompts.filter(p => p.category === currentCategory);
        }

        const start = 0;
        const end = currentPage * CONFIG.itemsPerPage;
        const toShow = filtered.slice(start, end);
        const hasMore = end < filtered.length;

        if (!append) {
            grid.innerHTML = '';
        }

        const startIndex = append ? (currentPage - 1) * CONFIG.itemsPerPage : 0;
        const newItems = toShow.slice(startIndex);

        newItems.forEach(item => {
            const card = document.createElement('div');
            card.className = 'pl-card';

            const toolsHtml = item.tools && item.tools.length > 0
                ? `<div class="pl-tools">
                    <span class="pl-tools-label">推奨ツール:</span>
                    ${item.tools.map(t => `<a href="${t.url}" target="_blank" rel="noopener" class="pl-tool-link">${t.name}</a>`).join('')}
                   </div>`
                : '';

            card.innerHTML = `
                <div class="pl-card-header">
                    <span class="pl-card-category">${item.category}</span>
                    <h3 class="pl-card-title">${item.title}</h3>
                </div>
                <div class="pl-card-body">
                    <pre class="pl-prompt">${escapeHtml(item.prompt)}</pre>
                </div>
                <div class="pl-card-footer">
                    <button class="pl-copy-btn" data-prompt="${escapeHtml(item.prompt)}">
                        📋 コピー
                    </button>
                    ${toolsHtml}
                </div>
            `;

            card.querySelector('.pl-copy-btn').addEventListener('click', (e) => {
                const prompt = item.prompt;
                navigator.clipboard.writeText(prompt).then(() => {
                    e.target.textContent = '✓ コピー完了!';
                    setTimeout(() => {
                        e.target.textContent = '📋 コピー';
                    }, 2000);
                });
            });

            grid.appendChild(card);
        });

        loadMore.style.display = hasMore ? 'block' : 'none';
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function injectStyles() {
        if (document.getElementById('pl-styles')) return;

        const style = document.createElement('style');
        style.id = 'pl-styles';
        style.textContent = `
            #prompt-library-app {
                font-family: 'Hiragino Sans', 'Meiryo', sans-serif;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            
            .pl-header {
                text-align: center;
                margin-bottom: 30px;
            }
            
            .pl-title {
                font-size: 2rem;
                color: #1a1a2e;
                margin-bottom: 10px;
            }
            
            .pl-subtitle {
                color: #666;
                font-size: 1.1rem;
            }
            
            .pl-filters {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 10px;
                margin-bottom: 30px;
            }
            
            .pl-category-btn {
                background: #f0f0f0;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 0.95rem;
                transition: all 0.3s;
            }
            
            .pl-category-btn:hover {
                background: #e0e0e0;
            }
            
            .pl-category-btn.active {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
            
            .pl-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
                gap: 20px;
            }
            
            .pl-card {
                background: white;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                overflow: hidden;
                transition: transform 0.3s, box-shadow 0.3s;
            }
            
            .pl-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }
            
            .pl-card-header {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 15px;
            }
            
            .pl-card-category {
                font-size: 0.75rem;
                background: rgba(255,255,255,0.2);
                padding: 3px 8px;
                border-radius: 4px;
            }
            
            .pl-card-title {
                font-size: 1.1rem;
                margin: 10px 0 0;
            }
            
            .pl-card-body {
                padding: 15px;
                max-height: 200px;
                overflow-y: auto;
            }
            
            .pl-prompt {
                background: #f8f9fa;
                padding: 12px;
                border-radius: 8px;
                font-size: 0.85rem;
                white-space: pre-wrap;
                word-break: break-word;
                margin: 0;
                font-family: 'Consolas', monospace;
            }
            
            .pl-card-footer {
                padding: 15px;
                border-top: 1px solid #eee;
            }
            
            .pl-copy-btn {
                background: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 0.9rem;
                transition: background 0.3s;
            }
            
            .pl-copy-btn:hover {
                background: #45a049;
            }
            
            .pl-tools {
                margin-top: 12px;
                display: flex;
                flex-wrap: wrap;
                align-items: center;
                gap: 8px;
            }
            
            .pl-tools-label {
                font-size: 0.8rem;
                color: #666;
            }
            
            .pl-tool-link {
                font-size: 0.8rem;
                color: #667eea;
                text-decoration: none;
                background: #f0f0ff;
                padding: 4px 10px;
                border-radius: 4px;
                transition: background 0.3s;
            }
            
            .pl-tool-link:hover {
                background: #e0e0ff;
            }
            
            .pl-load-more {
                text-align: center;
                margin-top: 30px;
            }
            
            .pl-more-btn {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 15px 40px;
                border-radius: 30px;
                font-size: 1rem;
                cursor: pointer;
                transition: transform 0.3s;
            }
            
            .pl-more-btn:hover {
                transform: scale(1.05);
            }
            
            .pl-loading, .pl-error {
                text-align: center;
                padding: 40px;
                color: #666;
            }
            
            .pl-error {
                color: #e74c3c;
            }
            
            @media (max-width: 768px) {
                .pl-grid {
                    grid-template-columns: 1fr;
                }
                .pl-title {
                    font-size: 1.5rem;
                }
            }
        `;
        document.head.appendChild(style);
    }
})();
