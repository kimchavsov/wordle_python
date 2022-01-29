import board

class Wordle:

  def __init__(self, answer):
    self.__game_board = board.create_board()
    self.__result_board = board.create_board()
    self.current_row = 0
    self.__answer = answer
    print(self.__answer)

  def get_game_board(self):
    return self.__game_board
  
  def get_result_baord(self):
    return self.__result_board

  def append_input(self, word_input):
    index = 0
    for letter in word_input:
      self.__game_board[self.current_row][index] = letter
      index += 1
    self.get_game_board()
    self.return_output()
    print(self.get_game_board())
    print(self.get_result_baord())
    
    return self.check_result()


  def return_output(self):
    for i in range(5):
      if self.__answer[i] == self.__game_board[self.current_row][i]:
        self.__result_board[self.current_row][i] = 'G'
      elif self.__game_board[self.current_row][i] in self.__answer:
        self.__result_board[self.current_row][i] = 'Y'
      else:
        self.__result_board[self.current_row][i] = 'X'

  def check_result(self):
    current_input = "".join(self.__game_board[self.current_row])
    if current_input == self.__answer:
      print("Congratulation! You won the game 🥳")
      print(f"Total attempt: {self.current_row + 1} / 6")
      return True
    else:
      self.__update_row()

  def __update_row(self):
    self.current_row += 1
  
