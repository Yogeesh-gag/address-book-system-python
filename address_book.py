from contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self,manager=None):
        print("\nEnter contact details: ")
        fields = ["First Name", "Last Name", "Address", "City", "State", "Zip Code", "phone", "email"]
        values = [input(f"{field}: ") for field in fields]
        first_name,last_name = values[0], values[1]

        if any(c.first_name==first_name and c.last_name==last_name for c in self.contacts):
            print("\nDuplicate contact. A person with this name already exists.")
            return

        contact = Contact(*values)
        self.contacts.append(contact)
        print("Contact added successfully")

        if manager:
            manager.city_person_map[contact.city].append(contact)
            manager.state_person_map[contact.state].append(contact)
            print("person add to dictionary")


    def edit_contact(self):
        print("\n--------Editing Contact Details--------")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")

        for contact in self.contacts:
            if contact.first_name == first and contact.last_name == last:
                print("Current contact details: ")
                contact.display_contact()

                print("Enter new contact details(leave blank to continue): ")
                contact.first_name = input(f"First Name: ") or contact.first_name
                contact.last_name = input(f"Last Name: ") or contact.last_name
                contact.address = input(f"Address: ") or contact.address
                contact.city = input(f"City: ") or contact.city
                contact.state = input(f"State: ") or contact.state
                contact.zip_code = input(f"Zip Code: ") or contact.zip_code
                contact.phone_number = input(f"Phone: ") or contact.phone_number
                contact.email = input(f"Email: ") or contact.email

                print("Contact details updated successfully")
                return

        print("Contact details not found.")

    def delete_contact(self):
        print("\n--------Deleting Contact Details--------")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")

        for contact in self.contacts:
            if contact.first_name == first and contact.last_name == last:
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
        print("Contact not found.")

    def add_multiple_contacts(self):
        while True:
            self.add_contact()
            cont = input("Do you want to add another contact? (y/n): ")
            if cont != "y":
                break

    def view_contacts(self):
        if not self.contacts:
            print("No contacts added")
        else:
            print("Contacts List: ")
            for contact in self.contacts:
                contact.display_contact()