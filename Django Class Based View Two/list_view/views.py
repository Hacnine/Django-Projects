from django.views.generic.list import ListView

from list_view.models import Student


# for list view
class StudentListView(ListView):
    template_name = 'student_list.html'
    model = Student
    # template_name_suffix = '_get'
    ordering = ['name']

    # if I want to change the default context name
    # context_object_name = 'students'

    # if want to filter data
    def get_queryset(self):
        return Student.objects.filter(course='EEE')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['freshers'] = Student.objects.all().order_by('name')
        return context

    def get_template_names(self):
        if self.request.COOKIES['user'] == 'Kabir':
            template_name = 'student_list.html'
        else:
            template_name = self.template_name
        return [template_name]
