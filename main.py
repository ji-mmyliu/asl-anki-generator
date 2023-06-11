from app.generate import generate_deck
import genanki
import json

WORD_LIST = "words.json"

my_deck, video_files = generate_deck(WORD_LIST)

my_package = genanki.Package(my_deck)
my_package.media_files = video_files
my_package.write_to_file(json.load(open(WORD_LIST, 'r'))['export_filename'])