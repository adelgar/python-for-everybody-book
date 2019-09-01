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
				hour = words[5].split(':')
				if hour[0] not in counts:
					counts[hour[0]] = 1
				else:
					counts[hour[0]] += 1
				#counts[words[1]] = counts.get(words[1], 0) + 1
	
	lst = list()
	for key, val in list(counts.items()):
		lst.append((key, val))
	
	lst.sort(reverse=False)
	
	for key, val in lst:
		print(key, val)
	print('\n')
		