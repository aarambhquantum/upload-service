from fastapi import Request, UploadFile
from src.lib.s3 import AWS_S3
from src.exceptions.errors.generic import FileUploadException
from src.configs.error_constants import ErrorMessages
from db.session import get_db, save_new_row, update_old_row
from src.schema.main import Video
from src.configs.enums import VideoTranscodingStatusEnum


db = get_db()

class UploadController:
  """Upload Controller"""
  
  @classmethod
  async def upload(self, request: Request, video: UploadFile, thumbnail_img: UploadFile, title: str, description: str):
    if not video.content_type.startswith('video/'):
      raise FileUploadException(ErrorMessages.FILE_FORMAT_ERROR)
    
    if not thumbnail_img.content_type.startswith('image/'):
      raise FileUploadException(ErrorMessages.FILE_FORMAT_ERROR)
    
    new_video = Video(
      title=title,
      description=description,
      transcoding_status=VideoTranscodingStatusEnum.PENDING,
      user_id=1,
      duration=10
    )
    response = save_new_row(new_video)
    
    s3 = AWS_S3()
    aws_video_url = await s3.upload_to_s3(video, path=f"videos/{response.id}")
    aws_thumbnail_url = await s3.upload_to_s3(thumbnail_img, path=f"images/{response.id}")
    
    new_video.thumbnail_url = aws_thumbnail_url
    new_video.video_url = aws_video_url
    
    response = update_old_row(new_video)
    
    return {"success": True, "data": response}
    
    
