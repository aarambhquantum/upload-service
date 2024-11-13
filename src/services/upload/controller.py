from fastapi import Request, UploadFile
from src.lib.s3 import AWS_S3
from src.exceptions.errors.generic import FileUploadException
from src.configs.error_constants import ErrorMessages

class UploadController:
  """Upload Controller"""
  
  @classmethod
  async def upload(self, request: Request, payload: UploadFile):
    print("TYPE", payload.content_type)     
    if not payload.content_type.startswith('video/'):
      raise FileUploadException(ErrorMessages.FILE_FORMAT_ERROR)
    s3 = AWS_S3()
    return await s3.upload_to_s3(payload.file, 'videos/sample')
