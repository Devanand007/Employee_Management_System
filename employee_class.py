class Employee:
    """A class representing employee in an organization

    Attributes:
        name (str): the name of the employee
        employee_id (int): the id of the employee
        title (str): the job title of the employee
        department (str) the department to which employee belongs

    Method:
        emp_display(): prints the detail of the employee which includes name, ID, title,department
        __str__() : return formatted string containing employee name and ID

    Example usage:
        emp = Employee("Devanand", 670876, "Software Engineer", "IT")
        emp.emp_display()
        print(str(emp))
    """
    def __init__(self,name, employee_id, title, department):
        """Initialize an employee object  with name,id,title,department"""
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def emp_display(self):
        """print the details of the employee"""
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        """return formatted string containing employee name and ID"""
        return f"Employee Name: {self.name} , Employee_ID: {self.employee_id}"


if __name__ == "__main__":
    emp = Employee("Devanand", 670876, "Software Engineer", "IT")
    emp.emp_display()
    print(str(emp))
