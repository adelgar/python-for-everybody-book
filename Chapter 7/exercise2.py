while True:
	fname = input('Enter the file name: ')
	try:
		fhand = open(fname)
		count = 0
		total = 0
		for line in fhand:
			line = line.rstrip()
			if line.startswith('X-DSPAM-Confidence:'):
				count = count + 1
				fnum = float(line[20:])
				total = total + fnum
				#print(fnum)
		average = total / count
		print('Average spam confidence: ', round(average, 12), '\n')
	except:
		if fname == 'done':
			print('Done!')
			exit()
		else:
			print('File cannot be opened: ', fname)
			print('\n')
