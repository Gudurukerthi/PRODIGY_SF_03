contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print()

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        phone = input("Enter the new phone number (or leave blank to keep the current one): ")
        email = input("Enter the new email address (or leave blank to keep the current one): ")
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, contact_info in contacts.items():
            file.write(f"{name},{contact_info['phone']},{contact_info['email']}\n")
    print("Contacts saved to contacts.txt.")

def load_contacts():
    global contacts
    try:
        with open("contacts.txt", "r") as file:
            contacts = {}
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
        print("Contacts loaded from contacts.txt.")
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")

def main():
    load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            save_contacts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
