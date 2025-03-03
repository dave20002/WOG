# World Of Games

Welcome to the World Of Games! This project contains three exciting games written in Python. The games are:

1. Memory Game
2. Guess Game
3. Currency Roulette Game

### How to play

### Memory Game
A sequence of numbers will appear for 1 second, and you have to guess it back.

### Guess Game
Guess a number and see if you chose like the computer.

### Currency Roulette Game
Try and guess the value of a random amount of USD in ILS.

### The score app
The score is written on separate scores.html website within Flask framework.
To manage Score application, there is a Docker container that must be in running state.
To start the Docker container use command:
_docker compose up_

To update the Score application, modify _main_score.py_ file. 
There is an automatic test run to check the validity of sore, that has to be in range 1-1000
This test is implemented by Jenkins pipeline and test/e2e.py file

For that purposes, Jenkins application running within Docker container on local computer, 
and running automated tests on local Windows computer agent within GitBash shell

## How to Run

### Prerequisites
- Python 3.9 or higher
- Docker

### Running Locally

1. Clone the repository:
    - git clone https://github.com/dave20002/WOG.git
    - cd /WOG

2. Install the required dependencies:
    - pip install -r requirements.txt
    
3. Run the main application:
    - python main.py

4. To run the score server:
    - python main_score.py
    

### Score app running and testing with Docker (automation)

1. Build the Docker image:
    - docker-compose build
    
2. Run the Docker container:
    - docker-compose up
    
The score server will be available at `http://localhost:8777`.

## Project Files

- [app.py]: Main application file to start the game.
- [currency_roulette_game.py]: Contains the Currency Roulette Game logic.
- [guess_game.py]: Contains the Guess Game logic.
- [memory_game.py]: Contains the Memory Game logic.
- [main_score.py]: Flask application to display the score.
- [utils.py]: Utility functions used across the project.
- [score.py] : Function to handle scoring.
- [Dockerfile]: Docker configuration for the project.
- [docker-compose.yaml]: Docker Compose configuration.
- [requirements.txt]: Python dependencies.
- [scores.txt]: File to store the scores.





