#Exercise 2
import re

while True:
    fname = input('Enter file: ')
    try:
        if fname == 'done':
            break
        else:
            fhand = open(fname)
    except:
        print('File cannot be opened:', fname, '\n')
    count = 0
    sum = 0
    for line in fhand:
        line = line.rstrip()
        x = re.findall('New Revision: ([0-9]+)', line) #Select only the numbers
        if len(x) > 0:
            count += 1
            sum = sum + int(x[0])
    avg = sum / count
    print(int(avg), '\n')

            

