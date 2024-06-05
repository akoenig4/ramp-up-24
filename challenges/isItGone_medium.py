def find_it(items, name):
	nameCap = name.capitalize()
	if name in items:
		print(nameCap + " is gone...")
	else:
		print(nameCap + " is here!")

find_it(["moshe", "lamp", "bed"], "moshe")