import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter contact phone: ").strip()
    email = input("Enter contact email: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact with this name already exists!")
            return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

def search_contact(contacts):
    name = input("Enter contact name to search: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: {contact}")
            return
    print("Contact not found!")

def update_contact(contacts):
    name = input("Enter contact name to update: ").strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            new_name = input(f"Enter new name (current: {contact['name']}): ").strip()
            if new_name:
                # Check if the new name already exists
                for c in contacts:
                    if c['name'].lower() == new_name.lower() and c != contact:
                        print("Contact with this name already exists!")
                        return
                contact['name'] = new_name

            phone = input(f"Enter new phone (current: {contact['phone']}): ").strip()
            email = input(f"Enter new email (current: {contact['email']}): ").strip()

            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email

            print("Contact updated successfully!")
            return
    print("Contact not found!")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            save_contacts(contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
