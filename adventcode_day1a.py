text = open('day1.txt', 'r')

floor = 0

for char in text.read():
	if char == '(':
		floor += 1
	elif char == ')':
		floor -= 1
print (floor)