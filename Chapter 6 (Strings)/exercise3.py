def count(word, letter):
	i = 0
	for let in word:
		if let == letter:
			i = i + 1
	print(i)
	print('\n')

while True:
	word = input('Enter a word: ')
	if word == 'done':
		print('Finish!!')
		break
	else:
		letter = input('Enter a letter: ')
		while True:
			if len(letter) != 1:
				letter = input('Please enter only one letter: ')
			else:
				break	
	count(word, letter)