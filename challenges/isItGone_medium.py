def find_it(items, name):
	nameCap = name.capitalize()
	if name in items:
		return (nameCap + " is gone...")
	else:
		return (nameCap + " is here!")

