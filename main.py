import sys
sys.dont_write_bytecode = True

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
        url = article['url']
        
        summary = summarize_article(title, content)
        summarized_articles.append((title, summary, url))

    # Print the summaries
    for idx, (title, summary) in enumerate(summarized_articles, 1):
        print(f"--- Article {idx} ---")
        print(f"Title: {title}\n")
        print(f"Summary: {summary}\n")
        print("----------------------\n")

    print("Sending email...")
    send_newsletter(summarized_articles)

if __name__ == "__main__":
    main()
