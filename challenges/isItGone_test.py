import isItGone_medium
import unittest

class Test_IsItGone(unittest.TestCase):
     def test_isGone(self):
        self.assertEqual(isItGone_medium.find_it(["moshe", "lamp", "bed"], "moshe"), "Moshe is gone...")
     def test_isHere(self):
        self.assertEqual(isItGone_medium.find_it(["moeshe", "lamp", "bed"], "moshe"), "Moshe is here!")