import snakeFill_hard
import unittest

class Test_SnakeFill(unittest.TestCase):
    def test_number(self):
       self.assertEqual(snakeFill_hard.snakefill(24), 9) 