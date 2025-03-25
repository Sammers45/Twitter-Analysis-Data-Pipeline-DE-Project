import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from tweepy import Client 


def run_etl_pipeline():
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAvCzwEAAAAAF0QVnZemBp5mZf4IkvEFhdoqzYE%3Dv3gIG45nFEAUpsV41gaCDStzjFIZtrJlSxN15cSlnjjrffNUZ8"


    ## Create tweepy client
    client = tweepy.Client(bearer_token = BEARER_TOKEN, wait_on_rate_limit=True)

    ## Getting India's Prime Minister "Narendra Modi's Tweets"
    username = "elonmusk"
    user_info = client.get_user(username=username)
    user_id = user_info.data.id

    # Fetch the Elon Musk's tweet
    response = client.get_users_tweets(
        id=user_id, 
        max_results=10,
        exclude="retweets",
        tweet_fields=["created_at","public_metrics"])

    '''
    if response.data:
        for tweet in response.data:
            print(tweet.text)
    else:
        print('No Tweets found.')'''

    tweet_list = []
    if response.data:
        for t in response.data:
            refined_text = {
                "text": t.text,
                "favorite_count": t.public_metrics["like_count"],  
                "retweet_count": t.public_metrics["retweet_count"],
                "created_at": t.created_at
            }
            tweet_list.append(refined_text)

    df = pd.DataFrame(tweet_list)
    df.to_csv("elonmusk.csv", index=False)