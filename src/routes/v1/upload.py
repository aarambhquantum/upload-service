from fastapi import APIRouter, Request, Response, Depends, UploadFile
from services.upload.controller import UploadController

router = APIRouter()

@router.post("/")
async def test(request: Request, payload: UploadFile):
  return await UploadController.upload(request, payload)