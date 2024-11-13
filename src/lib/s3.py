import aioboto3
from src.configs.env import get_settings
import logging
from src.configs.error_constants import ErrorMessages
from src.exceptions.errors.generic import FileUploadException

config = get_settings()
logger = logging.getLogger()

class AWS_S3:
  def __init__(self):
    self.session = aioboto3.Session(
      region_name=config.aws_region_name,
      aws_access_key_id=config.aws_access_key_id,
      aws_secret_access_key=config.aws_secret_access_key,
    )
    
  async def upload_to_s3(self, file, path: str, content_type: str = 'video/mp4'):
    try:      
      async with self.session.client("s3") as s3:
        await s3.upload_fileobj(
          file,
          config.aws_bucket_name,
          path,
          ExtraArgs={"ContentType": content_type},
        )
        return f"https://{config.aws_bucket_name}.s3.{config.aws_region_name}.amazonaws.com/{path}"
    except Exception as e:
      logger.exception(ErrorMessages.FILE_UPLOAD_ERROR)
      raise FileUploadException(ErrorMessages.FILE_UPLOAD_ERROR)