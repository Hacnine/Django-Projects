from django.shortcuts import render

from django_query_set.models import Student


def lookup(request):

    student_data = Student.objects.all()
    print(student_data.count())
    print('Return', student_data)
    return render(request, 'home_two.html', {'data': student_data})
