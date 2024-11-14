from fastapi import Request, status
# from src.main import app
from src.exceptions.errors.generic import FileUploadException
from starlette.responses import JSONResponse

def register_handlers(app):
  @app.exception_handler(FileUploadException)
  async def file_upload_exception_handler(request: Request, exception: FileUploadException):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={
      "status": "failure",
      "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
      "message": exception.message
    })
    