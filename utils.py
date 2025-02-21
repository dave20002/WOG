import os
from trio import open_file
#import memory_game

# A string representing a file name. By default “Scores.txt”
SCORES_FILE_NAME = "scores.txt"
# A number representing a bad return code for a function
BAD_RETURN_CODE = 22

# A function to clear the screen (useful when playing memory game or before a new game starts).
def screen_cleaner():
    if os.name == 'nt':
      os.system('cls')
    else:
        os.system('clear')


