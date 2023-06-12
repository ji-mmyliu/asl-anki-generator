"""
Run this file with a 'words.txt' file with your words on seperate lines to generate a 'words.json' file
"""

import json

words = [line.strip() for line in open("words.txt")]

config = {
    "name": "My ASL Deck",
    "export_filename": "asl_vocabulary.apkg",
    "words": words
}

json.dump(config, open("words.json", "w"))
