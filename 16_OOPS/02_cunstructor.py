class Employee:
    company_name = "Tech Solutions"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

e1= Employee("Alice", 30, 50000) # An object of the class Employee is created with name "Alice", age 30, and salary 50000
e1.display_info() # This line calls the display_info method of the Employee object e1 and prints the employee's information.

#Object in interospection
print(dir(e1)) # This line prints the dictionary containing the object's attributes and their values.

print(Employee.company_name) # This line prints the value of the class attribute company_name, which is "Tech Solutions".
