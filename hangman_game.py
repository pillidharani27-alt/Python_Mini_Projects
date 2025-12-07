import random
import word_file
import hangman_stages
chosen_word=random.choice(word_file.words)
lives=6
print(chosen_word)
disply=[]
for i in range(len(chosen_word)):
    disply+='_'
print(disply)
game_over=False
while not game_over:
    Guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == Guessed_letter:
            disply[position]=Guessed_letter
    print(disply)
    if Guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!")
    if '_' not in disply:
        game_over=True
        print("You Win!")
    print(hangman_stages.stages[lives])




