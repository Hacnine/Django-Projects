from django.db.models import Avg, Sum, Min, Max, Count, Q
from django.shortcuts import render

from django_query_set.models import Student


def aggregation(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    summation = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    count = student_data.aggregate(Count('marks'))

    # Q Objects
    student_data2 = Student.objects.filter(Q(id=6) and Q(roll=113))
    student_data2 = Student.objects.filter(Q(id=7) or Q(roll=114))
    student_data2 = Student.objects.filter(~Q(id=10))

    # Limiting QuerySet
    student_data2 = Student.objects.all()[:4]
    student_data2 = Student.objects.all()[3:7]
    # student_data2 = Student.objects.all()[-1]  # not valid
    student_data2 = Student.objects.all()[:9:2]


    context = {'average': average, 'summation': summation, 'minimum': minimum, 'maximum': maximum, 'count': count,
               'student_data2': student_data2}
    return render(request, 'aggregation.html', context)
