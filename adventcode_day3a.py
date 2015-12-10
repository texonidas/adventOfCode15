text = open('day3.txt', 'r')
cur_x = 0
cur_y = 0
coords = [(cur_x, cur_y)]

for char in text.read():
	if(char=='<'):
		cur_x -= 1
	if(char=='>'):
		cur_x += 1
	if(char=='v'):
		cur_y -= 1
	if(char=='^'):
		cur_y += 1
	coords.append((cur_x, cur_y))

print (len(set(coords)))