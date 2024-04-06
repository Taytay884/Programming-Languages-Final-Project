import arithmetic
import conditional
from variables import *
import re

arithmetic_order = ['*', '/', '+', '-']


def is_valid_program(program):
    # Define regular expressions for the grammar rules
    negative_number_pattern = r"-[1-9][0-9]*"
    number_pattern = r"0|[1-9][0-9]*"
    arithmetic_pattern = r"[\+\-\*/]"
    conditional_pattern = r"[<>]|=="

    # Combine all patterns
    full_pattern = re.compile(
        rf"({negative_number_pattern})|({number_pattern})|({arithmetic_pattern})|({conditional_pattern})"
    )

    # Check if every token in the program matches the pattern
    tokens = program.split()
    for token in tokens:
        if not full_pattern.fullmatch(token):
            return False

    return True


def evaluate_expression(expr):
    return eval(expr.replace('/', '//'))

def arithmetic_operation(tokens):
    print(tokens)
    while len(tokens) > 1:
        operator_index = arithmetic.find_strongest_arithmetic_operator_index(tokens)
        prev_token = tokens[operator_index - 1]
        next_token = tokens[operator_index + 1]
        result = evaluate_expression(f"{prev_token} {tokens[operator_index]} {next_token}")
        tokens[operator_index - 1] = result
        tokens.pop(operator_index)
        tokens.pop(operator_index)
        print(tokens)
    print(tokens[0])
    return tokens[0]


def run_program_operation(tokens):
    comparison_operation_index = conditional.find_comparison_operator_index(tokens)
    if comparison_operation_index != -1:
        left_side_tokens = tokens[:comparison_operation_index]
        left_side_result = arithmetic_operation(left_side_tokens)
        right_side_tokens = tokens[comparison_operation_index + 1:]
        right_side_result = arithmetic_operation(right_side_tokens)
        comparison_result = evaluate_expression(f"{left_side_result} {tokens[comparison_operation_index]} {right_side_result}")
        return comparison_result
    else:
        return arithmetic_operation(tokens)

def run_program_line(line):
    tokens = line.split()

    if is_variable_placement(tokens):
        # ['v0', '=', '25', '*', '8', '<', '10']
        # variable_token = v0
        # tokens = ['25', '*', '8', '<', '10']
        variable_token = tokens[0]
        tokens = tokens[2:]
        place_variables(tokens)
        operation_result = run_program_operation(tokens)
        variables[variable_token] = operation_result  # variable = operation_result
    else:
        place_variables(tokens)
        return run_program_operation(tokens)

def run_program_block(program):
    lines = program.split('\n')
    for line in lines:
        run_program_line(line)


if __name__ == '__main__':
    program = "v0 = -10 + 20 + v5 * 10 / 5 > v7\n" + "v1 = 3"
    run_program_block(program)
    print(variables)
