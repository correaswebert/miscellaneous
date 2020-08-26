"""
K-Map constructor

Give the input table and output vector to construct the K-Map. The input table
can also be auto generated sequentially, e.g., 0000-1111
"""

import math

# TODO: method to group the numbers to form minimal gate requirement
# TODO: method to output the minimal equation (in terms of letters -> A,B,...)

# we can use recursion as the gray code
def grayCodeConstructor(nbits):
    gray_codes = [0]         # 0 is present in all gray codes
    exp2_arr = [2**i for i in range(nbits)]
    num = 0
    for _ in range(2 ** nbits - 1):
        for exp2 in exp2_arr:
            if (num ^ exp2) not in gray_codes:
                num ^= exp2
                gray_codes.append(num)
                break
    return gray_codes

# if input_table to be given...

# max gates in col (if odd no. of gates, put +1 in col)
def kmapConstructor2(input_table, output):
    num_inputs = int(math.log2(len(input_table)))
    num_row_inputs, extra = divmod(num_inputs, 2)
    num_col_inputs = num_row_inputs + extra

    row_indices = grayCodeConstructor(num_row_inputs)
    col_indices = grayCodeConstructor(num_col_inputs)
    kmap = [[0]*(num_inputs + extra) for i in range(num_inputs)]
    
    one_indices = [i for i in range(len(output)) if output[i] == 1]
    for i in one_indices:
        i = bin(i)[2:]                  # remove the 0b from the index
        i = i.zfill(num_inputs)         # pad with zeroes for nbits repr
        i = [bit for bit in i]          # seperate bits into resp cols
        row_index = int(''.join(i[:num_row_inputs]), 2)
        col_index = int(''.join(i[num_row_inputs:]), 2)
        kmap[row_indices.index(row_index)][col_indices.index(col_index)] = 1
    
    for row in kmap: print(row)

# works only for square kmaps
def kmapConstructor(minterms, dcare=[]):
    # get max next power of 2 among both the input lists
    nbits = int(math.ceil(math.log2(max(minterms + dcare))))
    output = []
    for i in range(2**nbits):
        if i in minterms: output.append(1)
        elif i in dcare:  output.append(-1)
        else:             output.append(0)

    num_row_inputs = nbits // 2
    num_col_inputs = sum(divmod(nbits, 2))  # nbits//2 + (1 if nbits odd else 0)

    row_indices = grayCodeConstructor(num_row_inputs)
    col_indices = grayCodeConstructor(num_col_inputs)
    kmap = [[0]*(2**num_col_inputs) for i in range(2**num_row_inputs)]

    for i in range(2**nbits):
        if output[i] == 1:
            i_bin = bin(i)[2:].zfill(nbits)    # remove 0b part and lpad with 0s
            row = row_indices.index(int(i_bin[:num_row_inputs],2))
            col = col_indices.index(int(i_bin[num_row_inputs:],2))
            kmap[row][col] = 1
        if output[i] == -1:
            i_bin = bin(i)[2:].zfill(nbits)    # remove 0b part and lpad with 0s
            row = row_indices.index(int(i_bin[:num_row_inputs],2))
            col = col_indices.index(int(i_bin[num_row_inputs:],2))
            kmap[row][col] = 'X'
    
    return kmap

def extractGatesFromKmap(*args):
    pass

def representGrayCode(nbits):
    for code in grayCodeConstructor(nbits):
        code = bin(code)[2:]        # remove 0b from output str
        code = code.zfill(nbits)    # lpad with zeroes for uniformity
        print(code)
# representGrayCode(3)

def binaryTableConstructor(nbits):
    table = []
    for num in range(2 ** nbits):
        num = bin(num)[2:]                  # remove the 0b from the output
        num = num.zfill(nbits)              # lpad with zeroes for nbits repr
        num = [bit for bit in num]          # seperate bits into resp cols
        table.append(num)
    return table

def printKmap(kmap):
    ncols = len(kmap[0])

    print('+' + ('-'*(4*ncols))[1:])
    for row in kmap:
        print('|', end='')
        for elem in row:
            print(f" {elem}  ", end='')
        print("\n")

if __name__ == "__main__":
    minterms = [1,7]
    dcare = [6, 3]
    kmap = kmapConstructor(minterms, dcare)
    printKmap(kmap)