
def profit(info):
	print(round((info["sell_price"]-info["cost_price"])*info["inventory"]))

profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8501
})