file = open('day2.txt', 'r').read().split('\n')
paper = 0

for line in lines:
	nums = list(map(int, line.split('x')))
	paper += (2*nums[0]*nums[1])+(2*nums[0]*nums[2])+(2*nums[1]*nums[2])+(nums[0]*nums[1]*nums[2]/max(nums))
print (paper)