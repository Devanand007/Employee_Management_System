class Employee:
    def __init__(self,name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def emp_display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Title: {self.title}")
        print(f"Department: {self.department}")

    def __str__(self):
        return f"Employee Name: {self.name} , Employee_ID: {self.employee_id}"


if __name__ == "__main__":
    emp = Employee("Devanand", 670876, "Software Engineer", "IT")
    emp.emp_display()
    print(str(emp))
