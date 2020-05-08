#! python3
# /Users/jeremientakpe/TwitterSpotBot/autoreply.py

import tweepy
from config import create_api, gen_proverb
import json
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id = since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        if tweet.in_reply_to_status_id is not None:
            continue

        if not tweet.user.following:
            tweet.user.follow()
            
        api.update_status(status= f" {gen_proverb()}", in_reply_to_status_id = tweet.id,\
            auto_populate_reply_metadata=True)
    return new_since_id

def main():
    api = create_api()
    since_id = 1258698161281019910
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()