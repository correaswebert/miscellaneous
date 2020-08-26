def ispandigital(num, length=9):
    if not isinstance(num, int):
        return False
    if len(str(num)) != length:
        return False

    # create a length array to represent every digit
    # 0 => not exists; 1 => exists
    # sum = 9  =>  pandigital
    array = [0] * length
    while num:
        index = num % 10 - 1
        array[index] = 1
        num //= 10

    if sum(array) == length:
        return True
    return False


if __name__ == "__main__":

    ##################### TEST CASES for 'ispandigital' #######################
    tests = ((123, False),            # less digits
             (123.0, False),          # not integer
             (123456788, False),      # sum != 9
             (164325798, True))       # pandigital

    fail = 0
    for case in tests:
        if ispandigital(case[0]) != case[1]:
            fail += 1
            print(case)
    print(f"Success rate {round((1 - fail/len(tests)) * 100, 2)}%")


    wait = input("Press ENTER to escape!")
