from functools import reduce

count_palindromes = lambda lst: list(map(lambda sub_lst: reduce(lambda x, y: x + 1, filter(lambda string: string == string[::-1], sub_lst), 0), lst))

# Test case
lists_of_strings = [["aba", "hello","level"], ["rotator" , "racecar", "python"], ["radar", "madam", "apple", "banana"],[],["ola"]]
print(count_palindromes(lists_of_strings))  # Output will be [2, 2, 2, 0, 0]