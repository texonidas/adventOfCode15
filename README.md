# adventOfCode15#
## Preface ##
I'm a mechatronic engineer, with experience in C, C++, C#, Matlab, and T-SQL.

I decided to use Advent of Code this year to learn Python, a language I have no experience in. This repository contains my solutions and input files. Feel free to clone this repository and replace the dayN.txt files with your own inputs.

**OBLIGATORY OBVIOUS SPOILER WARNING:** This repository contains solutions for Advent of Code 2015.

## Advent of Code 2015 solutions ##
### Day 1: Not Quite Lisp ###
#### Part One ####
The first day was a relatively simple warm-up problem. Santa has a list of instructions to navigate the floors of an infinite apartment building. **(** means he needs to go up a floor, **)** means he needs to go down a floor.

The first step towards solving this task was getting the input into a Python script, easily achieved via the `open('day1.txt', 'r')` function. It was then as simple as iterating over each character in the text (using the `.read()` function to obtain the string), and incrementing or decrementing a `floor` variable depending on the character. Using the `print(floor)` function then displayed the result in the console.

#### Part Two ####
The second half of this problem was to determine which instruction was the first one to take Santa to floor -1.

This problem requires only a slight modification to the original solution; an `if` statement to check the current floor and break out of the for loop, and a counter to store how many instructions had been read, to be incremented at the end of each loop.

### Day 2: I Was Told There Would Be No Math ###
#### Part One ####
The second day's problem was slightly harder than the first. The elves have a list of perfect right rectangular prism (box) dimensions, and they are trying to calculate the required square footage of wrapping paper needed to get the job done. They need a little extra per present though; the area of the smallest side.

Each of the presents' dimensions were listed in the form lxwxh, where l, w, h are the length, width, and height (which has no correlation to the size of the values). To interpret this text, the `.split()` function was needed; firstly to split the initial text into a series of boxes (`.split('\n')`), and then to split each of the boxes into individual dimensions (`.split(' ')`).

This returned a list of strings. To convert them into a list of integers, chaining of a few functions was required. Firstly, the raw output of `.split('x')` was passed into the `map` function, along with the `int` argument, which mapped the values to integers (to noone's surprise). The `list()` function then converted the returned iterable to a list.

The final resulting line was:

	nums = list(map(int, line.split('x')))

With the dimensions of the present stored in `nums`, it was just a matter of calculating the paper needed, and adding it to a running total. The trickiest part of this was calculating the value of the smallest face. I achieved this by multiplying all three numbers together and dividing by the largest one, obtained using the `max()` function. The final line was rather unwieldy, however it was unavoidable given the calculation.

The final line was:

	paper += (2*nums[0]*nums[1])+(2*nums[0]*nums[2])+(2*nums[1]*nums[2])+(nums[0]*nums[1]*nums[2]/max(nums))

#### Part Two ####
The second half of the problem was to calculate the amount of ribbon required to tie the presents, calculated by taking the smallest perimeter of any one face. They also required extra footage equal to the cubic volume of the present, because they're elves and fuck you.

To calculate the smallest perimeter, I constructed a second list containing the perimeters of the faces (excluding the duplicate of each face). The length of ribbon was then easily calculable by finding the minimum element of the perimeter list via the `min()` function, and then adding the product of the original dimensions list.

### Day 3
#### Part One ####

#### Part Two ####

### Day 4
#### Part One ####

#### Part Two ####

### Day 5
#### Part One ####

#### Part Two ####

### Day 6
#### Part One ####

#### Part Two ####

### Day 7
#### Part One ####

#### Part Two ####

### Day 8
#### Part One ####

#### Part Two ####

### Day 9
Yet to be started.

### Day 10
Yet to be started.

### Day 11
Yet to be started.

### Day 12
Yet to be started.

### Day 13
Yet to be started.

### Day 14
Yet to be started.

### Day 15
Yet to be released.

### Day 16
Yet to be released.

### Day 17
Yet to be released.

### Day 18
Yet to be released.

### Day 19
Yet to be released.

### Day 20
Yet to be released.

### Day 21
Yet to be released.

### Day 22
Yet to be released.

### Day 23
Yet to be released.

### Day 24
Yet to be released.

### Day 25
Yet to be released.
