from django.shortcuts import render

from django_query_set.models import Student


def lookup(request):

    student_data = Student.objects.filter(name__exact='Tanvir')
    student_data = Student.objects.filter(name__iexact='tanvir')  # capital or small doesnt matter
    student_data = Student.objects.filter(city__contains='r')  # in city field which name contains 'r' letter

    student_data = Student.objects.filter(id__in=[1, 5, 7])
    student_data = Student.objects.filter(marks__in=[70])
    student_data = Student.objects.filter(marks__in=[60, 70])
    student_data = Student.objects.filter(marks__gt=60)
    student_data = Student.objects.filter(marks__gte=80)  # gte means greater than or equal
    student_data = Student.objects.filter(marks__lt=76)  # lt means less than
    student_data = Student.objects.filter(marks__lte=70)

    student_data = Student.objects.filter(name__startswith='J')
    student_data = Student.objects.filter(name__istartswith='j')
    student_data = Student.objects.filter(name__endswith='r')
    student_data = Student.objects.filter(name__iendswith='R')

    # student_data = Student.objects.filter(pass_date__range=('2020-12-22', '2021-01-09'))
    student_data = Student.objects.filter(pass_date__year__gt=2020)
    student_data = Student.objects.filter(pass_date__year__gte=2020)

    student_data = Student.objects.filter(pass_date__month=12)
    student_data = Student.objects.filter(pass_date__month__gte=12)

    student_data = Student.objects.filter(pass_date__week=52)
    student_data = Student.objects.filter(pass_date__week__gt=52)
    student_data = Student.objects.filter(pass_date__week_day=6)

    student_data = Student.objects.filter(pass_date__day=2)
    student_data = Student.objects.filter(pass_date__day__gt=2)
    student_data = Student.objects.filter(pass_date__day__gte=3)

    student_data = Student.objects.filter(pass_date__quarter=4)



    print('SQL Query:', student_data.query)
    return render(request, 'lookup.html', {'student_data': student_data})
