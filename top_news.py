#!/usr/bin/env python3
import requests

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "e415d475d8d94457b73fd8df5872f33c"


def fetch_top_news():
    try:
        response = requests.get(
            NEWS_API_URL,
            params={
                "apiKey": API_KEY,
                "sources": "bbc-news",
                "pageSize": 3,
            },
        )
        response.raise_for_status()
        news_data = response.json()
        #        print(news_data)

        if news_data["status"] == "ok":
            articles = news_data["articles"][:3]
            print("\n\033[1mTop 3 News Articles:\033[0m\n")
            for i, article in enumerate(articles, 1):
                print(f"{i}. {article['title']}")
                print(f"   {article['description']}")
                print(f"   {article['url']}\n")
        else:
            print("Failed to fetch news. Please try again later.")
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")


if __name__ == "__main__":
    fetch_top_news()
