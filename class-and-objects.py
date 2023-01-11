class Employee:
    company = 'Company 1'

    def __init__(self, name, email, designation):
        self.name = name
        self.email = email
        self.designation = designation

    def display(self):
        print("Name of employee is", self.name)
        print("Designation of employee is", self.designation)

    @classmethod
    def company_intro(cls):
        print("Welcome to the company..", cls.company)


emp1 = Employee('Employee 1', 'employee1@gmail.com', 'Software Engineer')
emp1.display()
emp2 = Employee('Employee 2', 'employee2@gmail.com', 'Web Designer')
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

vehicle1 = Vehicle()
vehicle1.name = 'City'
vehicle1.model = '2023'
vehicle1.shape = 'SUV'
vehicle1.display()
