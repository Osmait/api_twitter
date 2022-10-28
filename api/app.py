from fastapi import FastAPI
from routes.tweet import tweet

app = FastAPI()

app.include_router(tweet)
