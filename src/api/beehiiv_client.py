import os
import json
import requests

class BeehiivClient:
    """
    Minimal Beehiiv API Client to manage newsletter posts.
    """
    def __init__(self, api_key, publication_id):
        self.api_key = api_key
        self.pub_id = publication_id
        self.base_url = "https://api.beehiiv.com/v2"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_post(self, title, subtitle, content_html, publish_date=None):
        url = f"{self.base_url}/publications/{self.pub_id}/posts"
        data = {
            "title": title,
            "subtitle": subtitle,
            "body": content_html,
            "status": "draft", # Start as draft for safety
            "send_at": publish_date
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

if __name__ == "__main__":
    # Integration Test Skeleton
    # client = BeehiivClient(os.getenv("BEEHIIV_API_KEY"), os.getenv("BEEHIIV_PUB_ID"))
    pass
