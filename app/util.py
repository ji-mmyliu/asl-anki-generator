import requests
import logging
import os
import time
from . import DOWNLOAD_INTERVAL

def get_handspeak_url(word: str) -> str:
    assert len(word) >= 3, "The length of the word must be at least 3 characters"
    return f"https://www.handspeak.com/word/{word[:1]}/{word[:3]}/{word}.mp4"

"""
Downloads video from HandSpeak as the answer for the sign

Returns a string stating the relative path of the downloaded video
"""
def download_sign_video(word: str, force_redownload=False) -> str:
    filename = f'videos/{word}.mp4'

    if not force_redownload and os.path.isfile(filename):
        logging.warning(f"Sign video \"{filename}\" has been previously downloaded; skipping.")
        return filename # Video is already downloaded

    logging.info(f"Downloading {filename}...")
    time.sleep(DOWNLOAD_INTERVAL)

    r = requests.get(get_handspeak_url(word), allow_redirects=True)

    if not r.ok:
        logging.warning(f"Error downloading sign video for \"{word}\". Please double-check the spelling of the word.")
        return None # Download unsuccessful
    
    logging.info(f"Successfully downloaded \"{filename}\"!")

    os.makedirs('videos/', exist_ok=True)
    open(filename, 'wb').write(r.content)
    return filename