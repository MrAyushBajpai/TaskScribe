from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import User
from ..schemas import UserCreate, UserLogin
from ..deps import get_db
from ..auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username taken")

    new_user = User(
        username=user.username,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if not existing or not verify_password(user.password, existing.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": existing.id})
    return {"access_token": token}
