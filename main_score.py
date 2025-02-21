from flask import Flask
import utils

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        with open(utils.SCORES_FILE_NAME, 'r') as scores_file:
            score = scores_file.read().strip()

        # Check if the score is a valid digit
        if score.isdigit() and int(score) != 0:
            return f'''<html>
                        <head>
                            <title>Scores Game</title>
                        </head>
                        <body>
                            <h1>The score is:</h1>
                            <div id="score" style="font-size: 50px; color: blue;">{score}</div>
                        </body>
                        </html>'''
        else:
            raise ValueError("Invalid score value")
    except Exception:
        error = utils.BAD_RETURN_CODE
        return f'''<html>
                    <head>
                        <title>Scores Game</title>
                    </head>
                    <body>
                        <h1>ERROR</h1>
                        <div id="score" style="font-size: 50px; color: red">{error}</div>
                    </body>
                    </html>'''


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
