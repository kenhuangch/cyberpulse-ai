import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class XClient:
    """
    X (Twitter) API Client optimized for Free Tier.
    Free Tier 2026:
    - Post 500 tweets/month (approx 16/day).
    - Media uploads allowed.
    - NO profile updates via API.
    - NO follow/unfollow via API.
    - NO search/read via API.
    """
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv("X_BEARER_TOKEN"),
            consumer_key=os.getenv("X_CONSUMER_KEY"),
            consumer_secret=os.getenv("X_CONSUMER_SECRET"),
            access_token=os.getenv("X_ACCESS_TOKEN"),
            access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET")
        )

    def post_tweet(self, text):
        try:
            response = self.client.create_tweet(text=text)
            print(f"Successfully posted tweet: {response.data['id']}")
            return response
        except Exception as e:
            print(f"Error posting tweet: {e}")
            return None

    def post_thread(self, tweets):
        previous_tweet_id = None
        for i, text in enumerate(tweets):
            try:
                if i == 0:
                    response = self.client.create_tweet(text=text)
                else:
                    response = self.client.create_tweet(
                        text=text,
                        in_reply_to_tweet_id=previous_tweet_id
                    )
                previous_tweet_id = response.data['id']
                print(f"Posted thread element {i+1}: {previous_tweet_id}")
            except Exception as e:
                print(f"Error posting thread element {i+1}: {e}")
                break
