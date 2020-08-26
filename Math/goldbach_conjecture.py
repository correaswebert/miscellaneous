# Goldbach's Conjecture
# every even number can be expressed
# as sum of two primes


# finds all primes <= lim
from sieve import sieve	
	
# checks for primes satisfying Goldbach's Conj.
def goldy(num):
	primes = sieve(num);
	
	if(num % 2 != 0):
		print("Not even!")
	else:
		for i in primes:
			if num-i in primes:
				print(i,num-i)
				# avoids (5,7) & (7,5) for 12...etc.
				primes.remove(i)
				primes.remove(num-i)
				
goldy(int(input("Enter a number: ")))