#! python3
# /Users/jeremientakpe/TwitterSpotBot/favRetweet.py

import tweepy
from config import create_api
import json

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except:
                print("Error on fav")
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except:
                print("Error on fav and retweet")

    def on_error(self, status):
        print(status)

def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=["fr"])

if __name__ == "__main__":
    main(["#CIV225", "#BlackHistoryMonth", "#ivorianTouch"])