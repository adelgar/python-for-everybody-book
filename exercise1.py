inp1 = input('Enter Hours: ')
hours = float(inp1)
inp2 = input('Enter Rate: ')
rate = float(inp2)

if hours > 40:
	worked = hours - 40
	extra = worked * 1.5
	inp3 = (40 + extra) * rate
	pay = str(round(inp3, 2))
	print('Pay: ' + pay)
else:
	inp3 = hours * rate
	pay = str(round(inp3, 2))
	print('Pay: ' + pay)