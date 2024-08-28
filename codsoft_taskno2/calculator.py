# #This is a simple calculator with basic arithmetic operations which enables user to input numbers, an operation choice and displays the result.

#Import everything from tkinter module
from tkinter import *
from math import sqrt

root = Tk()
root.title("Simple Calculator App") #Change GUI title
img = PhotoImage(file = "codsoft_taskno2/icons8-calculator-64.png") #Change GUI PhotoImage
root.iconphoto(False, img)


last_result = 0

#Function to display number on screen
def onclick(number):
    if FieldEntry.get() == "0" or FieldEntry.get() == "Error": #Check if display is 0 or Error
        FieldEntry.delete(0, END) #If 0 or Error, clear.
        FieldEntry.insert(END, number) #Insert new number
    else:
        FieldEntry.insert(END, number)

#Function to clear screen  
def ClearScreen():
    FieldEntry.delete(0, END)

#Function to delete numbers from screen    
def Delete():
    CurrentEntry = FieldEntry.get()
    if CurrentEntry:  #Check if Entry is not empty
        NewEntry = CurrentEntry[:-1]  #Remove the last number
        FieldEntry.delete(0, END)  
        FieldEntry.insert(0, NewEntry) #Insert changed entry onto the screen

#Primary Operation Functions     
def operations(op):
    first_number = FieldEntry.get()
    global f_num, operation #Define global variables for storing the first number and the operation.
    operation = op #Store parameter in a global variable
    f_num = float(first_number) #Store local variable in a global variable
    FieldEntry.delete(0, END)

#Secondary Operation Functions 
def secondary_operations(sec_operation):
    number = float(FieldEntry.get()) #Store float inside local variable
    FieldEntry.delete(0, END)
    if sec_operation == "square":
        output = number*number
    elif sec_operation == "squareroot":
        output = sqrt(number)
    elif sec_operation == "oneover":
        output = 1/number
    else:
        FieldEntry.insert(0, "Error")

    #Check if the number is an integer or not
    if output % 1 == 0:
        FieldEntry.insert(0, int(output))  #Display as integer if no decimal part
    else:
        FieldEntry.insert(0, f"{output:.2f}") #Display as float with 2 decimal places if there is a decimal part
        

#Equal Sign Function
def equal():
    #Declare three global variables, one for first number inputted, second for the operation type, and third for storing the last result gotten from the function.
    global f_num, operation, last_result 
    second_number = float(FieldEntry.get())
    FieldEntry.delete(0, END)
    #If statement for the primary operation conditions
    if operation == "add": 
        result = f_num + second_number
    elif operation == "subtract":
        result = f_num - second_number
    elif operation == "multiply":
        result = f_num * second_number
    elif operation == "divide":
        if second_number != 0:
            result = f_num / second_number
        else:
            FieldEntry.insert(0, "Cannot divide by zero") #If the second number inputted is 0, print error message.
            return
    else:
        FieldEntry.insert(0, "Error")
        return
    
    last_result = float(result) #Storing the result of equal to operation inside a variable
    
    #Check if the number is an integer or not
    if result % 1 == 0:
        FieldEntry.insert(0, int(result))  #Display as integer if no decimal part
    else:
        FieldEntry.insert(0, f"{result:.2f}")  #Display as float with 2 decimal places if there is a decimal part
        
      
    
def percentage():
    global last_result #Declare last result global variable
    current_value = float(FieldEntry.get()) #Get current value
    if not current_value: #Case Handling if field is empty
        FieldEntry.insert(0, "0") 
        return
    
    result = (last_result * current_value) / 100 #Calculate the percentage
    FieldEntry.delete(0, END) #Clear the last result
    
    if result % 1 == 0:
        FieldEntry.insert(0, int(result))  #Display as integer if no decimal part
    else:
        FieldEntry.insert(0, f"{result:.2f}")  #Display as float with 2 decimal places if there is a decimal part
    

#Initialize Entry Widget    
FieldEntry = Entry(root, width= 20, border=3, justify="right")


#Initialize Buttons
Button1 = Button(root, text="%", pady=20, width=10, command=percentage)
Button2 = Button(root, text="CE", width=10, pady=20, command=ClearScreen)
Button3 = Button(root, text="C", width=10, pady=20, command=ClearScreen)
Button4 = Button(root, text="DEL", width=10, pady=20, command=Delete)

Button5 = Button(root, text="1/x", width=10, pady=20, command=lambda:secondary_operations("oneover"))
Button6 = Button(root, text="x²", width=10, pady=20, command=lambda:secondary_operations("square"))
Button7 = Button(root, text="2√x", width=10, pady=20, command=lambda:secondary_operations("squareroot"))
Button8 = Button(root, text="/", width=10, pady=20, command=lambda:operations("divide"))

Button9 = Button(root, text="7", width=10, pady=20, command=lambda:onclick("7"))
Button10 = Button(root, text="8", width=10, pady=20, command=lambda:onclick("8"))
Button11 = Button(root, text="9", width=10, pady=20, command=lambda:onclick("9"))
Button12 = Button(root, text="x", width=10, pady=20, command=lambda: operations("multiply"))

Button13 = Button(root, text="4", width=10, pady=20, command=lambda:onclick("4"))
Button14 = Button(root, text="5", width=10, pady=20, command=lambda:onclick("5"))
Button15 = Button(root, text="6", width=10, pady=20, command=lambda:onclick("6"))
Button16 = Button(root, text="-", width=10, pady=20, command=lambda:operations("subtract"))

Button17 = Button(root, text="1", width=10, pady=20, command=lambda:onclick("1"))
Button18 = Button(root, text="2", width=10, pady=20, command=lambda:onclick("2"))
Button19 = Button(root, text="3", width=10, pady=20, command=lambda:onclick("3"))
Button20 = Button(root, text="+", width=10, pady=20, command=lambda:operations("add"))

Button21 = Button(root, text="+/-", width=10, pady=20, command=lambda:onclick("-"))
Button22 = Button(root, text="0", width=10, pady=20, command=lambda:onclick("0"))
Button23 = Button(root, text=".", width=10, pady=20, command=lambda:onclick("."))
Button24 = Button(root, text="=", background="#be2ed6", width=10, pady=20, command=equal)


#Display Entry and Button Widgets on screen
FieldEntry.grid(row = 0, columnspan=4, ipady=40, ipadx=96)

Button1.grid(row=1, column=0)
Button2.grid(row=1, column=1)
Button3.grid(row=1, column=2)
Button4.grid(row=1, column=3)

Button5.grid(row=2, column=0)
Button6.grid(row=2, column=1)
Button7.grid(row=2, column=2)
Button8.grid(row=2, column=3)

Button9.grid(row=3, column=0)
Button10.grid(row=3, column=1)
Button11.grid(row=3, column=2)
Button12.grid(row=3, column=3)

Button13.grid(row=4, column=0)
Button14.grid(row=4, column=1)
Button15.grid(row=4, column=2)
Button16.grid(row=4, column=3)

Button17.grid(row=5, column=0)
Button18.grid(row=5, column=1)
Button19.grid(row=5, column=2)
Button20.grid(row=5, column=3)

Button21.grid(row=6, column=0)
Button22.grid(row=6, column=1)
Button23.grid(row=6, column=2)
Button24.grid(row=6, column=3)


#Run the Main Loop
root.mainloop()

