from engine import *
from variables import *
from blocks import *

many_while_and_ifs_program = \
            "v1 = 0\n" + \
              "while v1 < 3\n" + \
                "v1 = v1 + 1\n" + \
                "v2 = 0\n" + \
                "while v2 < 4\n" + \
                    "v9 = v9 + 100\n" + \
                    "v2 = v2 + 1\n" + \
                    "if v4 > -1\n" + \
                        "v4 = v4 + 100\n" + \
                        "if v4 > 50\n" + \
                            "v4 = v4 + 0\n" + \
                        "end_if\n" + \
                        "v5 = 300\n" + \
                    "end_if\n" + \
                "end_while\n" + \
                "v3 = 0\n" + \
                "while v3 < 5\n" + \
                    "v3 = v3 + 1\n" + \
                "end_while\n" + \
              "end_while"
many_while_and_ifs_program_result = {'v0': 0, 'v1': 3, 'v2': 4, 'v3': 5, 'v4': 1200, 'v5': '300', 'v6': 0, 'v7': 0, 'v8': 0, 'v9': 1200}

# v0 = input_number
# v1 = factorial_result
# v2 = current_factor
#
# Expected Result:
# v1 = 120
factorial_program = \
    "v0 = 5\n" + \
    "v1 = 1\n" + \
    "v2 = v0\n" + \
    "while v2 > 0\n" + \
        "v1 = v1 * v2\n" + \
        "v2 = v2 - 1\n" + \
    "end_while"
factorial_program_result = "5! = 5*4*3*2*1 = 120 | v1 = 120"

# Sum of Squares Calculation
#   - v1: Current natural number
#   - v2: Square of the current number
#   - v0: Sum of squares
#
# Expected Result:
#   v0 = 55
sum_of_squares = \
    "v1 = 1\n" + \
    "v2 = 0\n" + \
    "v0 = 0\n" + \
    "while v1 < 6\n" + \
        "v2 = v1 * v1\n" + \
        "v0 = v0 + v2\n" + \
        "v1 = v1 + 1\n" + \
    "end_while"
sum_of_squares_result = "1*1 + 2*2 + 3*3 + 4*4 + 5*5 = 55 | v0 = 55"

# Power of a Number Calculation
#   - v0: Base number
#   - v1: Exponent
#   - v2: Result of base^exponent
#
# Expected Result:
#   v0 = 2, v1 = 0, v2 = 32
power_of_number = \
    "v0 = 2\n" + \
    "v1 = 5\n" + \
    "v2 = 1\n" + \
    "while v1 > 0\n" + \
        "v2 = v2 * v0\n" + \
        "v1 = v1 - 1\n" + \
    "end_while"
power_of_number_result = "v0^v1 = 2^5 = 32 | v0 = 2, v2 = 32"

# Remainder Checker
remainder_check = \
    "v0 = 10\n" + \
    "v1 = 3\n" + \
    "v2 = 10 / 3"
remainder_check_result = "10 / 3 = 3 (1) | v2 = 3"



if __name__ == '__main__':
    print("------[START - Many while and ifs program]------")
    program = many_while_and_ifs_program
    run_program(program)
    print(f"Expected Result:    {many_while_and_ifs_program_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Many while and ifs program]------")
    print()

    print("------[START - Factorial calculator program]------")
    program = factorial_program
    run_program(program)
    print(f"Expected Result:    {factorial_program_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Factorial calculator program]------")
    print()

    print("------[START - Sum of squares program]------")
    program = sum_of_squares
    run_program(program)
    print(f"Expected Result:    {sum_of_squares_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Sum of squares program]------")
    print()

    print("------[START - Power of number program]------")
    program = power_of_number
    run_program(program)
    print(f"Expected Result:    {power_of_number_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Power of number program]------")
    print()

    print("------[START - Remainder Check]------")
    program = remainder_check
    run_program(program)
    print(f"Expected Result:    {remainder_check_result}")
    print(f"Result:             {variables}")
    reset_variables(variables)
    print("------[END - Remainder Check program]------")


