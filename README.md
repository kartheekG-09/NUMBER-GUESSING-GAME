Python Utility for Number Guessing Game


1. Project Title - Python Utility for Number Guessing Game

2. Project Overview
This project is a simple Number Guessing Game made using Python.
The computer selects a random number between 1 and 100. The user tries to guess the number. After each guess, the program tells the user whether the guess is too high or too low.
The program also counts the number of attempts and displays the final result.

3. Features

Generates a random number between 1 and 100.
Takes a guess from the user.
Checks the user's guess.
Gives "too high" or "too low" hints.
Counts the number of attempts.
Shows whether the user won or lost.
Allows the user to play again.
Uses separate Python files for different parts of the program.

4. Technologies / Tools Used
Python
Python `random` module
One Compiler
Git and GitHub for version control

5. Project Files
`main.py` - Starts and controls the game.
`game_setup.py` - Creates the random number and sets the maximum attempts.
`user_input.py` - Takes the user's guess.
`check_guess.py` - Checks whether the guess is correct, high, or low.
`game_result.py` - Shows hints and the final game result.
`play_again.py` - Handles the play-again option.
`README.md` - Project information and instructions.
`statement.md` - Problem statement, scope, target users, and features.

6. How to Run the Project
Install Python on your computer.
Keep all seven `.py` files in the same folder.
Open the folder in IDLE, VS Code, or another Python editor.
Open `main.py`.
Run `main.py`.
Enter a number between 1 and 100 when asked.
Follow the hints given by the program.

7. Testing
The program can be tested by:
Entering a number smaller than the secret number.
Entering a number larger than the secret number.
Entering the correct number.
Playing until all attempts are used.
Playing the game again.
Entering invalid input and checking the program's response.

8. Project Structure

NUMBER_GUESSING_GAME
│
├── main.py
├── game_setup.py
├── user_input.py
├── check_guess.py
├── game_result.py
├── game_rules.py
├── play_again.py
│
├── README.md
├── statement.md
└── diagrams.md
