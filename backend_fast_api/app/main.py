from typing import Union
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .infrastructure.database import get_db
from .application.userService import UserService
from .application.tweetService import TweetService
from .infrastructure.userRepository import UserRepository
from .infrastructure.tweetRepository import TweetRepository

app = FastAPI()

@app.post("/users/add")
def create_user(user_data: dict, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.create_user(user_data)

@app.put("/users/{user_id}")
def update_user(user_id:int, user_data: dict, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.update_user(user_data, user_id)

@app.get("/users/{user_id}")
def get_user(user_id: int, q: Union[str, None] = None, db: Session = Depends(get_db)):
    print(user_id)
    return {"item_id": user_id, "q": q} 

@app.post("/tweets/add")
def post_tweet(tweet_data: dict, db: Session = Depends(get_db)):
    tweet_service = TweetService(TweetRepository(db))
    return tweet_service.post_tweet(tweet_data)

@app.get("/tweets/{tweet_id}")
def get_tweet(tweet_id: int, q: Union[str, None] = None, db: Session = Depends(get_db)):
    tweet_service = TweetService(TweetRepository(db))
    tweet_info = tweet_service.get_tweet(tweet_id, q)
    return {"payload": tweet_info, "item_id": tweet_id, "q": q} 
