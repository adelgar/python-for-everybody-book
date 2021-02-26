fname = input('Enter file: ')
try:
	hname = open(fname)
	words = list()
	t = []
	for line in hname:
		line = line.rstrip()
		#print(line.upper())
		words = line.split()
		#print('LINE SPLITTED:\n', words, '\n')
		#print('List of words not repeated:', t, '\n')
		for word in words:
			#print('Word', word.upper())
			if not word in t:
				#print(word.upper(), 'is not in t')
				t.append(word)
				#print('Word list:', t, '\n')
	t.sort()
	print(t)
except:
	print('File cannot be opened:', fname)
	exit()