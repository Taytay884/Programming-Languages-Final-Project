# Rewrite the following program in one line by using nested filter, map and reduce functions:
print("Original program: ")
nums = [1,2,3,4,5,6]
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

squared = []
for even in evens:
    squared.append(even**2)

sum_squared = 0
for x in squared:
    sum_squared += x
print(sum_squared)

# to rewrite this logic we need part of the previous solution(exercise11.py) we took the inner part of the logic,
# and removed the looping over list of lists
print("New version: ")
from functools import reduce
sum_of_squares_of_even = lambda lst: reduce(lambda x, y: x + y, map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, lst)), 0)

print(sum_of_squares_of_even(nums))
