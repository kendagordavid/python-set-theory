'''Python set issubset() method returns True if all elements of a set A are present in another set 
B which is passed as an argument, and returns False if all elements are not present in Python.'''

set_win = {1,2,3,4,5,6,7,8,9}
set_lose = {2,3,4,5,6,7,8,9}
set_draw = {4,5,6,7,8,9,10}

""" When you pass the following code the out put will be either true or false """

print(set_draw.issubset(set_win))

"""Expected output: false"""