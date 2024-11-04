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

class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender)
        self.salary = salary
    def print_salary(self):
        print(f"Salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender,hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly rate is {self.hourly_pay}")

    def end_date(self):
        print(f"End date is {self.end_date}")
