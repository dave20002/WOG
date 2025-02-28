Project "World Of Game" with 3 games written on Python.
1. Currency roulette game
2. Guess game
3. Memory game
To play the Game, run command:
_python main.py_

The score is written on separate scores.html website within Flask framework.
To manage Score application, there is a Docker container that must be in running state.
To start the Docker container use command:
_docker compose up_

To update the Score application, modify _main_score.py_ file. 
There is an automatic test run to check the validity of sore, that has to be in range 1-1000
This test is implemented by Jenkins pipeline and test/e2e.py file

For that purposes, Jenkins application running within Docker container on local computer, 
and running automated tests on local Windows computer agent within GitBash shell



