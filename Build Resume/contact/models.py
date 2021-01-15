from django.db import models


class Employee(models.Model):
    # employee_id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField()
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.TextField(max_length=200)
    # this line was added and then removed.
    # last_name = models.CharField(max_length=30, default='newly added')

    # def __str__(self):
    #     return self.name, self.email
    #     # return str(self.employee_id)
