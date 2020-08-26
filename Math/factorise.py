# isPrime takes one arg: num
# returns True or False
from is_prime import isPrime
from factors  import factorsOf
from sieve import sieve

def factorize(num):
	prime_factors = []
	
	factors = factorsOf(num)
	primes  = sieve(num)
	
	for f in factors:
		if f in primes:
		#if isPrime(f):
			pow = 0
			while num % f**pow == 0:
				pow += 1
			
			prime_factors.append( (f, pow-1) )
			
	return prime_factors

def printAsPrimeFactors(p):
	for f in p:
		print( f"{f[0]}^{f[1]} x ", end="" )
	print("1")
	
'''
def factorise(num, divisor=1):
    # no. divides itself
	# start to check from next int
	divisor += 1
	quotient = 0

	while True:
		if isPrime(num):
			return str(num)

		elif num == 1:
			return '1'

		elif (num % divisor == 0):
			power = 0
			while (num % divisor == 0):
				quotient = num // divisor
				num = quotient
				power += 1
			
			print( str(divisor) + "^" + str(power) + " * " + factorise(quotient, divisor) , end="")
			
		divisor += 1
'''

# fails for 2520....
if __name__ == "__main__":
	user_num = int( input("Enter number to factorise: ") )
	printAsPrimeFactors( factorize(user_num) )