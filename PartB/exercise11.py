from functools import reduce
cumulative_sum_of_squares_of_even = lambda lst: list(map(lambda sub_lst: reduce(lambda x, y: x + y, map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, sub_lst)), 0), lst))

# Test cases
lists_of_numbers1 = [[7, 2, 5], [1, 6, 4, 9], [17, 0, 8, 19]]
print(cumulative_sum_of_squares_of_even(lists_of_numbers1))  # Output will be [4, 52, 64]
lists_of_numbers2 = [[7, 1, 5], [2, 4, 6], [0]]
print(cumulative_sum_of_squares_of_even(lists_of_numbers2))  # Output will be [0, 56, 0]
lists_of_numbers3 = []
print(cumulative_sum_of_squares_of_even(lists_of_numbers3))  # Output will be []