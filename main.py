import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

class Interview(BaseModel):
  interview_id: int
  company_name: str = Field(max_length=50)
  interview_datetime: datetime.datetime
  location: str

app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Success!!!!"}

@app.post("/interviews")
async def interviews(interviews: Interview):
  return {"interviews": interviews}