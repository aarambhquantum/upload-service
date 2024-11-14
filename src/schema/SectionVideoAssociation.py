from src.configs.db_constants import DBTables
from src.schema.main import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import (
  BIGINT
)

class SectionVideoAssociation(Base):
  __tablename__ = DBTables.SECTION_VIDEO_ASSOCIATION
  
  # Indexed columns
  id = Column(BIGINT, autoincrement=True, primary_key=True, index=True)
  
  # Foreign keys
  section_id = Column(BIGINT, ForeignKey(f"{DBTables.SECTION}.id"), nullable=False)
  video_id = Column(BIGINT, ForeignKey(f"{DBTables.VIDEO}.id"), nullable=False)