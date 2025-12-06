import random
import logo_art
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("your guessed is too low")
        return attempts - 1
    elif guessed_number > answer:
        print("your guessed is too high")
        return attempts - 1
    else:
        print(f"you guessed right....the answer was {answer}")
def game():
    print(logo_art.logo)
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level = input("Chosen level of difficulty...type 'easy' or 'hard' to choose: ")
    attempts = set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("you have entered wrong difficulty level.....play again ")
        return
    guessed_number =0
    while guessed_number != answer:
        print(f"you have {attempts} attempts remaining guess the number")
        guessed_number = int(input("Guess a number"))
        attempts=check_answer(guessed_number, answer, attempts)
        if attempts==0:
            print("you are out of guesses.....you lose")
            return
        elif guessed_number != answer:
            print("Guess again")
game()
