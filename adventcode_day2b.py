file = open('day2.txt', 'r').read().split('\n')
ribbon = 0

for line in lines:
	nums = list(map(int, line.split('x')))
	edges = [2*nums[0]+2*nums[1], 2*nums[0]+2*nums[2], 2*nums[1]+2*nums[2]]
	ribbon += (nums[0]*nums[1]*nums[2])+min(edges)
print (ribbon)