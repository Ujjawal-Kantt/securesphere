import streamlit as st
import requests

# NewsAPI credentials
API_KEY = "7c7c798ba157455299775fe83f2d8725"
NEWS_URL = "https://newsapi.org/v2/everything"

def fetch_cybersecurity_news():
    """Fetch latest cybersecurity-related news from NewsAPI."""
    params = {
        "q": "cybersecurity",  # Only fetch cyber-related news
        "apiKey": API_KEY,
        "language": "en",
        "sortBy": "publishedAt",
    }

    response = requests.get(NEWS_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

def show():
    st.title("🌐 Cybersecurity News")

    st.markdown("Fetching latest cybersecurity news...")

    if st.button("Fetch News"):
        news_articles = fetch_cybersecurity_news()
        
        if news_articles:
            st.info("📰 Latest Cyber News:")
            for article in news_articles[:10]:  # Show top 10 articles
                st.subheader(article["title"])
                st.write(article["description"])
                st.write(f"🔗 [Read More]({article['url']})")
                if article.get("urlToImage"):
                    st.image(article["urlToImage"], width=500)
                st.markdown("---")
        else:
            st.warning("⚠️ No cybersecurity news found!")
