from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.shortcuts import render

from code_blog.froms_blog import SignUpForm, LoginForm, PostForm
from code_blog.models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def user_signup(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            messages.success(request, 'Welcome! You have signed in successfully.')
            user = forms.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
            return HttpResponseRedirect('/dashboard/')

    else:
        forms = SignUpForm()
    return render(request, 'signup.html', {'forms': forms})


def user_login(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            forms = LoginForm(request=request, data=request.POST)

            if forms.is_valid():
                user_name = forms.cleaned_data['username']
                user_password = forms.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have logged in successfully.')
                    return HttpResponseRedirect('/dashboard/')

        else:
            forms = LoginForm()
            return render(request, 'login.html', {'forms': forms})

    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        full_name = request.user.get_full_name()
        group_name = request.user.groups.all()

        # track ip
        ip = request.session.get('ip', 0)
        # log in count
        log_count = cache.get('count', version=request.user.pk)

        return render(request, 'dashboard.html', {'ip': ip, 'posts': posts, 'count': log_count,
                                                  'fullname': full_name, 'groups': group_name})
    else:
        return HttpResponseRedirect('/login/')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def update_post(request, ids):
    if request.user.is_authenticated:

        if request.method == 'POST':
            pi = Post.objects.get(pk=ids)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                post = Post(title=title, description=description)
                form.save()
                # form = PostForm()
        else:
            pi = Post.objects.get(pk=ids)

            form = PostForm(instance=pi)
        return render(request, 'update_post.html', {'forms': form})

    else:
        return HttpResponseRedirect('/login/')


def add_post(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                post = Post(title=title, description=description)
                post.save()
                form = PostForm()
        else:
            form = PostForm()
            return render(request, 'add_post.html', {'forms': form})

        return render(request, 'add_post.html')
    else:
        return HttpResponseRedirect('/login/')


def delete_post(request, ids):
    if request.user.is_authenticated:

        if request.method == 'POST':
            pi = Post.objects.get(pk=ids)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')

    else:
        return HttpResponseRedirect('/login/')
