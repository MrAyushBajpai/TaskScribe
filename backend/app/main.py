from fastapi import FastAPI
from .database import engine, Base
from .routes import extract, tasks, users

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app FIRST
app = FastAPI(title="TaskScribe API")

# Then include routers
app.include_router(users.router)
app.include_router(extract.router)
app.include_router(tasks.router)
