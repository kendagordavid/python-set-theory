
# initialize the set
my_set = set([12, 10, 13, 15, 8, 9])
 
# remove elements one by one using discard() method.
# By using "(min(my_set))" the set will be discarded from minimal number to the maximum.
 
while my_set:
    my_set.discard(min(my_set))
    print(my_set)

    """ Expected output: 
{9, 10, 12, 13, 15}
{10, 12, 13, 15}
{12, 13, 15}
{13, 15}
{15}
set()"""