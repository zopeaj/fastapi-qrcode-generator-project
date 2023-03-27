import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import APIRouter
from app.api_v1.controller.qrCodeGeneratorController import qrcodeRouter


api_router = APIRouter()
api_router.include_router(qrcodeRouter, prefix="/qrcode", tags=["qrcode"])

