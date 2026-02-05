from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..nlp.extractor import extract_tasks
from ..schemas import TextInput
from ..models import Task
from ..deps import get_db

router = APIRouter(prefix="/extract", tags=["Extract"])

@router.post("/")
def extract(payload: TextInput, db: Session = Depends(get_db)):
    extracted = extract_tasks(payload.text)

    for item in extracted:
        task = Task(
            description=item["description"],
            owner=item["owner"],
            deadline=item["deadline"],
            priority=item["priority"]
        )
        db.add(task)

    db.commit()
    return {"message": "Tasks saved", "count": len(extracted)}
