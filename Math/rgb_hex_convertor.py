#RGB-to-Hex & Hex-to-RGB

# the main functions
def to_hex(r, g, b):
    # converts decimal to Hex
    r = str(hex(int(r))).upper()[2:]
    if len(r) < 2:
        r = '0' + r

    g = str(hex(int(g))).upper()[2:]
    if len(g) < 2:
        g = '0' + g

    b = str(hex(int(b))).upper()[2:]
    if len(b) < 2:
        b = '0' + b

    # the final Hex value
    return ('#' + r + g + b)


def to_rgb(val):
    # ignore the "#"
    val = val[1:]

    r = int(val[:2] , 16)
    g = int(val[2:4] ,16)
    b = int(val[4:] , 16)
    return r, g, b

###############################################################################

def inp():
    ask = input("For RGB-to-Hex press 'r'\n \
                For Hex-to-RGB press 'h'\n>").lower()

    while (ask != 'r' and ask != 'h'):
        ask = input("Enter valid input!\n>").lower()

# outputs

def out():
    if ask == 'r':
        r = input("Enter value of red: ")
        g = input("Enter value of green: ")
        b = input("Enter value of blue: ")
        print(to_hex(r,g,b))

    else:
        val = input("Enter hexadecimal value: ")

        while (0 <= len(val) < 7) or '#' not in val:
            try:
                val = input("Please enter a correct hexadecimal value: ")
            except ValueError:
                print("Your value is not hexadecimal!")

        print(to_rgb(val))

###############################################################################

if __name__ == '__main__':
    inp()
    out()
