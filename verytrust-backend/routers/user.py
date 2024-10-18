from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from classes.User import User, ReportedUser, UserDataRequest, UserRequest
from services import process_user_scoring
from tools import get_fake_data
from social_network.twitter_api import fetch_twitter_user_data
from social_network.instagram_api import fetch_instagram_user_data

user_router = APIRouter(
    prefix="/api",
    tags=["User Scoring"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post('/user_score')
async def obtain_user_score(request: UserDataRequest, db: Session = Depends(get_db)):
    username = request.username

    #user = get_fake_data(username)
    user = fetch_twitter_user_data(username=username)
    #user = fetch_instagram_user_data(username=username)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    score = process_user_scoring(user)
    user.score = score

    db_user = db.query(User).filter(User.user_id == user.user_id).first()
    if not db_user:
        db_user = User(
            user_id=user.user_id,
            username=user.username,
            created_at=user.created_at,
            followers_count=user.followers_count,
            following_count=user.following_count,
            tweet_count=user.tweet_count,
            listed_count=user.listed_count,
            protected=user.protected,
            verified=user.verified,
            location=user.location,
            media_count=user.media_count,
            score=user.score
        )
        db.add(db_user)
    else:
        db_user.score = user.score
    db.commit()
    db.refresh(db_user)

    if user.score < 20:
        reported_user = db.query(ReportedUser).filter(ReportedUser.user_id == user.user_id).first()
        if reported_user:
            reported_user.number_of_reports += 1
        else:
            reported_user = ReportedUser(user_id=user.user_id, number_of_reports=1)
            db.add(reported_user)
        db.commit()
        db.refresh(reported_user)

    return user


@user_router.post('/add_user')
async def add_user_to_db(user: UserRequest, db: Session = Depends(get_db)):
    db_user = User(
        user_id=user.user_id,
        username=user.username,
        created_at=user.created_at,
        followers_count=user.followers_count,
        following_count=user.following_count,
        tweet_count=user.tweet_count,
        listed_count=user.listed_count,
        protected=user.protected,
        verified=user.verified,
        location=user.location,
        media_count=user.media_count,
        score=user.score
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User added successfully", "user": db_user}