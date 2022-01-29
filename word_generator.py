from random import choice

def create_wordlist(): 
  word_list = [] 
  with open('words.txt') as datas:
    words = datas.readlines()
    for word in words:
      word = word.strip().upper()
      word_list.append(word)
  return word_list


def generate_word():
  return choice(create_wordlist())
