# ramdom module import here.
import random
# time module import here.
import time
#  Here, Game name is mentioned.
game_name="***** ROCK PAPER SCISSOR GAME *****"
print(f"\033[1;35m {game_name.center(170)}\033[0m")

# Here.writes the rules for play this game.
print("--: RULES OF THE GAME :--".center(170))
rules="Rock VS Paper -> Paper Wins \t"+"Rock VS Scissor -> Rock Wins\t"+"Paper VS Scissor -> Scissor Wins"
print(rules .center(170))

# Here, user enter his/her name. and  gets a best of luck message .
user_name=input("Enter Your Name : ")
print(f"\033[1;33mBest Of Luck!\033[0m {user_name.capitalize()}")

# user choices.
print("--: Choice word :--\n1.Rock\n2.Paper\n3.Scissor")

while True:
    # user enter his/her choice here
    uc=input("Enter Your Choice : ")
    print(f"{user_name.capitalize()} choice is : ",uc.capitalize())



    # here, computer choose his choice
    print("Now, Its Computer Turn")
    time.sleep(1)
    options=['rock','paper','scissor']
    cc=random.choice(options)
    print("Computer Choice is : ",cc.capitalize())

    #  user choice VS computer choice
    print(f"\033[31m{uc.upper()}\033[0m VS \033[31m{cc.upper()}\033[0m")

    #  write the main logic here
    
    if uc==cc:
        print("The Game Is Draw.")
    elif uc=='rock'and cc=='paper':
        print("Paper Win The Game")
    elif uc=='rock' and cc=='scissor':
        print("Rock Win The Game")
    elif uc=='paper' and cc=='scissor':
        print("Scissor Win The Game")
    elif uc=='paper' and cc=='rock':
        print("Paper Win The Game")
    elif uc=='scissor' and cc=='rock':
        print("Rock Win The Game")
    elif uc=='scissor' and cc=='paper':
            print("Scissor Win The Game")

    print("\nDo you want to play again?(Yes/No)")
    ans=input().lower()
    if ans=='no':
        break

geeting="\U0001F917"+" ** THANK YOU FOR PLAYING ** "+"\U0001F917"
print(f"\033[1;33m{geeting.center(170)}\033[0m")
