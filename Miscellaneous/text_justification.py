import random

# BUG: doesn't work for current string with colsize = (10, 20, 30) ... inf loop

# ---------- psuedo-code --------------
# while extra_spaces >= current_spaces:
#     equally_distribute()
# if extra_spaces < current_spaces:
#     randomly_distribute()


def justifyLine(text, colsize=80):
    words = text.split(' ')                 # extract words from the text
    num_spaces = len(words) - 1             # number of spaces
    space_arr = [1] * num_spaces            # space array (justfn. done here)
    extra_spaces = colsize - len(text)      # how many more spaces to add
    current_spaces = num_spaces             # how many spaces present now
    justified_line = ""

    while extra_spaces >= current_spaces:
        for i in range(num_spaces):
            space_arr[i] += 1
            current_spaces += 1
            extra_spaces -= 1

    if extra_spaces < current_spaces:
        while extra_spaces > 0:
            rand_space_index = random.randint(0, num_spaces-1)
            space_arr[rand_space_index] += 1
            extra_spaces -= 1

    space_arr.append(2)                     # in case used for .md, linebreaker
    spaces = [' '*i for i in space_arr]     # render spaces given by space_arr
    for w, sp in zip(words, spaces):
        justified_line += w + sp
    return justified_line


def wrapNjustify(text, colsize=80):
    """Wrap text around the colsize barrier, and justify the lines"""

    # text must end with space or the function does not terminate as it searches
    # for space chars to get EOL and no EOL encountered for end of doc.
    text += ' '
    pointer_loc = 0         # current pointer location
    loc_EOL = colsize       # current line's EOL location
    end_loc = len(text)     # text's end location
    justified_text = ""

    while pointer_loc < end_loc:
        # don't start line with space
        if text[pointer_loc] == ' ':
            pointer_loc += 1
        # get to previous word, if current position is in middle of a word
        while text[loc_EOL] != ' ':
            loc_EOL -= 1
        current_line = text[pointer_loc: loc_EOL]
        justified_text += justifyLine(current_line, colsize) + "\n"
        # print(justifyLine(buffer) + "\n")
        pointer_loc = loc_EOL + 1
        loc_EOL += colsize
        if loc_EOL >= end_loc:
            loc_EOL = end_loc - 1

    return justified_text


if __name__ == "__main__":
    test_string = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'

    try:
        colsize = int(input("Enter max column barrier: "))
    except ValueError:
        colsize = 80

    string = input("Enter the text.\n")
    if string == '':
        string = test_string

    print(wrapNjustify(string, colsize))
    for i in range(colsize):
        print(' ', end='')
    print('|')

# TODO
# consectetur,     from   a  Lorem   Ipsum      # output produced
# consectetur,   from    a   Lorem   Ipsum      # better looking
# random distributor can be further constrained for better output

# BUG
# Enter max column barrier: 20
# Enter the text.
# Swebert is cool.
# Traceback (most recent call last):
#   File "text_justification.py", line 75, in <module>
#     print(wrapNjustify(string, colsize))
#   File "text_justification.py", line 52, in wrapNjustify
#     while text[loc_EOL] != ' ':
# IndexError: string index out of range
