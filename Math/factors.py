def factorsOf(num):
	factors = []
	
	factors.append(1)
	factors.append(num)
	
	i=2
	lim = num
	while i < lim:
		if num % i == 0:
			factors.append(i)
			lim = num // i
			
			if lim == i: break
			
			factors.append(lim)
		
		i += 1
			
	return sorted(factors)


if __name__ == "__main__":
	try:	
		user_num = int( input("Enter a positive integer: ") )
		print( factorsOf(user_num) )
		
	except ValueError:
		print("Not an integer!")