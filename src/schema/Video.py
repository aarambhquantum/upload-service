from src.configs.db_constants import DBTables
from sqlalchemy import Column, String, Enum, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import (
  BIGINT
)
from src.configs.enums import VideoTranscodingStatusEnum
from datetime import datetime
from src.schema.main import Base

class Video(Base):
  __tablename__ = DBTables.VIDEO
  
  # Indexed columns
  id = Column(BIGINT, primary_key=True, autoincrement=True, index=True)
  title = Column(String(255), nullable=False, index=True)
  
  description = Column(String(5000), nullable=True)
  video_url = Column(String(255), nullable=False)
  transcoding_status = Column(Enum(VideoTranscodingStatusEnum), default=VideoTranscodingStatusEnum.PENDING)
  created_at = Column(DateTime, default=datetime.utcnow)
  transcoded_video_url = Column(String(255), nullable=True)
  thumbnail_url = Column(String(255), nullable=False)
  duration = Column(BIGINT, nullable=False)
  
  # Foreign keys  
  user_id = Column(Integer, ForeignKey(f'{DBTables.USER}.id'), nullable=False)
  
  # Relationships - Helps with queries as we can get user data from video record and vice versa.
  user = relationship("User", back_populates="videos")
  

  