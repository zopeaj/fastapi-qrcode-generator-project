import os
import sys
from dotenv import load_dotenv



path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from api.api_v1.routes import api_router


app = FastAPI()

app.add_router(api_router, prefix="/main")
