import requests
import typing

def get_handspeak_url(word: str) -> str:
    assert len(word) >= 3, "The length of the word must be at least 3 characters"
    return f"https://www.handspeak.com/word/{word[:1]}/{word[:3]}/{word}.mp4"

"""
Downloads video from HandSpeak as the answer for the sign

Returns a string stating the relative path of the downloaded video
"""
def download_sign_video(word: str) -> str:
    r = requests.get(get_handspeak_url(word), allow_redirects=True)

    if not r.ok:
        return None # Download unsuccessful
    
    filename = f'videos/{word}.mp4'
    open(filename, 'wb').write(r.content)
    return filename