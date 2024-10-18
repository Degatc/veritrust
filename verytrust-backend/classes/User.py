# user_models.py
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, index=True)
    created_at = Column(DateTime, nullable=True)
    followers_count = Column(Integer, nullable=True)
    following_count = Column(Integer, nullable=True)
    tweet_count = Column(Integer, nullable=True)
    listed_count = Column(Integer, nullable=True)
    protected = Column(Boolean, nullable=True)
    verified = Column(Boolean, nullable=True)
    location = Column(String, nullable=True)
    media_count = Column(Integer, nullable=True)
    score = Column(Integer, nullable=True)
    reports = relationship("ReportedUser", back_populates="user")

class ReportedUser(Base):
    __tablename__ = 'reported_users'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.user_id'), nullable=False)
    number_of_reports = Column(Integer, nullable=False)
    user = relationship("User", back_populates="reports")




# Modèle Pydantic pour les requêtes utilisateur
class UserDataRequest(BaseModel):
    username: str

class UserRequest(BaseModel):
    user_id: int
    username: str
    created_at: datetime | None
    followers_count: int | None
    following_count: int | None
    tweet_count: int | None
    listed_count: int | None
    protected: bool | None
    verified: bool | None
    location: str | None
    media_count: int | None
    score: int | None

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    user_id: int
    username: str
    created_at: datetime | None
    followers_count: int | None
    following_count: int | None
    tweet_count: int | None
    listed_count: int | None
    protected: bool | None
    verified: bool | None
    location: str | None
    media_count: int | None
    score: int | None

    class Config:
        orm_mode = True

class ReportedUserRequest(BaseModel):
    user_id: int
    number_of_reports: int

    class Config:
        orm_mode = True