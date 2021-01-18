from django.shortcuts import render

from django_query_set.models import Student


def home2(request):
    # student_data = Student.objects.get(pk=1)
    # student_data = Student.objects.get(name='Tanvir')  # name should be unique
    # student_data = Student.objects.last()
    # student_data = Student.objects.order_by('name').last()
    # student_data = Student.objects.latest('pass_date')
    # student_data = Student.objects.earliest('pass_date')
    #
    student_data = Student.objects.all()
    print(student_data.exists())

    one_data = Student.objects.get(pk=3)
    print(student_data.filter(pk=one_data.pk).exists())

    # to insert a data into database
    # student_data = Student.objects.create(name='Hanif', roll=115, city='Maymansigh', marks=60, pass_date='2009-02-1')
    # student_data = Student.objects.get_or_create(name='Hanif', roll=115, city='Maymansigh', marks=60, pass_date='2009-02-1')

    # update one id with multiple value
    # student_data = Student.objects.filter(id=3).update(name='Jund', marks=60)

    # update update which marks is 60 with multiple value
    # student_data = Student.objects.filter(marks=60).update(marks=70)

    # student_data = Student.objects.update_or_create(name='Hujaifa', marks=65, defaults={'name': 'Jabir al Hujaifa'})

    objs = [
        Student(name='Khalid', roll=121, city='Maymansigh', marks=60, pass_date='2009-02-1'),
        Student(name='Walid', roll=122, city='Maymansigh', marks=60, pass_date='2009-02-1'),
    ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for studemt in all_student_data:
    #     studemt.city = 'Makka'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])

    # student_data =  Student.objects.get(pk=5).delete()
    # student_data =  Student.objects.get(marks=60).delete()
    # student_data = Student.objects.all().delete()
    student_data = Student.objects.all()
    print(student_data.count())
    print('Return', student_data)
    return render(request, 'home_two.html', {'data': student_data})
