def is_block_start(line):
    tokens = line.split()
    first_token = tokens[0]
    return first_token == 'if' or first_token == 'while'

def find_block_end(block):
    block_start_line = block[0]
    block_start_token = block_start_line.split()[0]
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
    block_start_line = block[0]
    block_start_token = block_start_line.split()[0]
    return block_start_token == 'while'

