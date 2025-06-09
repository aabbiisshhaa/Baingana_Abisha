class Developer:
    def skills(self):
        print("- Software Developer: Writing efficient code")
        super().skills()

class Designer:
    def skills(self):
        print("- UI Designer: Creating user-friendly designs")
        super().skills()

class Trainer:
    def skills(self):
        print("- Tech Trainer: Training new team members")
        super().skills()

# Base class to stop the chain
class EmployeeBase:
    def skills(self):
        print("- EmployeeBase: Basic work ethics")

# SeniorEmployee inherits from Developer, Designer, Trainer, and EmployeeBase
class SeniorEmployee(Developer, Designer, Trainer, EmployeeBase):
    def skills(self):
        print("Senior Employee skills are:")
        super().skills()

# Create instance and call skills()
# MRO order is: SeniorEmployee -> Developer -> Designer -> Trainer -> EmployeeBase -> object
senior = SeniorEmployee()
senior.skills()             
