class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward

    def annualSalary(self):
        return (self.pay * 12) + (self.reward)

class Employee:
    def __init__(self, name, role, pay, reward):
        self.name = name
        self.role = role
        self.ctc = Salary(pay, reward)

    def costToCompany(self):
        return (self.ctc.annualSalary())

emp1 = Employee('Shree dharma','SDE1',140000, 100000)
print(emp1.costToCompany())
