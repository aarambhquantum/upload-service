from fastapi import Request

class UploadController:
  """Upload Controller"""
  
  @classmethod
  async def upload(self, request: Request, payload: str):
    try:
      return {"message": "Logged in"}
    except Exception as e:
      return {"error": str(e)}
