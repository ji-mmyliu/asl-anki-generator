# ASL Anki Flashcard Deck Generator
Give us a list of words, we'll give you an Anki flashcard deck with the word as a question and a video of the sign as the answer. We'll even find the video for you!

## Usage
1. First clone the repository and enter the folder:
```bash
git clone https://github.com/ji-mmyliu/asl-anki-generator.git
cd asl-anki-generator
```

2. Install all the Python dependencies using Pip (feel free to activate a virtual environment):
```bash
python3 -m pip install -r requirements.txt
```

3. Clone `words.json.sample` into `words.json` and edit however you'd like.

4. Generate the Anki deck using the following command:
```bash
python3 main.py
```

Enjoy! Feel free to [submit an issue](https://github.com/ji-mmyliu/asl-anki-generator/issues/new) for any concerns or inquiries.
