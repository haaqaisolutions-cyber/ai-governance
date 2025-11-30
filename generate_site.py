import json
from datetime import datetime

def generate_html():
    # Read the aggregated articles
    try:
        with open('articles.json', 'r', encoding='utf-8') as f:
            articles = json.load(f)
    except FileNotFoundError:
        print("❌ articles.json not found. Run aggregator.py first.")
        return

    # Build HTML content
    html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Governance Watch</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; color: #333; background: #f5f7fa;
            max-width: 1200px; margin: 0 auto; padding: 20px;
        }}
        header {{ 
            background: linear(135deg, #667eea 0%, #764ba2 100%);
            color: white; padding: 3rem 2rem; border-radius: 12px;
            margin-bottom: 2rem; text-align: center;
        }}
        h1 {{ font-size: 2.5rem; margin-bottom: 0.5rem; }}
        .tagline {{ font-size: 1.2rem; opacity: 0.9; }}
        .stats {{ 
            background: white; padding: 1rem; border-radius: 8px;
            margin: 1rem 0; box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            display: inline-block;
        }}
        .articles-grid {{
            display: grid; gap: 1.5rem;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        }}
        .article-card {{
            background: white; padding: 1.5rem; border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: transform 0.2s;
            border-left: 4px solid #667eea;
        }}
        .article-card:hover {{ transform: translateY(-3px); }}
        .article-title {{ 
            font-size: 1.1rem; margin-bottom: 0.5rem; 
            color: #2c3e50; text-decoration: none; display: block;
        }}
        .article-description {{ 
            color: #666; font-size: 0.9rem; margin-bottom: 1rem;
            line-height: 1.5;
        }}
        .article-meta {{
            display: flex; justify-content: between; align-items: center;
            font-size: 0.8rem; color: #888;
        }}
        .source {{ font-weight: 600; color: #667eea; }}
        .date {{ color: #999; }}
        footer {{
            text-align: center; margin-top: 3rem; padding: 2rem;
            color: #666; border-top: 1px solid #eee;
        }}
        .last-updated {{ font-size: 0.9rem; margin-top: 1rem; }}
        @media (max-width: 768px) {{
            .articles-grid {{ grid-template-columns: 1fr; }}
            header {{ padding: 2rem 1rem; }}
            h1 {{ font-size: 2rem; }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>🤖 AI Governance Watch</h1>
        <p class="tagline">Curated intelligence on AI policy, regulation, and digital governance</p>
        <div class="stats">
            📊 {len(articles)} articles curated • 🔄 Auto-updated
        </div>
    </header>

    <main>
        <div class="articles-grid">
'''

    # Add each article as a card
    for article in articles:
        html_content += f'''
            <article class="article-card">
                <a href="{article['link']}" class="article-title" target="_blank">
                    {article['title']}
                </a>
                <p class="article-description">
                    {article['description']}
                </p>
                <div class="article-meta">
                    <span class="source">📰 {article['source'][:30]}</span>
                    <span class="date">📅 {article['published'][:16]}</span>
                </div>
            </article>
        '''

    # Close HTML
    html_content += f'''
        </div>
    </main>

    <footer>
        <p>Curated with 🤍 for the tech policy community</p>
        <p class="last-updated">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
        </p>
    </footer>
</body>
</html>
'''

    # Write to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated index.html with {len(articles)} articles")
    print("🌐 Open index.html in your browser to preview")

if __name__ == "__main__":
    generate_html()