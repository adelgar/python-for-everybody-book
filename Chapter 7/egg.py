while True:
	fname = input('Enter the file name: ')
	try:
		fhand = open(fname)
		count = 0
		for line in fhand:
			line = line.rstrip()
			if line.startswith('X-DSPAM-Confidence:'):
				count = count + 1
		print('There were', count, 'subject lines in', fname, '\n')
	except:
		if fname == 'done':
			print('Done!')
			exit()
		elif fname == 'na na boo boo':
			print(fname.upper(), "TO YOU - You have been punk'd!\n")
		else:
			print('File cannot be opened: ', fname, '\n')
