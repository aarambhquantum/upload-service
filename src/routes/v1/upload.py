from fastapi import APIRouter, Request, UploadFile, Form
from services.upload.controller import UploadController
from services.upload.serializer import InitiateUploadInbound
from utils.response import success_response

router = APIRouter()

@router.post("/initiate")
async def test(request: Request, payload: InitiateUploadInbound):
  response = await UploadController.initiateUpload(request, payload)
  return success_response(response)