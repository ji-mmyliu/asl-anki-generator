from app.generate import generate_deck
import genanki
import json
import logging

WORD_LIST = "words.json"

deck_config = json.load(open(WORD_LIST, 'r'))
my_deck, video_files = generate_deck(deck_config)

my_package = genanki.Package(my_deck)
my_package.media_files = video_files
my_package.write_to_file(deck_config['export_filename'])

logging.info(f"Anki deck with {len(video_files)} cards successfully exported to \"{deck_config['export_filename']}\"!")
