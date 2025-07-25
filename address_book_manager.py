
from collections import defaultdict

from address_book import AddressBook

class AddressBookManager:

    def __init__(self):
        self.books = {}
        self.city_person_map=defaultdict(list)
        self.state_person_map=defaultdict(list)
        # print(self.city_person_map.values())

    def create_address_book(self):
        name=input("Enter the unique name for the new address book: ")
        if name in self.books:
            print("Book is already found in the address book")
        else:
            self.books[name]=AddressBook()
            print(f"Address book created for {name}")
            return

    def select_address_book(self):
        if not self.books:
            print("No Address Books available")
            return

        print("Available Address Books:")
        for name in self.books:
            print(f"\t{name}")

        selected=input("Enter the name of the address book to use:")
        if selected in self.books:
            self.manage_address_book(self.books[selected])
        else:
            print("Address book not found")

    def manage_address_book(self, book):
        while True:
            print("\n--- Manage Address Book ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                book.add_contact(self)
            elif choice == "2":
                book.view_contacts()
            elif choice == "3":
                break
            else:
                print("Invalid choice")

    def search_person_by_city_or_state(self):
        if not self.books:
            print("No Address Books available")
            return

        criteria = input("Search by city or state?: ").strip().lower()
        if criteria not in ("city", "state"):
            print("Invalid choice")
            return
        value=input(f"Enter the {criteria.title()} name to search for: ").strip()

        for book_name,book in self.books.items():
            for contact in book.contacts:
                if (criteria=="city" and contact.city.lower()==value.lower()) or (criteria=="state" and contact.state==value.lower()):
                    print(f"Found in Address Book {book_name}")
                    contact.display_contact()
                else:
                    print(f"Not found in Address Book {book_name}")

    def view_persons_by_city_or_state(self):
        choice=input("View by city or state?:").strip().lower()

        if choice=="city":
            name=input("Enter the city name: ").strip().title()
            persons=self.city_person_map.get(name,[])
        elif choice=="state":
            name=input("Enter the state name: ").strip()
            persons=self.state_person_map.get(name,[])
        else:
            print("Invalid choice")
            return None

        if not persons:
            print(f"No persons found in {choice.title()} {name}.")
            return None

        print(f"\n Persons in {choice.title()}:{name}")
        for person in persons:
            person.display_contact()

        return persons,name

    def count_persons_by_city_or_state(self):
        persons,name=self.view_persons_by_city_or_state()
        if persons is None:
            return
        print(f"Total number of persons in {name}:{len(persons)}")

        print("Contact Numbers")
        for person in persons:
            print(f"{person.first_name} {person.last_name} {person.phone_number}")



