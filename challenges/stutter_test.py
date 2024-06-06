import stutter_easy
import unittest

class Test_Stutter(unittest.TestCase):
    def stutter(self):
        self.assertEqual(stutter_easy.stutter("adir koenig"), "ad... ad... adir koenig?")