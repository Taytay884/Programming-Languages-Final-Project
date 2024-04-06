import arithmetic
import conditional
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


def run_program(program):
    print(program)
    result = evaluate_expression(f"{program}")
    print(f"{result}")
    tokens = program.split()

    # Function to evaluate arithmetic expressions
    def evaluate_expression(expr):
        return eval(expr.replace('/', '//'))

    # Initialize variables
    current_number = None
    current_operator = None

    # Iterate through tokens
    for token in tokens:
        if token.startswith('-') and token[1:].isdigit():
            # Handle negative numbers
            current_number = int(token)
        elif token.isdigit():
            # Handle positive numbers
            current_number = int(token)
        elif token in ['+', '-', '*', '/']:
            # Handle arithmetic operators
            current_operator = token
        elif token in ['<', '>', '==']:
            # Handle conditionals
            if current_number is not None and current_operator is not None:
                next_token = tokens[tokens.index(token) + 1]
                if next_token.isdigit() or (next_token.startswith('-') and next_token[1:].isdigit()):
                    result = evaluate_expression(f"{current_number} {current_operator} {next_token}")
                    print(f"Conditional {current_number} {current_operator} {next_token} is {result}")
                else:
                    print(f"Invalid operand after conditional '{token}'")
            else:
                print(f"Conditional '{token}' without an operand")
        else:
            print(f"Invalid token '{token}'")

    # Check if any operations were performed
    if current_number is not None:
        print("Final result:", current_number)


def run_program_line(line):
    tokens = line.split()
    comparison_operation_index = conditional.find_comparison_operator_index(tokens)

    if comparison_operation_index != -1:
        left_side_tokens = tokens[:comparison_operation_index]
        left_side_result = arithmetic_operation(left_side_tokens)
        right_side_tokens = tokens[comparison_operation_index + 1:]
        right_side_result = arithmetic_operation(right_side_tokens)
        result = evaluate_expression(f"{left_side_result} {tokens[comparison_operation_index]} {right_side_result}")
        return result
    else:
        print(arithmetic_operation(tokens[:comparison_operation_index]))

if __name__ == '__main__':
    program = "-10 + 20 * 10 / 5 == 8 + 9"
    result = run_program_line(program)
    print(result)
