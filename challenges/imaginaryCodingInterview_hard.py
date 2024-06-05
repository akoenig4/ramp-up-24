def interview(lst, tot):
	qualified = True
	if len(lst) < 8 or tot > 120 or lst[0]>5 or lst[1]>5 or lst[2]>10 or lst[3]>10 or lst[4]>15 or lst[5]>15 or lst[6]>20 or lst[7]>20:
		qualified = False
	if qualified:
		print("qualified")
	else:
		print("disqualified")

interview([5, 5, 10, 10, 15, 15, 20, 20], 120)