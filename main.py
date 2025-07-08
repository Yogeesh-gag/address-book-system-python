from address_book import AddressBook

if __name__ == "__main__":
    #uc1-create addressbook class
    book = AddressBook()

    #uc2-adding contact to address book
    book.addContact()

    #uc3-editing the contact details in the address book
    book.edit_contact()

    #uc4-delete contact in the address book
    book.delete_contact()