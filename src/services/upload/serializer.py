from pydantic import BaseModel
from typing import Optional
from src.configs.enums import VideoTranscodingStatusEnum

class InitiateUploadInbound(BaseModel):
  filename: str
  
class InitiateUploadOutbound(BaseModel):
  upload_id: str