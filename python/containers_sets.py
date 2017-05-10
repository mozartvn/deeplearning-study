# Sets
# A set is an unordered collection of distinct elements. As a simple examples, consider the following:

animals = {'cat', 'dog'}
print ('cat' in animals)
print ('fish' in animals)
animals.add('fish')  # add element to set
print ('fish' in animals)
animals.add('cat') # Adding an element that is already in the set does nothing
print(len(animals))
animals.remove('cat') # remove an element from set
print(len(animals))

# Loops : Iterating over a set has the same syntax as iterating over a list; however since sets are unordered, you cannot make a

animals = {'cat', 'dog', 'fish'}

for idx, animal in enumerate(animals):
  print ('#%d: %s' % (idx + 1, animal))

#Set comphrehensions : Like lists and dicitonaries, we can easily construct sets using set comphrehenions

from math import sqrt
nums = {int(sqrt(x)) for x in list(range(30))}
print(nums)