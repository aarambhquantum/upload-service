from src.configs.db_constants import DBTables
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class Course(Base):
  __tablename__ = DBTables.COURSE
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  title = Column(BIGINT, index=True, nullable=False)
  created_at = Column(DateTime, default=datetime.utcnow)
  
  # Foreign key
  owner_id = Column(BIGINT, ForeignKey(f'{DBTables.USER}.id'), nullable=False)
  
  # Relationship
  owner = relationship("User", back_populates="courses")
  topics = relationship("Topic", secondary="CourseTopicAssociation", back_populates="courses")
  sections = relationship("Section", back_populates="courses")