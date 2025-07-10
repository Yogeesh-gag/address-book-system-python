from address_book_manager import AddressBookManager
from address_book import AddressBook

def run_book_menu(book, manager):
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Add Multiple Contacts")
        print("5. Sort Contacts by Name")
        print("6. Sort Contacts by City/State/Zip")
        print("7. Save to Text File")
        print("8. Load from Text File")
        print("9. Save to CSV")
        print("10. Load from CSV")
        print("11. Save to JSON")
        print("12. Load from JSON")
        print("13. View All Contacts")
        print("14. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == '1':
            book.add_contact(manager)
        elif choice == '2':
            book.edit_contact()
        elif choice == '3':
            book.delete_contact()
        elif choice == '4':
            book.add_multiple_contacts(manager)
        elif choice == '5':
            book.sort_contacts_by_name()
        elif choice == '6':
            book.sort_contacts_by_field()
        elif choice == '7':
            filename = input("Enter filename to save (.txt): ")
            book.save_to_text_file(filename)
        elif choice == '8':
            filename = input("Enter filename to load (.txt): ")
            book.load_from_text_file(filename)
        elif choice == '9':
            filename = input("Enter filename to save (.csv): ")
            book.save_to_csv(filename)
        elif choice == '10':
            filename = input("Enter filename to load (.csv): ")
            book.load_from_csv(filename)
        elif choice == '11':
            filename = input("Enter filename to save (.json): ")
            book.save_to_json(filename)
        elif choice == '12':
            filename = input("Enter filename to load (.json): ")
            book.load_from_json(filename)
        elif choice == '13':
            book.view_contacts()
        elif choice == '14':
            break
        else:
            print("Invalid choice. Try again.")

def run_manager_menu(manager):
    while True:
        print("\nAddress Book System:")
        print("1. Create New Address Book")
        print("2. Select Existing Address Book")
        print("3. Search Person by City/State")
        print("4. View Persons by City/State")
        print("5. Count Persons by City/State")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            manager.create_address_book()
        elif choice == '2':
            manager.select_address_book()
        elif choice == '3':
            manager.search_person_by_city_or_state()
        elif choice == '4':
            manager.view_persons_by_city_or_state()
        elif choice == '5':
            manager.count_persons_by_city_or_state()
        elif choice == '6':
            print("Exiting Address Book System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    # Create default AddressBook and Manager
    default_book = AddressBook()
    manager = AddressBookManager()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Manage Default Address Book")
        print("2. Manage Multiple Address Books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            run_book_menu(default_book, manager)
        elif choice == '2':
            run_manager_menu(manager)
        elif choice == '3':
            print("Program Terminated.")
            break
        else:
            print("Invalid choice. Try again.")
