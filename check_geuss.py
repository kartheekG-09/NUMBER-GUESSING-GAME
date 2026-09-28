# Check whether the guess is correct

def check_guess (guess , Unknown_Number):
     if guess == Unknown_Number :
        return  "correct"

     elif guess < Unknown_Number :
        return "low"

     else:
        return "high"
