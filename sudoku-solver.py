from constant import *


def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print ('- - - - - - - - - - -')
    
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print('| ', end='')

      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + ' ', end='')

def find_empty_squares(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        print(i, j)

def get_box_list(board, top_left_coords):
  row_idx = top_left_coords[0]
  col_idx = top_left_coords[1]

  box_list = []

  for row in range(row_idx, row_idx + 3):
    box_list += [board[row][col] for col in range(col_idx, col_idx + 3)]
  
  return box_list

def check_line(line):
  for value in line:
    return False if value != 0 and line.count(value) > 1 else True

def check_board(board):
  valid = True

  # Check rows
  for i in range(len(board)):
    valid = check_line(board[i])
    if not valid: return False

  # Check columns
  for i in range(len(board[0])):
    valid = check_line([row[i] for row in board])
    if not valid: return False

  # Check 9 X 9 block
  for row in range(0, 7, 3):
    for col in range(0, 7, 3):
      valid = check_line(get_box_list(board, (row, col)))
      if not valid: return False

  return valid

print(check_board(TEST_BOARD))