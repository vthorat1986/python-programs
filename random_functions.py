#!/usr/bin/python
import random

list = [3 , 4 , 67 , 523 , 1 , 33]
print (list)

# random.choice(seq)
print ('Randomly selected number from list is : ', random.choice(list))
print ('Randomly selected number from list is : ', random.choice(list))

# random.randrange(start, stop, step)
print ('Randomly selected even no. between 100 & 1000 : ', random.randrange(100, 1000, 2))
print ('Randomly selected even no. between 100 & 1000 : ', random.randrange(100, 1000, 2))

# random.random() => Seletes any random value that is greater than ZERO but less than ONE
print ('random() : ', random.random())

# random.seed(x)
random.seed(10)
print ('random() with seed as 10: ', random.random())
random.seed(10)
print ('random() with seed as 10 : ', random.random()) # will print same random number as the seed value is same
random.seed(20)
print ('random() with seed as 20 : ', random.random())

# random.shuffle(list)
print ('Normal list : ', list)
random.shuffle(list)
print ('Shuffled list : ', list)
random.shuffle(list)
print ('Shuffled list : ', list)

# random.uniform(x, y) => returns floating number between x & y
print ('Random no. between 5 to 10 : ', random.uniform(5, 10))