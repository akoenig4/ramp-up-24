import imaginaryCodingInterview_hard
import unittest

class Test_CodingInterview(unittest.TestCase):
    def test_overtime_on_question(self):
        self.assertEqual(imaginaryCodingInterview_hard.interview([6, 5, 10, 10, 15, 15, 20, 20], 120), "disqualified")
    def test_overtime_overall(self):
         self.assertEqual(imaginaryCodingInterview_hard.interview([5, 5, 10, 10, 15, 15, 20, 20], 150), "disqualified")
    def test_under_8_questions(self):
         self.assertEqual(imaginaryCodingInterview_hard.interview([5, 5, 10, 10, 15, 15, 20], 120), "disqualified")
    def test_qualified(self):
          self.assertEqual(imaginaryCodingInterview_hard.interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")
