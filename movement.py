import numpy

def shift_zeros_left(arr):
	sorted(arr,key=bool)
	return arr

def shift_zeros_right(arr):
	arr = shift_zeros_left(arr)
	return arr[::-1]


def combine_left(arr):
	size = len(arr)
	for l in range(1,size-1):
		if arr[l] == arr[l+1]:
			arr[l] = arr[l]*2
			arr[l+1] = 0
	return arr


def combine_right(arr):
	arr = arr[::-1]
	arr = combine_left(arr)
	return arr[::-1]



def board_right(board):
	for row in board:
		shift_zeros_left(row)
		combine_right(row)
		shift_zeros_left(row)
	return board

def board_left(board):
	for row in board:
		shift_zeros_right(row)
		combine_left(row)
		shift_zeros_right(row)
	return board

def board_up(board):
	size = len(board)
	for j in range(size):
		col = board[:][j]
		shift_zeros_right(col)
		combine_left(col)
		shift_zeros_right(col)
	return board

def board_down(board):
	size = len(board)
	for j in range(size):
		col = board[:][j]
		shift_zeros_left(col)
		combine_right(col)
		shift_zeros_left(col)
	return board