from math import floor, sqrt



# factors -> the list of prime factors
def prettyFactorsList(factors):
    # the final list of factor ^ power
    factor_list = []

    # to obtain unique factors for finding their powers
    factor_set = set(factors)

    # add (factor, power) tuple to the factor_list
    for num in factor_set:
        factor_list.append( (num, factors.count(num)) )

    print(factor_list)



def prettyPrintFactors(factors):
    # to obtain unique factors for finding their powers
    factor_set = set(factors)

    for num in factor_set:
        print( str(num) + "^" + str(factors.count(num)) + " *" , end=" ")

    # as the sequance ends with ... * , so put a terminating 1
    print(1)


def factorize(n):
    """Base condition is clubbed with return statement as while loop affects it"""
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = int(floor(sqrt(n)))
    d = 1
    q = 2 if n % 2 == 0 else 3
    # another way to write it...
    # q = n % 2 == 0 and 2 or 3

    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return [q] + factorize(n//q) if q <= maxq else [n]


if __name__ == "__main__":
    user_num = int( input("Enter a number: ") )
    prettyPrintFactors( factorize(user_num) )
    prettyFactorsList( factorize(user_num) )

    wait = input("Press ENTER to exit!")
