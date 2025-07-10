import csv

from pywin.Demos.app.customprint import PrintDemoView

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

    def sort_contacts_by_name(self):
        if not self.contacts:
            print("No contacts added")
            return

        sorted_contacts = sorted(self.contacts, key=lambda c: c.first_name + " " + c.last_name)

        print("Contacts sorted alphabetically by  name ")
        for contact in sorted_contacts:
            contact.display_contact()

    def sort_contacts_by_field(self):
        if not self.contacts:
            print("No contacts to sort.")
            return

        field = input("Sort by City, State, or Zip Code? ").strip().lower()

        if field == "city":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.city.lower())
        elif field == "state":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.state.lower())
        elif field == "zip":
            sorted_contacts = sorted(self.contacts, key=lambda c: int(c.zip_code))
        else:
            print("Invalid field. Choose from City, State, or Zip.")
            return

        print(f"\nContacts sorted by {field.title()}:")
        for contact in sorted_contacts:
            contact.display_contact()

    def save_to_file(self,filename):
        try:
            with open(filename, "w") as file:
                for contact in self.contacts:
                    line=f"{contact.first_name}|{contact.last_name}|{contact.address}|{contact.city}|{contact.state}|{contact.zip_code}|{contact.phone_number}|{contact.email}"
                    file.write(line+"\n")
            print(f"Address book saved successfully to '{filename}'")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self,filename):
        try:
            with open(filename, "r") as file:
                self.contacts.clear()
                for line in file:
                    parts= line.strip().split("|")
                    if len(parts) == 8:
                        contact = Contact(*parts)
                        self.contacts.append(contact)
            print(f"Address book loaded successfully from '{filename}'")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_csv(self,filename):
        try:
            with open(filename, "w") as file:
                writer=csv.writer(file)

                writer.writerow(["First Name","Last Name","Address","City","State","Zip Code","Phone Number","Email"])
                for contact in self.contacts:
                    writer.writerow([
                        contact.first_name,
                        contact.last_name,
                        contact.address,
                        contact.city,
                        contact.state,
                        contact.zip_code,
                        contact.phone_number,
                        contact.email
                    ])
            print(f"Address book saved successfully to '{filename}' as CSV")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_csv(self,filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                self.contacts.clear()

                for line in reader:
                    if len(line) == 8:
                        contact = Contact(*line)
                        self.contacts.append(contact)

            print(f"Address book loaded successfully from '{filename}' as CSV \n")
            for contact in self.contacts:
                contact.display_contact()
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"Error loading file: {e}")

