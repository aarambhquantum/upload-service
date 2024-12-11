from pydantic import BaseModel
from typing import List
from src.configs.enums import VideoTranscodingStatusEnum

class InitiateUploadInbound(BaseModel):
  filename: str
  
class InitiateUploadOutbound(BaseModel):
  upload_id: str
  
class GetPresignedUrlInbound(BaseModel):
  files: List[str]
  video_name: str
  
class ETag(BaseModel):
  ETag: str
  PartNumber: int

class CompleteMultiPartUploadInbound(BaseModel):
  filename: str
  upload_id: str
  etags: List[ETag]
  