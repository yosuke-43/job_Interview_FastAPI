from sqlalchemy.orm import Session
from . import models, schemas

# 面接一覧取得
def get_interviews(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Interview).offset(skip).limit(limit).all()

# 面接登録
def create_interview(db: Session, interview: schemas.Interview):
  db_interview = models.Interview(
    company_name=interview.company_name,
    interview_datetime=interview.interview_datetime,
    location=interview.location
  )
  db.add(db_interview)
  db.commit()
  db.refresh(db_interview)
  return db_interview

# 面接削除
def delete_interview(db: Session, interview_id: int):
    interview = db.query(models.Interview).filter(models.Interview.interview_id == interview_id).first()
    db.delete(interview)
    db.commit()
