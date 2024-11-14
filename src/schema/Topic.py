from src.configs.db_constants import DBTables
from src.schema.main import Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from sqlalchemy.orm import relationship
from datetime import datetime

class Topic(Base):
  __tablename__ = DBTables.TOPIC
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
  title = Column(String(255), nullable=False, index=True)
  
  created_at = Column(DateTime, default=datetime.utcnow())
  
  # Relationships
  courses = relationship("Course", secondary="CourseTopicAssociation", back_populates="topics")