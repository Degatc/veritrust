import json
import os
import requests
from dotenv import load_dotenv
from classes.User import User
from tools import json_instagram_data_to_user_object

load_dotenv()

access_token = os.getenv('INSTAGRAM_BEARER_TOKEN')

instagram_base_url = 'https://graph.instagram.com/'

def get_instagram_user_id(username: str) -> str | None:
    try:
        search_url = f"{instagram_base_url}me?fields=id,username&access_token={access_token}"

        response = requests.get(search_url)
        
        if response.status_code != 200:
            print(f"Error fetching Instagram user ID: {response.status_code}")
            return None

        user_data = response.json()
        
        if user_data.get("username") == username:
            return user_data.get("id")
        
        return None

    except Exception as e:
        print(f"Error fetching Instagram user ID: {e}")
        return None


def fetch_instagram_user_data(username) -> User | None:
    try:
        user_id = get_instagram_user_id(username)
        
        if user_id is None:
            print(f"User {username} not found.")
            return None

        user_info_url = f"{instagram_base_url}{user_id}?fields=id,username,account_type,media_count,followers_count,follows_count,name,profile_picture_url,biography,website&access_token={access_token}"
        
        response = requests.get(user_info_url)
        
        if response.status_code != 200:
            print(f"Error fetching Instagram user data: {response.status_code}")
            return None
        
        user_data = response.json()

        user = json_instagram_data_to_user_object(user_data)
        
        return user
    
    except Exception as e:
        print(f"Error fetching Instagram data: {e}")
        return None