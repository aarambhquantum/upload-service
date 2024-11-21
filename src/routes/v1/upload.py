from fastapi import APIRouter, Request, UploadFile, Form
from services.upload.controller import UploadController

router = APIRouter()

@router.post("")
async def test(request: Request, video: UploadFile, thumbnail_img: UploadFile, title: str = Form(...), description: str = Form(...)):
  return await UploadController.upload(request, video, thumbnail_img, title, description)