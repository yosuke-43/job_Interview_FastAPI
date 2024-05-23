import datetime
from pydantic import BaseModel, Field

class InterviewCreate(BaseModel):
  company_name: str = Field(max_length=50)
  interview_datetime: datetime.datetime
  location: str

class Interview(InterviewCreate):
  interview_id: int

  class Config:
    orm_mode = True