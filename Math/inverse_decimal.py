def det(mat):
	val = 0
	size = len(mat)
	if size == 1:
		return mat[size-1][size-1]
		
	else:
		for col_of_mat in range(size):
			sub_mat = [ [ mat[row][col] for col in range(0, size) if col != col_of_mat ] for row in range(1, size)  ]
			
			val += pow(-1, col_of_mat) * mat[0][col_of_mat] * det(sub_mat)
				
	return val	


def cofactor(mat):
	size = len(mat)
	
	cofact_mat = []
	
	for row in range(size):
		row_of_cofact = []
		for col in range(size):
			arr = [ [ mat[i][j] for j in range(size) if j != col ] for i in range(size)if i != row ]
		
			row_of_cofact.append( pow(-1, row+col+2) * det(arr) )
			
		cofact_mat.append( row_of_cofact )
				
	return cofact_mat
	

def inverse(mat):
	cofact_mat = cofactor(mat)
	deter = det(mat)
	
	size = len(mat)
	inv = [ [ (1/deter) * cofact_mat[j][i] for j in range(size) ] for i in range(size) ]
	
	return inv
	
	
def print_mat(mat):
	size = len(mat)
	precision = 5
	for i in range(size):
		for j in range(size):
			print( round(mat[i][j],precision) , end="   ")
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

matrix = [  [2,-3,1,9],
			[1,1,-1,6],
			[0,-5,3,8],
			[2,0,1,-2]   ]
print_mat( inverse(matrix) )
