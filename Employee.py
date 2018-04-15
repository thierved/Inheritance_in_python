
class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def display_info(self):
         print('Employee name: {}\nEmployee salary: ${}'.format(self._name, self._salary))
