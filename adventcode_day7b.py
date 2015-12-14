instructions = open('day7.txt', 'r').read().split('\n')

nodes = []
for instruction in instructions:
	nodes.append([instruction.split(' ')[-1], None])

def nodeValue( str ):
	for node in nodes:
		if node[0] == str:
			return node[1]

def nodeIndex( str ):
	index = 0
	for node in nodes:
		if node[0] == str:
			return index
		index += 1

nodes[nodeIndex('b')][1] = 46065
while ([value for node in nodes for value in node].count(None)) > 0:
	for instruction in instructions:
		words = instruction.split(' ')
		if (nodeValue(words[-1]) == None):
			if (len(words) == 3):
				try:
					input1 = int(words[0])
				except ValueError:
					input1 = nodeValue(words[0])
				nodes[nodeIndex(words[2])][1] = input1
			elif (len(words) == 4):
				try:
					input1 = int(words[1])
				except ValueError:
					input1 = nodeValue(words[1])
				nodes[nodeIndex(words[3])][1] = None if (input1 == None) else (65535 - int(input1))
			else:
				try:
					input1 = int(words[0])
				except ValueError:
					input1 = nodeValue(words[0])
				try:
					input2 = int(words[2])
				except ValueError:
					input2 = nodeValue(words[2])
				if (words[1]=='OR'):
					nodes[nodeIndex(words[4])][1] = None if ((input1 == None) | (input2 == None)) else (int(input1) | int(input2))
				elif (words[1]=='AND'):
					nodes[nodeIndex(words[4])][1] = None if ((input1 == None) | (input2 == None)) else (int(input1) & int(input2))
				elif (words[1]=='LSHIFT'):
					nodes[nodeIndex(words[4])][1] = None if (input1 == None) else (int(input1) << input2)
				else:
					nodes[nodeIndex(words[4])][1] = None if (input1 == None) else (int(input1) >> input2)
	#print ([value for node in nodes for value in node].count(None))
print (nodeValue('a'))