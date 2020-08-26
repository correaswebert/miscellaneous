def gcd(num_list=[], *args):
    if not num_list:
        args = num_list

    number_of_nums = len(args)
    g = args[0]     # random assignment of GCD
	
    for i in range(number_of_nums-1):
        a = args[i]
        b = args[i+1]
		
        # Euclid's method
        while b != 0:
            temp = b
            b = a % b
            a = temp
			
        # as gcd is checked pair-wise,
        # inter-pair checking not done
        # but gcd is smallest found, if any
        if (g > a): g = a
		
        return g
	
if __name__ == "__main__":
        print(gcd(13,169,12))

        wait = input("\nPress ENTER to exit")
