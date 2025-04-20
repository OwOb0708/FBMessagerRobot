# app/db/models.py

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base

class CheckinLog(Base):
    __tablename__ = "checkin_log"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(String, index=True)
    message_text = Column(String)
    checkin_time = Column(DateTime, default=datetime.utcnow)
