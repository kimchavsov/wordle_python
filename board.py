def create_board():
  board = []
  for _row in range(6):
    row = []
    for _col in range(5):
      col = ''
      row.append(col)
    board.append(row)
  
  return board
