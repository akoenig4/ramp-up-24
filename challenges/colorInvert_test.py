import colorInvert_easy
import unittest

class Test_ColorInvert(unittest.TestCase):
    def test_white(self):
        self.assertEqual(colorInvert_easy.color_invert((255,255,255)), (0,0,0))

    def test_black(self):
        self.assertEqual(colorInvert_easy.color_invert((0,0,0)), (255,255,255))
    
    def test_something_in_between(self):
        self.assertEqual(colorInvert_easy.color_invert((75,14,189)), (180,241,66))