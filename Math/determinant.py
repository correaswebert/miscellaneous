def determinant(matrix):
	size = len(matrix)
	if size == 1:
		return matrix[size-1][size-1]
	
	value = 0
	for col_of_matrix in range(size):
		sub_matrix = [ [ matrix[row][col] for col in range(0, size) if col != col_of_matrix ] for row in range(1, size)  ]
		
		value += pow(-1, col_of_matrix) * matrix[0][col_of_matrix] * determinant(sub_matrix)
				
	return value	


def print_determinant(matrix):
	n = len(matrix)
	for i in range(n):
		print('|', end=' ')
		for j in range(n):
			print(str(matrix[i][j]), end=' ')
		print('|')

if __name__ == "__main__":
	'''	
	matrix = [  [1,0,0,0],
				[0,1,0,0],
				[0,0,1,0],
				[0,0,0,1]  ]
	'''
				
	size = int( input("Enter n for A(nxn): ") )
	matrix = []
	
	for i in range(size):
		row = input("Enter row %d: " % (i+1) ).split(' ')
		matrix.append([ int(elem) for elem in row ])
	
	print( determinant(matrix) )