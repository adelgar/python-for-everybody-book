import re

while True:
    reg = input('Enter a regular expression: ')
    if reg == 'done':
        print('Program finished\n')
        break
    hand = open('mbox.txt')
    count = 0
    for line in hand:
        line = line.rstrip()
        if re.search(reg, line):
            count += 1
    print('mbox.txt had', count, 'lines that matched', reg, '\n')
