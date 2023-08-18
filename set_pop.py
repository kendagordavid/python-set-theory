#write a set first.
set_a = {1,2,3,4,5,6,7,8,9}
print("Initial:")
#print
print(set_a)

set_a.pop()
print("set after popping an element.")
print(set_a)
""" By using while len() you can be able to make a 
 loop which pops out one element per loop"""  
while len(set_a) > 0:
    set_a.pop()
    print(set_a)
#Expected output
'''  Initial:
{1, 2, 3, 4, 5, 6, 7, 8, 9}
set after popping an element.
{2, 3, 4, 5, 6, 7, 8, 9}
{3, 4, 5, 6, 7, 8, 9}
{4, 5, 6, 7, 8, 9}
{5, 6, 7, 8, 9}
{6, 7, 8, 9}
{7, 8, 9}
{8, 9}
{9}
set()'''