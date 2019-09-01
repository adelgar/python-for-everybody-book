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
				if words[1] not in counts:
					counts[words[1]] = 1
				else:
					counts[words[1]] += 1
				#counts[words[1]] = counts.get(words[1], 0) + 1
	
	lst = list()
	for key, val in list(counts.items()):
		lst.append((val, key))
	
	lst.sort(reverse=True)
	
	key, val = lst[0]
	print(val, key, '\n')
		