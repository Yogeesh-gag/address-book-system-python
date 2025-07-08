
class Contact:

    def __init__(self, first_name, last_name, address,city, state, zip_code,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def display_contact(self):
        details={
            "Name":f"{self.first_name} {self.last_name}",
            "Address":f"{self.address},{self.city},{self.state},{self.zip_code}",
            "Phone Number":f"{self.phone_number}",
            "Email":f"{self.email}"
        }
        for key,value in details.items():
            print(f"{key}: {value}")

