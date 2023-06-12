import genanki
import json
import typing

from .models import asl_card_model
from .util import download_sign_video

def generate_note(word: str) -> genanki.Note:
    my_note = genanki.Note(
        model=genanki.BASIC_MODEL,
        fields=[word[0].upper() + word[1:], f'[sound:{word}.mp4]']
    )
    return my_note

"""
Returns a generated deck based on the configuration in deck_config AND a list of strings indicaing the file names of videos
"""
def generate_deck(deck_config: any) -> typing.Tuple[genanki.Deck, typing.List[str]]:
    deck_name = deck_config['name']

    my_deck = genanki.Deck(
        1725443770,
        deck_name)
    
    video_files = []
    
    for word in deck_config['words']:
        # Download answer sign video
        video_file = download_sign_video(word)

        # Check if word exists
        if not video_file:
            continue

        # Generate Anki flashcard
        my_deck.add_note(generate_note(word))

        # Add video file location to list
        video_files.append(video_file)
    
    return (my_deck, video_files)
