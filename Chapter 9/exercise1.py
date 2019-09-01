fname = input('Enter a file name: ')
try:
	fhand = open(fname)
	words = list()
	worddict = dict()
	i = 0
	for line in fhand:
		line = line.rstrip()
		words = line.split()
		for word in words:
			worddict[word] = i
			i = i + 1
	print(worddict)
	while True:
		inp = input('\nIs this word in the dictionary? (Type "done" to exit)\n')
		if inp == 'done':
			break
		elif inp in worddict:
			print(inp, 'is in the dictionary!')
		else:
			print(inp, 'is not in the dictionary')
except:
	print('Incorrect file name')
		
	