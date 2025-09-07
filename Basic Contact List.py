# This is the list where I will store all of the contact dictionaries.
contacts = [
    {
        "name": "Bob",
        "phone": "555-9876"
    },
    {
        "name": "Carol",
        "phone": "555-3333"
    }
]

# This loops the program with a menu display that allows the user to choose an option
while True:
    print("""---Contact List Menu---
          1. Add a New Contact
          2. View all Contacts
          3. Quit""")
    choice = input("Select Your Choice: ")
    
    # If the user chooses '1', we ask for the new contact's details.
    if choice == "1":
        newName = input("What is the name? ")
        newNumber = input("What is the phone number? ")
        newContact = {"name": newName, "phone": newNumber}

        contacts.append(newContact)
        
    # If the user chooses '2', it prints the contact list.
    elif choice == "2":
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    
    # If the user chooses '3' then the while loop breaks and the program exits
    elif choice == "3":
        print("Goodbye!")
        break