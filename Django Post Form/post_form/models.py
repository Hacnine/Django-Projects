from django.db import models


class Employee(models.Model):
    name1 = models.CharField(max_length=140, default=None)
    email1 = models.CharField(max_length=140, default='SOME Eamil')


# class Employee:
#     name1 = 'mu'
#     email1 = 'eu'
#
#     def __init__(self, name, email, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.email = email
#
#         employee = Employee
#         employee.name1 = name
#         employee.name1 = email
#
#         print("First number = " + str(employee.name1))
#         print("Second number = " + str(employee.name1))
#
#
#
#     class InnerEmployee:
#
#         # parameterized constructor
#         def __init__(self, name, email):
#
#             self.name = name
#             self.email = email
#
#             employee = Employee(name, email)
#
#
#
#
#
#         # def display(self):
#         #     print("First number = " + str(self.name))
#         #     print("Second number = " + str(self.email))
#
#             # creating object of the class
#
#
# obj = Employee.InnerEmployee(1000, 2000)
#
# # obj.display()
