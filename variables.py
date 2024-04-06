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
    # Dictionary to define the precedence of operators
    if first_token in variables and second_token == '=':
        return True
    return False


def place_variables(tokens):
    for i, token in enumerate(tokens):
        if token in variables:
            tokens[i] = variables[token]


