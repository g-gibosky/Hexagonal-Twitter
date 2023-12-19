from ..domain.models import Tweet
from sqlalchemy.orm import Session


class TweetRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, tweet_data: dict) -> Tweet:
        db_tweet = Tweet(**tweet_data)
        self.db.add(db_tweet)
        self.db.commit()
        self.db.refresh(db_tweet)
        return db_tweet
    
    def get_tweet(self,tweet_id)-> Tweet:
        tweet = self.db.query(Tweet).filter(Tweet.id == tweet_id).first()
        return tweet
