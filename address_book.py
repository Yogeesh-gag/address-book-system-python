from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def addContact(self):
        print("\nEnter contact details: ")
        fields = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "phone", "email"]
        values = [input(f"{field}: ") for field in fields]

        contact = Contact(*values)
        self.contacts.append(contact)
        print("Contact added successfully")