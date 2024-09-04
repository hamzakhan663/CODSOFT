from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Contact Book")
img = PhotoImage(file = "codsoft_taskno5/icons8-contact-48.png")
root.iconphoto(False, img)


contacts = []
is_editing = False


def ClearEntries():
    NameEntry.delete(0, END)
    NumberEntry.delete(0, END)
    EmailEntry.delete(0, END)
    AddressEntry.delete(0, END)

def AddContact():
    global is_editing
    name = NameEntry.get()
    number = NumberEntry.get()
    email = EmailEntry.get()
    address = AddressEntry.get()
    
    if is_editing:
            # If already editing, don't do anything
            return
    if name and number:
        NewContact = {
        "name": name,
        "number": number,
        "email": email,
        "address": address
        }
            
        contacts.append(NewContact)
        messagebox.showinfo("Message", "Contact Successfully Added")
   
    
    
        ClearEntries()
        is_editing = False
    
    else:
        messagebox.showwarning("Warning", "Name and Phone Number fields cannot be empty")
    
    print(contacts)
    
def ContactWindow(): 
    contact_window = Toplevel(root)
    contact_window.title("Contact List")
    contact_window.geometry("320x278")
    img = PhotoImage(file = "codsoft_taskno5/icons8-contact-48.png")    
    contact_window.iconphoto(False, img)
    ContactList = Listbox(contact_window, width=40, height=10, border=None, activestyle="none", bg="lightgrey")
    ContactList.grid(row=0, columnspan=2, pady=20)
        
    
    def UpdateContactList():
        ContactList.delete(0, END)
        for contact in contacts:
            ContactString = f"Name: {contact['name']} - Phone Number: {contact['number']}"
            ContactList.insert(END, ContactString)
            
            
            
    
    
    def UpdateContact():
        global is_editing, selected_index
        selected_indices = ContactList.curselection() #Assign selected tasks to variable
        if is_editing:
            # If already editing, don't do anything
            return
        if selected_indices:
            selected_index = selected_indices[0] #Assign first item in tuple to variable
            contact = contacts[selected_index]
            
            ClearEntries()
            NameEntry.insert(0, contact['name'])
            NumberEntry.insert(0, contact['number'])
            EmailEntry.insert(0, contact['email'])
            AddressEntry.insert(0, contact['address'])
            AddContactButton.config(text="Save Changes", command=SaveContact)
            
            is_editing = True
            
    def SaveContact():
        global is_editing, selected_index
        original_contact = contacts[selected_index]
        
        updated_contact = {
            "name": NameEntry.get(),
            "number": NumberEntry.get(),
            "email": EmailEntry.get(),
            "address": AddressEntry.get(),
        }
        
        if original_contact != updated_contact:
            contacts[selected_index] = updated_contact
        
            UpdateContactList()
            messagebox.showinfo("Message", "Contact Successfully Updated")
            ClearEntries()
            contact_window.destroy()
            
            is_editing = False
        
        else:
        # If there's no change, show a message
            messagebox.showinfo("Message", "No changes detected")
        
        AddContactButton.config(text = "Add Contact", command=AddContact)
        
        
    def DeleteContact():
        global is_editing, selected_index
        selected_index = ContactList.curselection() #Assign selected task to variable
        if is_editing:
            # If already editing, don't do anything
            return
        if selected_index: #If task is in selection
            selected_index = selected_index[0]
            if 0 <= selected_index < len(contacts):
                contacts.pop(selected_index)
                ContactList.delete(selected_index)
                UpdateContactList()
        
                
    UpdateContactList()            
    
    
    UpdateContactButton = Button(contact_window, text="Update Contact", bg="#8256B1", command=UpdateContact)
    DeleteContactButton = Button(contact_window, text="Delete Contact", bg="#8256B1", command=DeleteContact)
    
    
    UpdateContactButton.grid(row = 1, column = 0, padx=10)
    DeleteContactButton.grid(row = 1, column = 1, padx=10)
    
    
    

#Initialization of widgets

NameLabel = Label(root, text="Enter Name")
NameEntry = Entry(root)

NumberLabel = Label(root, text="Enter Phone Number")
NumberEntry = Entry(root)

EmailLabel = Label(root, text="Enter Email Address")
EmailEntry = Entry(root)

AddressLabel = Label(root, text="Enter Home Address")
AddressEntry = Entry(root)

AddContactButton = Button(root, text="Add Contact", command = AddContact, bg="#8256B1")
ViewContactButton = Button(root, text="View Contact", command = ContactWindow)







#Layout of widgets

NameLabel.grid(row=0, columnspan=3)
NameEntry.grid(row=1, columnspan=3)

NumberLabel.grid(row=2, columnspan=3)
NumberEntry.grid(row=3, columnspan=3)

EmailLabel.grid(row=4, columnspan=3)
EmailEntry.grid(row=5, columnspan=3)

AddressLabel.grid(row=6, columnspan=3)
AddressEntry.grid(row=7, columnspan=3, pady=10)

AddContactButton.grid(row = 8, column = 0, padx=10)
ViewContactButton.grid(row = 8, column = 1, padx=10)

root.mainloop()