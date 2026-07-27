# Class: Class is a blueprint for creating objects. It defines a set of attributes 
# and methods that the created objects will have. 
# In Python, classes are defined using the `class` keyword.

#Object: An object is an instance of a class. It is created from the class blueprint and can have 
# its own unique values for the attributes defined in the class.

class Employee:
    # Class attribute
    company_name = "Tech Solutions"

    def get_salary(self):
        return 340

e= Employee() # A object of the class Employee is created and assigned to the variable e
print(e.get_salary()) # This line calls the get_salary method of the Employee object e and prints the returned value, which is 340.

