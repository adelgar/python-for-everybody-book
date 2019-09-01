import string

while True:
    fname = input('Enter a file name:\n')
    if fname == 'done':
        exit()
    try:
        fhand = open(fname, encoding='utf-8')
    except:
        print('File', fname, 'cannot be opened')
    

    print('\n')
    
    counts = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(str.maketrans('', '', string.punctuation + string.whitespace + string.digits))
        line = line.lower()
        f = tuple(line)
        for letter in f:
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1
        #print(line)
        #print(f)
    #print(counts)
    sum = 0
    for key in counts:
        sum += counts[key]
    #print(sum)
    for key in counts:
        counts[key] = (counts[key]/sum)*100
    print(counts)
    
    lst = list()
    
    for key, val in list(counts.items()):
        lst.append((key, val))

    lst.sort()

    for key, val in lst:
        print(key, val)