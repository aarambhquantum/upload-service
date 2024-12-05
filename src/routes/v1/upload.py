from fastapi import APIRouter, Request, UploadFile, Form
from services.upload.controller import UploadController
from services.upload.serializer import InitiateUploadInbound, GetPresignedUrlInbound, CompleteMultiPartUploadInbound
from utils.response import success_response

router = APIRouter()

@router.post("/initiate")
async def initiate_upload(request: Request, payload: InitiateUploadInbound):
  response = await UploadController.initiate_upload(request, payload)
  return success_response(response)

@router.post("/generate-presigned-urls")
async def get_presigned_urls(request: Request, payload: GetPresignedUrlInbound):
  response = await UploadController.generate_presigned_urls(request, payload)
  return success_response(response)

@router.post("/complete")
async def complete_upload(request: Request, payload: CompleteMultiPartUploadInbound):
  response = await UploadController.complete_multipart_upload(request, payload)
  return success_response(response)