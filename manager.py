import Employee as em 

class Manager(em.Employee):

    def __init__(self, name, salary):
        super().__init__(name, salary)

    def hire_employee(self, name, salary):
        hired = em.Employee(name, salary)
        print("======= hired a new employee =========")
        hired.display_info()
        print("======================================")
    
    def display_info(self):
        super().display_info()



