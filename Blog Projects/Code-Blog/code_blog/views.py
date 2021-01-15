from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from code_blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class ProfileView(CreateView):
    model = Post
    template_name = 'profile.html'
    fields = '__all__'


    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user_data = form.save()
    #         group = Group.objects.get(name='Editor')
    #         user_data.groups.add(group)
    #
    #         messages.set_level(request, messages.DEBUG)
    #         messages.debug(request, 'You have signed up successfully.')
    #         messages.info(request, 'Now you can log in')
    #         return HttpResponseRedirect('/auth/login/')
    #
    # else:
    #     form = SignUpForm()
    # return render(request, 'user_form.html', {'forms': form})
