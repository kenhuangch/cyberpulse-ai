import requests

class NewsAggregator:
    """
    Aggregates news from various sources.
    """
    def fetch_hacker_news(self, limit=5):
        """
        Fetches top AI stories from Hacker News.
        """
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        story_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"
        
        try:
            ids = requests.get(top_stories_url).json()[:50] # Check first 50
            ai_stories = []
            for story_id in ids:
                story = requests.get(story_url.format(story_id)).json()
                title = story.get('title', '').lower()
                if 'ai' in title or 'llm' in title or 'openai' in title or 'gpt' in title:
                    ai_stories.append({
                        "title": story.get('title'),
                        "url": story.get('url'),
                        "source": "Hacker News"
                    })
                if len(ai_stories) >= limit:
                    break
            return ai_stories
        except Exception as e:
            print(f"Error fetching HN: {e}")
            return []

    def fetch_all(self):
        return self.fetch_hacker_news()

if __name__ == "__main__":
    agg = NewsAggregator()
    print(agg.fetch_all())
