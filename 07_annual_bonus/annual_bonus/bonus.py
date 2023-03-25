class AnnualBonus:
    """Class that calculates annual bonus for employee"""

    def __init__(self, first_name, last_name, employee_id, annual_salary, annual_assessment):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.annual_salary = annual_salary
        self.annual_assessment = annual_assessment

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def email(self):
        return f"{self.first_name.lower()}{self.last_name.lower()}{self.employee_id}@fz.pl"

    def calculate_bonus(self):
        return (self.annual_salary * (self.annual_assessment - 100)/100)

ann = AnnualBonus("Michal", "Zak", "", 60000, 105)
ann2 = AnnualBonus("Michal", "Zak", "1", 70000, 106)


# print(ann, ann.email, ann.calculate_bonus())
# print(ann2, ann2.email, ann2.calculate_bonus())
