import sys
sys.dont_write_bytecode = True

from openai import OpenAI
from config import OPENAI_API_KEY

# Set up OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_article(title, content):
    """
    Summarizes a news article using OpenAI.

    Args:
        title (str): Title of the article.
        content (str): Content of the article.

    Returns:
        str: Summary of the article.
    """
    if not content:
        return "No content available to summarize."

    prompt = f"Summarize the following news article in 3-4 sentences:\n\nTitle: {title}\n\nContent: {content}\n\nSummary:"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes news articles."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.5
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        print(f"Error summarizing article: {e}")
        return "Summary unavailable."
    