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

not_close_block_test = \
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
                "end_while\n" + \
                "v3 = 0\n" + \
                "while v3 < 5\n" + \
                    "v3 = v3 + 1\n" + \
                "end_while\n" + \
              "end_while"


invalid_arithmetic_operation = "3 + 1 + 2 2"
arithmetic_operation_with_bool = "v0 = 2 > 1\n" + \
                                      "v1 = v0 * 3"
arithmetic_operation_illegal_token = "1 <= 2"

conditional_operation_with_many_condition_tokens = "1 < 2 < 3"
conditional_operation_without_left_side = "< 1"
conditional_operation_without_right_side = "3 <"
conditional_operation_with_invalid_arithmetic = "v0 = 2 > 1\n" + \
                                                "v1 = 32 / 8 > v0 * 3"

program_line_not_enough_tokens = "v0"
not_exists_variables = "v10 = 3 * 52"
program_line_with_invalid_token = "v0 = 53 + a < 52"


def run_test(test, expected_result = ""):
    try:
        run_program(test)
        print(f"Expected Result:    {expected_result}")
        print(f"Result:             {variables}")
    except CustomError as e:
        print(f"\nTest failed because of an error: {e}\n")


if __name__ == '__main__':
    print("------[START - Many while and ifs program]------")
    run_test(many_while_and_ifs_program, many_while_and_ifs_program_result)
    reset_variables(variables)
    print("------[END - Many while and ifs program]------")
    print()

    print("------[START - Factorial calculator program]------")
    program = factorial_program
    run_test(factorial_program, factorial_program_result)
    reset_variables(variables)
    print("------[END - Factorial calculator program]------")
    print()

    print("------[START - Sum of squares program]------")
    run_test(sum_of_squares, sum_of_squares_result)
    reset_variables(variables)
    print("------[END - Sum of squares program]------")
    print()

    print("------[START - Power of number program]------")
    run_test(power_of_number, power_of_number_result)
    reset_variables(variables)
    print("------[END - Power of number program]------")
    print()

    print("------[START - Remainder Check]------")
    run_test(remainder_check, remainder_check_result)
    reset_variables(variables)
    print("------[END - Remainder Check program]------")
    print()

    print("------[START - Not close block Check]------")
    run_test(not_close_block_test)
    reset_variables(variables)
    print("------[END - Not close block Check program]------")
    print()

    print("------[START - Invalid Arithmetic Check]------")
    run_test(invalid_arithmetic_operation)
    reset_variables(variables)
    print("------[END - Invalid Arithmetic Check]------")
    print()

    print("------[START - Arithmetic with booleans Check]------")
    run_test(arithmetic_operation_with_bool)
    reset_variables(variables)
    print("------[END - Arithmetic with booleans Check]------")
    print()

    print("------[START - Arithmetic with illegal token Check]------")
    run_test(arithmetic_operation_illegal_token)
    reset_variables(variables)
    print("------[END - Arithmetic with illegal token Check]------")
    print()

    print("------[START - Conditional operation with many conditions Check]------")
    run_test(conditional_operation_with_many_condition_tokens)
    reset_variables(variables)
    print("------[END - Conditional operation with many conditions Check]------")
    print()

    print("------[START - Conditional operation without left-side Check]------")
    run_test(conditional_operation_without_left_side)
    reset_variables(variables)
    print("------[END - Conditional operation without left-side Check]------")
    print()

    print("------[START - Conditional operation without right-side Check]------")
    run_test(conditional_operation_without_right_side)
    reset_variables(variables)
    print("------[END - Conditional operation without right-side Check]------")
    print()

    print("------[START - Conditional operation with invalid arithmetic Check]------")
    run_test(conditional_operation_with_invalid_arithmetic)
    reset_variables(variables)
    print("------[END - Conditional operation with invalid arithmetic Check]------")
    print()

    print("------[START - Not enough tokens Check]------")
    run_test(program_line_not_enough_tokens)
    reset_variables(variables)
    print("------[END - Not enough tokens Check]------")
    print()

    print("------[START - Not existing variable Check]------")
    run_test(not_exists_variables)
    reset_variables(variables)
    print("------[END - Not existing variable Check]------")
    print()

    print("------[START - Invalid token Check]------")
    run_test(program_line_with_invalid_token)
    reset_variables(variables)
    print("------[END - Invalid token Check]------")
    print()