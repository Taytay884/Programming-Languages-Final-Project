def find_strongest_arithmetic_operator_index(tokens):
    # Dictionary to define the precedence of operators
    precedence = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    # Initialize variables
    strongest_operator_index = -1
    max_precedence = -1

    # Iterate through the tokens
    for i, token in enumerate(tokens):
        if token in precedence:
            # Check if this operator has higher precedence
            if precedence[token] > max_precedence:
                max_precedence = precedence[token]
                strongest_operator_index = i

    return strongest_operator_index
