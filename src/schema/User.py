from src.schema.main import Base
from sqlalchemy import Column, String
from src.configs.db_constants import DBTables
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from sqlalchemy.orm import relationship


class User(Base):
  __tablename__ = DBTables.USER
  
  id = Column(BIGINT, primary_key=True)
  email = Column(String(100), nullable=False)
  
  # Relationships
  videos = relationship("Video", back_populates="user")
  courses = relationship("Course", back_populates="owner")