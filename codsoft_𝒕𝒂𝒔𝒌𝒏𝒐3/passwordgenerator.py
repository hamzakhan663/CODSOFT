from tkinter import *

def onclick(Operation):
    op = Operation
    if op == "generate":
        ...
        
    elif op == "reset":
        ...
    
root = Tk()
root.title("Password Generator")
img = PhotoImage(file = "Password Generator/icons8-password-48.png")
root.iconphoto(False, img)


FirstEntry = Entry(root)
FirstButton = Button(root, text="Generate", command = lambda: onclick("generate"))
SecondButton = Button(root, text="Reset", command = lambda: onclick("reset"))

FirstEntry.grid(row=0, columnspan=2)
FirstButton.grid(row=1, column=0)
SecondButton.grid(row=1, column=1)

root.mainloop()