from tkinter import *
import random #import random module


#Functions for Password Operations
def onclick(Operation):
    global SecondLabel, length #define two global variables
    op = Operation
    if op == "generate": #Operation for generating passwords
        length = int(FirstEntry.get())
        if length > 0: #if length is greater than 0
            databook = random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()', k=length) #store characters in variable
            password = ''.join(databook) #join list elements
            SecondLabel = Label(root, text = f"Your Password: {password}", wraplength=260, anchor='w', justify='center', bg="grey") #Label to display password on screen
            SecondLabel.grid(row = 2, columnspan=2, sticky='ew', padx=10, pady=10) #Password Label Layout
            
        else:
            raise ValueError ("Enter Valid Length")
            
    elif op == "reset": #Operation for Entry Reset
        if length:
            FirstEntry.delete(0, END) #Delete Former Entry
            SecondLabel.config(text="") #Delete Former Label text
            
#Main Window Initialization
root = Tk()
root.title("Password Generator")
img = PhotoImage(file = "codsoft_taskno3/icons8-password-48.png")
root.iconphoto(False, img)
root.configure(bg="grey")

#Widgets Initialization
FirstLabel = Label(root, text="Specify the desired length of the password",  bg='grey')
FirstEntry = Entry(root)

FirstButton = Button(root, text="Generate Password", command = lambda: onclick("generate"), relief="raised", bg="green")
SecondButton = Button(root, text="Reset Password", command = lambda: onclick("reset"), relief="raised", bg="red")

#Widgets Layout
FirstLabel.grid(row = 0, columnspan = 2, padx=5, pady=10)
FirstEntry.grid(row=1, columnspan=2, padx=5, pady=10)

FirstButton.grid(row=4, column=0, sticky='ew', padx=5, pady=10)
SecondButton.grid(row=4, column=1, sticky='ew',padx=5, pady=10)

#Run the program loop
root.mainloop()