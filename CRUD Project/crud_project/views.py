from django.shortcuts import render, HttpResponseRedirect
from .form_model import UserRegistration
from .models import User


def custom_url_converters(request, year):
    student = {'id': year}
    return render(request, 'path_converters.html', student)


def update(request):
    if request.method == 'POST':
        updates = User.objects.get(pk=7)
        form = UserRegistration(request.POST, instance=updates)
        if form.is_valid():
            form.save()


def add_show(request):
    # for update
    # update(request)
    user = User.objects.all()

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # to save data
            db1 = User(name=name, email=email, password=password)
            db1.save()
    else:
        form = UserRegistration()
    return render(request, 'add_show.html', {'models': form, 'users': user})


def edit_update(request, em_id):
    if request.method == 'POST':
        updates = User.objects.get(pk=em_id)

        form = UserRegistration(request.POST, instance=updates)
        if form.is_valid():
            form.save()
    else:
        updates = User.objects.get(pk=em_id)
        form = UserRegistration(instance=updates)
    return render(request, 'update_delete.html', {'forms': form})


def delete_data(request, emp_id):
    if request.method == 'POST':
        pi = User.objects.get(pk=emp_id)
        pi.delete()
    return HttpResponseRedirect('/')


def redirect_home(request):
    return HttpResponseRedirect('/')