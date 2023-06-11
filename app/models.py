import genanki

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