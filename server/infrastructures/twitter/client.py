import os
from typing import List, Optional

import httpx
from authlib.integrations.httpx_client import OAuth1Auth
from django.urls import reverse


class TwitterClient:
    def __init__(self) -> None:
        self.CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
        self.CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
        self.ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
        self.ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
        self.auth = OAuth1Auth(
            self.CONSUMER_KEY,
            self.CONSUMER_SECRET,
            self.ACCESS_TOKEN,
            self.ACCESS_TOKEN_SECRET,
        )
        self.headers = {"Authorization": f"Bearer {self.BEARER_TOKEN}"}
        self.timeout = 300

    
    async def search_tweets(
        self,
        q: str, 
        max_id: str,
        access_token: Optional[str] = None,
        access_token_secret: Optional[str] = None,
    ) -> httpx.Response:
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params = {"q": q, "max_id": max_id, "count": str(100), "tweet_mode": "extended"}
        if access_token and access_token_secret:
            auth = OAuth1Auth(
                self.CONSUMER_KEY,
                self.CONSUMER_SECRET,
                access_token,
                access_token_secret,
            )
            async with httpx.AsyncClient(auth=auth, timeout=self.timeout) as client:
                response = await client.get(url, params=params)
        else:
            async with httpx.AsyncClient(
                headers=self.headers, timeout=self.timeout
            ) as client:
                response = await client.get(url, params=params)
        response.raise_for_status()
        return response
