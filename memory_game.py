import random
from time import sleep

import app
import utils
from score import add_score

# Ask user to continue play
def play_again():
  while True:
    answer = input('Play this game again? (Y/N)')
    if answer in (['Y', 'y', 'Yes', 'yes']):
      utils.screen_cleaner()
      difficulty = int(input('Select difficulty level(1-5):'))
      utils.screen_cleaner()
      play(difficulty)
    elif answer in (['N', 'n', 'No', 'no']):
      print('Bye!')
      break
    else:
      print('Must be Yes or No:')
      continue
    exit()

# Create list of numbers to guess
def generate_sequence(difficulty):
  numbers = [random.randint(1, 101) for _ in range(difficulty)]
  return numbers

# Prompts the user to input a list of numbers matching the length of the
# generated sequence.
def get_list_from_user(difficulty):
  while True:
    user_answer = input(f'Type {difficulty} numbers separated by spaces:\n')
    user_answer = user_answer.split()
    user_answer = [int(number) for number in user_answer]
    if len(user_answer) == difficulty:
      return user_answer
    else:
      print(f'You must enter exactly {difficulty} numbers.')

# Compares two lists to verify if they are identical, returning True if they match and False otherwise.
def is_list_equal(list_a,list_b):
  if list_a == list_b:
    return True
  else:
    return False

# Executes the game by invoking the functions above and returns True if the user wins, and False if the user loses.
def play(difficulty):
  list1 = generate_sequence(difficulty)
  print(list1)
  sleep(1.3)
  utils.screen_cleaner()
  list2 = (get_list_from_user(difficulty))
  if is_list_equal(list1,list2):
    add_score(difficulty)
    print('You won!')
    play_again()
  else:
    print('You lost!')
    play_again()
    return False