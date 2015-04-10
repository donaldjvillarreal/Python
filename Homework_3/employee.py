#Employee class definition.
class Employee:
    #Class variable (shared by all objects of this class).
    employee_count = 0

    #Object initialization function.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    #Instance function.
    def promoted(self, pay_increase):
        self.salary += pay_increase
        


employee1 = Employee("Jane", 100)
employee2 = Employee("Jack", 90)
print("There are %d employees" % Employee.employee_count)
employee1.promoted(20)
print("%s is making %d" % (employee1.name, employee1.salary))
print("%s is making %d" % (employee2.name, employee2.salary))
