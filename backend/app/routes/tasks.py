from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Task
from ..schemas import TaskOut
from ..deps import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
