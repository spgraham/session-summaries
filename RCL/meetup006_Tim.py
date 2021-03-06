"""
Created on Wed Apr 10 17:38:43 2019

Meetup006
"""

my_dict = {'a':100, 'b':200, 'c':300, 'd':400}

# dictionaries can be defined using the curly brackets { } 
# dicts contain keys:values , items are separated by commas

# for loops can be used to iterate through iterable items such as a list, dictionary and tuples

# to define a for loop

# for item in object:  
#   execute commands

# if only one variable is defined in a for loop to iterate through in a dictionary, by default only keys will be operated on

for i in my_dict:
    print(i)

# but you can define the for loop to operate on the keys or the values by using .keys() or .values() function

for val in my_dict.values():
    print(val)

# to operate on both the keys and its associated values use two variables and the function .items() when defining the for loop

for k,v in my_dict.items():
    print(k,v)
    

# for loops using the built-in function called range() are often quite useful
# range() is always start inclusive, but stop exclusive, by default range starts at 0 if starting point is not defined

for number in range(5):
    print(number)

# output is 0 1 2 3 4

# range() can be used by defining the range(start, stop, step)

for j in range(3,10,2):
    print(j)    
    
# output is 3 5 7 9

    
# for loops can iterate through strings as well
    
for letters in "This sentence":
    print(letters)


set_x = [0.0, 0.2, 0.4, 0.6]

# The challenge is to increase set_x to 2.0 in increments of 0.2



# one possible solution
 
set_x = [i/5 for i in range(11)]

print("set_x =", set_x)

# note that when the print() function is indented, it is part of the for loop, otherwise it is a a stand-alone function command 
