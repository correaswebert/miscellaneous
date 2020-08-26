from ratio import fracOp, printFrac


# keep max zero row at bottom
def zeroesAtBottom(mat):
	num_row = len(mat)
	num_col = len(mat[0])
	
	zeroes = [0] * num_row
	
	for row in range(num_row):
		for elem in mat[row]:
			# 
			if elem == 0:
				zeroes[row] += 1
			else:
				break

zeroesAtBottom( [ [3,0,0], [0,1,0], [1,1,1] ] )

def echelon(mat):
	num_row = len(mat)
	num_col = len(mat[0])

	for col in range(num_col):
		for row in range(col+1, num_row):
			try:
				ratio = mat[row][col] / mat[col][col]
			except ZeroDivisionError:
				# check for non-zero element
				# in column
				for check in range(col+1, num_row):
					if mat[check][col] != 0:
						for num_elem in range(num_col):
							temp = mat[col][num_elem]
							mat[col][num_elem] = mat[check][num_elem]
							mat[check][num_elem] = temp
				row -= 1
				break
			# perform row-op to
			# vanish the elem
			for select_row in range(num_col):
				mat[row][select_row] -= ratio * mat[col][select_row]
	
	print_matrix(mat)


def print_matrix(mat):
	num_row = len(mat)
	num_col = len(mat[0])

	# print row-echeloned matrix
	for row in range(num_row):
		for col in range(num_col):
			print(mat[row][col], end="\t")
		print()
			

matrix = [  [3., 5., 1., 4.],
			[2.,  -1., 1., 1.],
			[5., 4., 2., 5.]  ]
			
# incorrect
matrix = [ [0,0,0], [0,0,1], [0,1,0] ]
		
#matrix = [ [1,1,0,1], [1,2,2,1], [3,4,2,3] ]
print_matrix(matrix)
print()
echelon(matrix)
