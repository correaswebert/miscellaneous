# nth Polygonal number

# (no. of sides) * [(no. of sides) - 1] * [(term no.) - 2]
# ________________________________________________________  +  (no. of sides)
#                            2


def polyNumber(sides=None, term=None):
    if sides == None and term == None:
        sides = int(input("Enter number of sides of polygon: "))
        term = int(input("Enter the nth term number: "))

    ans = ( (sides-1) * (term-2) * sides / 2 ) + sides
    return ans

# sum of two consecutive Tri nos. is Sqr no.
def check():
    num = int(input("Enter a number: "))
    m = int(P(3, num))
    n = int(P(3, num-1))

    print(a**2,'=',m,'+',n)

if "name" == "__main__" :
		polyNumber()
		wait = input("Press ENTER to exit!")
