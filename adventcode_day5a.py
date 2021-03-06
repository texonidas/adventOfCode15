import re

lines = open('day5.txt', 'r').read().split('\n')
good_words = 0
reg1 = re.compile(r"(.)\1+")
reg2 = re.compile(r"([aeiou])")
reg3 = re.compile(r"(ab|cd|pq|xy)+")

for line in lines:
	check1 = len(reg1.findall(line)) > 0
	check2 = len(reg2.findall(line)) >= 3
	check3 = len(reg3.findall(line)) == 0
	if check1 & check2 & check3:
		good_words+=1
print (good_words)
		