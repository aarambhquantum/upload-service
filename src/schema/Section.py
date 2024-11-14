from src.configs.db_constants import DBTables
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from datetime import datetime
from src.schema.main import Base

class Section(Base):
  __tablename__ = DBTables.SECTION
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  
  title = Column(String(255), nullable=False)
  order = Column(Integer, default=0)
  created_at = Column(DateTime, default=datetime.utcnow)
  
  # Foreign key
  course_id = Column(BIGINT, ForeignKey(f'{DBTables.COURSE}.id'), nullable=False)
  
  # Relationships
  course = relationship("Course", back_populates="sections")
  videos = relationship("Video", secondary="SectionVideoAssociation", back_populates="sections")