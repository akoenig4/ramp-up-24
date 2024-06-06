import stutter_easy
import unittest

class Test_Stutter(unittest.TestCase):
    def test_stutter(self):
        self.assertEqual(stutter_easy.stutter("adir koenig"), "ad... ad... adir koenig?")