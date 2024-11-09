from src.schema.main import Base
from sqlalchemy import Column
from src.configs.db_constants import DBTables
from sqlalchemy.dialects.postgresql import (
  BIGINT,
  VARCHAR
)


class User(Base):
  __tablename__ = DBTables.USER
  
  id = Column(BIGINT, primary_key=True)
  email = Column(VARCHAR(100), nullable=False)