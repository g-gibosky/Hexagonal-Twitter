from typing import Union
from ..domain.tweet import Tweet
from ..infrastructure.tweetRepository import TweetRepository


class TweetService:
    def __init__(self, tweet_repository: TweetRepository):
        self.tweet_repository = tweet_repository

    def post_tweet(self, tweet_data: dict) -> Tweet:
        return self.tweet_repository.save(tweet_data)
    
    def get_tweet(self,tweet_id:int, q: Union[str, None] = None) -> Tweet:
        return self.tweet_repository.get_tweet(tweet_id)

    # Additional methods for tweet management
