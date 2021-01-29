from django.views.generic import DetailView, ListView
from list_view.models import Student


# for list view
class StudentDetailView(DetailView):
    template_name = 'student_detail.html'
    model = Student
    # context_object_name = 'stu'
    pk_url_kwarg = 'idd'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stu'] = self.model.objects.all()
        return context


class StudentLstView(ListView):
    model = Student
    template_name = 'student_list2.html'


