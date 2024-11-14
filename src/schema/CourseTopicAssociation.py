from src.configs.db_constants import DBTables
from src.schema.main import Base
from sqlalchemy import Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import BIGINT
from datetime import datetime

class CourseTopicAssociation(Base):
  __tablename__ = DBTables.COURSE_TOPIC_ASSOCIATION
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  
  # Foreign key
  course_id = Column(BIGINT, ForeignKey(f'{DBTables.COURSE}.id'), nullable=False)
  topic_id = Column(BIGINT, ForeignKey(f'{DBTables.TOPIC}.id'), nullable=False)
  