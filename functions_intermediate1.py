import random

# If no arguments are provided, the function should return a random integer between 0 and 100.
# def no_argument(min=0, max=100):
#   return round(random.random() * max)
# print(no_argument())

# If only a max number is provided, the function should return a random integer between 0 and the max number.
# def max_provided(min=0, max=0):
#   return round(random.random() * max)
# print(max_provided(max=10))

# If only a min number is provided, the function should return a random integer between the min number and 100
# def min_provided(min=1, max=100):
#     return round(random.random() * (max - min) + min)
# print(min_provided(min=10))
  
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# def both_provided(min=0, max=1):
#   return round(random.random() * (max - min) + min)
# print(both_provided(min=50, max=200))

# Here are a couple of important notes about using random.random() and rounding. (Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)

# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num
  
# Here's a little bit of code to get you started, with some test cases and expected outputs. Test each function call one at a time and a few times each to make sure you're getting the correct range.
# def randInt(min=   , max=   ):
#     num = random.random()
#     return num
# def randInt(min=0, max=100):
#   return round(random.random() * (max - min) + min)
# print(randInt(min=50, max=500))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

