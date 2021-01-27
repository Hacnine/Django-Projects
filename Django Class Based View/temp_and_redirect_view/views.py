from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView


# class HomeTemplateView(TemplateView):
#     template_name = 'temp_home.html'


class HomeTemplateView(TemplateView):
    template_name = 'temp_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'jabir'
        context['age'] = 25
        # context = {'name': 'jabir', 'age': 23, }
        print(kwargs)
        return context


class GoogleRedirectView(RedirectView):
    url = 'https://www.google.com'
    permanent = True
    query_string = True
    # query_string = True


