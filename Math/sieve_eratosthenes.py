def sieve(lim):
	num_list = [1] * (lim+1)
	num_list[0] = num_list[1] = 0

	for n in range(2,lim//2 + 1):
		if num_list[n] == 1:
			for elem in range(n*n, lim+1, n):
				num_list[elem] = 0

	primes = []
	for i, prime in enumerate(num_list):
		if prime == 1:
			primes.append(i)
	print(primes)

sieve(101)

wait = input()
# http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
# https://rosettacode.org/wiki/Sieve_of_Eratosthenes
