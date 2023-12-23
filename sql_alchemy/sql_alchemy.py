from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from env import settings

engine = create_engine(
    settings.sqlalchemy_database_url
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
