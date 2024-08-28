from tkinter import *
import random

#Initialization of global score variables
player_score = 0
computer_score = 0
ties = 0

def game(player_choice):
    global player_score, computer_score, ties #define global score variables
    computer_choices = ['Rock', 'Paper', 'Scissors'] #List of computer choices

    computer_choice = random.choice(computer_choices)
        
    SecondLabel.config(text=f"Computer choice: {computer_choice}") #Update Computer choice Label
    
    
    #If function for game functionality
    if player_choice == computer_choice:
        result = "Tied Victory!"
        ties+=1 #score increment for ties
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
        (player_choice == 'Paper' and computer_choice == 'Rock') or \
        (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "Player's Victory!"
        player_score+=1 #score increment for player
    else:
        result = "Computer's Victory!"
        computer_score+=1 #score increment for computer

    ThirdLabel.config(text=result) #Update Result Label
   
    
#Score Window Function
def Scores_window():
    # Create a new window for the scores
    scores_window = Toplevel(root)
    scores_window.title("Scores")
    scores_window.geometry("300x200")
    scores_window.configure(bg="grey")
    img = PhotoImage(file = "codsoft_taskno4/icons8-one-to-one-48.png")
    scores_window.iconphoto(False, img)
    
    #New Window Label Widgets
    PlayerLabel = Label(scores_window, text=f"Player\n {player_score}", bg="grey", fg="white")
    ComputerLabel = Label(scores_window, text=f"Computer\n {computer_score}", bg="grey", fg="white")
    TieLabel = Label(scores_window, text=f"Ties\n {ties}", bg="grey", fg="white")
    
    # Layout for Labels
    PlayerLabel.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    ComputerLabel.grid(row=0, column=1, padx=10, pady=10, sticky="ew") 
    TieLabel.grid(row=0, column=2, padx=10, pady=10, sticky="ew")



#Main Window Initialization
root = Tk()
root.title("Rock Paper Scissors")
root.configure(bg="grey")

#Window Images
img = PhotoImage(file = "codsoft_taskno4/icons8-joystick-48.png")
img2 = PhotoImage(file = "codsoft_taskno4/icons8-rock-48.png")
img3 = PhotoImage(file = "codsoft_taskno4/icons8-paper-48 (1).png")
img4 = PhotoImage(file = "codsoft_taskno4/icons8-scissors-48.png")
root.iconphoto(False, img)


#Label Initializations
ZeroLabel = Label(root, text="Welcome to the Rock-Paper-Scissors Game", bg="black", fg="white")
FirstLabel = Label(root, text="Choose Rock, Paper, or Scissors", bg="grey")
SecondLabel = Label(root, text="", bg="grey", fg="white")
ThirdLabel = Label(root, text="", bg="grey", fg="white")

#Button Initializations
FirstButton = Button(root, image=img2, bg="green", command = lambda:game('Rock'))
SecondButton = Button(root, image=img3, bg="blue", command = lambda:game('Paper'))
ThirdButton = Button(root, image=img4, bg="yellow", command = lambda:game('Scissors'))
ScoresButton = Button(root, text="Show Scores", command=Scores_window, relief="raised", bg="black", fg="white")

#Label Layout
ZeroLabel.grid(row=0, columnspan=3)
FirstLabel.grid(row=1, columnspan = 3, pady=10)
SecondLabel.grid(row =3, columnspan = 3, pady=10)
ThirdLabel.grid(row=4, columnspan=3, pady=10)

#Button Layout
FirstButton.grid(row=2, column = 0, pady=10)
SecondButton.grid(row=2, column = 1, pady=10)
ThirdButton.grid(row=2, column = 2, pady=10)
ScoresButton.grid(row =5, columnspan=3)


#Run the program loop
root.mainloop()