from random import choice

def draw(board):
  print('-------')
  for y in range(3):
    print('|' + '|'.join(board[y]) + '|')
    print('-------')

def place(board, pos, piece):
  y = int(pos / 3)
  x = int((pos - 1) % 3)
  board[y][x] = piece 
  return board

def check(board):
  return ""

def get_empty_spaces(board):
  return []

def game():
  board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
  ]
  result = check(board)
  while result == "":
    # Player turn
    player_spot = input("Your turn")
    place(board, player_spot, "X")

    # Check to see if you won  
    result = check(board)
    if result == "X":
      print("YOU WIN")
      break

    robot_spot = choice(get_empty_spaces(board))
    place(board, robot_spot, "O")

    # Check to see if someone won  
    result = check(board)


game()