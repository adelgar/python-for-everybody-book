while True:
	fname = input('Enter a file name:\n')
	try:
		if fname == 'done':
			break
		else:
			fhand = open(fname)
	except:
		print('\nFile cannot be opened:', fname)
	
	counts = dict()
	for line in fhand:
		line = line.rstrip()
		if line.startswith('From'):
			words = line.split()
			if not words[0] == 'From:':
				email = words[1].split('@')
				#print(email[1])
				counts[email[1]] = counts.get(email[1], 0) + 1
	
	print('\n', counts, '\n')