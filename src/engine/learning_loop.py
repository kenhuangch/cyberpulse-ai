import json
import os

class LearningLoop:
    """
    Self-learning logic: Analyzes past tweet performance and optimizes prompt strategies.
    """
    def __init__(self, stats_path):
        self.stats_path = stats_path
        if not os.path.exists(stats_path):
            self.history = []
        else:
            with open(stats_path, 'r') as f:
                self.history = json.load(f)

    def log_performance(self, tweet_id, content, likes, rts, context_type):
        """
        Record the performance of a specific tweet.
        """
        entry = {
            "tweet_id": tweet_id,
            "content": content,
            "likes": likes,
            "rts": rts,
            "type": context_type # e.g., 'news', 'reply', 'hot_take'
        }
        self.history.append(entry)
        with open(self.stats_path, 'w') as f:
            json.dump(self.history, f, indent=2)

    def get_best_strategies(self, limit=3):
        """
        Identify top performing content archetypes.
        """
        if not self.history:
            return "No data yet. Stick to baseline cyberpunk persona."
        
        # Sort by engagement (likes + rts * 2)
        sorted_history = sorted(self.history, key=lambda x: x['likes'] + x['rts'] * 2, reverse=True)
        top_examples = sorted_history[:limit]
        
        summary = "Based on past performance, these tweets went viral. Mimic their structure:\n"
        for ex in top_examples:
            summary += f"- [{ex['type']}] {ex['content']}\n"
        return summary

if __name__ == "__main__":
    # Test logic
    loop = LearningLoop("/Users/framelab/.openclaw/workspace/cyberpulse-ai/data/performance_log.json")
    # loop.log_performance("123", "AI is cool!", 50, 10, "hot_take")
    print(loop.get_best_strategies())
