from django.shortcuts import render


def django_course(request):
    return render(request, 'course/course_info.html')
