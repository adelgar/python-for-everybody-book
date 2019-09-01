def chop(t):
	end = len(t)-1
	del t[end]
	del t[0]
	return None

	
def middle(t):
	return t[1:len(t)-1]
		
t = [1, 2, 3, 5, 65, 87, 6]
rem = chop(t)
print(t)
print(rem,'\n')
p = [1, 2, 3, 5, 65, 87, 6]
rest = middle(p)
print(rest)