from django.shortcuts import render
from .form_model import UserRegistration
from model_form.models import User


def update(request):
    if request.method == 'POST':
        updates = User.objects.get(pk=7)
        form = UserRegistration(request.POST, instance=updates)
        if form.is_valid():
            form.save()


def f_model(request):
    # for update
   # update(request)
    
    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # to save data
            db1 = User(name=name, email=email, password=password)
            db1.save()
            
            # to delete data
            # delte = User(id=2)
            # delte.delete()

            print('Name:', name)
            print('Email: ', email)
            print('password', password)
            print("See in Terminal. It has come form 'POST'")

    else:
        form = UserRegistration()
        print("See in Terminal. It has come form 'GET'")
    return render(request, 'model_form.html', {'models': form})

