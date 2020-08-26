"""
def findGcd(num1, num2):
	while num2 != 0:
		temp = num2
		num2 = num1 % num2
		num1 = temp
	
	return num1
"""
from gcd import gcd as findGcd

# the frac is improper,
# index(0): numerator
# index(1): denominator
def toMixed(frac):
	num, den = frac[0], frac[1]
	
	whole = num // den
	num %= den
	
	return [whole, num, den]


# the fractions, num1 & num2, is non-mixed,
# index(0): numerator
# index(1): denominator
def fracOp(frac1, oper, frac2):
	# set the result to zero
	num, den = 0, 1
	
	if oper == '+':
		num = frac1[0]*frac2[1] + frac1[1]*frac2[0]
		den = frac1[1]*frac2[1]
		
	elif oper == '-':
		num = frac1[0]*frac2[1] - frac1[1]*frac2[0]
		den = frac1[1]*frac2[1]
		
	elif oper == '*':
		num = frac1[0]*frac2[0]
		den = frac1[1]*frac2[1]
		
	elif oper == '/':
		num = frac1[0]*frac2[1]
		den = frac1[1]*frac2[0]
	
	# converts to proper fraction
	gcd = findGcd(num, den)
	if gcd != 1:
		num //= gcd
		den //= gcd	
	
	return [num, den]


def printFrac( frac ):
	
	if len(frac) == 2:
		# -- for non-mixed fraction -- #
		num = frac[0]
		den = frac[1]
		
		if den == 1:
			print(num)
		else:
			print(num, '/', den)
	
	elif len(frac) == 3:
		# -- for mixed fraction -- #
		whole = frac[0]
		num   = frac[1]
		den   = frac[2]
		
		print( whole, '*', '(', num, '/', den, ')' )


if __name__ == "__main__":
	frac1 = input("Enter numerator and denominator (separated by space) for Fraction(1): ").split(" ")
	frac2 = input("Enter numerator and denominator (separated by space) for Fraction(2): ").split(" ")
	
	for i in range(2):
		frac1[i] = int(frac1[i])
		frac2[i] = int(frac2[i])
	
	res  = []
	oper = ['+', '-', '*', '/']
	
	for i in range(4):
		val = fracOp(frac1, oper[i], frac2)
		res.append(val)
	
	print()
	for i in range(4):
		print(f"Operation {oper[i]} : ", end="")
		printFrac(res[i])
	