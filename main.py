from game import Wordle
from word_generator import generate_word, create_wordlist


def check_valid_input(inp, word_list):
  return (len(inp) == 5) and (inp.isalpha() and (inp in word_list))


def main():

  word_list = create_wordlist()
  game = Wordle(generate_word())
  game_on = True
  cur_row = 0

  while game_on:
    # Get User input and validate the file
    user_ans = input("Please enter your answer: ").upper()
    while not check_valid_input(user_ans, word_list):
      print("Please enter a valid 5 letter word!!!")
      user_ans = input("Please enter your answer: ").upper()
    
    check_won = game.append_input(user_ans)

    if check_won:
      break

    if cur_row == 5:
      game_on = False
      print("You Lose! Please try harder next time 😁")
    
    # Update row
    cur_row += 1

if __name__ == '__main__':
  main()