import stringToInt_very_easy
import unittest

class Test_StringToInt(unittest.TestCase):
    def string_one(self):
        self.assertEqual(stringToInt_very_easy.string_int("6"), 6)