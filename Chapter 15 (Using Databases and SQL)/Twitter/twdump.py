import sqlite3

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM People')
print('People:')
count = 0

for row in cur:
    print(row)
    count = count + 1

print(count, 'rows.')

cur.execute('SELECT * FROM Follows')
print('Follows:')

count = 0

for row in cur:
    print(row)
    count = count + 1

print(count, 'rows.')
cur.close()