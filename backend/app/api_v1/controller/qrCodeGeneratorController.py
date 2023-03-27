import os
import sys

path = os.environ["FILE_PATH"]
sys.path.append(path)

from typing import Optional
from fastapi import APIRouter, Path, status
from fastapi.responses import Response


from app.services.business.abstracts.QrcodeService import QRCodeService

qrcodeRouter = APIRouter()
qrcodeService = QRCodeService()


@qrcodeRouter.post("/generateqrcode/")
def postDatatoGenerateQRCode(generate_data: DataToGenerate) -> GenerateData:
    filename = qrcodeService.generateQRCode(generate_data.getFileName(), generate_data.getDataToEncode(), generate_data.getScaleNumber())
    if filename is not None:
        return Response(content=filename, status=status.HTTP_201_CREATED, media_type="application/text")
    return Response(content={"detail": "Error in generating code"}, status=status.HTTP_400_BAD_REQUEST, media_type="application/json")

@qrcodeRouter.get("/generateqrcode/{filename}")
def getDatalookQRCode(filename: str =  Path(...)):
    content =  qrcodeService.lookUpQRCode(filename)
    if content is not None:
        return Response(content=content, status=status.HTTP_200_OK, media_type="image/png")
    return Response(content={"detail": "File not found"}, status=status.HTTP_404_NOT_FOUND, media_type="application/json")

@qrcodeRouter.get("/generateqrcode/")
def generateDataCodes(datatoencode: str, filename: Optional[str] = None, scale: Optional[int]):
    if filename is not None:
        filenamedata = qrcodeService.generateQRCode(filename, datatoencode, scale)
        content = qrcodeService.lookUpQRCode(filenamedata)
        return Response(content=content, status=200, media_type="image/png")

    filedata = qrcodeService.generateQRCode(None, datatoencode, scale)
    qrcodeService.lookUpQRCode(filedata)
    return Response(content=content, status=200, media_type="image/png")

