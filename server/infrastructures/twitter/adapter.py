import asyncio
from typing import List
from infrastructures.twitter.client import TwitterClient


class TwitterAdapter:
    def __init__(self) -> None:
        self.twitter_client = TwitterClient()

    def _get_next_max_id(self, tweets) -> str:
        return str(int(tweets["statuses"][-1]["id_str"]) - 1)

        
    def search_tweets(self, q: str):
        tweets = asyncio.run(self.twitter_client.search_tweets(q, "-1")).json()
        returnlist = tweets.get("statuses")

        for i in range(3):
            if len(tweets["statuses"]) > 0:
                    max_id = self._get_next_max_id(tweets)
                    tweets = asyncio.run(self.twitter_client.search_tweets(q, max_id)).json()
                    returnlist.extend(tweets.get("statuses", []))
            else:
                break
        return returnlist