from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from classes.User import ReportedUser, ReportedUserRequest

report_router = APIRouter(
    prefix="/api",
    tags=["Report User"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@report_router.post('/report_user')
async def report_user(request: ReportedUserRequest, db: Session = Depends(get_db)):
    reported_user = ReportedUser(
        user_id=request.user_id,
        number_of_reports=request.number_of_reports
    )
    db.add(reported_user)
    db.commit()
    db.refresh(reported_user)

    return {"message": "User reported successfully", "reported_user": reported_user}