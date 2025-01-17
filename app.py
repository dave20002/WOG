import currency_roulette_game
import guess_game
import memory_game
import utils
from colorama import Fore, Style

def welcome():
    username = input('Type your name: ')
    utils.screen_cleaner()
    print(f'Hi {Fore.YELLOW}{username}{Style.RESET_ALL}, and welcome to the {Fore.GREEN}World of Games:{Fore.LIGHTBLUE_EX} The Epic Journey{Style.RESET_ALL}\n\n')

def start_play():
    game_name = {1:'Memory', 2:'Guess', 3:'Currency Roulette'}
    game_description = {1:"A sequence of numbers will appear for 1 second and you have to guess it back.\n",
                        2:"Guess a number and see if you chose like the computer.\n",
                        3:"try and guess the value of a random amount of USD in ILS\n"}
    game_options = [1, 2, 3]
    level_options = [1, 2, 3, 4, 5]
    print(f'''Please choose a game to play:\n
    1. {Fore.LIGHTCYAN_EX}Memory Game{Style.RESET_ALL} - a sequence of numbers will appear for 1 second and you have to guess it back.\n
    2. {Fore.LIGHTCYAN_EX}Guess Game{Style.RESET_ALL} - guess a number and see if you chose like the computer.\n
    3. {Fore.LIGHTCYAN_EX}Currency Roulette{Style.RESET_ALL} - try and guess the value of a random amount of USD in ILS\n''')
    while True:
        game = input('Your game number is: ')
        game = int(game)
        if game in game_options:
            break
        else:
            print('Wrong choice. Try again, please: ')
    while True:
        level = input('Select the difficulty level between 1 and 5: ')
        level = int(level)
        if level in level_options:
            break
        else:
            print('Wrong choice. Try again, please: ')
    utils.screen_cleaner()
    print(f'You have selected the {Fore.LIGHTYELLOW_EX}"{game_name[game]} Game"{Style.RESET_ALL} with difficulty level {Fore.LIGHTRED_EX}{level}{Style.RESET_ALL}')
    print(f'{Fore.LIGHTGREEN_EX}{game_description[game]}{Style.RESET_ALL}')
    if game == 1:
        input(f'Press {Fore.LIGHTBLUE_EX}"Enter"{Style.RESET_ALL} key to start playing...')
        utils.screen_cleaner()
        memory_game.play(level)
    elif game == 2:
        guess_game.play(level)
    elif game == 3:
        currency_roulette_game.play(level)
    else:
        print('No game or level selected')