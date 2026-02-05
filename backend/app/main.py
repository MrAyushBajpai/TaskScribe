from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users, tasks, extract

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://taskscribe.vercel.app",  # change if your domain differs
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(extract.router, prefix="/extract", tags=["extract"])
