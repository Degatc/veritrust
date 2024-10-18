from datetime import datetime, timezone
from math import exp
from classes.User import User

def process_user_scoring(user: User) -> int:
    score = 100

    if user.followers_count is not None and user.following_count is not None:
        if user.followers_count == 0:
            score -= 40
        else:
            ratio = user.followers_count / user.following_count
            
            if 0.5 <= ratio < 1:
                score -= 10
    
            elif ratio < 0.5:
                penalty = 50 * (1 - ratio)
                penalty = min(50, penalty)
                score -= penalty

    if user.created_at:
        account_age = (datetime.now(timezone.utc) - user.created_at).days
        
        if account_age < 30 and user.following_count > 1000:
            score -= 50
        
        elif account_age < 90:
            score -= 30
        
        if user.following_count / account_age > 50:
            score -= 20

    if user.tweet_count is not None:
        if user.tweet_count < 10:
            score -= 20
        elif user.tweet_count >= 1000 and account_age >= 365:
            score += 10

    if user.media_count is not None:
        if user.media_count < 5:
            score -= 20
        elif user.tweet_count is not None and user.media_count / user.tweet_count > 0.5:
            score -= 15

    if user.protected:
        score += 10

    if user.verified:
        score += 5

    if user.location:
        score += 10

    score = max(0, min(100, score))
    return round(score)

