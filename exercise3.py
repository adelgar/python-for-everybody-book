inp1 = input('Enter Hours: ')
hours = float(inp1)
inp2 = input('Enter Rate: ')
rate = float(inp2)
inp3 = hours * rate
pay = str(round(inp3, 2))
print('Pay: ' + pay)