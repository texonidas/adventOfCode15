instructions = open('day6.txt', 'r').read().split('\n')

lights = []
for i in range(1000):
    col = []
    for j in range(1000):
        col.append(0)
    lights.append(col)   

for instruction in instructions:
	words = instruction.split(' ')
	if (words[0]=='turn'):
		start = words[2].split(',')
		end = words[4].split(',')
		flag = True if words[1]=='on' else False
		for i in range(int(start[0]),int(end[0])+1):
			for j in range(int(start[1]),int(end[1])+1):
				if(flag):
					lights[i][j] += 1
				elif(lights[i][j] != 0):
					lights[i][j] -= 1
	if (words[0]=='toggle'):
		start = words[1].split(',')
		end = words[3].split(',')
		for i in range(int(start[0]),int(end[0])+1):
			for j in range(int(start[1]),int(end[1])+1):
				lights[i][j] += 2
total = 0
for col in lights:
	for elem in col:
		total += elem
print (total)