# User Input
def get_guess():
    while True :
        try:
            guess = int(input(" Enter your guess: "))
        except ValueError:
            print(' Insert a Number in between 1 , 100.')
            continue
        except:
             return None

        if 1 <= guess <= 100:
            return guess

        print('Numberr guessed BY USER MUST be between 1 and 100.')
