    number = NumberEntry.get()
    email = EmailEntry.get()
    address = AddressEntry.get()
    
    NewContact = {
    "name": name,
    "number": number,
    "email": email,
    "address": address
    }
        
    contacts.append(NewContact)
    
    
    
    messagebox.showinfo("Message", "Contact Successfully Added")
    
    NameEntry.delete(0, END)
    NumberEntry.delete(0, END)
    EmailEntry.delete(0, END)
    AddressEntry.delete(0,END)
    

    
    
def ContactWindow(): 
    contact_window = Toplevel(root)
    contact_window.title("Contact List")
    contact_window.geometry("320x300")
    img = PhotoImage(file = "codsoft_taskno5/icons8-contact-48.png")
    contact_window.iconphoto(False, img)
    
    ContactList = Listbox(contact_window, width=40, height=10, border=None, activestyle="none", bg="lightgrey")
    ContactList.grid(row=0, columnspan=2, pady=20)
    
    def UpdateContactList():
        ContactList.delete(0, END)
        for contact in contacts:
            ContactString = f"Name: {contact['name']} - Phone Number: {contact['number']}"
            ContactList.insert(END, ContactString)
            
    UpdateContactList()
    
    def UpdateContact():
        ...
        
    def DeleteContact():
        selected_index = ContactList.curselection() #Assign selected task to variable
        if selected_index: #If task is in selection
            selected_index = selected_index[0]
            if 0 <= selected_index < len(contacts):
                contacts.pop(selected_index)
                ContactList.delete(selected_index)
        