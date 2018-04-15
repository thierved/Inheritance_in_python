import Employee as em
import manager as mn

def main():

    employee = [em.Employee('Sadou', 4500),em.Employee('Madian', 2500), em.Employee('Ismaila', 2000)]
    manager = mn.Manager('Thierno', 6000)
    manager.hire_employee('Ibrahim', 2500)
    manager.display_info()

    for emp in employee:
        emp.display_info()


if __name__ == '__main__': main()
