from fastapi import APIRouter, Request, Response, Depends
from services.upload.controller import UploadController

router = APIRouter()

@router.post("/")
async def test(request: Request, payload: str):
  return await UploadController.upload(request, payload=payload)