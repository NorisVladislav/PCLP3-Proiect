
import pytest
from Problema1 import Employee, Manager  
def test_employee_creation():
    employee = Employee("GHERGHEL E", 50000)
    assert employee.name == "GHERGHEL E"
    assert employee.salary == 50001 
    assert employee.tasks == {}


def test_manager_creation():
    manager = Manager("VLADISLAV N", 80000, "IT")
    assert manager.name == "VLADISLAV N"
    assert manager.salary == 80001  
    assert manager.department == "D05_IT"
    assert manager.tasks == {}


def test_update_salary():
    employee = Employee("GHERGHEL E", 50000)
    employee.update_salary(55001) 
    assert employee.salary == 55000


def test_modify_task():
    employee = Employee("GHERGHEL E", 50000)
    employee.modify_task("Task1", "Completed")  
    assert "Task1" in employee.tasks
    assert employee.tasks["Task1"] == "In Progress"


