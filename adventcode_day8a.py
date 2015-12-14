import ast

lines = open('day8.txt', 'r').read().split('\n')
raw = 0
processed = 0

for line in lines:
	raw += len(line)
	processed += len(ast.literal_eval(line))
print (raw-processed)