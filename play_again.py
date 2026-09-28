# another GAme
def play_again():
    try:
        answer = input('Would you like to play THE NUMBER GUESSING GAME again? [ YES/NO ]: ')
    except:
        print('Thanks for playing NUMBER GUESSING game!')
        return False

    if answer.strip().lower() == 'yes':
        return True

    print()
    print('Thank you for playing the NUMBER GUESSING GAME!')
    return False
