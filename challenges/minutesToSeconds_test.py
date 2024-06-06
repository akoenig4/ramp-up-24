import minutesToSeconds_very_easy
import unittest

class Test_MinutesToSeconds(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(minutesToSeconds_very_easy.convert(0),0)
    def test_nonzero(self):
        self.assertEqual(minutesToSeconds_very_easy.convert(50),3000)