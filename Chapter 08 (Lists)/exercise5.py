fname = input('Enter a file name: ')
try:
	fhand = open(fname)
	count = 0
	for line in fhand:
		line = line.rstrip()
		if line.startswith('From'):
			words = line.split()
			if not words[0] == 'From:':
				count = count + 1
				print(words[1])
	print('\nThere were', count, 'lines in the file with From as the first word')
except:
	print('File', fname, 'not found')