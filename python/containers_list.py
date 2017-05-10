# Lists

# A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:

xs = [3, 1, 2]
print (xs, xs[2])
print (xs[-1])
xs[2] = 'foo'
print (xs)
xs.append('bar') # add new element to end of list
print(xs)
x = xs.pop() # remove and return the last element of the list
print (x, xs)

# Slicing: in addition to accessing list elements one at a time, Python provides concise syntax to access sublists; this is known as slicing

nums = list(range(5)) # [0, 1, 2, 3, 4]
print (nums)
print (nums[2:4]) # get a slice from index 2 to 4 (exclusive) => [ 2, 3]
print (nums[2:]) # get a slide from index 2 to the end; [2, 3, 4]
print (nums[:]) # get a slide of the whole list; [0, 1, 2, 3, 4
print (nums[:-1]) # slide indices can be negative; prints ["0, 1, 2, 3]"
nums[2:4] = [8, 9] # Assign a new sublist to a slice
print (nums) # [0, 1, 8, 9, 4]


# loops : you can loop over the elements of a list like this

animals = ['cat', 'dog', 'monkey']
for animal in animals:
  print(animal)

# if you want to access to the index of each element within the body of a loop, use the build-in enumerate function:

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
  print('#%d: %s' % (idx + 1, animal))

# List comphehensions: When programming, frequently we want to transform one type of data into another. as a simple examples, consider the following code that computes square numbers:

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
  squares.append(x ** 2)

print(squares)

# you can make this code simpler using list comprehension
nums = [0, 1, 2, 3, 4]
squares = [ x ** 2 for x in nums ]
print(squares)
