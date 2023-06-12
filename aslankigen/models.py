import genanki
import typing
from pydantic import BaseModel

asl_card_model = genanki.Model(
    2145444652,
    "ASL Card Model",
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Sign'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br>{{Sign}}',
        },
    ])

class WordsConfig(BaseModel):
    name: str
    export_filename: str
    words: typing.List[str]