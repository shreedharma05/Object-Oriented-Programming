class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward

    def annualSalary(self):
        return (self.pay * 12) + (self.reward)

class Employee:
    def __init__(self, name, role, ctc):
        self.name = name
        self.role = role
        self.ctc = ctc

    def costToCompany(self):
        return (self.ctc.annualSalary())

ctc = Salary(140000, 100000)
emp1 = Employee('Shree dharma','SDE1',ctc)
print(emp1.costToCompany())
