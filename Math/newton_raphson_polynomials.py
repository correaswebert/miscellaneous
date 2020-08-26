def createPoly():
    """Create a polynomial by accepting numerical user input"""
    poly = []
    print("Enter 'q' to terminate.")
    
    i = 0
    while True:
        coeff = input(f"Coefficient of x^{i}: ")
        if coeff == 'q': break
        try:
            # in case user enters non-integer
            poly.append(int(coeff))
            i += 1
        except ValueError:
            pass
        
    return poly


def printPolynomial(poly, coeff_precision=3):
    poly_string = ""
    ndigits = coeff_precision
    degree = len(poly)

    # coeff of poly ... used for cases below
    c0, c1 = False, False
    if poly[0] is not 0:
        c0 = True
    if poly[1] is not 0:
        c1 = True
    
    # don't print something like ... 1 + 0*x  or  0 + 3*x
    if c0 is True and not c1:
        poly_string += f"[{round(poly[0], ndigits)}]"
    elif c1 is True and not c0:
        poly_string += f"[{round(poly[1], ndigits)} * x]"  
    else:
        poly_string += f"[{round(poly[0], ndigits)}]  + \
                         [{round(poly[1], ndigits)} * x]"
    
    for i in range(2,degree):
        coeff = round(poly[i], ndigits)
        if coeff != 0:
            poly_string += f"  +  [{coeff} * (x ^ {i})]"
    
    print(poly_string)
    
    
# currently func is a polynomial
def valueOfPolyAt(func, x ):
    val = 0
    degree = len(func)
    for i in range(degree):
        val += func[i] * (x**i)
    return val


'''
Only polynomials currently...  
func -> a0 + a1*x + a2*x^2 + ... + an*x^n
func =  [ a0, a1, a2, ... , an ]
'''
def diff( func, x=None ):
    
    degree = len(func)
    
    '''
    # this is commented because the code alters the
    # original func list instead of making a cpoy
    # and then altering it... so the original func
    # is destroyed, hence the alternative code...
    
    for i in range(degree):
        func[i] *= i
    
    # remove the constant term of 
    # original polynomial
    func.pop(0)
    
    if x is not None:
        val = 0
        for i in range(degree - 1):
            val += func[i] * ( x**i )
        return val
    
    return func
    '''
    
    diff_func = []
    for i in range(degree):
        diff_func.append(func[i] * i)
    
    if x is not None:
        val = 0
        for i in range(1, degree):
            val += diff_func[i] * ( x**(i-1) )
        return val
    
    return [ diff_func[i] for i in range(1,degree) ]
    

def newtonRaphson( poly, x, iterations ):
    '''
    Have to devise a way to find out the x.  
    Taking x as input is still making it 
    semi-automatic...  
    '''
    x1, x2 = x, 0
    
    diff_poly = diff(poly)
    diffValAt = lambda x: valueOfPolyAt(diff_poly,x)
    
    funcValAt = lambda x: valueOfPolyAt( poly, x )
    
    for _ in range(iterations):
        x2 = x1 - ( funcValAt(x1) / diffValAt(x1) )
        x1 = x2
    
    return x2


if __name__ == "__main__":
    
    print("Welcome to Newton-Raphson approximation method")
    print("Currently only for polynomials...\n")
    
    user_poly = createPoly()
    x = int( input("Enter value of x: ") )
    approx = newtonRaphson( user_poly, x, 10 )
    
    print()
    printPolynomial(user_poly)
    print( "The root close to {0} is approximately {1}".format(x, approx) )
    print()

    wait = input("Press ENTER to exit!")
