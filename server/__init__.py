from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/exports", StaticFiles(directory="exports"), name="anki_package_exports")

from . import server