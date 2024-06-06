def snakefill(n):
	area = n**2
	size = 1
	for x in range(area):
		if (size*2) <= area:
			size *= 2
		else:
			return(x)
