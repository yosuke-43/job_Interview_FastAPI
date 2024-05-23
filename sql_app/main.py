from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# API部分

# @app.get("/")
# async def index():
#   return {"message": "Success!!!!"}

# Read
@app.get("/interviews", response_model=List[schemas.Interview])
async def read_interviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  interviews = crud.get_interviews(db, skip=skip, limit=limit)
  return interviews

# Create
@app.post("/interviews", response_model=schemas.Interview)
async def create_interview(interview: schemas.InterviewCreate, db: Session = Depends(get_db)):
  return crud.create_interview(db=db, interview=interview)

# Delete
@app.delete("/interviews/{interview_id}")
async def delete_interview(interview_id: int, db: Session = Depends(get_db)):
    return crud.delete_interview(db=db, interview_id=interview_id)
