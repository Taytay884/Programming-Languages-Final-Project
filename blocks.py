class tokens_consts:
    if_token = 'if'
    while_token = 'while'

def is_block_start(line):
    tokens = line.split()
    first_token = tokens[0]
    return first_token == tokens_consts.if_token or first_token == tokens_consts.while_token

def find_block_end(block):
    block_start_token = get_block_start_token(block)
    end_token = "end_" + block_start_token  # end_if or end_while
    counter = 0
    for index, line in enumerate(block):
        start_token = line.split()[0]
        if start_token == end_token:
            counter = counter - 1
            if counter == 0:
                return index
        if start_token == block_start_token:
            counter = counter + 1

    return -1


def is_while_block(block):
    block_start_token = get_block_start_token(block)
    return block_start_token == tokens_consts.while_token

def get_block_start_token(block):
    return block[0].split()[0]