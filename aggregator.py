import feedparser
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time

# Your curated RSS feeds - USING ACTUAL FEED URLs
FEEDS = [
    'https://www.brookings.edu/articles/feed/',  # Brookings feed
    'https://cis-india.org/feed',  # CIS India feed
    'https://www.eff.org/rss/updates.xml',  # EFF feed
    'https://digital-strategy.ec.europa.eu/en/library/feed',  # EU feed
    'https://www.technologyreview.com/feed/'  # MIT Tech Review feed
]

# Your targeted keywords
KEYWORDS = [
    'AI governance', 'algorithmic', 'regulation', 'policy',
    'data privacy', 'GDPR', 'surveillance', 'encryption',
    'platform', 'DSA', 'DMA', 'AI Act', 'digital rights'
]

def fetch_and_filter():
    articles = []
    
    for feed_url in FEEDS:
        try:
            print(f"🔍 Checking {feed_url}")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:8]:  # Check latest 8 entries
                title = entry.title.lower()
                summary = entry.get('summary', '').lower()
                content = title + " " + summary
                
                # Check if any keyword matches
                if any(keyword.lower() in content for keyword in KEYWORDS):
                    # Get a clean description
                    description = entry.get('summary', 'No description available')
                    if description:
                        soup = BeautifulSoup(description, 'html.parser')
                        description = soup.get_text()[:150] + "..."
                    
                    articles.append({
                        'title': entry.title,
                        'link': entry.link,
                        'source': feed.feed.get('title', feed_url),
                        'published': entry.get('published', entry.get('updated', 'No date')),
                        'description': description
                    })
                    
                    print(f"   ✅ Found: {entry.title[:50]}...")
            
            time.sleep(1)  # Be nice to the servers
            
        except Exception as e:
            print(f"   ❌ Error with {feed_url}: {e}")
            continue
    
    # Sort by date (newest first) and keep top 12
    articles.sort(key=lambda x: x['published'], reverse=True)
    return articles[:12]

if __name__ == "__main__":
    print("🚀 Starting AI Governance Watch aggregation...")
    latest_articles = fetch_and_filter()
    
    # Save to JSON file
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(latest_articles, f, indent=2, ensure_ascii=False)
    
    print(f"🎉 Success! Found {len(latest_articles)} relevant articles.")
    print("📁 Saved to articles.json")