from classes.User import User
from datetime import datetime

def json_twitter_data_to_user_object( data ) -> User :

    if isinstance(data['created_at'], str) and data['created_at']:
        created_at = datetime.strptime(data['created_at'], "%Y-%m-%d %H:%M:%S%z")
    else:
        created_at = data['created_at']

    return User (
        username=data['username'],
        user_id=data['id'],
        created_at=created_at,
        followers_count=data['public_metrics']['followers_count'],
        following_count=data['public_metrics']['following_count'],
        tweet_count=data['public_metrics']['tweet_count'],
        listed_count=data['public_metrics']['listed_count'],
        protected=data['protected'],
        verified=data['verified'],
        location=data['location'],
        media_count=None,
        score=None,
    )

def json_instagram_data_to_user_object( data ) -> User :

    return User (
        username=data['username'],
        user_id=data['id'],
        created_at=None,
        followers_count=None,
        following_count=None,
        tweet_count=None,
        listed_count=None,
        protected=None,
        verified=None,
        location=None,
        media_count=data['media_count'],
        score=None
    )

def get_fake_data(username: str) -> User:
    users_data = [
        {
            "username": "Henry",
            "id": "8284967890",
            "created_at": "2024-10-15 19:23:17+00:00",
            "public_metrics": {
                "followers_count": 0,
                "following_count": 5000,
                "tweet_count": 1,
                "listed_count": 0
            },
            "protected": False,
            "verified": False,
            "location": None,
            "media_count": None,
            "score": None
        },
        {
            "username": "Alice",
            "id": "1234567890",
            "created_at": "2024-10-14 12:00:00+00:00",
            "public_metrics": {
                "followers_count": 100,
                "following_count": 200,
                "tweet_count": 50,
                "listed_count": 5
            },
            "protected": False,
            "verified": True,
            "location": "Paris",
            "media_count": 10,
            "score": 75
        },
        {
            "username": "Thomas",
            "id": "2345678901",
            "created_at": "2024-10-13 15:30:00+00:00",
            "public_metrics": {
                "followers_count": 250,
                "following_count": 150,
                "tweet_count": 100,
                "listed_count": 2
            },
            "protected": True,
            "verified": False,
            "location": "Londres",
            "media_count": 5,
            "score": 80
        },
        {
            "username": "Paul",
            "id": "3456789012",
            "created_at": "2024-10-12 08:45:00+00:00",
            "public_metrics": {
                "followers_count": 500,
                "following_count": 300,
                "tweet_count": 200,
                "listed_count": 10
            },
            "protected": False,
            "verified": True,
            "location": "New York",
            "media_count": 20,
            "score": 90
        },
        {
            "username": "Bard",
            "id": "4567890123",
            "created_at": "2024-10-11 10:00:00+00:00",
            "public_metrics": {
                "followers_count": 750,
                "following_count": 400,
                "tweet_count": 300,
                "listed_count": 15
            },
            "protected": False,
            "verified": True,
            "location": "Berlin",
            "media_count": 25,
            "score": 95
        }
    ]
    
    for user_data in users_data:
        if user_data["username"] == username:
            return json_twitter_data_to_user_object(user_data)

    raise ValueError(f"User with username '{username}' not found")