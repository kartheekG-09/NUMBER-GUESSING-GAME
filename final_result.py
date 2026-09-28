
# Show the final result
def show_result(won, Unknown_Number, attempts):
    print()
    print(" = = "*10 )
    print("             GAME RESULT")
    print("= = " *10 )

    if won:
        print("Result: You won !!")
        
    else:
        print("Result: You lost THE GAME !")
        print("The correct number is:", Unknown_Number)

    print()
    print(" Attempts used:", attempts)

def show_message(result):
    if result == "low":
        print("Your guess is low.")
        print("Guess a bigger number")
    else:
        print("Your guess is high.")
        print("Guess a smaller number.")

def show_correct_message(Unknown_Number, attempts):
    print()
    print("Congratulations ,NUMBER RIGHTLY GUESSED")
    print("The unknown number was:", Unknown_Number)
    print("Attempts:", attempts)

def show_attempts_left(attempts, max_attempts):
    attempts_left = max_attempts - attempts
    print('Remaining opportunities :', attempts_left)
    return attempts_left

def show_no_attempts_message():
    print(" All your attempts are exhausted .")
