from django.shortcuts import render
# from . models import Employee
from contact.models import Employee


def contact(request):
    return render(request, 'contact_html.html')


def databases(request):
    # stu = Employee.objects.get(pk=3)
    stu = Employee.objects.all()
    return render(request, 'databases/databases_html.html', {'students': stu})
