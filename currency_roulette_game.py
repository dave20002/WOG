import requests, random
import score1

# Ask user to continue play
def play_again(difficulty):
  global secret_number
  secret_number = random.randint(1, 100)
  while True:
    answer = input('Play again? (Y/N)')
    if answer in (['Y', 'y', 'Yes', 'yes']):
      play(difficulty)
    elif answer in (['N', 'n', 'No', 'no']):
      print('Bye!')
      break
    else:
      print('Must be Yes or No:')
      continue
    exit()

# Generate secret number
secret_number = random.randint(1,100)

# interval for the correct answer based on the game's difficulty level.
def get_money_interval(difficulty):
    url = "https://api.frankfurter.app/latest?from=USD&to=ILS"
    response = requests.get(url)
    data = response.json()
    ils_currency = data["rates"]["ILS"]
    difference = 10 - difficulty
    amount = round(secret_number * ils_currency,2)
    return {'sum':amount, 'min':amount - difference, 'max':amount + difference }

# Prompts the user to input a guess for the converted value of a  specified amount in USD.
def get_guess_from_user():
    return input(f'How much is {secret_number} dollar? ')

# Executes the game by employing the functions above, and returns True if the user wins, and False if the user loses.
def compare_results(difficulty):
    user_guess_num = get_guess_from_user()
    user_guess_num = int(user_guess_num)
    min_allowed_value = get_money_interval(difficulty)['min']
    max_allowed_value = get_money_interval(difficulty)['max']
    if min_allowed_value <= user_guess_num <= max_allowed_value:
        return True
    else:
        return False

# Executes the game by invoking the functions above and returns True if the user wins, and False if the user loses.
def play(difficulty):
    get_money_interval(difficulty)
    if compare_results(difficulty):
        print("You won!")
        score1.add_score(difficulty)
        play_again(difficulty)
        return True
    else:
        print(f'You lost! The right answer is {get_money_interval(difficulty)['sum']} shekel')
        play_again(difficulty)
        return False
