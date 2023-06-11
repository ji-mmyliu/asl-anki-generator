import genanki
import json
import typing

from .models import asl_card_model

def generate_note(word: str) -> genanki.Note:
    my_note = genanki.Note(
        model=asl_card_model,
        fields=['Hello', 'Saluting sign with hand', '[sound:hello.mp4]']
    )

"""
Returns a generated deck based on the JSON file provided in src_json AND a list of strings indicaing the file names of videos
"""
def generate_deck(src_json: str) -> typing.Tuple(genanki.Deck, [str]):
    deck_config = json.load(open(src_json, 'r'))
    deck_name = deck_config['name']

    my_deck = genanki.Deck(
        1725443770,
        deck_name)
    
    video_files = []
    
    for word in deck_config['words']:
        my_deck.add_note(generate_note(word))
        video_files.append("")
    
    return (my_deck, video_files)
