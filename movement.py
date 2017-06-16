import numpy


def update_left(arr,j):
	a = numpy.zeros((len(arr),0))
	a[:j] = arr[:j]
	a[j+1:len(arr)-(j+2)] = arr[j+2:]
	return a

def update_right(arr,j):
	a = arr[::-1]
	j =update_left(a,j)
	return j[::-1]

def left_row(row):
	size = len(row)
	for j in range(size-1):
		if row[j]== row[j+1]:
			row[j] = row[j]*2
			a = update_right(row,j)
			return a
	return row

def right_row(row):
	size = len(row)
	row = row[::-1]
	for j in range(size-1):
		if row[j]== row[j+1]:
			row[j] = row[j]*2
			a = update_right(row,j)
			return a[::-1]
	return row[::-1]


def up_col(col):
	size = len(col)
	for j in range(size-1):
		if col[j]== col[j+1]:
			col[j] = col[j]*2
			a = update_right(col,j)
			return a
	return col


def down_col(col):
	size = len(col)
	col = col[::-1]
	for j in range(size-1):
		if col[j]== col[j+1]:
			col[j] = col[j]*2
			a = update_right(col,j)
			return a
	return col[::-1]




def shift_left(board):
	temp = board
	size = len(board)
	for row in board:
		left_row(row)
	return board

def shift_right(board):
	temp = board
	size = len(board)
	for row in board:
		right_row(row)
	return board

def shift_up(board):
	temp = board
	size = len(board)
	for j in range(size):
		col = board[:][j]
		up_col(col)
	return board

def shift_down(board):
	temp = board
	size = len(board)
	for j in range(size):
		col = board[:][j]
		down_col(col)
	return board
