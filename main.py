import game
from word_generator import generate_word

def main():
  print('Hello')
  new_game = game.Wordle('HELLO')
  print(new_game.append_input('HELLO'))
  new_game.check_result()
  print(new_game.get_game_board())
  print(generate_word())

if __name__ == '__main__':
  main()