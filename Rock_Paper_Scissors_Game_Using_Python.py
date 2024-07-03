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
    match uc:
        case '1' |'rock':
            choice="rock"
            # print(f"{user_name.capitalize()} choice is : ",uc.capitalize())
        case '2'| 'paper':
            choice="paper"
            # print(f"{user_name.capitalize()} choice is : ",uc.capitalize())
        case '3' | 'scissor':
            choice="scissor"
            # print(f"{user_name.capitalize()} choice is : ",uc.capitalize())
        case _:
            print("w")

    print(f"{user_name.capitalize()} choice is : ",choice.capitalize())



    # here, computer choose his choice
    print("Now, Its Computer Turn")
    time.sleep(1)
    options=['rock','paper','scissor']
    computer_choice=random.choice(options)
    print("Computer Choice is : ",computer_choice.capitalize())

    #  user choice VS computer choice
    print(f"\033[31m{choice.upper()}\033[0m VS \033[31m{computer_choice.upper()}\033[0m")

    #  write the main logic here
    
    if choice==computer_choice:
        print("The Game Is Draw.")
    elif choice=='rock'and computer_choice=='paper':
        print("Paper Win The Game")
    elif choice=='rock' and computer_choice=='scissor':
        print("Rock Win The Game")
    elif choice=='paper' and computer_choice=='scissor':
        print("Scissor Win The Game")
    elif choice=='paper' and computer_choice=='rock':
        print("Paper Win The Game")
    elif choice=='scissor' and computer_choice=='rock':
        print("Rock Win The Game")
    elif choice=='scissor' and computer_choice=='paper':
            print("Scissor Win The Game")

    print("\nDo you want to play again?(Yes/No)")
    ans=input().lower()
    if ans=='no':
        break

geeting="\U0001F917"+" ** THANK YOU FOR PLAYING ** "+"\U0001F917"
print(f"\033[1;33m{geeting.center(170)}\033[0m")
