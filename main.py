from address_book_manager import AddressBookManager
from address_book import AddressBook

if __name__ == "__main__":
    #uc1-create addressbook class
    book = AddressBook()

    #uc2-adding contact to address book
    # book.add_contact()
    # book.add_contact()

    #uc3-editing the contact details in the address book
    # book.edit_contact()

    #uc4-delete contact in the address book
    # book.delete_contact()

    #uc5-add multiple contacts in the address book
    # book.add_multiple_contacts()

    #uc6-Multiple address book
    manager=AddressBookManager()


    # while True:
    #     print("\n=== Address Book System ===")
    #     print("1. Create New Address Book")
    #     print("2. Select Existing Address Book")
    #     print("3. Exit")
    #     choice = input("Enter your choice: ")
    #
    #     if choice == '1':
    #         manager.create_address_book()
    #     elif choice == '2':
    #         manager.select_address_book()
    #     elif choice == '3':
    #         print("Exiting Address Book System.")
    #         break
    #     else:
    #         print("Invalid choice. Try again.")

    #uc7-prevent duplicate entry of contact
    # book.add_contact()
    # book.add_contact()

    #uc8-search a person by city or state
    # manager.search_person_by_city_or_state()

    #uc9-search a person by state or city using dictionary mapping
    # manager.view_persons_by_city_or_state()

    #uc10-get contact number of person by city or person
    # manager.count_persons_by_city_or_state()


