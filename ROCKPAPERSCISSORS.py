#-----------------------------------------------------------------------
#
# STEP-1 :- GET USER INPUT
# STEP-2 :- VALIDATE THE USER INPUT
# STEP-3 :- COMPUTER INPUT
# STEP-4 :- COMPUTE WINNER
# STEP_5 :- PLAY AGAIN(YES/N0)
#
#-----------------------------------------------------------------------
from random import choices
options = ["rock","paper","scissors"]
def game():
    user_input = input("Enter (rock/ paper/ scissors):").lower()
    if user_input not in options:
        print("Invalid Choice")
        return
    computer_choice = choices(options)
    print("User Choice is:",user_input)
    print("Computer choice is:",computer_choice)
   
    if user_input == computer_choice:
        print("TIE")
    elif ((user_input == "rock" and computer_choice == "scissors")  
    or (user_input == "scissors" and computer_choice == "paper")  
    or (user_input == "paper" and computer_choice == "rock")):
        print("User win")
    else:
        print("Computer win")
def main():
    #play again
    game()
    play = input("Do you want to play again:(y/n):").lower()
    while play != "y":
        print("Thanks for playing...")
        break
   
if __name__ == '__main__':
    main()
