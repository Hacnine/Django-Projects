from django.shortcuts import render
from .models import Student, Teacher, Constructor


def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    constructor_data = Constructor.objects.all()
    context = {'student_data': student_data, 'teacher_data': teacher_data, 'constructor_data': constructor_data}

    return render(request, 'home.html', context)
