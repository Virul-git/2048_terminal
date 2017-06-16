import numpy 
import movement

board = numpy.zeros((3,3))

board[2] = [0,2,0]

print board

board = movement.board_up(board)

print board

board = movement.board_down(board)

print board

board = movement.board_right(board)

print board

board = movement.board_left(board)

print board