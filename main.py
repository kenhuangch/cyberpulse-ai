import os
from src.engine.aggregator import NewsAggregator
from src.api.x_client import XClient
from dotenv import load_dotenv

load_dotenv()

def main():
    print("CyberPulse AI ⚡️ Starting daily operation...")
    
    # 1. Fetch News
    aggregator = NewsAggregator()
    stories = aggregator.fetch_all()
    
    if not stories:
        print("No AI news found today. System idling.")
        return

    # 2. Format Tweet (Simplified for now)
    x = XClient()
    header = "⚡️ [CyberPulse AI] Top AI Signals for Today:\n\n"
    body = ""
    for i, s in enumerate(stories[:3]): # Top 3
        body += f"{i+1}. {s['title']}\n"
    
    footer = "\nStay tuned. Full newsletter coming soon. #CyberPulse #AI"
    
    full_tweet = header + body + footer
    
    # 3. Post to X
    print(f"Posting to X:\n{full_tweet}")
    x.post_tweet(full_tweet)

if __name__ == "__main__":
    main()
