import numpy

def shift_zeros_left(arr):
	# print arr
	# print sorted(arr,key=bool)
	return sorted(arr,key=bool)

def shift_zeros_right(arr):
	arr = shift_zeros_left(arr)
	return arr[::-1]


def combine_left(arr):
	size = len(arr)
	for l in range(0,size-1):
		if arr[l] == arr[l+1]:
			arr[l] = arr[l]*2
			arr[l+1] = 0
	return arr


def combine_right(arr):
	arr = arr[::-1]
	arr = combine_left(arr)
	return arr[::-1]



def board_right(board):
	size = len(board)
	for j in range(size):
		col = board[j]
		# print col
		col =shift_zeros_left(col)
		col =combine_right(col)
		col =shift_zeros_left(col)
		board[j] = col
	# print board
	return board

def board_left(board):
	size = len(board)
	for j in range(size):
		col = board[j]
		# print col
		col =shift_zeros_right(col)
		# print col
		col =combine_left(col)
		col =shift_zeros_right(col)
		board[j] = col
	return board

def board_up(board):
	size = len(board)
	for j in range(size):
		col = board[:,j]
		# print col
		col =shift_zeros_right(col)
		# print col
		col =combine_left(col)
		col =shift_zeros_right(col)
		board[:,j] = col
	return board

def board_down(board):
	size = len(board)
	for j in range(size):
		col = board[:,j]
		# print col
		col =shift_zeros_left(col)
		col =combine_right(col)
		col =shift_zeros_left(col)
		board[:,j] = col
	# print board
	return board