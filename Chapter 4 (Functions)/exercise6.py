def computepay(hours, rate):
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

inp1 = input('Enter Hours: ')
try:
	hours = float(inp1)
	inp2 = input('Enter Rate: ')
	try:
		rate = float(inp2)
		computepay(hours, rate)
	except:
		print('Error, please enter numeric input')
except:
	print('Error, please enter numeric input')