import uvicorn
from fastapi import FastAPI
from classes.User import Base
from database import engine
from routers.report import report_router
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="VeryTrust API",
    description="Workshop I2/E2"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(report_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)