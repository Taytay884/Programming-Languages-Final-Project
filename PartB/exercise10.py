from functools import reduce

def concatenate_strings(strings):
     return reduce(lambda x, y: x + ' ' + y, strings)


# Test cases
strings_list1 = ["Functools", "are", "cool"]
print(concatenate_strings(strings_list1))  # Output will be "hello world python"
strings_list2 = ["Programming"]
print(concatenate_strings(strings_list2))  # Output will be "Programming"
