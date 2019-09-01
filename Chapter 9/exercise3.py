fname = input('Enter a file name: ')
try:
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
				
print(counts)
			
	