# parts of a function
# parts of a dataclass

# Type-casts to int after getting result
"""1 // .5 #="""

# == False # Compares the unicode characters
"""“1” > “200”"""

# escape characters
'''print('I\'ll do great on this exam')'''

# truthiness
'''
x = 4
print(x == 5 or 10)
or 10 means 10 == True so the entire thing print to "True"

False == False but "False" == True

if something is empty / 0 / False       == False
'''

# mutability
'''
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

lst2 = lst1.append(1)
lst2 == None
lst1 = [1, 2, 3, 1]

LISTS ARE MUTABLE
DATACLASSES ARE MUTABLE
PRIMITIVES ARE NOT MUTABLE -> MUST BE ASSIGNED TO A NEW VARIABLE
'''

# datclasses
'''
from datclasses import dataclass

@datclass
'''

# check to make sure its calling a function w/ parenthesis() and not a variable
# Ex: Function ->print() vs print <- Variable

# designer will get documentation

# imports
'''
from dataclasses import dataclass
from bakery import assert_equal
from random import choice
'''