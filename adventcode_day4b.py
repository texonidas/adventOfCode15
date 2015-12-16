import hashlib

key = open('day4.txt', 'r').read()
check = 0
flag = True

while flag:
	input = key + str(check)
	hash = hashlib.md5()
	hash.update(input.encode('utf-8'))
	if (hash.hexdigest()[:6] == '000000'):
		print(check)
		flag = False
	check += 1