# Contact Book using Python

# Define a list to store contacts
contacts = []

# Function to add a new contact
def add_contact(name, phone, email):
    contact = {'name': name, 'phone': phone, 'email': email}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to delete a contact by name
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    print("Contact deleted successfully!")

# Function to update a contact's details by name
def update_contact(name, phone=None, email=None):
    for contact in contacts:
        if contact['name'] == name:
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            print("Contact updated successfully!")
            return
    print("Contact not found!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Main function to handle user input
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. View Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            view_contacts()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
