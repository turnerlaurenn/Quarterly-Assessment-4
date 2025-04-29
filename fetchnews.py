import sys
sys.dont_write_bytecode = True

import requests
from config import NEWS_API_KEY

# Comma-separated list of trusted source IDs
TRUSTED_SOURCES = "bbc-news,reuters,the-guardian-uk"

def get_latest_articles(page_size=5):
    """
    Fetches the latest articles from trusted sources and prints their headlines and URLs.
    """
    url = f"https://newsapi.org/v2/top-headlines?sources={TRUSTED_SOURCES}&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        
        for idx, article in enumerate(articles, 1):
            title = article.get("title")
            url = article.get("url")
            print(f"{idx}. {title}")
            print(f"   {url}\n")
    else:
        print(f"Error fetching articles: {response.status_code}")

if __name__ == "__main__":
    get_latest_articles()