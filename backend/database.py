from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from .config import settings
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# SQLALCHEMY_DATABASE_URL =  f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine("postgres://todo_ahd0_user:djsd6AnKzsd6F3xvM6pWaEbfiWqOK91r@dpg-cdk2qrien0honmehmvo0-a/todo_ahd0")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()