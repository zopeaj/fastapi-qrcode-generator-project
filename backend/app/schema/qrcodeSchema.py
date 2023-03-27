from pydantic import BaseModel
from typing import Optional, Any

class DataToGenerate(BaseModel):
    filename: Optional[str] = None
    datatoencode: Optional[Any] = None
    scaleNumber: Optional[int] = None

    def getFileName(self):
        return self.filename

    def getDataToEncode(self):
        return self.datatoencode

    def getScaleNumber(self):
        return self.scaleNumber

class GenerateData(BaseModel):
    filename: Optional[str] = None

    def getFileName(self):
        return self.filename

