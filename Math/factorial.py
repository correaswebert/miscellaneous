def factorial(num):
    
    if not (isinstance(num,int) and num > 0):
        raise Exception("Number must be a positive integer!")

    fact = 1
    for i in range(1, num+1):
        fact *= i
                
    return fact


user_num = int( input("Enter a number: ") )
print( str(user_num) + "! = " + str(factorial(user_num)) )

wait = input("Press ENTER to exit!")
