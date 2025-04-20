# init_db.py
from app.db.database import Base, engine
from app.db.models import CheckinLog

Base.metadata.create_all(bind=engine)
