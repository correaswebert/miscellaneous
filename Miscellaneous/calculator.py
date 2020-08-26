def unspace(r_str):
    u_str = ''
    for char in r_str:
        if char != ' ': u_str += char
    return u_str


# u_str is return value of unspace
def tree(u_str):
    # check if string contains only numbers; no operators
    try:
        return int(u_str)
    except:
        None
    
    for oper in ['+', '-', '*', '/', '^']:
        pos = u_str.find(oper)
        if pos > 0:
            l_str, r_str = u_str.split(oper, maxsplit=1)
            return [tree(l_str), oper, tree(r_str)]

# print( tree(unspace( "1 + 2 / 3 * 4 - 5" )) )
# output: [1, '+', [[[2, '/', 3], '*', 4], '-', 5]]


# parsed is return value of tree
def calculate(parsed):
    lexpr = parsed[0]
    rexpr = parsed[2]
    oper = parsed[1]

    while type(lexpr) == list:
        lexpr = calculate(lexpr)
    while type(rexpr) == list:
        rexpr = calculate(rexpr)
        
    # finally calculate result
    if oper == "+":
        return lexpr + rexpr
    if oper == "-":
        return lexpr - rexpr
    if oper == "*":
        return lexpr * rexpr
    if oper == "/":
        return lexpr / rexpr
    if oper == "^":
        return lexpr ** rexpr

def evaluate(expression):
    return calculate(tree(unspace(expression)))

"""Process
> (1 + 2 / (4 - 2)) * 3 - 4
    > 1 + 2 / (4 - 2)) * 3 - 4
        > 4 - 2)) * 3 - 4
        < 2
    > 1 + 2 / 2) * 3 - 4
    < 2
> 2 * 3 - 4
"""

"""what's happening
1
1
1 +
1 +
1 + 2
1 + 2
1 + 2 /
1 + 2 /

4
4
4 -
4 -
4 - 2
1 + 2 / 2
1 + 2 / 24
1 + 2 / 24
1 + 2 / 24 -
1 + 2 / 24 -
1 + 2 / 24 - 2
-0.9166666666666667
-0.91666666666666671
-0.91666666666666671
-0.91666666666666671 +
-0.91666666666666671 +
-0.91666666666666671 + 2
-0.91666666666666671 + 2
...
"""

'''
# assumes properly syntaxed expression given
def debracket(expr):
    temp = ''
    for i,char in enumerate(expr):
        print(temp)
        if char == '(':
            # exclude current char '('
            temp += debracket(expr[i+1:])
        elif char == ')':
            return str(calculate(tree(unspace(temp))))
        else:
            temp += char
    return temp
'''

def debracket(expr):
    i = 0
    size = len(expr)
    buffer = []

    while i < size:
        print(expr)
        char = expr[i]
        if char == '(':
            buffer.append(i)
        if char == ')':
            prev_loc = buffer.pop()
            expr[prev_loc : i] = evaluate(expr[prev_loc : i])
            size = len(expr)
            i = prev_loc
        i += 1

expression = '(1 + 2 / (4 - 2)) * 3 - 4'
print(debracket(expression))

# 2 ^ 4 * 4 - 3 * 4 * 5 = 4
def equalTo():
    expression = '2 ^ 4 * 4 - 3 * 4 * 5' #input("Enter expression: ")
    exp_ls = tree(unspace(expression))
    result = round(calculate(exp_ls), 10)
    print(result)

# equalTo()