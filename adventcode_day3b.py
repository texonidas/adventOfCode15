text = open('day3.txt', 'r')
cur_x = 0
cur_y = 0
robo_x = 0
robo_y = 0
coords = [(cur_x, cur_y)]
count = 0

for char in text.read():
	if count % 2 == 0:
		if(char=='<'):
			cur_x -= 1
		elif(char=='>'):
			cur_x += 1
		elif(char=='v'):
			cur_y -= 1
		elif(char=='^'):
			cur_y += 1
		coords.append((cur_x, cur_y))
	else:
		if(char=='<'):
			robo_x -= 1
		elif(char=='>'):
			robo_x += 1
		elif(char=='v'):
			robo_y -= 1
		elif(char=='^'):
			robo_y += 1
		coords.append((robo_x, robo_y))
	count += 1
print (len(set(coords)))
