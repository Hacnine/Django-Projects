
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ContactForm


def func_view(request):
    return HttpResponse('Mellow Function')


class ClassView(View):
    name = 'Jabir'

    def get(self, request):
        return HttpResponse(f'Mellow {self.name} in ClassView ')
        # return HttpResponse(self.name)


class ChildClassView(ClassView):
    def get(self, request):
        context = {'name': 'Jabir'}
        return render(request, 'home.html', context)


#############################################################################
# Form example
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Your form is submitted.')

    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Your form is submitted.')


#############################################################################


def passing_template(request, template_name):
    # template_name = 'form.html'
    return render(request, template_name, )


class PassingTemplateView(View):
    def get(self, request, template_name):
        # template_name = 'form.html'
        return render(request, template_name)