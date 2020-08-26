from math import sqrt

def isPrime(num):
	
	if num == 2:
		return True
	
        # step = 2, as even numbers non prime
        # limit sqrt of num as no factors later

	for i in range(3, int(sqrt(num)), 2):
		if num % i == 0:
			return False
	return True
	
if __name__ == "__main__":	
        try:
                user_num = int( input( "Enter a positive integer: ") )
		
                if user_num < 0: raise ValueError
		
                print('Prime' if isPrime(user_num) else 'Not prime')
		
        except ValueError:
                print("Not a positive integer!")

        wait = input("\nPress ENTER to exit")
