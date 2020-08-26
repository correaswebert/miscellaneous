def conv(num, unit, s1, s2, s3, s4):

	string = ''
	# works even if num not an arg... why???
	temp = (num // unit) % 10
	
	while temp > 0:
		if temp == 9:
			string += s4
			break
		elif temp < 4:
			for i in range(temp):
				string += s1
				temp -= 1
		elif temp == 4:
			string += s2
			break
		else:
			string += s3
			temp -= 5
		
	return string
			
def toRoman(num):
	
	# cannot encode greater than 5000
	if num > 4999:
		return "Overflow!"
		
	ans = ''
	
	temp = num // 1000
	for i in range(temp): 
		ans += 'M'
	
	ans += conv(num, 100, 'C', 'CD', 'D', 'CM')
	ans += conv(num, 10,  'X', 'XL', 'L', 'XC')
	ans += conv(num, 1,   'I', 'IV', 'V', 'IX')
			
	return ans
	
num = int(input("Enter a number to encode: "))
print(toRoman(num))

# for i in range(100):
#	 print(toRoman(i))