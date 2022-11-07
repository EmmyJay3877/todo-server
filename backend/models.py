from .database import Base
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, 
    server_default=text('now()'))