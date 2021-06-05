# Python Object-Oriented Programming
# Class allows us to group data(Attributes) and function(Methods) to be used.


print('================ LESSON 1 ===================')
# Class is basically a blueprint.
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def feedback(self):
        return '\nHello, {}.\nYour email is {}'.format(self.fullname(), self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp_1 = Employee('Corey', 'Schefer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# These 2 will be come the instances of the class ("Class Instance")

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_2.feedback())

print('================ LESSON 2 ===================')
print(emp_1.raise_amt)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_1.raise_amt = 1.05
print(emp_1.raise_amt)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print('================ LESSON 3 ===================')
