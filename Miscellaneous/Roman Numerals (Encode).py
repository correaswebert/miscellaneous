"""
Convert given number to its roman numeral representation
Source for question and commmented code is shown below
http://rosettacode.org/wiki/Roman_numerals/Encode
"""

# def conv(unit, s1, s2, s3, s4):

# 	string = ''
# 	temp = (num // unit) % 10
	
# 	while 0 < temp:
# 		if temp == 9:
# 			string += s4
# 			break
# 		elif temp < 4:
# 			for _ in range(temp):
# 				string += s1
# 				temp -= 1
# 		elif temp == 4:
# 			string += s2
# 			break
# 		else:
# 			string += s3
# 			temp -= 5
		
# 	return string
			
# def toRoman(num):
# 	if num > 4999:
# 		return "Overflow!"
# 	ans = ''
	
# 	# convert thousands place
# 	temp = num // 1000
# 	for _ in range(temp): ans += 'M'
	
# 	ans += conv(100, 'C', 'CD', 'D', 'CM')	# convert hundreds place
# 	ans += conv(10,  'X', 'XL', 'L', 'XC')	# convert tens place
# 	ans += conv(1,   'I', 'IV', 'V', 'IX')	# convert ones place
			
# 	return ans
	
# num = int(input("Enter a number>>> "))
# print(f"Roman numeral for it is {toRoman(num)}")

roman =        "MDCLXVmdclxvi" 	# UPPERCASE for thousands
adjust_roman = "CCXXmmccxxii"	# for adding the roman prefixes
arabic =        (1_000_000, 500_000, 100_000, 50_000, 10_000, 5000, 1000, 500, 100, 50, 10, 5, 1)
adjust_arabic = (100_000, 100_000,  10_000, 10_000,  1000, 1000,  100, 100,  10, 10,  1, 1, 0)

def arabic_to_roman(dclxvi):
    '''Convert an integer from the decimal notation to the Roman notation'''
    org = dclxvi 	# original number, user input
    out = ""		# roman numeral output
    for scale, arabic_scale  in enumerate(arabic):
        if org == 0: break		# if original number is reduced to zero, stop
        multiples = org // arabic_scale
        org -= arabic_scale * multiples		# sub arabic value from original
        out += roman[scale] * multiples		# add arabic char to output
		# if original is greater than 40, 90, 400, 900, ...
		# add roman with prefix and also subtract equal amount from the original
        if (org >= -adjust_arabic[scale] + arabic_scale):
            org -= -adjust_arabic[scale] + arabic_scale		# sub that amount
            out +=  adjust_roman[scale]  + roman[scale]		# add char with pre
    return out
 
if __name__ == "__main__": 
    test = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,40,50,60,
			69,70,80,90,99,100,200,300,400,500,600,666,700,800,900,1000,1009,
			1444,1666,1945,1997,1999,2000,2008,2500,3000,4000,4999,5000,6666,
			10000,50000,100000,500000,1000000)
 
    for val in test: 
        print("%8d %s" %(val, arabic_to_roman(val)))