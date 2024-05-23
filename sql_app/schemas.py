import datetime
from pydantic import BaseModel, Field
from typing import Optional

class InterviewCreate(BaseModel):
  company_name: str = Field(max_length=50)
  interview_datetime: datetime.datetime
  location: str

class InterviewUpdate(BaseModel):
    company_name: Optional[str] = None
    interview_datetime: Optional[datetime.datetime] = None
    location: Optional[str] = None

class Interview(InterviewCreate):
  interview_id: int

  class Config:
    orm_mode = True