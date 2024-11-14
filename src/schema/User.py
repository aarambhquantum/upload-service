from src.schema.main import Base
from sqlalchemy import Column, String
from src.configs.db_constants import DBTables
from sqlalchemy.dialects.postgresql import (
  BIGINT
)


class User(Base):
  __tablename__ = DBTables.USER
  
  id = Column(BIGINT, primary_key=True)
  email = Column(String(100), nullable=False)