from app import db
from app.models import Questions, Responces

from sqlalchemy import create_engine
from sqlalchemy import text
# or from sqlalchemy.sql import text

engine = create_engine('sqlite:///app.db', echo=True)

Responces.__table__.drop(engine)