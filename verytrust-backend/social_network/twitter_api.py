import os
import tweepy
from dotenv import load_dotenv
from classes.User import User
from tools import json_twitter_data_to_user_object

load_dotenv()

bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

client = tweepy.Client(bearer_token=bearer_token)

def fetch_twitter_user_data(username) -> User | None :

    try:
        user_data = client.get_user(username=username, user_fields=['created_at', 'public_metrics', 'protected', 'verified', 'location'])
        data = user_data.data

        user = json_twitter_data_to_user_object( data )

        return user

    except tweepy.TweepyException as e:
        print(f"Error fetching data: {e}")
        return None