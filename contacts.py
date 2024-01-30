contact = {}

def display_contact():
    print("Name\t\tcontact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input(" 1. Add new contact \n 2.Search contact \n 3. Display contact \n 4. Update contact \n 5. Delete contact \n Enter ur choice: "))
    if choice == 1:
        name = input("\nEnter contact Name: ")
        number = input("Enter contact number: ")
        contact[name] = number
        print("Contact added successfully...\n")
    
    elif choice == 2:
        search_contact = input("\nEnter contact name: ")
        if search_contact in contact:
            print(search_contact,"'s contact number is",contact[search_contact])
        else:
            print("Contact not found")
            
    elif choice == 3:
        display_contact()
        
    elif choice == 4:
        edit_contact = input("Enter the contact name to edit: ")
        if edit_contact in contact:
            number = input("\nEnter mobile number: ")
            contact[edit_contact] = number
            print("Contact Updated successfully...")
            
    elif choice == 5:
        del_contact = input("Enter the contact to delete: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n: ")
            if confirm == "y" or confirm == "Y":
                contact.pop(del_contact)
                print("Contact deleted successfully...\n")
            display_contact()
    
    else:
        break