class Salary:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def anual_salary(self):
        return (self.base*12) + self.bonus
