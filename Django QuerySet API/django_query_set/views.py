from django.db.models import Q
from django.shortcuts import render

from django_query_set.models import Student, Employee


def home(request):
    # student_data = Student.objects.all()

    # student_data = Student.objects.order_by('id')

    # student_data = Student.objects.filter(marks=70)

    # student_data = Student.objects.exclude(marks=70)

    # student_data = Student.objects.order_by('-id')

    # student_data = Student.objects.order_by('?')

    # student_data = Student.objects.order_by('name').reverse()

    # student_data = Student.objects.order_by('name').reverse()[:3]

    student_data = Student.objects.values()

    # student_data = Student.objects.values('name', 'city')

    student_data = Student.objects.distinct('name')  # it will remove duplicate rows

    # student_data = Student.objects.values('id', 'name')

    # student_data = Student.objects.values_list('id',  'name', named=True)
    
    # student_data = Student.objects.using('default')

    # student_data = Student.objects.dates('pass_date', 'month')

    # now we are using second table name is 'Employee'

    query_set_1 = Student.objects.values_list('id', 'name', named=True)
    query_set_2 = Employee.objects.values_list('id', 'name', named=True)
    student_data = query_set_2.union(query_set_1)

    student_data = query_set_2.union(query_set_1, all=True)

    student_data = query_set_2.intersection(query_set_1)

    student_data = query_set_1.difference(query_set_2)

    # AND
    student_data = Student.objects.filter(id=4) and Student.objects.filter(roll=110)
    student_data = Student.objects.filter(id=4, roll=110)
    student_data = Student.objects.filter(Q(id=4) and Q(roll=110))

    # OR operator
    student_data = Student.objects.filter(Q(id=1) or Q(roll=109))

    student_data = Student.objects.all()

    print('Return:', student_data, '\n')
    print('SQL Query:', student_data.query)

    return render(request, 'home.html', {'student_data': student_data})
