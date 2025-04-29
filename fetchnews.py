import sys
sys.dont_write_bytecode = True

import requests
from config import NEWS_API_KEY

def fetch_articles():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'sources': 'bbc-news',  # Or 'reuters', etc.
        'apiKey': NEWS_API_KEY,
        'pageSize': 5,  # Number of articles you want
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

            # If no full content, just use description + URL
            content = description if description else url

            fetched_articles.append({
                'title': title,
                'content': content
            })

            # Debugging print
            print(f"Fetched: {title}\nLink: {url}\n")

        return fetched_articles

    except requests.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []
