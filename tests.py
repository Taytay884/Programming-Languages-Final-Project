from engine import *
from variables import *

'''
Each variable in this file represents program execution in our language.
These tests are representing edge-cases and limitations of our language.
'''


# Showcase for nested blocks
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

'''
The next tests should result in failure message in order to test our validations mechanism.
'''
should_fail_result = "Should Fail"

invalid_block_structure = \
            "v1 = 0\n" + \
              "if v1 < 3\n" + \
                "v1 = v1 + 1\n" + \
              "end_if\n" + \
              "end_if\n" + \
            "if v1 < 3"

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
arithmetic_operation_illegal_token = "1 <= 2"

boolean_variable_invalid_placement = "v0 = 2 > 1"
boolean_variable_invalid_placement_2 = "v1 = 32 / 8 > 1 * 3 2"


conditional_operation_with_many_condition_tokens = "1 < 2 < 3"
conditional_operation_without_left_side = "< 1"
conditional_operation_without_right_side = "3 <"
conditional_operation_with_invalid_arithmetic = "v1 = 32 / 8 + 1 * 3 2"

program_line_not_enough_tokens = "v0"
not_exists_variables = "v10 = 3 * 52"
program_line_with_invalid_token = "v0 = 53 + a < 52"

# Executes a specific test program, prints the expected result and the actual result.
def run_test(test, expected_result = ""):
    result = ''
    try:
        print(f"Expected Result:    {expected_result}")
        run_program(test)
        result = f"Result:             {variables}"
    except CustomError as e:
        result = f"\nResult:             Test failed because of an error: {e}\n"
    finally:
        print(result)


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
    run_test(not_close_block_test, should_fail_result)
    reset_variables(variables)
    print("------[END - Not close block Check program]------")
    print()

    print("------[START - Invalid Arithmetic Check]------")
    run_test(invalid_arithmetic_operation, should_fail_result)
    reset_variables(variables)
    print("------[END - Invalid Arithmetic Check]------")
    print()

    print("------[START - Boolean variable invalid placement Check]------")
    run_test(boolean_variable_invalid_placement, should_fail_result)
    reset_variables(variables)
    print("------[END - Boolean variable invalid placement Check]------")
    print()

    print("------[START - Boolean variable invalid placement 2 Check]------")
    run_test(boolean_variable_invalid_placement_2, should_fail_result)
    reset_variables(variables)
    print("------[END - Boolean variable invalid placement 2 Check]------")
    print()

    print("------[START - Arithmetic with illegal token Check]------")
    run_test(arithmetic_operation_illegal_token, should_fail_result)
    reset_variables(variables)
    print("------[END - Arithmetic with illegal token Check]------")
    print()

    print("------[START - Conditional operation with many conditions Check]------")
    run_test(conditional_operation_with_many_condition_tokens, should_fail_result)
    reset_variables(variables)
    print("------[END - Conditional operation with many conditions Check]------")
    print()

    print("------[START - Conditional operation without left-side Check]------")
    run_test(conditional_operation_without_left_side, should_fail_result)
    reset_variables(variables)
    print("------[END - Conditional operation without left-side Check]------")
    print()

    print("------[START - Conditional operation without right-side Check]------")
    run_test(conditional_operation_without_right_side, should_fail_result)
    reset_variables(variables)
    print("------[END - Conditional operation without right-side Check]------")
    print()

    print("------[START - Conditional operation with invalid arithmetic Check]------")
    run_test(conditional_operation_with_invalid_arithmetic, should_fail_result)
    reset_variables(variables)
    print("------[END - Conditional operation with invalid arithmetic Check]------")
    print()

    print("------[START - Not enough tokens Check]------")
    run_test(program_line_not_enough_tokens, should_fail_result)
    reset_variables(variables)
    print("------[END - Not enough tokens Check]------")
    print()

    print("------[START - Not existing variable Check]------")
    run_test(not_exists_variables, should_fail_result)
    reset_variables(variables)
    print("------[END - Not existing variable Check]------")
    print()

    print("------[START - Invalid token Check]------")
    run_test(program_line_with_invalid_token, should_fail_result)
    reset_variables(variables)
    print("------[END - Invalid token Check]------")
    print()

    print("------[START - Invalid block structure Check]------")
    run_test(invalid_block_structure, should_fail_result)
    reset_variables(variables)
    print("------[END - Invalid block structure Check]------")
    print()
