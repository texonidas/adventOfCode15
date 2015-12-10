text = open('day1.txt', 'r')

floor = 0

for char in text.read():
	if char == '(':
		floor += 1
	if char == ')':
		floor -= 1
print (floor)