text = open('day1.txt', 'r')

floor = 0
current = 1

for char in text.read():
	if char == '(':
		floor += 1
	if char == ')':
		floor -= 1
	if floor == -1:
		break
	current += 1
print(current)