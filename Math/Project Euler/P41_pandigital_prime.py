from itertools import permutations
from math import sqrt

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False 
    # step = 2, as even numbers non prime
    # limit sqrt of num as no factors later
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def pandigitalPrimes():
    # returns a list of permuts of the given list
    lst4 = list(permutations(range(1,5)))   # digits 1 thru 4
    lst7 = list(permutations(range(1,8)))   # digits 1 thru 7

    # converts the given tuple (ordered fashion) into number
    # eg. numify -> (1,2,3) returns 123
    # (1,2,3) is returned from permutations object
    def numify(tup):
        number = 0
        for digit in tup:
            number = number * 10 + digit
        return number
    
    pandigPrimes = []
    for item in lst4 + lst7:
        num = numify(item)
        if isPrime(num):
            pandigPrimes.append(num)
    
    # for i in pandigPrimes: print(i,)
    print(pandigPrimes)

pandigitalPrimes()
wait = input()
