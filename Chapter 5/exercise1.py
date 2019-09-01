total = 0
count = 0
while True:
	line = input('Enter a number: ')
	try:		
		if line == 'done':
			average = total / count
			break
		else:
			number = float(line)
			total = total + number
			count = count + 1
	except:
		print('Invalid input')	
print(total, count, average)
		