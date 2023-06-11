import unittest
from .util import get_handspeak_url
from .generate import generate_deck

class TestGetHandspeakUrl(unittest.TestCase):
    def test_get_handspeak_url(self):
        actual = get_handspeak_url("hello")
        expected = "https://www.handspeak.com/word/h/hel/hello.mp4"
        self.assertEqual(actual, expected)

# class TestGenerateDeck(unittest.TestCase):
#     def test_generate_deck(self):
#         actual = generate_deck({})