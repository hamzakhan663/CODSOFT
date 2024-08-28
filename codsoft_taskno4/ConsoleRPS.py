import random
from time import sleep


choice = False


while choice == False:
    print("Rock-Paper-Scissors")
    player_choice = input("Choose rock, paper, or scissors\n").capitalize()

    computer_choices = ['Rock', 'Paper', 'Scissors']

    computer_choice = random.choice(computer_choices)

    if player_choice not in computer_choices:
        print ("Invalid choice")
        continue
        
    print (f"Computer choice: {computer_choice}")
    sleep(1)
    
    if player_choice == computer_choice:
        result = "Tie"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
        (player_choice == 'Paper' and computer_choice == 'Rock') or \
        (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "I win!"

    print (result)
    
    sleep(1)
    
    rematch = input("Do you desire to play again?\nYes or no\n").capitalize()
    
    if rematch == "Yes":
        choice = False
        
    elif rematch == "No":
        choice = True
        
    else:
        print("Invalid response - Game Forfeited.")
        break


            