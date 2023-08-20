'''The difference() method returns a set that contains the difference between two sets.
Meaning: The returned set contains items that exist only in the first set, and not in both sets.'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

#The code in line 8 looks for the difference between x and y

z = y.difference(x)

print(z)

'''Expected output:{'microsoft', 'google'}'''