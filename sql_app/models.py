from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class Interview(Base):
  __tablename__ = 'interviews'
  interview_id = Column(Integer, primary_key=True, index=True)
  company_name = Column(String, index=True)
  interview_datetime = Column(DateTime, nullable=False)
  location = Column(String, index=True)