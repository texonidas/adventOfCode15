file = open('day2.txt', 'r')
paper = 0
text = file.read()
lines = text.split('\n')
for line in lines:
	nums = list(map(int, line.split('x')))
	paper += (2*nums[0]*nums[1])+(2*nums[0]*nums[2])+(2*nums[1]*nums[2])+(nums[0]*nums[1]*nums[2]/max(nums))
print (paper)