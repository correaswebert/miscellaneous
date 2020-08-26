ARABIC = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
ROMAN = (1, 5, 10, 50, 100, 500, 1000)


def subtractable(val1, val2):
    # Don't subtract a letter from another letter more than ten times greater
    try:
        if val2 == 'I' and (val1 == 'V' or val1 == 'X'):
            return True
        elif val2 == 'X' and (val1 == 'L' or val1 == 'C'):
            return True
        elif val2 == 'C' and (val1 == 'D' or val1 == 'M'):
            return True
    # if any values is ''
    except ValueError:
        pass
    return False


def romanToArabic(roman):
    # the final value to be returned
    result = 0
    # stores prev value in case of subtraction ::= XL ~ 40 (50 - 10)
    buffer = ''
    for char in reversed(roman):
        # get roman value corresponding to arabic value
        temp = ARABIC.index(char)
        # if subtraction to be done, do it
        if subtractable(buffer, char):
            result -= ROMAN[temp]
        else:
            result += ROMAN[temp]
        buffer = char
    return result


class ArabicNumber:

    def __init__(self, number):
        self.number = number
        self.arabic = ''
    
        if not isinstance(number, int):
            raise Exception("Roman numbers are integers!")
        elif number <= 0:
            raise Exception("Roman numbers are positive!")
        if number > 4999:
            raise Exception("Can't represent greater than 4999.")

        temp = number // 1000
        for i in range(temp):
            self.arabic += 'M'

        def conv(num, unit, s1, s2, s3, s4):
            string = ''
            temp = (num // unit) % 10

            while temp > 0:
                if temp == 9:
                    string += s4
                    break
                elif temp < 4:
                    for i in range(temp):
                        string += s1
                        temp -= 1
                elif temp == 4:
                    string += s2
                    break
                else:
                    string += s3
                    temp -= 5

            return string

        self.arabic += conv(number, 100, 'C', 'CD', 'D', 'CM')
        self.arabic += conv(number, 10,  'X', 'XL', 'L', 'XC')
        self.arabic += conv(number, 1,   'I', 'IV', 'V', 'IX')

    def __str__(self):
        return self.arabic
    
    def __add__(self, other):
        return self.number + other.number
    
    def __sub__(self, other):
        return self.number - other.number
    
    def __mul__(self, other):
        return self.number * other.number
    
    def __div__(self, other):
        return self.number // other.number



if __name__ == "__main__":
    '''
    tests = {
        1: 'I',
        4: 'IV',
        9: 'IX',
        949: 'CMXLIX'
    }
    num_test = len(tests)
    test_passed = 0
    for k, v in tests.items():
        try:
            if romanToArabic(v) == k:
                test_passed += 1
            else:
                print(f"Failed ::= IN - {v.ljust(5)} EXP - {k} OUT - {romanToArabic(v)}")
        except:
            print(f"!!! Error ::=  IN - {v}")
    
    print(f'Passed: {test_passed}   Failed: {num_test - test_passed}')

    user_in = input("Enter Roman numeral: ")
    print(romanToArabic(user_in))
    '''
    a1 = ArabicNumber(9)
    a2 = ArabicNumber(440)
    print(f'{a1} + {a2} = {a1 + a2}')
    print(f'{a1} - {a2} = {a1 - a2}')
    print(f'{a1} * {a2} = {a1 * a2}')
    # print(f'{a1} / {a2} = {a1 / a2}')
    wait = input("Press ENTER to exit!")