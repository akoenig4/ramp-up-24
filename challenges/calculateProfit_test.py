import caluclateProfit_medium
import unittest

class Test_CalculateProfit(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(caluclateProfit_medium.profit({
  "cost_price": 0,
  "sell_price": 0,
  "inventory": 0
}), 0)
        
    def test_non_zeros(self):
        self.assertEqual(caluclateProfit_medium.profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8501
}), 44035)



