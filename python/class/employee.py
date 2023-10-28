from salary import Salary


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.aggregate_salary = salary

    def total_salary(self):
        return self.aggregate_salary.anual_salary()


salary1 = Salary(10000, 700)
emp = Employee('João', 30, salary1)
print(emp.total_salary())
