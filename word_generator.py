from random import choice

def generate_word():
  word_list = []
  with open('words.txt') as datas:
    words = datas.readlines()
    for word in words:
      word = word.strip().upper()
      word_list.append(word)
  
  return choice(word_list)
