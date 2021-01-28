from django.views.generic import DetailView, ListView
from generic_view.models import Student


# for list view
class StudentDetailView(DetailView):
    template_name = 'student_detail.html'
    model = Student
    context_object_name = 'stu'
    pk_url_kwarg = 'idd'


class StudentLstView(ListView):
    model = Student
    template_name = 'student_list2.html'
