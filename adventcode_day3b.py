text = open('day3.txt', 'r')
cur_x = 0
cur_y = 0
robo_cur_x = 0
robo_cur_y = 0
coords = [(cur_x, cur_y)]
robo_coords = [(robo_cur_x, robo_cur_y)]
count = 0

for char in text.read():
	if count % 2 == 0:
		if(char=='<'):
			cur_x -= 1
		if(char=='>'):
			cur_x += 1
		if(char=='v'):
			cur_y -= 1
		if(char=='^'):
			cur_y += 1
		coords.append((cur_x, cur_y))
	if count % 2 == 1:
		if(char=='<'):
			robo_cur_x -= 1
		if(char=='>'):
			robo_cur_x += 1
		if(char=='v'):
			robo_cur_y -= 1
		if(char=='^'):
			robo_cur_y += 1
		robo_coords.append((robo_cur_x, robo_cur_y))
	count += 1
print (len(set(coords+robo_coords)))
