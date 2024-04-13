from error import *
from validation import is_comparison_operation

# Our data memory.
variables = {
    'v0': 0,
    'v1': 0,
    'v2': 0,
    'v3': 0,
    'v4': 0,
    'v5': 0,
    'v6': 0,
    'v7': 0,
    'v8': 0,
    'v9': 0
}


def is_variable_placement(tokens):
    first_token = tokens[0]
    second_token = tokens[1]

    if second_token == '=':
        if first_token in variables:
            if is_comparison_operation(tokens[2:]):
                raise CustomError("Variable placement cannot be boolean")
            return True
        else:
            raise CustomError("Variables are: v0, v1, v2, ... v9")
    return False


def place_variables(tokens):
    for i, token in enumerate(tokens):
        if token in variables:
            tokens[i] = str(variables[token])
        elif token[0] == 'v':
            raise CustomError("Variables are: v0, v1, v2, ... v9")


def reset_variables(variables_dict):
    for var in variables_dict:
        variables_dict[var] = 0
