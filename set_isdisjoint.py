""" Python set isdisjoint() function check whether the two sets are disjoint or not, 
if it is disjoint then it returns True otherwise it will return False.
 Two sets are said to be disjoint when their intersection is null.  """
 
set_a = {"green","yellow","red","pink","orange","blue","black"}
set_b = {"green","yellow","red","pink","orange","blue","black"}
print(set_a.isdisjoint(set_b))

""" Expected output should be: false.This means that the two sets a and b, are joint and not disjoint """

