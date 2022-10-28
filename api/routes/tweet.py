
from select import select
from fastapi import APIRouter
from config.db import conn
from models.tweet import tweet as tw

tweet = APIRouter()

@tweet.get('/')
def tweets(limit:int = 10):
    """_summary_

    Args:
        limit (int, optional): _description_. Defaults to 10.

    Returns:
        list: list tweet
    """
    
    return conn.execute(tw.select()).fetchmany(limit)

@tweet.get("/{id:int}")
def one_tweets(id):
    """_summary_

    Args:
        id (int): parameter to search for a tweet

    Returns:
        object: tweet
    """
    return conn.execute(tw.select().where(tw.c.id ==id)).first()

@tweet.get("/{user:str}")
def search_user_tweet(user:str):
    """_summary_

    Args:
        user (str): _description_

    Returns:
        _type_: _description_
    """
    return conn.execute(tw.select().where(tw.c.user == user)).all()

    
        

