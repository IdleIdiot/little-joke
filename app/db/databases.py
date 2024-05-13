from ..config import settings

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = settings.database_url


engine: Engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # encoding="utf-8",
    echo=True,
)
session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)

Base = declarative_base()
