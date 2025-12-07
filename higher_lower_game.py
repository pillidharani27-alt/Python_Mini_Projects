import random
import os

import game_art
import game_database

print(game_art.GAME_LOGO)
score=0
def display_account_info(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name} a{description}  from {country}"
def check_answer(guess,followers_1,followers_2):
    if followers_1<followers_2:
        if guess==1:
            return  False
        else:
            return True
    else:
        if guess==1:
            return  True
        else:
            return False

account_2=random.choice(game_database.data)
continue_flag=True
while continue_flag:
   account_1=account_2
   account_2=random.choice(game_database.data)
   while account_1==account_2:
        account_2=random.choice(game_database.data)

   print(f"compare 1:{display_account_info(account_1)}")
   print(game_art.vs)
   print(f"compare 2:{display_account_info(account_2)}")
   guess=int(input("whose has more followers ? type 1 or 2:"))
   followers=account_1['followers']
   followers=account_2['followers']


   is_correct=check_answer(guess,followers,followers)
   os.system('cls')
   print(game_art.GAME_LOGO)
   if is_correct:
        score +=1
        print(f"you are right.your score is: {score}")
   else:
        print(f"you are wrong.your final score is: {score}")
        continue_flag=False
