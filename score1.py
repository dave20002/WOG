import utils

#open file to read score and store its value
def add_score(difficulty):
    try:
        scores_file = open(utils.SCORES_FILE_NAME,'r+')
    except FileNotFoundError:
        scores_file = open(utils.SCORES_FILE_NAME,'w')
        scores_file.write('0\n')
        scores_file.seek(0)
        scores_file = open(utils.SCORES_FILE_NAME,'r+')
    try:
        current_score = scores_file.readline().strip()
        if not current_score.isdigit():
            current_score = '0'
        new_score = int(current_score) + (difficulty * 3) + 5
        scores_file.seek(0)
        scores_file.write(f'{new_score}')
        scores_file.truncate()
    finally:
        scores_file.close()