from department_class import Department, Employee


class Company:
    """A class representing a company.

    Attributes:
        departments (dict): A dictionary where department names are keys and Department objects are values.

    Methods:
        add_department(department): Add a department to the company.
        remove_department(department_name): Remove a department from the company based on its name.
        display_departments(): Display all departments in the company.

    Example usage:
        company = Company()
        department = Department("IT")
        emp1 = Employee("Devanand", 670876, "Software Engineer", "IT")
        department.add_employee(emp1)
        company.add_department(department)
        company.display_departments()
        company.remove_department("IT")
    """
    def __init__(self):
        """Initialize a company object with an empty dictionary of departments."""
        self.departments = {}

    def add_department(self, department_local):
        """Add a department to the company"""
        self.departments[department_local.name] = department_local

    def remove_department(self, department_name):
        """ Remove the department from the company"""
        if department_name in self.departments:
            del self.departments[department_name]
            return True
        return False

    def display_departments(self):
        """Display all department_local in the company"""
        for department_name, department_local in self.departments.items():
            print(f"Department: {department_name} ")
            department_local.list_employees()
            print()


if __name__ == "__main__":
    company = Company()
    department = Department("IT")
    emp1 = Employee("Devanand", 670876, "Software Engineer", "IT")
    department.add_employee(emp1)
    company.add_department(department)
    company.display_departments()
    company.remove_department("IT")
