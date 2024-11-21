from pydantic import BaseModel
from typing import Optional
from src.configs.enums import VideoTranscodingStatusEnum

class AddVideoInBound(BaseModel):
  id: Optional[int] = None
  title: str
  description: str
  video_url: str
  transcoding_status: VideoTranscodingStatusEnum
  thumbnail_url: Optional[str] = ""
  duration: Optional[int] = 0
  user_id: int