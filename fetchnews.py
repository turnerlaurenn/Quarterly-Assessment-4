import sys
sys.dont_write_bytecode = True

import requests
from config import NEWS_API_KEY

def fetch_articles():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'sources': 'bbc-news',  # or 'reuters', 'the-wall-street-journal'
        'apiKey': NEWS_API_KEY,
        'pageSize': 5,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        articles = data.get('articles', [])

        fetched_articles = []
        for article in articles:
            title = article['title']
            url = article['url']
            description = article.get('description', '')

            # 🛠 Tiny Upgrade: combine everything into one text block
            combined_content = f"Title: {title}\nDescription: {description}\nURL: {url}"

            fetched_articles.append({
                'title': title,
                'content': combined_content
            })

            # Debugging print
            print(f"Fetched: {title}\nLink: {url}\n")

        return fetched_articles

    except requests.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []
