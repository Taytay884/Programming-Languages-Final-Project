import re

import blocks
from error import *

# Define regular expressions for each BNF rule
if_statement_pattern = 'if'
end_if_statement_pattern = 'end_if'
while_statement_pattern = 'while'
end_while_statement_pattern = 'end_while'
variable_pattern = 'v[0-9]'
equals_pattern = '='
condition_pattern = '(<|>|==)'
arithmetic_pattern = '(\+|-|\*|/)'  # Escape the arithmetic symbols
number_pattern = '-?[0-9]+'

# Combine all patterns into a dictionary
patterns = {
    '<if statement>': if_statement_pattern,
    '<end-if-statement>': end_if_statement_pattern,
    '<while statement>': while_statement_pattern,
    '<end-while-statement>': end_while_statement_pattern,
    '<variable>': variable_pattern,
    '=': equals_pattern,
    '<condition>': condition_pattern,
    '<arithmetic>': arithmetic_pattern,
    '<number>': number_pattern,
}

arithmetic_operation_pattern = (
    fr'^('
    fr'({number_pattern}|{variable_pattern})'  # First token: number or variable
    fr'\s({arithmetic_pattern})\s'  # Second token: arithmetic
    fr'({number_pattern}|{variable_pattern})'  # Third token: number or variable
    fr'(\s({arithmetic_pattern})\s({number_pattern}|{variable_pattern}))*'  # Additional pairs of <arithmetic> <number/variable>
    fr')$'
)

def validate_token(token):
    valid_token_pattern = re.compile('|'.join(patterns.values()))
    # Check if the token matches any BNF rule
    return valid_token_pattern.match(token)


def validate_arithmetic_operation(tokens):
    line = ' '.join(tokens)
    if not (re.match(arithmetic_operation_pattern, line) or re.match(f"^{number_pattern}$|^{variable_pattern}$", line)):
        raise CustomError(f"'{line}' is an invalid arithmetic operation")

def validate_comparison_operation(tokens):
    line = ' '.join(tokens)
    conditions = re.compile(condition_pattern).findall(line)
    if len(conditions) > 1:
        raise CustomError(f"'{line}' has more than 1 condition")


def validate_program_line(tokens):
    if len(tokens) < 2:
        raise CustomError(f"'{' '.join(tokens)}' is an invalid program line,"
                          f" program line length should have at least 2 tokens")
    for token in tokens:
        if not validate_token(token):
            raise CustomError(f"{token} is an invalid token")


def validate_program_block(block):
    if blocks.find_block_end(block) == -1:
        raise CustomError("Missing block end")
