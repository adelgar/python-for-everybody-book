while True:
	fname = input('Enter a file name: ')
	try:
		if fname == 'done':
			break
		else:
			fhand = open(fname)
	except:
		print('File cannot be opened:', fname)
	
	counts = dict()
	for line in fhand:
		line = line.rstrip()
		if line.startswith('From'):
			words = line.split()
			if not words[0] == 'From:':
				counts[words[1]] = counts.get(words[1], 0) + 1
						
	print(counts, '\n')
	
	tallest = None
	for key in counts:
		#print(tallest)
		#print(key)
		#print('Value in dict:', counts[key])
		value = counts[key]
		if tallest == None or value > tallest:
			tallest = value
			email = key
		
	print(email, tallest, '\n')