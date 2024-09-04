from tkinter import *
from tkinter import messagebox


contacts = [] #List of contacts stored as dictionaries
is_editing = False #editing flag for Updating contacts
filtered_contacts = [] #List of contacts currently showing in listbox after search


#Function to delete all entry fields
def ClearEntries():
    NameEntry.delete(0, END)
    NumberEntry.delete(0, END)
    EmailEntry.delete(0, END)
    AddressEntry.delete(0, END)

#Function to Add a new contact
def AddContact():
    global is_editing #Declare global variable
    
    #Store Entry values inside variables
    name = NameEntry.get()
    number = NumberEntry.get()
    email = EmailEntry.get()
    address = AddressEntry.get()
    
    if is_editing:
            # If already editing, don't do anything
            return
        
        #If name and number fields are not empty
    if name and number:
        #Store input into dictionary
        NewContact = {
        "name": name,
        "number": number,
        "email": email,
        "address": address
        }
            
        #Store the new contact in the contact list
        contacts.append(NewContact)
        
        
        #Pop up message
        messagebox.showinfo("Message", "Contact Successfully Added")

    
        #Call Function to Delete Entry Fields
        ClearEntries()
        is_editing = False #Reset Button to normal state
    
    else:
        messagebox.showwarning("Warning", "Name and Phone Number fields cannot be empty")
    
    
#Function to display contact information in another window
def ContactWindow(): 
    global is_editing
    
    contact_window = Toplevel(root)
    contact_window.title("Contact List")
    contact_window.geometry("360x350")
    img = PhotoImage(file = "codsoft_taskno5/icons8-contact-48.png")    
    contact_window.iconphoto(False, img)
    
   ###################### SEARCH FUNCTION ################################
   
    def SearchContact():       
        global is_editing
        
        SearchTerm = SearchEntry.get().lower() #name/number to be searched
        
        
        matches_found = [contact for contact in contacts if SearchTerm in contact['name'].lower() or SearchTerm in contact['number'].lower()] #for each contact in contacts list if name/number searched is in contact list, add contact to list "matches_found"
        
        #if matches_found list is not empty, populate listbox with matches_found list (searched contact)
        if matches_found:
            UpdateContactList(matches_found)
        else:
            messagebox.showwarning("Warning", "Contact Does Not Exist") 
            
            
                
   #Initialization for Search Widgets
    SearchEntry = Entry(contact_window)
    SearchButton = Button(contact_window, text="Search", command=SearchContact)


    SearchEntry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")  # `sticky="ew"` makes it expand horizontally
    SearchButton.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
        
    #################### LISTBOX UPDATE FUNCTION ################################
    
    ContactList = Listbox(contact_window, width=40, height=10, border=None, activestyle="none", bg="lightgrey")
    ContactList.grid(row=2, columnspan=2, pady=20, sticky="ew")
        
    #Populate contact listbox with information from contact list
    def UpdateContactList(search_results):
        ContactList.delete(0, END) #Clearing List to prevent duplicates
        
        if search_results is None: 
            search_results = contacts #if no search results are provided, listbox shows all contacts
            
        global filtered_contacts
        filtered_contacts = search_results #value of search results stored in variable, whether filtered or full list
        
        #Loop through filtered contact list
        for contact in filtered_contacts:
            ContactString = f"Name: {contact['name']} - Phone Number: {contact['number']}" #Contact List String Format
            ContactList.insert(END, ContactString)
            
            
    ########################## UPDATE CONTACT FUNCTION ########################      
    
    
    def UpdateContact():
        global is_editing, selected_index
         
        selected_indices = ContactList.curselection() #Assign selected tasks to variable
        if is_editing:
            # If already editing, don't do anything
            return
        if selected_indices:
            selected_index = selected_indices[0] #Assign first item in tuple to variable
            
            #If there's a contact in filtered contact list i.e if you are performing a search, store selected index of filtered contact in contact variable ELSE store selected index of contact list in contact variable
            if filtered_contacts:
                contact = filtered_contacts[selected_index]
            else:
                contact = contacts[selected_index] #Assign selected item in contact list to variable
            
            ClearEntries() #Delete all values in entry fields
            
            #Insert Information from contact list into entry fields for updating 
            NameEntry.insert(0, contact['name'])
            NumberEntry.insert(0, contact['number'])
            EmailEntry.insert(0, contact['email'])
            AddressEntry.insert(0, contact['address'])
            
            AddContactButton.config(text="Save Changes", command=SaveContact)
            
            is_editing = True #Editing flag changed to show editing mode
        else:
            messagebox.showwarning("Warning", "Please select a contact to update")    
    
    ################### SAVE CONTACT INFORMATION #################
    
    
    #Function to Save Contact Information after Updating      
    def SaveContact():
        global is_editing, selected_index
    
        if is_editing: 
    # Determine which contact to update based on whether search results are being used
    # If `filtered_contacts` is not empty, get the contact from `filtered_contacts` using `selected_index`.
    # If `filtered_contacts` is empty, get the contact from the full `contacts` list using `selected_index`.

            if filtered_contacts:
                contact_to_update = filtered_contacts[selected_index]
            else:
                contact_to_update = contacts[selected_index]  # Contact information prior to Updating

        # Contact information after Updating
            updated_contact = {
                "name": NameEntry.get(),
                "number": NumberEntry.get(),
                "email": EmailEntry.get(),
                "address": AddressEntry.get(),
        }
        
    # Update the contact in the full `contacts` list.
    # If working with `filtered_contacts`, find the original index in `contacts` and update it.
    # If no search filter is applied (`filtered_contacts` is empty), directly update the contact at `selected_index`.
            if filtered_contacts:
                original_index = contacts.index(contact_to_update)
                contacts[original_index] = updated_contact
            else:
                contacts[selected_index] = updated_contact
        
            UpdateContactList(filtered_contacts if filtered_contacts else contacts)  # Reflect changes made to the contact information in the contact ListBox
            messagebox.showinfo("Message", "Contact Successfully Updated") 
            ClearEntries()  # Delete values in the entry fields
            contact_window.destroy()
        
            AddContactButton.config(text="Add Contact", command=AddContact)
        
            is_editing = False  # Reset editing state
    
        else:
        # If there's no change, show a message
            messagebox.showinfo("Message", "No changes detected")
            AddContactButton.config(text="Save Changes", command=SaveContact)
            is_editing = False  # Reset editing state

        
            
            
            
           

            
        
    ################# DELETE CONTACT INFORMATION ######################
    
    #Function to Delete Contact
    def DeleteContact():
        global is_editing, selected_index
        selected_indices = ContactList.curselection()  # Assign selected task to variable
        
        if is_editing:
            # If already editing, don't do anything
            return
        
        if selected_indices:  # If a task is selected
            selected_index = selected_indices[0]  # Assign index in tuple to variable
            
            # Get the contact to delete from the contacts list using selected index
            if filtered_contacts:
                contact_to_delete = filtered_contacts[selected_index]  # Contact to delete from filtered_contacts
                
                # Remove the contact from the full contacts list
                if contact_to_delete in contacts:
                    contacts.remove(contact_to_delete) 

                # Remove the contact from the filtered_contacts list
                if contact_to_delete in filtered_contacts:
                    filtered_contacts.remove(contact_to_delete)  
                
            else:
                contact_to_delete = contacts[selected_index]  # Get the contact to delete from contacts
                
                # Remove the contact from the full contacts list
                contacts.pop(selected_index)  
                
            # Update the contact list box to reflect changes
            UpdateContactList(filtered_contacts if filtered_contacts else contacts)
            
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete")
    UpdateContactList(contacts)

    
    #Update and Delete Button Widget Initialization
    
    UpdateContactButton = Button(contact_window, text="Update Contact", bg="#8256B1", command=UpdateContact, width = 20)
    DeleteContactButton = Button(contact_window, text="Delete Contact", bg="#8256B1", command=DeleteContact, width = 20)
    
    #Update and Delete Button Widget Layout
    UpdateContactButton.grid(row=3, column=0, sticky="ew", padx=5)
    DeleteContactButton.grid(row=3, column=1, sticky="ew", padx =5)
    
    
    

#Main Window

root = Tk()
root.title("Contact Book")
img = PhotoImage(file = "codsoft_taskno5/icons8-contact-48.png")
root.iconphoto(False, img)


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



