while True:
	fname = input('Enter the file name: ')
	try:
		fhand = open(fname)
		for line in fhand:
			line = line.rstrip().upper()
			print(line)
	except:
		if fname == 'done':
			print('Done!')
			exit()
		else:
			print('File cannot be opened: ', fname)
			print('\n')
