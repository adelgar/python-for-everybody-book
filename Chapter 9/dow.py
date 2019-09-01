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
			if words[1] not in counts:
				counts[words[1]] = 1
			else:
				counts[words[1]] += 1
				
print(counts)
			
	