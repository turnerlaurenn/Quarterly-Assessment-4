import sys
sys.dont_write_bytecode = True

import re

from fetchnews import fetch_articles
from summarize import summarize_article
from sendemail import send_newsletter

def main():
    print("Fetching articles...")
    articles = fetch_articles()

    if not articles:
        print("No articles fetched.")
        return

    print(f"Fetched {len(articles)} articles.")
    print("\nSummarizing articles...\n")

    summarized_articles = []
    for article in articles:
        title = article['title']
        content = article['content']
        
        # Use regex to extract the URL from the content
        url_match = re.search(r'URL: (https?://\S+)', content)  # This regex finds a URL starting with http:// or https://
        url = url_match.group(1) if url_match else None  # If a URL is found, use it; otherwise, set to None
        
        summary = summarize_article(title, content)
        summarized_articles.append((title, summary, url))

    # Print the summaries
    for idx, (title, summary, url) in enumerate(summarized_articles, 1):
        print(f"--- Article {idx} ---")
        print(f"Title: {title}\n")
        print(f"Summary: {summary}\n")
        print(f"URL: {url}\n")  # Now displaying the URL
        print("----------------------\n")


    print("Sending email...")
    send_newsletter(summarized_articles)

if __name__ == "__main__":
    main()
