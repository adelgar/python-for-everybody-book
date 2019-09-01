def maximum(value, tallest):
	if tallest == None or value > tallest:
		tallest = value
		return tallest
	else:
		return tallest	

def minimum(value, smallest):
	if smallest == None or value < smallest:
		smallest = value
		return smallest
	else:
		return smallest
		
		
total = 0
count = 0
tallest = None
smallest = None
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
			tallest = maximum(number, tallest)
			smallest = minimum(number, smallest)
	except:
		print('Invalid input')	
print('Total number: ', total)
print('Total inputs: ', count)
print('Maximum number introduced: ', tallest)
print('Minimum number introduced: ', smallest)
		