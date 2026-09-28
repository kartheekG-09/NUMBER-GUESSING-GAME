# Python Code for NUMBER GUESSING GAME

from game_setup import Generate_Unknown_Number, get_Maximum_Attempts
from user_input import get_guess
from check_guess import check_guess
from game_result import show_result
from game_result import show_message
from game_result import show_correct_message
from game_result import show_attempts_left, show_no_attempts_message

from play_again import play_again

def play_game():
    print()
    print("Welcome to the Game of NUMBER GUESSING!")

    secret_number = Generate_Unknown_Number()
    Maximum_Attempts = get_Maximum_Attempts()
    attempts = 0
    won = False

    print("You have MAXIMUM OF ", Maximum_Attempts, "attempts.")
    print()

    while attempts < Maximum_Attempts:
        print("- " * 20)
        guess = get_guess()

        if guess is None:
            print("No input received . GAME ENDS.")
            break

        attempts += 1
        print("NUMBER OF ATTEMPT:", attempts)

        result = check_guess(guess, secret_number)

        if result == "correct":
            show_correct_message(secret_number, attempts)
            won = True
            break
        else:
            show_message(result)

        attempts_left = show_attempts_left(attempts, Maximum_Attempts)
        if attempts_left == 0:
            show_no_attempts_message()

    show_result(won, secret_number, attempts)

print("   PYTHON NUMBER GUESSING GAME ")
print("  ============================= ")

while True:
    play_game()
    if not play_again():
        break
