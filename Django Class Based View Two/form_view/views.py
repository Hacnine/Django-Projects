from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from form_view.forms import ContactForm


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/submitted/'
    initial = {'msg': 'It is a initial data.'}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        return super().form_valid(form)
        # return HttpResponse('Message sent')



class SubmitTemplateView(TemplateView):
    template_name = 'submit.html'
