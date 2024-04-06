import arithmetic
import conditional
from variables import *
from blocks import *

arithmetic_order = ['*', '/', '+', '-']

def evaluate_expression(expr):
    return eval(expr.replace('/', '//'))

def arithmetic_operation(tokens):
    while len(tokens) > 1:
        operator_index = arithmetic.find_strongest_arithmetic_operator_index(tokens)
        prev_token = tokens[operator_index - 1]
        next_token = tokens[operator_index + 1]
        result = evaluate_expression(f"{prev_token} {tokens[operator_index]} {next_token}")
        tokens[operator_index - 1] = result
        tokens.pop(operator_index)
        tokens.pop(operator_index)
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


def run_program_block(block):
    block_start_line = block[0]
    block_end_index = find_block_end(block)
    tokens = block_start_line.split()
    condition_as_line = ' '.join(tokens[1:])

    is_block_conditions_met = run_program_line(condition_as_line)
    if not is_block_conditions_met:
        return block_end_index

    # block conditions met
    block_current_index = 1
    while block_current_index < block_end_index:
        line = block[block_current_index]
        if is_block_start(line):
            block = block[block_current_index:]
            block_end_line_index = run_program_block(block)  # block_end_line_index is the line index of the block
            block_current_index = block_current_index + block_end_line_index + 1
        else:
            run_program_line(line)
            block_current_index = block_current_index + 1

    return block_end_index


def run_program(program_as_string):
    lines = program_as_string.split('\n')
    program_length = len(lines)
    program_counter = 0
    while program_counter < program_length:
        line = lines[program_counter]
        if is_block_start(line):
            block = lines[program_counter:]
            block_end_line_index = run_program_block(block)  # block_end_line_index is the line index of the block
            program_counter = program_counter + block_end_line_index + 1
        else:
            run_program_line(line)
            program_counter = program_counter + 1


if __name__ == '__main__':
    program = "v0 = -10 + 20 + v5 * 10 / 5 > v7\n" + \
              "v1 = 3\n" + \
              "if v1 < 4\n" + \
                "v1 = 99\n" + \
                "if v1 < 50\n" + \
                    "v1 = 200\n" + \
                "end_if\n" +\
              "end_if"
    run_program(program)
    print(variables)
