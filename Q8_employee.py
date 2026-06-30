# Program : Employee Management System
# Concepts: OOP, Dictionary, Tuple


# Employee Class
class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple

    # Method to display employee details
    def show_details(self):
        print("-" * 40)
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.details[0]}")
        print(f"Salary      : ₹{self.details[1]}")
        print("-" * 40)


# Dictionary to store Employee objects
employees = {}

# Input details of 3 employees
for i in range(1, 4):
    print(f"\nEnter Details of Employee {i}")

    emp_id = int(input("Employee ID : "))
    name = input("Name         : ")
    department = input("Department   : ")
    salary = float(input("Salary       : "))

    # Create Employee Object
    emp = Employee(emp_id, name, department, salary)

    # Store object in dictionary
    employees[emp_id] = emp


# Display Employee Details
print("\n" + "=" * 50)
print("👨‍💼 Employee Details")
print("=" * 50)

for emp in employees.values():
    emp.show_details()