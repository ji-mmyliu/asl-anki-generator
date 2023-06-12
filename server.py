from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

import genanki
import logging
import time
import os
import uuid

from aslankigen.generate import generate_deck
from aslankigen.models import WordsConfig

app = FastAPI()
app.mount("/exports", StaticFiles(directory="exports"), name="anki_package_exports")

@app.post("/generate-deck")
async def generate_asl_anki_package(deck_config: WordsConfig, request: Request):
    my_deck, video_files = generate_deck(deck_config.dict())

    my_package = genanki.Package(my_deck)
    my_package.media_files = video_files

    # Prepare export folder
    export_folder = os.path.join('exports', f"artifact-{uuid.uuid4().hex[-7:]}-{time.strftime('%Y%m%d-%H%M%S')}")
    os.makedirs(export_folder, exist_ok=True)

    # Write exported anki package file
    export_file = os.path.join(export_folder, deck_config.export_filename)
    my_package.write_to_file(export_file)

    logging.info(f"Anki deck with {len(video_files)} cards successfully exported to \"{export_file}\"!")
    return f"{request.base_url}{export_file}"
