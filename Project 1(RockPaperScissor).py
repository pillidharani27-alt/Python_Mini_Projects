Rock='''
        ______
-------'______)___)
        (__________)
        (__________)
        (_________)
----,__(_______)'''
paper='''_________
------'_________)
        (___________)
        (_____________)
        (_____________)
        (____________)
------'____________)'''
Scissors='''__________
--------'___________)
         (______________)
         (______________)
         (--------)
         (--------)
-------'_________)'''
image=[Rock,paper,Scissors]
import random
user_choice=int(input("Enter your choice:type o for Rock,1 for Paper or 2 for Scissor: "))
if user_choice>=3 or user_choice<0:
    print("you entered invalid: you lose")
else:
    print(image[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice")
    print(computer_choice)
    print(image[computer_choice])
    if computer_choice==user_choice:
        print("it's a draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win")

