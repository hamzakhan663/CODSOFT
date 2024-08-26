from tkinter import *

#Functions
def on_click(TaskOperation):
    global selected_index, is_editing
    operation = TaskOperation
    if operation == "ADD":
        if is_editing:
            # If already editing, don't do anything
            return
        if FirstEntry.get():
            NewTask = FirstEntry.get()
            FirstListBox.insert(0, NewTask)
            FirstEntry.delete(0, END)
            is_editing = False
        else:
            return
        
    elif operation == "DELETE":
        if is_editing:
            # If already editing, don't do anything
            return
        selected_index = FirstListBox.curselection()
        if selected_index:
            for index in reversed(selected_index):
                FirstListBox.delete(index)
                
                
                
    elif operation == "EDIT":
        if is_editing:
            # If already editing, don't do anything
            return
        selected_indices = FirstListBox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            SelectedTask = FirstListBox.get(selected_index)
            FirstEntry.delete(0, END)
            FirstEntry.insert(0, SelectedTask)
            is_editing = True
       
        
def save():       
    global selected_index, is_editing
    if selected_index is not None:
        EditedTask = FirstEntry.get()
        if EditedTask:
            FirstListBox.delete(selected_index)  # Remove the old task
            FirstListBox.insert(selected_index, EditedTask)  # Insert the updated task
        FirstEntry.delete(0, END)  # Clear the Entry widget
        selected_index = None  # Reset the selected index
        is_editing = False


#Create the main widget
root = Tk()
root.title("To-Do List App")
img = PhotoImage(file = "To-Do List/icons8-todo-list-64.png")
root.iconphoto(False, img)

selected_index = None
is_editing = False


#Widgets Initialization   
FirstLabel = Label(root, text="Input New Task")
SecondLabel = Label(root, text="")
FirstEntry = Entry(root, border=3, justify="left", width = 64, bd=3, relief="raised")
FirstListBox = Listbox(root, width=100, height=10, border=None, activestyle="none", font = ("Century", 12), background="#22828A", selectbackground= "#1E2C45" , selectforeground="White")




FirstButton = Button(root, text = "Add Task", width=20, command= lambda: on_click("ADD"), bd=3, relief="raised", bg="#8256B1")
SecondButton = Button(root, text = "Edit Task", width=20, command= lambda: on_click("EDIT"), bd=3, relief="raised")
ThirdButton = Button(root, text = "Delete Task", width=20, command= lambda: on_click("DELETE"), bd=3, relief="raised", bg="#8256B1")
FourthButton = Button(root, text = "Save Task", width=10, command= save, bd=3, relief="raised")



#App Layout
FirstLabel.grid(row = 0, columnspan=3)
SecondLabel.grid(row = 4, columnspan=1)
FirstEntry.grid(row=1, columnspan=3)
FirstListBox.grid(row=2, columnspan=3)


FirstButton.grid(row=3, column=0)
SecondButton.grid(row=3, column=1)
ThirdButton.grid(row=3, column=2)
FourthButton.grid(row=5, column=1)

root.mainloop()