def computegrade(score):
	if score < 0 or score > 1:
		print('Bad score')
	elif score < 1 and score >= 0.9:
		print('A')
	elif score < 0.9 and score >= 0.8:
		print('B')
	elif score < 0.8 and score >= 0.7:
		print('C')
	elif score < 0.7 and score >= 0.6:
		print('D')
	elif score < 0.6:
		print('F')

inp = input('Enter score:  ')

try:
	score = float(inp)
	computegrade(score)
except:
	print('Bad score')