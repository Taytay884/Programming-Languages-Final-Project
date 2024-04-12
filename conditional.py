def find_comparison_operator_index(tokens):
    # Dictionary to define the precedence of operators
    operators = ['<', '>', '==']

    # Iterate through the tokens
    for index, token in enumerate(tokens):
        if token in operators:
            return index

    return -1
