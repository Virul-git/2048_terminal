import numpy
import os
import random
import movement


def check_row(board):
	for row in board:
		size = len(row)
		for j in range(0,size-1):
			if row[j] == row[j+1]:
				return True
	return False

def check_col(board):
	size = len(board[0])
	for j in range(0,size-1):
		col = board[:,j]
		for k in range(0,size-1):
			if col[k] == col[k+1]:
				return True
	return False

def init_board(size):
	board = numpy.zeros((size+1,size+1))
	return board

def select_size():
	while True:
		try:
			os.system("clear")
			print "1.2x2 2.3x3 3.4x4, select any of the above board sizes"
			size = int(raw_input("Enter your option: "))
			if (size < 4 and size >0):
				break
			else:
				continue
		except:
			print "Error!!!!!!!!!!!!"
	return size

def spawn_num(board,size):
	empty_list = []
	size = size +1
	for j in range(size):
		for i in range(size):
			if board[j][i] == 0:
				empty_list.append((j,i))
	length = len(empty_list)


	# print length 
	# print empty_list

	if length < 1:
		if check_if_game_over(board):
			print board
			print "Game Over"
			quit()
		else:
			None
	elif length ==1:
		s = random.randint(1,3)
		element = empty_list[0]
		if s ==1:
			board[element[0]][element[1]] = 2 
		else:
			board[element[0]][element[1]] = 2
		if check_if_game_over(board):
			print board
			print "Game Over"
			quit()
		else:
			None
	else:
		k  = random.randint(1,length-1)
		print k
		s = random.randint(1,3)
		element = empty_list[k]
		if s ==1:
			board[element[0]][element[1]] = 2 
		else:
			board[element[0]][element[1]] = 2


def Movement(board,a):
	if a == 'w' or a == 'W':
		movement.board_up(board)
	elif a == 'S' or a == 's':
		movement.board_down(board)
	elif a == 'a' or a == 'A':
		movement.board_left(board)
	elif a == 'd' or a == 'D':
		movement.board_right(board)
	else:
		quit()



def board_update(board):
	while True:
		try:
			os.system("clear")
			print board
			valids = ['w','s','a','d','W','S','D','A','q','Q']
			a = raw_input(" Enter w (or) a (or) s (or) d:--> ")
			if a in valids:
				break
			else:
				continue
		except:
			pass
	Movement(board,a)
	print board


def check_if_game_over(board):
	empty_list = []
	size = len(board[0])
	for j in range(size):
		for i in range(size):
			if board[j][i] == 0:
				empty_list.append((j,i))
	length = len(empty_list)
	if length != 0:
		pass
	elif length == 0:
		if check_row(board) or check_col(board):
			pass
		else:
			os.system("clear")
			print board
			print "Game Over !!!!!!!!!!!!!!"
			quit()


def main():

	size = select_size()
	board = init_board(size)
	spawn_num(board,size)
	while True:
		board_update(board)
		spawn_num(board,size)
		check_if_game_over(board)


	print board


if __name__ == "__main__":
	main()