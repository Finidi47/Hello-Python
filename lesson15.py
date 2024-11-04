# inheritance
# error handling
# dates

class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob= dob
        self.gender = gender
    def print_details(self):
        print(f"Name: {self.name} ID:{self.id_number} DOB:{self.dob} Gender:{self.gender}")

