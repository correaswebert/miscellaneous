"""
# newtonRaphson returns root of equation
# near to a specified number, x (arg)
# to find sqrt we give equation
# x^2 - (num) = 0
# and iterations are set to 100

# x is set to num/2 as sqrt is smaller than it
# so it will waste lesser iterations

# for fractions it still works fast and
# accurate enough as the answer lies in [0,1]
from newton_raphson import newtonRaphson

# exp means n-th root exponent
def naturalExp(base, exp):
	poly = [0]*(exp+1)
	poly[0]   = -base
	poly[exp] = 1
	
	x = base/exp
	
	if exp % 2 == 0 and base < 0:
		return None
		
	return newtonRaphson( poly, x, 10000 )
"""

# uses Newton-Raphson method to find the answer
# for real base & exponent
def realExp( base, exp ):
	func = lambda x: x**exp - base
	diff = lambda x: exp * x**(exp-1)
	
	x = base / exp;
	
	for i in range(10000):
		x -= func(x) / diff(x)
	
	return x
	
if __name__ == "__main__":
	user_num  = float( input("Enter a number: ") )
	user_root = float( input("Enter n for n-th root: ") )
	
	root = realExp(user_num, user_root)
	
	print("\n"*7)
	if root is not None:
		print(f"({user_num})^(1/{user_root}) = {root}")
	else:
		print("Complex number answer!")