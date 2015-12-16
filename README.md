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

### Day 3: Perfectly Spherical Houses in a Vacuum
#### Part One ####
I originally over-engineered the solution to day three, which I will explain in more detail further down. In this problem, Santa is delivering presents to an infinite two-dimensional grid of houses according to cardinal directions radioed in by an elf at the North Pole, because context is important. He moves one house at a time, delivering a single present to each house he stops at. The goal is to find out how many houses receive at least one present.

To begin this problem, I created `cur_x` and `cur_y` variables, intialised to 0. I then created a list, `coords`, to store the coordinates of each house Santa visits. Using a `for` loop, I iterated through each character, and incremented or decremented either `cur_x` or `cur_y` accordingly. After adjusting the position, I added the new coordinates to the `coords` list as a tuple using the `.append()` function.

This is where my solutions diverged.

##### Initial Solution #####
Due to a misunderstanding of the question, I intitially thought I needed to find all the houses Santa visits more than once, rather than at least once. **HUGE** difference.

I used the coordinates list to find the maximum and minimum x and y values Santa visited, then used them to generate a finite two-dimensional grid of those dimensions with zeroes. I then offset each of the coordinates to centre them on the origin of the grid, and incremented the value of cell at that location. I then used `.count()` to find all of the elements that were two or greater, however I could not get the correct answer to the problem, even when I realised that I had interpreted the question wrong and updated the condition accordingly.

At this point I had written a series of loops and list generators to the tune of 50-60 lines, when a suggestion from David simplified the whole problem.

##### Final Solution #####
Python contains a function called `set()`, which can be passed a list, and will return all unique values within that list.

This means that in the end my mess of lists and lists of lists was simplified to a single line:

	print (len(set(coords)))

Much to my dismay. I learned an important lesson though. **Don't get stuck trying to solve a problem they way you thought you needed to.**

#### Part Two ####
In the second part of this problem, Santa has built himself a Robo-Santa, because robots are **awesome**. They now interpret the instructions by alternating between inferior Flesh-Santa and perfect shiny Robo-Santa. The goal remains the same.

This problem again required only slight modification. I added another set of coordinates, `robo_x` and `robo_y`, to track the position of Better-Santa, and a counter to track the how many instructions had been given. To determine whose turn it was, I used an `if: else:` statement based on the modulo (remainder of a division) of the current instruction with 2, `count % 2`. If it was 0, it was Shit-Santa's turn, otherwise it was Super-Santa's.

I then created a copy of the original loop inside Awesome-Santa's case, replacing `cur_x`, `cur_y` with `robo_x` and `robo_y` respectively. This included in the appending of coordinates to `coords`.

The end result was 260 more houses visited, which just goes to show how specifically awesome robots are.

### Day 4: The 	Ideal Stocking Stuffer
#### Part One ####
Day four was a less challenging problem than the previous day's, requiring importing a single library. Santa has started mining AdventCoins, and he needs to find MD5 hashes that start with five zeroes in hexadecimal. The input to the hash is the given key with an integer appended to the end.

To generate the hashes, I had to import `hashlib`, a standard library for Python that is used for, unsurprisingly, generating hashes. Unfortunately, the only way to find the lowest value that generates a hash with five leading zeroes is via brute force. To this end, I appended an integer to the given key (stored in day4.txt), and then hashed the resultant string, using `.update()`. I then converted the result to hexadecimal, and checked if the first five characters were zeroes.

#### Part Two ####
The second part of this challenge was a very small modifcation. The goal was to find the first integer that resulted in a hash starting with six zeroes. To achieve this I changed the 4 in the index to a 5, and added another 0 to the check string.

### Day 5
#### Part One ####
In day six, Santa has suffered from a mental slip, and assigned human traits to the strings on his list. He has defined nice strings as those that contains at least three vowels, contains at least one set of double letters, and does not include the strings ab, cd, pq, or xy.

As the experienced amongst you may have realised, this required the use of regular expression, also known as regex. Python contains a standard library called `re` that provides regex functionality. I used [regexr](http://regexr.com/) to test my regular expressions. Three seperate expressions were required to check the conditions, one for each condition.

The three regular expressions ended up as:

	reg1 = re.compile(r"(.)\1+")
	reg2 = re.compile(r"([aeiou])")
	reg3 = re.compile(r"(ab|cd|pq|xy)+")

The first expression checks for any duplicate character, `{.)`, and then matches the group again using `\1`. The second places the five vowels into square brackets, `[aeiou]`, which is the equivalent of `OR`. The third uses explicit ORs to match the disallowed strings.

Each of the compiled regexs are then evaluated on a string by string basis, and a matching count is taken using `len()` and `.findall()`.

#### Part Two ####
The second part of this problem gave different conditions for naughty and nice, continuing Santa's rapid decline into madness. A nice string needs to contain a pair of any two letters that appears twice within the string, and contains a set of any three letters where the first and last letter match.

The new regexs were:

	reg1 = re.compile(r"(.)(.){1}(\1)")
	reg2 = re.compile(r"(..)(.)*(\1)")

The first expression matches any character, then matches any one character, indicated by `(.){1}`. The third matching group, `(\1)`, matches the first again. The second expression matches any two characters, and then matches zero or more of any character, shown by `(.)*`, before matching the pair again. The code then check that both of these condition matched at least once using the same method as before.

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
