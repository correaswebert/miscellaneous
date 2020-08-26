# det function calculates determinant of matrix
# takes one argument: matrix
# gives output value
from determinant import det

# operates on fractions with given operator
# takes 3 args: frac1, oper, frac2
# frac1(2) is a list -> [num, den]
# oper is a char -> '+','-','*','/'
from ratio import fracOp


def cofactor(matrix):
	size = len(matrix)
	
	cofactor_mat = []
	
	for row in range(size):
		row_of_cofact = []
		for col in range(size):
			arr = [ [ matrix[i][j] for j in range(size) if j != col ] for i in range(size) if i != row ]
		
			row_of_cofact.append( pow(-1, row+col+2) * det(arr) )
			
		cofactor_mat.append( row_of_cofact )
				
	return cofactor_mat
	

def inverse(mat):
	
	size = len(mat)
	inv = []
	cofactor_mat = cofactor(mat)
	deter = det(mat)
	
	if deter == 0:
		# raise Exception("Singular matrix!")
		print("Singular matrix, inverse does not exist!")
		return []
		
	if size == 1:
		return [[[ 1, mat[0][0] ]]]
	
	inv = [ [ fracOp( [1,deter], '*', [cofactor_mat[j][i],1] ) for j in range(size) ] for i in range(size) ]
			
	return inv

	
def print_mat(mat):
	size = len(mat)
	precision = 5
	for i in range(size):
		for j in range(size):
			num = mat[i][j][0]
			den = mat[i][j][1]
			if den == 1:
				print( num, end="       " )
			else:
				print( num,'/',den , end="     ")
		print()
		
	''' to properly space matrix elements
	max_ = 1
	precision = 3
	for i in range(size):
		for j in range(size):
			temp = len( int(mat[i][j]) )
			max_ = temp if temp > max_
	# to accomodate sign & precision
	max_ += 1 + precision
	
	for i in range(size):
		for j in range(size):
			temp = len( int(mat[i][j]) )
			for space in range(max_ - temp):
				print(" ", end="")
			print( round(mat[i][j], precision), end=" ")
		print()
	'''

'''
matrix = [  
			[2,-3,1],
			[1,1,-1],
			[2,0,1]   
		 ]
'''
if __name__ == "__main__":
	size = int( input("Enter n for A(nxn): ") )
	matrix = []
	
	for i in range(size):
		row = input("Enter row %d: " % (i+1) ).split(' ')
		matrix.append([ int(elem) for elem in row ])
			
	print()
	print_mat( inverse(matrix) )
	