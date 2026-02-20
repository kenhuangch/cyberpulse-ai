import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class XClient:
    """
    Client for interacting with the X (Twitter) API v2.
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
        """
        Posts a series of tweets as a thread.
        """
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

if __name__ == "__main__":
    # Test
    # x = XClient()
    # x.post_tweet("CyberPulse AI ⚡️ Initializing... Stay tuned for the future of AI news. #CyberPulse #AI")
    pass
