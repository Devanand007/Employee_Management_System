from employee_class import Employee


class Department:
    """A class representing a department in an organization.

        Attributes:
            name (str): The name of the department.
            employees (list): A list of Employee objects representing employees in the department.

        Methods:
            add_employee(employee): Add an employee to the department.
            remove_employee(emp_id): Remove an employee from the department based on employee ID.
            list_employees(): List all employees in the department.

        Example usage:
            department = Department("IT")
            emp1 = Employee("Devanand", 670876, "Software Engineer", "IT")
            department.add_employee(emp1)
            department.list_employees()
            department.remove_employee(670876)
        """
    def __init__(self, name):
        """Initialize department object with name and an empty list of employees"""
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to the department"""
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """Remove an employee from the department"""
        for employee in self.employees:
            if employee.employee_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

    def list_employees(self):
        """List of all employees in the department"""
        for employee in self.employees:
            print(employee)


if __name__ == "__main__":
    department = Department("IT")
    emp1 = Employee("Devanand", 670876, "Software Engineer", "IT")
    emp2 = Employee("David", 123456, "Network Engineer", "IT")
    department.add_employee(emp1)
    department.add_employee(emp2)
    print("Employees in the IT department:")
    department.list_employees()
    print("Removing employee with ID 670876:")
    department.remove_employee(670876)
    print("Updated list of employees in the IT department:")
    department.list_employees()

