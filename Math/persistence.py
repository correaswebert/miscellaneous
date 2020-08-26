"""Calculate the Additive/Multiplicative persistence of a number

Additive persistence is the number of times the digits of the number should be
added so that the final result is a single digit. For example,
139 -> 1+3+9 = 13 -> 1+3 = 4 ... 139 has additive persistence of 2

Multiplicative persistence is similar to additive persistence, just that
we have to replace the addition operation with multiplication. For example,
39 -> 3*9 = 27 -> 2*7 = 14 -> 1*4 = 4 ... 39 has multiplicative persistence of 3
"""

def additivePersistence(num):
    """Returns int, assumes +int passed as args"""
    if num < 10:
        print(num)
        return 0
    print(num, "->", end=' ')
    
    temp = 0
    while num != 0:
        temp += num % 10
        num //= 10
    
    return 1 + additivePersistence(temp)

def multiplicativePersistence(num):
    """Returns int, assumes +int passed as args"""
    if num < 10:
        print(num)
        return 0
    print(num, "->", end=' ')
    
    temp = 1
    while num != 0:
        temp *= num % 10
        num //= 10
    
    return 1 + multiplicativePersistence(temp)
    

if __name__ == "__main__":
    user_num = int(input("Enter number: "))
    print()

    print("Additive persistence")
    ap = additivePersistence(user_num)
    print(ap)
    print()

    print("Multiplicative persistence")
    mp = multiplicativePersistence(user_num)
    print(mp)

    # least numbers with Mult. Per. from 1-9
    # (10, 1), (25, 2), (39, 3), (77, 4),
    # (679, 5), (6788, 6), (68889, 7), (2677889, 8), (26888999, 9)
