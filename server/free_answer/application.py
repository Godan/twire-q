

from free_answer.models.question import Question
from infrastructures.twitter.adapter import TwitterAdapter

from typing import List, Any
from datetime import datetime 

class FreeAnswerApplication:
    def start_aggregate(self, question: Question) -> None:
        question.start_aggregate()

    def end_aggregate(self, question: Question) -> None:
        question.end_aggregate()

    def search_tweets_from_question(self, question: Question) -> List[Any]:
        adapter = TwitterAdapter()
        query = f"{question.hashtag} since:{question.aggregate_start_time:%Y-%m-%d} "

        def filter_tweet_from_created_at(tweet):
            # TODO： 時間周りをキレイにしておく
            created_at = datetime.strptime(tweet.get("created_at"), '%a %b %d %H:%M:%S %z %Y').astimezone()
            if  created_at >= question.aggregate_end_time.astimezone() :
                return False
            elif created_at <= question.aggregate_start_time.astimezone():
                return False
            return True

        tweets = adapter.search_tweets(query)
        tweets = list(filter(filter_tweet_from_created_at, tweets))
        return tweets

    def save_tweets(self, question: Question, tweets: List[Any]) -> None:
        question.result_json = tweets
        question.save()