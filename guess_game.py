import random, utils
from score import add_score

# Ask user to continue play
def play_again():
  while True:
    answer = input('Play this game again? (Y/N)')
    if answer in (['Y', 'y', 'Yes', 'yes']):
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

def generate_number(difficulty):
    return random.randint(0, difficulty)

#Prompts the user to input a number within the range of 0 to the difficulty and returns the entered number.
def get_guess_from_user(difficulty):
    while True:
        num = input(f'Enter number in range from 0 to {difficulty}:\n')
        num = int(num)
        if num <= difficulty:
            break
        else:
            print('The number you have selected is too big. Please, try again:')
    return num

# Compares the generated secret number with the user's input and
# determines if they match.
def compare_results(a,b):
    if a == b:
        return True
    else:
        return False

# The play function
def play(difficulty):
    a = generate_number(difficulty)
    b = get_guess_from_user(difficulty)
    if not compare_results(a,b):
        print('You loss')
        print(f'secret number was {a}')
        play_again()
        return False
    else:
        add_score(difficulty)
        print('You won')
        play_again()
        return True

