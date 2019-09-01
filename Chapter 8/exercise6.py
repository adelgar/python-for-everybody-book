numlist = []
while True:
	inp = input('Enter a number: ')
	try:
		if inp == 'done':
			print('Maximun:', max(numlist))
			print('Minimum:', min(numlist))
			break
		else:
			num = float(inp)
			numlist.append(num)
	except:
		print('\nERROR:', inp, 'is not a number\n')