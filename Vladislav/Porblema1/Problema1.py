#X=VLADISLAV
#Y=NORIS VICTOR

class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"\nTotal number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    """Class representing a manager, inheriting from Employee"""
    mgrCount = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"D05_{department}"
        Manager.mgrCount += 1

    def display_emp_count(self):
        "Displays the number of managers"
        print(f"Total number of manager(s) is {Manager.mgrCount}")

    def display_employee(self):
        print("Name: ", self.name)

    def __del__(self):
        Manager.mgrCount -= 1

    def display_manager(self):
        print("Name: ", self.name, ", Salary: ", self.salary, ", Department: ", self.department)


# Crearea a 2 obiecte ale clasei Employee
employee1 = Employee("GHERGHEL E", 50000)
employee2 = Employee("SIMIONESCU R", 60000)

# Crearea a 3 obiecte ale clasei Manager
manager1 = Manager("VLADISLAV N", 80000, "IT")
manager2 = Manager("NEACSU A", 75000, "HR")
manager3 = Manager("BUZDEA M", 85000, "Marketing")

# Apelarea metodei 'display_employee' pentru obiectele din clasa Employee
print("Total employees:")
employee1.display_employee()
employee2.display_employee()

# Apelarea metodei 'display_manager' pentru obiectele din clasa Manager
print("\nTotal managers:")
manager1.display_employee()
manager2.display_employee()
manager3.display_employee()

# Afișarea valorii atributului 'empCount' pentru o instanță a clasei Employee și pentru una a clasei Manager
employee1.display_emp_count()
manager1.display_emp_count()

