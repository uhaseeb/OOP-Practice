class Employee:
    company = 'Cogent Labs'
    company_location = 'Lahore'
    __company_employees = 500

    def __init__(self, name, email, designation, company):
        self.name = name
        self.email = email
        self.designation = designation
        self.company = company

    def display(self):
        print("Name of employee is", self.name)
        print("Email of employee is", self.email)
        print("Designation of employee is", self.designation)
        print("My company is:", self.company)
        print("Company employees are", self.__company_employees)

    @classmethod
    def company_intro(cls):
        print("Welcome to the company..", cls.company)


emp1 = Employee('Employee 1', 'employee1@gmail.com', 'Software Engineer', 'Paramsync')
print(emp1.company_location)
emp1.company_location = 'Karachi'
print(emp1.company_location)
emp1.display()

emp2 = Employee('Employee 2', 'employee2@gmail.com', 'Web Designer', 'Flync')
emp2.display()
Employee.company_intro()


class Vehicle:
    type = 'Car'

    def display(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Shape:", self.shape)
        print("type:", self.type)


vehicle1 = Vehicle()
vehicle1.name = 'Zest'
vehicle1.model = '2023'
vehicle1.shape = 'SUV'
vehicle1.type = 'Jeep'
vehicle1.display()

vehicle2 = Vehicle()
vehicle2.name = 'City'
vehicle2.model = '2023'
vehicle2.shape = 'SUV'
vehicle2.display()
