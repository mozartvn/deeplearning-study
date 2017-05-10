# Tuples
# A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:

d = { (x, x+1) : x for x in list(range(10))} #  Create a dictionary with tuple keys
t = (5, 6) # Create a tuple
print (type(t))
print (d[t])
print (d[(1, 2)])
