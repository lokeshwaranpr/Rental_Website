from fastapi import HTTPException, APIRouter, status, Response, Depends
from sqlalchemy.orm import Session
from .. import database

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(db: Session = Depends(database.get_db)):
    