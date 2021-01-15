from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from authentications.form.forms_auth import SignUpForm, EditUserProfileForm, EditAdminProfileForm


def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/auth/dashboard/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user_data = form.save()
                group = Group.objects.get(name='Editor')
                user_data.groups.add(group)

                messages.set_level(request, messages.DEBUG)
                messages.debug(request, 'You have signed up successfully.')
                messages.info(request, 'Now you can log in')
                return HttpResponseRedirect('/auth/login/')



        else:
            form = SignUpForm()
        return render(request, 'user_form.html', {'forms': form})


# user sign up
def user_login(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/auth/dashboard/')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)

            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)

                if user is not None:
                    messages.set_level(request, messages.DEBUG)
                    messages.debug(request, 'You have signed up successfully.')
                    messages.info(request, 'Now you can manage.')

                    login(request, user)
                    return HttpResponseRedirect('/auth/dashboard/')

        else:
            form = AuthenticationForm()

        return render(request, 'authentications.html', {'forms': form})


def user_dashboard(request):
    if request.user.is_authenticated:  # 'is_authenticated' authenticates user
        return render(request, 'dashboard.html', {'name': request.user.username})
    else:
        return HttpResponseRedirect('/auth/dashboard/')


def user_change_profile(request):
    if request.user.is_authenticated:  # 'is_authenticated' authenticates user

        if request.method == 'POST':
            form = EditUserProfileForm(data=request.POST, instance=request.user)

            if form.is_valid():
                form.save()

                messages.success(request, 'Profile Updated!')
                return HttpResponseRedirect('/auth/dashboard/')
        else:

            if request.user.is_superuser:
                form = EditAdminProfileForm(instance=request.user)
                return render(request, 'change_profile.html', {'name': request.user, 'forms': form})

            else:
                form = EditUserProfileForm(instance=request.user)
                return render(request, 'change_profile.html', {'name': request.user, 'forms': form})
    else:
        return HttpResponseRedirect('/auth/login/')


def user_change_pass(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()

                # after update password not to log out:
                update_session_auth_hash(request, form.user)

                return HttpResponseRedirect('/auth/dashboard/')

        else:
            form = PasswordChangeForm(user=request.user)

        return render(request, 'change_password.html', {'forms': form})

    else:
        return HttpResponseRedirect('/auth/login/')


def change_pass_without_old(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()

                # after update password not to log out:
                update_session_auth_hash(request, form.user)

                return HttpResponseRedirect('/auth/dashboard/')

        else:
            form = SetPasswordForm(user=request.user)

        return render(request, 'change_passwords_without_old.html', {'forms': form})

    else:
        return HttpResponseRedirect('/auth/login/')


def user_details(request, ids):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=ids)
        form  = EditAdminProfileForm(instance=pi)
        return render(request, 'user_detail.html', {'forms': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')
